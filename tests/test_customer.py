import pytest
from models.customer import Customer


def test_name_is_cleaned():
    assert Customer("  hope kathomi ", "Driver 10002").name == "Hope Kathomi"


def test_empty_name_fails():
    with pytest.raises(ValueError):
        Customer("   ", "Driver 10002")


def test_driver_id_is_kept_as_given():
    assert Customer("Sandra", "Driver 10002").driver_id == "Driver 10002"


def test_empty_driver_id_fails():
    with pytest.raises(ValueError):
        Customer("Sandra", "   ")


def test_negative_payment_fails():
    with pytest.raises(ValueError):
        Customer("Sandra", "Driver 10002", -50)


def test_add_payment():
    c = Customer("Kinya", "Driver 10002", 100)
    c.add_payment(50)
    assert c.payment == 150


def test_add_payment_zero_fails():
    c = Customer("Kinya", "Driver 10002")
    with pytest.raises(ValueError):
        c.add_payment(0)


def test_to_dict_and_from_dict():
    c = Customer("Bradley", "Driver 10003", 200)
    copy = Customer.from_dict(c.to_dict())
    assert copy.name == "Bradley"
    assert copy.driver_id == "Driver 10003"
    assert copy.payment == 200
