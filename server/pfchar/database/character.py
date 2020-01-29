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
            r_get('characters', self._char_id + '.' + path)
        except DatabaseError as e:
            raise CharacterReadError('Could not retrieve the value at: .' + self._char_id + '.' + path)

    def _set_char_value(self, path, value):
        try:
            r_set('characters', '.' + self._char_id + '.' + path, value)
        except DatabaseError as e:
            raise CharacterWriteError('Could not write the value ' + value + ' at .' + self._char_id + '.' + path)

    def __str__(self):
        return r_get('characters', self._char_id)

    @property
    def id(self):
        return self._char_id

    @property
    def str(self):
        return self._get_char_value('ability.str.score')

    @str.setter
    def str(self, value):
        self._set_char_value('ability.str.score', value)

    @property
    def dex(self):
        return self._get_char_value('ability.dex.score')

    @dex.setter
    def dex(self, value):
        self._set_char_value('ability.dex.score', value)

    @property
    def con(self):
        return self._get_char_value('ability.con.score')

    @con.setter
    def con(self, value):
        self._set_char_value('ability.con.score', value)

    @property
    def int(self):
        return self._get_char_value('ability.int.score')

    @int.setter
    def int(self, value):
        self._set_char_value('ability.int.score', value)

    @property
    def wis(self):
        return self._get_char_value('ability.wis.score')

    @wis.setter
    def wis(self, value):
        self._set_char_value('ability.wis.score', value)

    @property
    def cha(self):
        return self._get_char_value('ability.cha.score')

    @cha.setter
    def cha(self, value):
        self._set_char_value('ability.cha.score', value)

    @property
    def strAdjust(self):
        return self._get_char_value('ability.str.adjust')

    @strAdjust.setter
    def strAdjust(self, value):
        self._set_char_value('ability.str.adjust', value)

    @property
    def dexAdjust(self):
        return self._get_char_value('ability.dex.adjust')

    @dexAdjust.setter
    def dexAdjust(self, value):
        self._set_char_value('ability.dex.adjust', value)

    @property
    def conAdjust(self):
        return self._get_char_value('ability.con.adjust')

    @conAdjust.setter
    def conAdjust(self, value):
        self._set_char_value('ability.con.adjust', value)

    @property
    def intAdjust(self):
        return self._get_char_value('ability.int.adjust')

    @intAdjust.setter
    def intAdjust(self, value):
        self._set_char_value('ability.int.adjust', value)

    @property
    def wisAdjust(self):
        return self._get_char_value('ability.wis.adjust')

    @wisAdjust.setter
    def wisAdjust(self, value):
        self._set_char_value('ability.wis.adjust', value)

    @property
    def chaAdjust(self):
        return self._get_char_value('ability.cha.adjust')

    @chaAdjust.setter
    def chaAdjust(self, value):
        self._set_char_value('ability.cha.adjust', value)

    @property
    def totalHP(self):
        return self._get_char_value('hitpoints.total')

    @totalHP.setter
    def totalHP(self, value):
        self._set_char_value('hitpounts.total', value)

    @property
    def dr(self):
        return self._get_char_value('hitpoints.dr')

    @dr.setter
    def dr(self, value):
        self._set_char_value('hitpoints.dr', value)

    @property
    def currentHP(self):
        return self._get_char_value('hitpoints.current')

    @currentHP.setter
    def currentHP(self, value):
        self._set_char_value('hitpoints.current', value)

    @property
    def nonlethal(self):
        return self._get_char_value('hitpoints.nonlethal')

    @nonlethal.setter
    def nonlethal(self, value):
        self._set_char_value('hitpoints.nonlethal', value)


def new_char(userid):
    char = {
        'uid': userid,
        'classes': [],
        'level': 1,
        'experience': 0,
        'growth': 'medium',
        'ability': {
            'str': {
                'base': 0,
                'adjust': 0
            },
            'dex': {
                'base': 0,
                'adjust': 0
            },
            'con': {
                'base': 0,
                'adjust': 0
            },
            'int': {
                'base': 0,
                'adjust': 0
            },
            'wis': {
                'base': 0,
                'adjust': 0
            },
            'cha': {
                'base': 0,
                'adjust': 0
            }
        },
        'hitpoints': {
            'total': 0,
            'dr': 0,
            'current': 0,
            'nonlethal': 0
        },
        'skills': {
            'acrobatics': {
                'name': 'Acrobatics',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Acrobatics',
                'attr': 'dex',
                'trained': False,
                'penalties': 'armor',
                'ranks': 0,
                'temp_adjust': 0,
            },
            'appraise': {
                'name': 'Appraise',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Appraise',
                'attr': 'int',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'bluff': {
                'name': 'Bluff',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Bluff',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'climb': {
                'name': 'Climb',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Climb',
                'attr': 'str',
                'trained': False,
                'penalties': 'armor',
                'ranks': 0,
                'temp_adjust': 0
            },
            'craft': {
                'name': 'Craft',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Craft',
                'attr': 'int',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'diplomacy': {
                'name': 'Diplomacy',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Diplomacy',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'disable_device': {
                'name': 'Disable Device',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Disable%20Device',
                'attr': 'dex',
                'trained': True,
                'penalties': 'armor',
                'ranks': 0,
                'temp_adjust': 0
            },
            'disguise': {
                'name': 'Disguise',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Disguise',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'escape_artist': {
                'name': 'Escape Artist',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Escape%20Artist',
                'attr': 'dex',
                'trained': False,
                'penalties': 'armor',
                'ranks': 0,
                'temp_adjust': 0
            },
            'fly': {
                'name': 'Fly',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Fly',
                'attr': 'dex',
                'trained': False,
                'penalties': 'armor',
                'ranks': 0,
                'temp_adjust': 0
            },
            'handle_animal': {
                'name': 'Handle Animal',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Handle%20Animal',
                'attr': 'cha',
                'trained': True,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'heal': {
                'name': 'Heal',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Heal',
                'attr': 'wis',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'intimidate': {
                'name': 'Intimidate',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Intimidate',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'ranks': 0,
                'temp_adjust': 0
            },
            'knowlege_arcana': {
                'name': 'Knowlege Arcana',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_dungeoneering': {
                'name': 'Knowlege Dungeoneering',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_engineering': {
                'name': 'Knowlege Engineering',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_geography': {
                'name': 'Knowlege Geography',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_history': {
                'name': 'Knowlege History',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_local': {
                'name': 'Knowlege Local',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_nature': {
                'name': 'Knowlege Nature',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_nobility': {
                'name': 'Knowlege Nobility',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_planes': {
                'name': 'Knowlege Planes',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'knowlege_religion': {
                'name': 'Knowlege Religion',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Knowlege',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'linguistics': {
                'name': 'Linguistics',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Linguistics',
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perception': {
                'name': 'Perception',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perception',
                'attr': 'wis',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_act': {
                'name': 'Perform Act',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_comedy': {
                'name': 'Perform Comedy',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_dance': {
                'name': 'Perform Dance',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_keyboard_instruments': {
                'name': 'Perform Keyboard Instruments',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_oratory': {
                'name': 'Perform Oratory',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_percussion_instruments': {
                'name': 'Perform Percussion Instruments',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_string_instruments': {
                'name': 'Perform String Instruments',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_wind_instruments': {
                'name': 'perform Wind Instruments',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'perform_sing': {
                'name': 'Perform Sing',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Perform',
                'attr': 'cha',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'profession': {
                'name': 'Profession',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Profession'
                'attr': 'wis',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'ride': {
                'name': 'Ride',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Ride'
                'attr': 'dex',
                'trained': False,
                'penalties': 'armor',
                'rank': 0,
                'adjust': 0
            },
            'sense_motive': {
                'name': 'Sense Motive',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Sense%20Motive'
                'attr': 'wis',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'sleight_of_hand': {
                'name': 'Sleight of Hand',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Sleight%20of%20Hand'
                'attr': 'dex',
                'trained': True,
                'penalties': 'armor',
                'rank': 0,
                'adjust': 0
            },
            'spellcraft': {
                'name': 'Spellcraft',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Spellcraft'
                'attr': 'int',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'stealth': {
                'name': 'Stealth',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Stealth'
                'attr': 'dex',
                'trained': False,
                'penalties': 'armor',
                'rank': 0,
                'adjust': 0
            },
            'survival': {
                'name': 'Survival',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Survival'
                'attr': 'wis',
                'trained': False,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            },
            'swim': {
                'name': 'Swim',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Swim'
                'attr': 'str',
                'trained': False,
                'penalties': 'armor',
                'rank': 0,
                'adjust': 0
            },
            'use_magic_device': {
                'name': 'Use Magic Device',
                'nethys_link': 'https://aonprd.com/Skills.aspx?ItemName=Use%20Magic%20Device'
                'attr': 'cha',
                'trained': True,
                'penalties': '',
                'rank': 0,
                'adjust': 0
            }
        }
    }

    id = 'uuid_' + uuid.uuid4().hex
    r_set('character', id, char)

    return Character(id)
