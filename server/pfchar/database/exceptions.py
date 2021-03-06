class DatabaseError(Exception):
    pass


class UserError(DatabaseError):
    pass


class UserNotFoundError(UserError):
    pass


class UserPasswordError(UserError):
    pass


class CharacterError(DatabaseError):
    pass


class CharacterWrongUserError(CharacterError):
    pass


class CharacterReadError(CharacterError):
    pass


class CharacterWriteError(CharacterError):
    pass
