import json
import redis
from redis.exceptions import RedisError
from pfchar.settings import DB_HOST, DB_PORT, DB_NR
from pfchar.database.exceptions import DatabaseError


redis_instance = redis.Redis(host=DB_HOST, port=DB_PORT, db=DB_NR)

if not redis_instance.exists('users'):
    redis_instance.execute_command('JSON.SET', 'users', '.', json.dumps({}))
if not redis_instance.exists('characters'):
    redis_instance.execute_command('JSON.SET', 'characters', '.', json.dumps({}))


def r_get(key, *args):
    try:
        path = args[0]
    except IndexError as e:
        path = ''

    try:
        result = redis_instance.execute_command('JSON.GET', key, '.' + path)
    except RedisError as e:
        print(str(e))
        raise DatabaseError('Could not get the value at key "' + key + '" with path "' + path + '".')

    if result is not None:
        return json.loads(result)
    else:
        return None


def r_set(key, *args):
    if len(args) == 1:
        path = ''
        value = args[0]
    elif len(args) == 2:
        path = args[0]
        value = args[1]

    try:
        redis_instance.execute_command('JSON.SET', key, '.' + path, json.dumps(value))
    except RedisError as e:
        print(str(e))
        raise DatabaseError('Could not set the value "' + value + '" at key "' + key + '" with path "' + path + '".')



def r_exists(key, *args):
    if len(args) == 0:
        path = ''
    else:
        path = args[0]

    try:
        result = redis_instance.execute_command('JSON.TYPE', key, '.' + path)
    except RedisError as e:
        print(str(e))
        raise DatabaseError('There was an error when trying to determine if path "' + path + '" exists at "' + key + '".')

    return result is None


def r_append(key, *args):
    if len(args) == 1:
        path = ''
        value = args[0]
    elif len(args) == 2:
        path = args[0]
        value = args[1]

    try:
        redis_instance.execute_command('JSON.ARRAPPEND', key, '.' + path, json.dumps(value))
    except RedisError as e:
        print(str(e))
        raise DatabaseError('Could not append "' + value + '" at key "' + key + '" with path "' + path + '".')
