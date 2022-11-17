from enum import Enum


class ErrorCode(Enum):
    NO_ERROR = {'code': 0, 'message': 'Ok'}
    INVALID_NAME = {'code': 1, 'message': 'Invalid name'}
    INVALID_EMAIL = {'code': 2, 'message': 'Invalid email'}
    INVALID_USER = {'code': 3, 'message': 'Invalid user'}
    ERROR_GENERIC = {'code': 4, 'message': 'Generic error'}
