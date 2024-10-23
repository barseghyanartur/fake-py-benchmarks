"""
Which one is more performant?

```
In [1]: from faker import Faker

In [2]: FAKER = Faker()

In [3]: from fake import FAKER as FAKEPY

In [4]: from mimesis import Person

In [5]: FAKER.user_name()
Out[5]: 'anncraig'

In [6]: FAKEPY.username()
Out[6]: 'special_that_nested_ptwsltqbxwkieqprarpa'

In [7]: MIMESIS = Person()

In [8]: MIMESIS.username()
Out[8]: 'situated_1994'

In [9]: %timeit FAKER.user_name()
111 µs ± 17.5 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [10]: %timeit FAKEPY.username()
5.54 µs ± 97.6 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [10]: %timeit MIMESIS.username()
4.16 µs ± 128 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
```
"""

import cProfile

from mimesis import Person
from mimesis.locales import Locale
from faker import Faker
from fake import FAKER
from humanize.number import intcomma

MIMESIS = Person(Locale.EN)
FAKER_FAKER = Faker()


def calculate_uniqueness(iterations, sequence):
    unique_names_count = len(set(sequence))
    uniqueness = round((unique_names_count / iterations) * 100, 2)
    return f'{intcomma(unique_names_count)} of {intcomma(iterations)} ({uniqueness}%) are unique'


counts = (
    10_000,
    100_000,
    1_000_000,
)

for count in counts:
    names_mimesis = [MIMESIS.username() for _ in range(count)]
    print('[Mimesis] {}'.format(calculate_uniqueness(count, names_mimesis)))
    print('*' * 20)

    print('Generating using Mimesis:')
    cProfile.run('[MIMESIS.username() for _ in range(count)]')
    print('*' * 20)

    names_faker = [FAKER_FAKER.user_name() for _ in range(count)]
    print('[Faker] {}'.format(calculate_uniqueness(count, names_faker)))
    print('*' * 20)

    print('Generating using Faker:')
    cProfile.run('[FAKER_FAKER.user_name() for _ in range(count)]')
    print('*' * 20)

    names_fakepy = [FAKER.username() for _ in range(count)]
    print('[fake.py] {}'.format(calculate_uniqueness(count, names_fakepy)))
    print('*' * 20)

    print('Generating using fake.py:')
    cProfile.run('[FAKER.username() for _ in range(count)]')
    print('*' * 20)

    print('-----' * 20)
