"""
AccountFactory class using FactoryBoy

Documentation on Faker Providers:
    https://faker.readthedocs.io/en/master/providers/baseprovider.html

Documentation on Fuzzy Attributes:
    https://factoryboy.readthedocs.io/en/stable/fuzzy.html

"""
import factory
from datetime import date
from factory.fuzzy import FuzzyChoice, FuzzyDate
from models.account import Account

class AccountFactory(factory.Factory):
    """ Creates fake Accounts """

    class Meta:
        model = Account

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    disabled = FuzzyChoice(choices=[True, False])
    date_joined = FuzzyDate(date(2008, 1, 1))