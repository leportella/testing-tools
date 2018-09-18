from datetime import datetime

import factory
from factory import fuzzy
from pytz import utc

from student.models import Student, Parent


class ParentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Parent

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student

    parent = factory.SubFactory(ParentFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    resume = factory.Faker('text')
    age = fuzzy.FuzzyInteger(6, 12)
    email = factory.LazyAttribute(
        lambda o: f'{o.first_name.lower()}.{o.last_name.lower()}@mail.org')
    date_started = fuzzy.FuzzyDateTime(datetime.now(tz=utc))
    gender = fuzzy.FuzzyChoice(['male', 'female', 'other'])
