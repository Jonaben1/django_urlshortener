from django.conf import settings
from random import choice
from string import ascii_letters, digits


SIZE = getattr(settings, 'MAXIMUM_URL_CHARS', 7)
CHARS = ascii_letters + digits

def random_code(chars=CHARS):
    return ''.join([choice(chars) for _ in range(SIZE)])



def unique_code(instance):
    shorten_code = random_code()
    model_class = instance.__class__
    if model_class.objects.filter(short_url=shorten_code).exists():
        return unique_code(instance)
    return shorten_code


