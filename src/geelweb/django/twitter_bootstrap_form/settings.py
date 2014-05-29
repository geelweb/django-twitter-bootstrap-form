from django.conf import settings

BOOTSTRAP_REQUIRED_SUFFIX = getattr(settings, 'BOOTSTRAP_REQUIRED_SUFFIX', ' *')
