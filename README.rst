.. image:: https://img.shields.io/travis/ExCiteS/geokey-extension-boilerplate/master.svg
    :alt: Travis CI Build Status
    :target: https://travis-ci.org/ExCiteS/geokey-extension-boilerplate

.. image:: https://img.shields.io/coveralls/ExCiteS/geokey-extension-boilerplate/master.svg
    :alt: Coveralls Test Coverage
    :target: https://coveralls.io/r/ExCiteS/geokey-extension-boilerplate

geokey-extension-boilerplate
============================

This is my awesome GeoKey extension.

Install
-------

Install the extension from PyPI:

.. code-block:: console

    pip install geokey-extension-boilerplate

Or from cloned repository:

.. code-block:: console

    cd geokey-extension-boilerplate
    pip install -e .

Add the package to installed apps:

.. code-block:: console

    INSTALLED_APPS += (
        ...
        'geokey_extension_boilerplate',
    )

Migrate the models into the database:

.. code-block:: console

    python manage.py migrate geokey_extension_boilerplate

Copy static files:

.. code-block:: console

    python manage.py collectstatic

You're now ready to go!

Test
----

Run tests:

.. code-block:: console

    python manage.py test geokey_extension_boilerplate

Check code coverage:

.. code-block:: console

    coverage run --source=geokey_extension_boilerplate manage.py test geokey_extension_boilerplate
    coverage report -m --omit=*/tests/*,*/migrations/*
