fake.py vs Faker vs mimesis
===========================
.. _Faker: https://faker.readthedocs.io/
.. _fake.py: https://fakepy.readthedocs.io/
.. _mimesis: https://mimesis.readthedocs.io/
.. _username results: results/username.txt

`fake.py`_ vs `mimesis`_ vs `Faker`_ ``username`` benchmark.

Prerequisites
-------------
Install
~~~~~~~
.. code-block:: sh

    pip install -r requirements.in

Usage
-----
.. code-block:: sh

    python username.py

Results
-------
username
~~~~~~~~
**Generating 10,000 usernames:**

- `mimesis`_: 0.121 seconds. 9,985 of 10,000 (99.85%) are unique.
- `Faker`_: 1.250 seconds. 9,433 of 10,000 (94.33%) are unique
- `fake.py`_: 0.193 seconds. 10,000 of 10,000 (100.0%) are unique.

**Generating 100,000 usernames:**

- `mimesis`_: 1.228 seconds. 98,269 of 100,000 (98.27%) are unique.
- `Faker`_: 12.395 seconds. 72,111 of 100,000 (72.11%) are unique.
- `fake.py`_: 1.872 seconds. 100,000 of 100,000 (100.0%) are unique.

**Generating 1,000,000 usernames:**

- `mimesis`_: 12.288 seconds. 843,729 of 1,000,000 (84.37%) are unique.
- `Faker`_: 139.753 seconds. 343,662 of 1,000,000 (34.37%) are unique.
- `fake.py`_: 19.956 seconds. 1,000,000 of 1,000,000 (100.0%) are unique.

See `username results`_ for details.
