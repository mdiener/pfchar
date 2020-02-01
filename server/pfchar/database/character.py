import json
import uuid
from pfchar.database.connection import r_get, r_set
from pfchar.database.exceptions import CharacterWrongUserIdError, DatabaseError, CharacterReadError, CharacterWriteError


class Character(object):
    def __init__(self, id, userid):
        self._char_id = id

        if self._get_char_value('userid') != userid:
            raise CharacterWrongUserIdError('Could not get the character as it belongs to a different user.')

    def _get_char_value(self, path):
        try:
            return r_get('characters', self._char_id + '.' + path)
        except DatabaseError as e:
            raise CharacterReadError('Could not retrieve the value at: .' + self._char_id + '.' + path)

    def _set_char_value(self, path, value):
        try:
            r_set('characters', '.' + self._char_id + '.' + path, value)
        except DatabaseError as e:
            raise CharacterWriteError('Could not write the value ' + value + ' at .' + self._char_id + '.' + path)

    def __str__(self):
        return json.dumps(r_get('characters', self._char_id))

    def _create_from_string(self, value, text):
        str_val = ''

        if value >= 0:
            str_val += '+' + str(value)
        else:
            str_val += '-' + str(value)

        return str_val + ' ' + text

    @property
    def id(self):
        return self._char_id

    @property
    def name(self):
        return self._get_char_value('basics.name');

    @property
    def classes(self):
        classes = self._get_char_value('basics.classes')
        for index, entry in enumerate(classes):
            classes[index] = [r_get('templates', 'classes.' + entry[0] + '.name'), entry[1]]

        return classes

    @property
    def race(self):
        return r_get('templates', 'races.' + self._get_char_value('basics.race') + '.name')

    @property
    def basics(self):
        basics = self._get_char_value('basics')
        basics['race'] = self.race
        basics['classes'] = self.classes

        return basics

    @property
    def misc(self):
        return self._get_char_value('misc')

    @property
    def feats(self):
        feats = []

        for feat_ident in self._get_char_value('feats'):
            feat = r_get('templates', 'feats.' + feat_ident)
            feats.append(feat)

        for key, trait in r_get('templates', 'races.' + self._get_char_value('basic.race') + '.traits').items():
            if 'direct_bonus' in trait:
                if 'feats' in trait['direct_bonus']:
                    for feat_ident in trait['direct_bonus']['feats']:
                        feat = r_get('templates', 'feats.' + feat_ident)
                        feat['from'] = 'From Racial Trait "' + trait['name'] + '".'

        return feats

    @property
    def traits(self):
        return r_get('templates', 'races.' + self._get_char_value('basics.race') + '.traits')

    @property
    def attributes(self):
        attrs = self._get_char_value('attributes')

        if r_exists('templates', 'races.' + self._get_char_value('basics.race') + '.direct_bonus.attributes'):
            race_attr_bonus = r_get('templates', 'races.' + self._get_char_value('basics.race') + '.direct_bonus.attributes')
            if 'str' in race_attr_bonus:
                attrs['str']['bonus']['total'] += race_attr_bonus['str']
                attrs['str']['bonus']['from'].append(self._create_from_string(race_attr_bonus['str'], 'from Racial Bonus'))
            if 'dex' in race_attr_bonus:
                attrs['dex']['bonus']['total'] += race_attr_bonus['dex']
                attrs['dex']['bonus']['from'].append(self._create_from_string(race_attr_bonus['dex'], 'from Racial Bonus'))
            if 'con' in race_attr_bonus:
                attrs['con']['bonus']['total'] += race_attr_bonus['con']
                attrs['con']['bonus']['from'].append(self._create_from_string(race_attr_bonus['con'], 'from Racial Bonus'))
            if 'int' in race_attr_bonus:
                attrs['int']['bonus']['total'] += race_attr_bonus['int']
                attrs['int']['bonus']['from'].append(self._create_from_string(race_attr_bonus['int'], 'from Racial Bonus'))
            if 'wis' in race_attr_bonus:
                attrs['wis']['bonus']['total'] += race_attr_bonus['wis']
                attrs['wis']['bonus']['from'].append(self._create_from_string(race_attr_bonus['wis'], 'from Racial Bonus'))
            if 'cha' in race_attr_bonus:
                attrs['cha']['bonus']['total'] += race_attr_bonus['cha']
                attrs['cha']['bonus']['from'].append(self._create_from_string(race_attr_bonus['cha'], 'from Racial Bonus'))

        for feat in self.feats:
            if 'direct_bonus' in feat:
                if 'attributes' in feat['direct_bonus']:
                    if 'str' in feat['direct_bonus']['attributes']:
                        bonus = feat['direct_bonus']['attributes']['str']['bonus']
                        attrs['str']['bonus']['total'] += bonus
                        attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from Feat "' + feat['name'] + '"'))
                    if 'dex' in feat['direct_bonus']['attributes']:
                        bonus = feat['direct_bonus']['attributes']['dex']['bonus']
                        attrs['dex']['bonus']['total'] += bonus
                        attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from Feat "' + feat['name'] + '"'))
                    if 'con' in feat['direct_bonus']['attributes']:
                        bonus = feat['direct_bonus']['attributes']['con']['bonus']
                        attrs['con']['bonus']['total'] += bonus
                        attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from Feat "' + feat['name'] + '"'))
                    if 'int' in feat['direct_bonus']['attributes']:
                        bonus = feat['direct_bonus']['attributes']['int']['bonus']
                        attrs['int']['bonus']['total'] += bonus
                        attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from Feat "' + feat['name'] + '"'))
                    if 'wis' in feat['direct_bonus']['attributes']:
                        bonus = feat['direct_bonus']['attributes']['wis']['bonus']
                        attrs['wis']['bonus']['total'] += bonus
                        attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from Feat "' + feat['name'] + '"'))
                    if 'cha' in feat['direct_bonus']['attributes']:
                        bonus = feat['direct_bonus']['attributes']['cha']['bonus']
                        attrs['cha']['bonus']['total'] += bonus
                        attrs['str']['bonus']['from'].append(self._create_from_string(bonus, 'from Feat "' + feat['name'] + '"'))


def new_char(userid, char_name, char_class, char_race):
    id = 'uuid_' + uuid.uuid4().hex
    char = r_get('templates', 'character')
    char['userid'] = userid
    char['id'] = id
    char['basics']['name'] = char_name
    char['basics']['level'] = 1
    char['basics']['classes'] = [[char_class, 1]]
    char['basics']['race'] = char_race

    r_set('characters', id, char)

    return Character(id, userid)
