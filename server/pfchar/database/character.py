import json
import uuid
from pfchar.database.connection import r_get, r_set, r_exists
from pfchar.database.exceptions import CharacterWrongUserError, DatabaseError, CharacterReadError, CharacterWriteError


class Character(object):
    def __init__(self, id, userid):
        self._char_id = id

        if self._get_char_value('uid') != userid:
            raise CharacterWrongUserError('Could not get the character as it belongs to a different user.')

    def _get_char_value(self, path):
        try:
            return r_get('characters', self._char_id + '.' + path)
        except DatabaseError as e:
            raise CharacterReadError('Could not retrieve the value at: .' + self._char_id + '.' + path)

    def _set_char_value(self, path, value):
        try:
            r_set('characters', self._char_id + '.' + path, value)
        except DatabaseError as e:
            raise CharacterWriteError('Could not write the value ' + value + ' at .' + self._char_id + '.' + path)

    def __str__(self):
        return json.dumps(r_get('characters', self._char_id))

    def _create_from_string(self, value, text):
        str_val = ''

        if value >= 0:
            str_val += '+' + str(value)
        else:
            str_val += str(value)

        return str_val + ' ' + text

    def _set_level(self, value):
        value = 0 if value == '' else int(value)
        value = 1 if value == 0 else value

        exp = self._get_char_value('exp')
        growthCurve = r_get('templates', 'mechanics.growth.' + exp['growth'])

        if value == 1:
            exp['experience'] = 0
        elif value > 20:
            exp['experience'] = 0
        else:
            exp['experience'] = growthCurve[value - 2]

        exp['level'] = value

        self._set_char_value('exp', exp)

    def _set_experience(self, value):
        value = 0 if value == '' else int(value)
        exp = self._get_char_value('exp')
        growthCurve = r_get('templates', 'mechanics.growth.' + exp['growth'])
        newLvl = 0

        for index, entry in enumerate(growthCurve):
            if value < entry:
                newLvl = index + 1
                break

        exp['level'] = newLvl
        exp['experience'] = value

        self._set_char_value('exp', exp)

    def set(self, path, value):
        if path == 'exp.experience':
            self._set_experience(value)
            return
        if path == 'exp.level':
            self._set_level(value)
            return

        self._set_char_value(path, value)

    @property
    def id(self):
        return self._char_id

    @property
    def complete(self):
        return {
            'basics': self.basics,
            'attributes': self.attributes,
            'hitpoints': self.hitpoints,
            'feats': self.feats,
            'skills': self.skills,
            'exp': self.exp,
            'traits': self.traits,
            'initiative': self.initiative,
            'attack': self.attack
        }

    @property
    def name(self):
        return self._get_char_value('basics.name')

    @property
    def hitpoints(self):
        return self._get_char_value('hitpoints')

    @property
    def exp(self):
        exp = self._get_char_value('exp')
        growthCurve = r_get('templates', 'mechanics.growth.' + exp['growth'])

        if exp['level'] > 20:
            exp['nextLevel'] = 0
        else:
            nextLevelExp = 0
            for entry in growthCurve:
                if exp['experience'] < entry:
                    nextLevelExp = entry
                    break
            exp['nextLevel'] = nextLevelExp

        return exp

    @property
    def race(self):
        return r_get('templates', 'races.' + self._get_char_value('basics.race'))

    @property
    def basics(self):
        race = self.race

        basics = self._get_char_value('basics')
        basics['race'] = race['name']
        basics['languages']['available'] = self.race['languages']['extended']

        return basics

    @property
    def feats(self):
        feats = {}

        for feat_ident in self._get_char_value('feats'):
            feat = r_get('templates', 'feats.' + feat_ident)
            feats[feat_ident] = feat

        traits = self.traits
        for trait_key in traits.keys():
            try:
                for feat_ident in traits[trait_key]['dicrect_bonus']['feats'].keys():
                    feat = r_get('templates', 'feats.' + feat_ident)
                    feat['from'] = 'from racial traif "' + traits[trait_key]['name'] + '".'
                    feats[feat_ident] = feat
            except KeyError as e:
                pass

        return feats

    @property
    def attack(self):
        attack = self._get_char_value('attack')
        classes = self._get_char_value('exp.classes')
        clsname = ''
        clslvl = 0
        for key in classes.keys():
            if clslvl < classes[key]:
                clsname = key
                clslvl = classes[key]

        bab = r_get('templates', 'classes.' + clsname + '.bab')
        attack['bab'] = bab[clslvl - 1]

        for key, feat in self.feats.items():
            try:
                bonus = feat['direct_bonus']['attack']
                attack['base']['bonus']['total'] += bonus
                attack['base']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
            except KeyError as e:
                pass

        for key, skill in self.skills.items():
            try:
                bonus = skill['direct_bonus']['attack']
                attack['base']['bonus']['total'] += bonus
                attack['base']['bonus']['from'].append(self._create_from_string(bonus, 'from skill "' + skill['name'] + '".'))
            except KeyError as e:
                pass

        for key, trait in self.traits.items():
            try:
                bonus = trait['direct_bonus']['attack']
                attack['base']['bonus']['total'] += bonus
                attack['base']['bonus']['from'].append(self._create_from_string(bonus, 'from trait "' + trait['name'] + '".'))
            except KeyError as e:
                pass

        race = self.race
        try:
            bonus = self.race['direct_bonus']['cmd']
            attack['cmd']['bonus']['total'] += bonus
            attack['cmd']['bonus']['from'].append(self._create_from_string(bonus, 'from race ' + race['name']))
        except KeyError as e:
            pass
        try:
            bonus = self.race['direct_bonus']['cmb']
            attack['cmb']['bonus']['total'] += bonus
            attack['cmb']['bonus']['from'].append(self._create_from_string(bonus, 'from race ' + race['name']))
        except KeyError as e:
            pass

        return attack

    @property
    def initiative(self):
        initiative = self._get_char_value('initiative')

        for key, feat in self.feats.items():
            try:
                bonus = feat['direct_bonus']['initiative']
                initiative['bonus']['total'] += bonus
                initiative['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
            except KeyError as e:
                pass

        for key, skill in self.skills.items():
            try:
                bonus = skill['direct_bonus']['initiative']
                initiative['bonus']['total'] += bonus
                initiative['bonus']['from'].append(self._create_from_string(bonus, 'from skill "' + skill['name'] + '".'))
            except KeyError as e:
                pass

        for key, trait in self.traits.items():
            try:
                bonus = trait['direct_bonus']['initiative']
                initiative['bonus']['total'] += bonus
                initiative['bonus']['from'].append(self._create_from_string(bonus, 'from trait "' + trait['name'] + '".'))
            except KeyError as e:
                pass

        return initiative

    @property
    def traits(self):
        return r_get('templates', 'races.' + self._get_char_value('basics.race') + '.traits')

    @property
    def attributes(self):
        attrs = self._get_char_value('attributes')
        attrs['str']['bonus'] = {
            'total': 0,
            'from': []
        }
        attrs['dex']['bonus'] = {
            'total': 0,
            'from': []
        }
        attrs['con']['bonus'] = {
            'total': 0,
            'from': []
        }
        attrs['int']['bonus'] = {
            'total': 0,
            'from': []
        }
        attrs['wis']['bonus'] = {
            'total': 0,
            'from': []
        }
        attrs['cha']['bonus'] = {
            'total': 0,
            'from': []
        }

        if r_exists('templates', 'races.' + self._get_char_value('basics.race') + '.direct_bonus.attributes'):
            race_attr_bonus = r_get('templates', 'races.' + self._get_char_value('basics.race') + '.direct_bonus.attributes')
            if 'str' in race_attr_bonus:
                attrs['str']['bonus']['total'] += race_attr_bonus['str']
                attrs['str']['bonus']['from'].append(self._create_from_string(race_attr_bonus['str'], 'from racial bonus.'))
            if 'dex' in race_attr_bonus:
                attrs['dex']['bonus']['total'] += race_attr_bonus['dex']
                attrs['dex']['bonus']['from'].append(self._create_from_string(race_attr_bonus['dex'], 'from racial bonus.'))
            if 'con' in race_attr_bonus:
                attrs['con']['bonus']['total'] += race_attr_bonus['con']
                attrs['con']['bonus']['from'].append(self._create_from_string(race_attr_bonus['con'], 'from racial bonus.'))
            if 'int' in race_attr_bonus:
                attrs['int']['bonus']['total'] += race_attr_bonus['int']
                attrs['int']['bonus']['from'].append(self._create_from_string(race_attr_bonus['int'], 'from racial bonus.'))
            if 'wis' in race_attr_bonus:
                attrs['wis']['bonus']['total'] += race_attr_bonus['wis']
                attrs['wis']['bonus']['from'].append(self._create_from_string(race_attr_bonus['wis'], 'from racial bonus.'))
            if 'cha' in race_attr_bonus:
                attrs['cha']['bonus']['total'] += race_attr_bonus['cha']
                attrs['cha']['bonus']['from'].append(self._create_from_string(race_attr_bonus['cha'], 'from racial bonus.'))

        for key, feat in self.feats.items():
            try:
                attributes = feat['direct_bonus']['attributes']
                if 'str' in attributes:
                    bonus = attributes['str']
                    attrs['str']['bonus']['total'] += bonus
                    attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
                if 'dex' in attributes:
                    bonus = attributes['dex']
                    attrs['dex']['bonus']['total'] += bonus
                    attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
                if 'con' in attributes:
                    bonus = attributes['con']
                    attrs['con']['bonus']['total'] += bonus
                    attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
                if 'int' in attributes:
                    bonus = attributes['int']
                    attrs['int']['bonus']['total'] += bonus
                    attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
                if 'wis' in attributes:
                    bonus = attributes['wis']
                    attrs['wis']['bonus']['total'] += bonus
                    attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
                if 'cha' in attributes:
                    bonus = attributes['cha']
                    attrs['cha']['bonus']['total'] += bonus
                    attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from feat "' + feat['name'] + '".'))
            except KeyError as e:
                pass
        return attrs

    @property
    def skills(self):
        skills = self._get_char_value('skills')
        traits = self.traits
        feats = self.feats
        race = self.race

        for skill_key in skills.keys():
            skills[skill_key]['bonus'] = {
                'total': 0,
                'from': []
            }

            for trait_key in traits.keys():
                try:
                    bonus = traits[trait_key]['direct_bonus']['skills'][skill_key]
                    if isinstance(bonus, dict):
                        bonus_total = bonus['bonus']
                        if 'upgrade' in bonus:
                            if skills[skill_key]['ranks'] >= bonus['upgrade']['ranks']:
                                bonus_total = bonus['upgrade']['bonus']
                    else:
                        bonus_total = bonus
                    skills[skill_key]['bonus']['total'] += bonus_total
                    skills[skill_key]['bonus']['from'].append(self._create_from_string(bonus_total, 'from racial trait "' + traits[trait_key]['name'] + '".'))
                except KeyError as e:
                    pass

            for feat_key in feats.keys():
                try:
                    bonus = feats[feat_key]['direct_bonus']['skills'][skill_key]
                    if isinstance(bonus, dict):
                        bonus_total = bonus['bonus']
                        if 'upgrade' in bonus:
                            if skills[skill_key]['ranks'] >= bonus['upgrade']['ranks']:
                                bonus_total = bonus['upgrade']['bonus']
                    else:
                        bonus_total = bonus
                    skills[skill_key]['bonus']['total'] += bonus_total
                    skills[skill_key]['bonus']['from'].append(self._create_from_string(bonus_total, 'from feat "' + feats[feat_key]['name'] + '".'))
                except KeyError as e:
                    pass

            try:
                bonus = race['direct_bonus']['skills'][skill_key]
                if isinstance(bonus, dict):
                    if 'upgrade' in bonus:
                        if skills[skill_key]['ranks'] >= bonus['upgrade']['ranks']:
                            bonus_total = bonus['upgrade']['bonus']
                else:
                    bonus_total = bonus
                skills[skill_key]['bonus']['total'] += bonus_total
                skills[skill_key]['bonus']['from'].append(self._create_from_string(bonus_total, 'from race ' + race['name']))
            except KeyError as e:
                pass

        return skills


def new_char(userid, char_name, char_class, char_race):
    id = 'uuid_' + uuid.uuid4().hex
    char = r_get('templates', 'character')
    char['uid'] = userid
    char['basics']['name'] = char_name
    char['basics']['race'] = char_race.lower()
    char['exp']['level'] = 1
    char['exp']['classes'][char_class.lower()] = 1

    char['basics']['languages']['known'] = r_get('templates', 'races.' + char_race.lower() + '.languages.base')
    char['basics']['speed']['base'] = r_get('templates', 'races.' + char_race.lower() + '.speed')

    r_set('characters', id, char)

    return Character(id, userid)
