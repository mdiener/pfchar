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
        char = r_get('characters', self._char_id)
        return json.dumps(char)

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
        }
    }

    id = 'uuid_' + uuid.uuid4().hex
    r_set('character', id, char)

    return Character(id)
