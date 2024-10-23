fake.py vs factory_boy
======================
.. _factory_boy: https://factoryboy.readthedocs.io/
.. _fake.py: https://fakepy.readthedocs.io/
.. _minimal factories results: results/minimal.txt

`fake.py`_ vs `factory_boy`_ factories benchmark.

Prerequisites
-------------
Install
~~~~~~~
.. code-block:: sh

    pip install -r requirements.in

Migrate
~~~~~~~
.. code-block:: sh

    python manage.py migrate

Usage
-----
.. code-block:: sh

    python manage.py run_django_auth_user_minimal_benchmark

Results
-------
Minimal factories
~~~~~~~~~~~~~~~~~
Generation of 100 (Django) ``User`` records using identical factories:

- `fake.py`_: 11.699 seconds
- `factory_boy`_: 12.062 seconds

See `minimal factories results`_ for details.
