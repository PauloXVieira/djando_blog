import string
from random import SystemRandom
from django.utils.text import slugify


def randon_latters(k=5):
    return "".join(SystemRandom().choices(string.ascii_lowercase + string.digits, k=k))


def slugify_new(text, k=5):
    return slugify(text) + "-" + randon_latters(k)
