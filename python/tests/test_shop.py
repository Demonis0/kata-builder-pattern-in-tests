from shop import ConcreteUserBuilder, Shop, User

user = User()

def test_happy_path():
    # user.address = fsf_address
    # user.age = 25
    # user.verified = True

    user = ConcreteUserBuilder()
    user = user.user

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    # user.address = fsf_address
    # user.age = 16
    # user.verified = True

    user = ConcreteUserBuilder()
    user.underage()
    user = user.user

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    # user.address = fsf_address
    # user.age = 25
    # user.verified = False

    user = ConcreteUserBuilder()
    user.not_verified()
    user = user.user

    assert not Shop.can_order(user)

def test_foreigners_must_be_foreign_fee():
    # user.address = paris_address
    # user.age = 25
    # user.verified = True

    user = ConcreteUserBuilder()
    user.address_france()
    user = user.user

    assert Shop.must_pay_foreign_fee(user)
