import json

from flask import request, session, make_response
from pfchar.database.character import Character
from pfchar.database.exceptions import CharacterReadError, CharacterWriteError, CharacterWrongUserError


class RESt(object):
    def __init__(self):
        super(RESt, self).__init__()

    def _unauthorized(self):
        return self._json_response({
            'status': 'error',
            'message': 'You are not authorized to access this ressource.'
        }, 401)

    def _bad_request(self):
        return self._json_response({
            'status': 'error',
            'message': 'Data you submitted was not formatted properly. Please try again.'
        }, 400)

    def _json_response(self, data, status):
        return make_response(data, status, {
            'Content-Type': 'application/json'
        })

    def character(self, charid):
        if not session.get('loggedin', False):
            return _unauthorized()

        try:
            char = Character(charid, session.get('uid'))
        except CharacterWrongUserError as e:
            return _unauthorized()

        if request.method == 'GET':
            return self._json_response(char.complete, 200)
        else:
            data = request.get_json()
            if 'path' not in data or 'value' not in data:
                return self._bad_request()

            try:
                char.set(data['path'], data['value'])
            except CharacterWriteError as e:
                return self._json_response({
                    'status': 'error',
                    'message': 'Could not set the value "' + json.dumps(data['value']) + '" for key "' + data['path'] + '"'
                }, 500)

            return ('', 204)
