from .base import *
import os


if os.environ.get("DJANGO_DEVELOPMENT") == 'production':
    from .production import *
elif os.environ.get("DJANGO_DEVELOPMENT") == 'local':
    from .local import *
else:
    from .local import *

