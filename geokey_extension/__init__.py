from geokey.extensions.base import register


VERSION = (0, 0, 0)
__version__ = '.'.join(map(str, VERSION))

register(
    'geokey_extension',
    'My Awesome Extension',
    display_admin=True,
    superuser=False
)
