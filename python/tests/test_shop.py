from shop import Shop, User

user = User(
        name="bob",
        email="bob@domain.tld"
    )

def test_happy_path(fsf_address):
    user.address = fsf_address
    user.age = 25
    user.verified = True

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(fsf_address):
    user.address = fsf_address
    user.age = 16
    user.verified = True

    assert not Shop.can_order(user)



def test_cannot_order_if_not_verified(fsf_address):
    user.address = fsf_address
    user.age = 25
    user.verified = False

    assert not Shop.can_order(user)

def test_foreigners_must_be_foreign_fee(paris_address):
    user.address = paris_address
    user.age = 25
    user.verified = True

    assert Shop.must_pay_foreign_fee(user)
