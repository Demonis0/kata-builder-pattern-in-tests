from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Address:
    line1: str
    line2: str
    city: str
    zip_code: str
    country: str


@dataclass
class User:
    name: str
    email: str
    age: int
    address: Address
    verified: bool
    
    def __init__(self):
        self.name = "Bob"
        self.email = "bob@domain.tld"
        self.age = 20
        self.address = Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")
        self.verified = True


## Source aide builder pattern en python : https://refactoring.guru/design-patterns/builder/python/example
class UserBuilder(ABC):
    @property
    @abstractmethod
    def user(self) -> None:
        pass

    @abstractmethod
    def underage(self) -> None:
        pass

    @abstractmethod
    def not_verified(self) -> None:
        pass

    @abstractmethod
    def foreign(self) -> None:
        pass


class ConcreteUserBuilder(UserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._user = User()

    @property
    def user(self) -> User:
        user = self._user
        self.reset()
        return user

    def address_usa(self) -> None:
        self._user.address = Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")

    def address_france(self) -> None:
        self._user.address = Address("33 quai d'Orsay", "", "Paris", "75007", "France")

    def underage(self) -> None:
        self._user.age = 16

    def not_verified(self) -> None:
        self._user.verified = False

    def foreign(self) -> None:
        self._user.address.country = "France"


class UserUnderage():
    def __init__(self) -> None:
        pass

    def get_user(self) -> User:
        builder = ConcreteUserBuilder()
        builder.underage()
        return builder.user


class UserDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> UserBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: UserBuilder) -> None:
        self._builder = builder


class Shop:
    @classmethod
    def can_order(cls, user):
        if user.age <= 18:
            return False
        if not user.verified:
            return False
        else:
            return True

    @classmethod
    def must_pay_foreign_fee(cls, user):
        return user.address.country != "USA"
