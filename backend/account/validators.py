import re

from django.core.exceptions import ValidationError


def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError('Допустимые символы a-z, A-Z, 0-9, _')