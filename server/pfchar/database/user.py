import bcrypt
import uuid
import json
from pfchar.database.connection import r_get, r_set, r_exists, r_append
from pfchar.database.exceptions import UserNotFoundError, UserPasswordError
from pfchar.database.character import new_char, Character


class User(object):
    def __init__(self, email=None, uid=None):
        self._uid = None

        if uid is not None:
            self._uid = uid
            if not r_exists('users', self._uid):
                raise UserNotFoundError('Could not retrieve the user with the provided uid.')
        elif email is not None:
            self._get_user_by_email(email)
        else:
            raise UserNotFoundError('Could not get the user either by the provided email or uid.')

    def _get_user_by_email(self, email):
        all_users = r_get('users')
        for uid, userdata in all_users.items():
            if userdata['email'] == email:
                self._uid = uid

        if self._uid is None:
            raise UserNotFoundError('Could not find the user with the specified email.')

    def check_password(self, password):
        hashed_pw = r_get('users', self._uid + '.password').encode()
        if not bcrypt.checkpw(password.encode(), hashed_pw):
            raise UserPasswordError('The provided password is not correct.')

    @property
    def uid(self):
        return self._uid

    @property
    def email(self):
        return r_get('users', self._uid + '.email')

    @property
    def characters(self):
        charids = r_get('users', self._uid + '.characters')
        chars = []
        for charid in charids:
            chars.append(Character(charid, self._uid))

        return chars

    @property
    def last_selected_char(self):
        charid = r_get('users', self._uid + '.last_selected');
        return Character(charid)

    def add_character(self, char):
        r_append('users', self._uid + '.characters', char.id)


def new_user(email, password):
    uid = 'uuid_' + uuid.uuid4().hex
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = {
        'password': hashed_pw.decode('utf-8'),
        'email': email,
        'characters': [],
        'last_selected': ''
    }

    r_set('users', uid, user)

    return User(email=email)
