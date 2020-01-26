import bcrypt
import uuid
import json
from pfchar.database.connection import r_get, r_set, r_exists
from pfchar.database.exceptions import UserNotFoundError, UserPasswordError
from pfchar.database.character import new_char


class User(object):
    def __init__(self, email=None, uid=None):
        self._uid = None

        if userid is not None:
            self._uid = userid
            if r_exists('users', self._uid):
                raise UserNotFoundError('Could not retrieve the user with the provided uid.')
        elif email is not None:
            self._get_user_by_email(email)
        else:
            raise UserNotFoundError('Could not get the user either by the provided email or uid.')

    def _get_user_by_email(self, email):
        all_users = r_get('users')
        for uid, user in all_users.items():
            if user['email'] == email:
                self._uid = uid

        if self._user is None:
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
        return r_get('users', self._uid + '.characters')

    @property
    def last_selected_char(self):
        return r_get('users', self._uid + '.last_selected')

    def new_character(self):
        char = new_char(self._uid)

        r_append('users', self._uid + '.characters', char)


def new_user(email, password):
    uid = str(uuid.uuid4())
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = {
        'password': hashed_pw.decode('utf-8'),
        'email': email,
        'characters': [],
        'last_selected': ''
    }

    r_set('users', uid, json.dumps(user))

    return User(uid=uid)
