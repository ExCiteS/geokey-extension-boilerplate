"""Main initialisation for extension."""

VERSION = (0, 0, 0)
__version__ = '.'.join(map(str, VERSION))


try:
    from geokey.extensions.base import register

    register(
        'geokey_extension',
        'My Awesome Extension',
        display_admin=True,
        superuser=False,
        version=__version__
    )
except BaseException:
    print 'Please install GeoKey first'
