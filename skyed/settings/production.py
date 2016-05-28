from .base import *

DEBUG = False
SECRET_KEY = 'c(qefe16js8xm7*kzy#m*sorafo=^c9oe+zi$p4sq+1mw56765ufdgfp+n!efefef'
ALLOWED_HOSTS=['skyed.pythonanywhere.com','localhost']

try:
    from .local import *
except ImportError:
    pass
