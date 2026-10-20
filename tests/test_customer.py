import pytest
from models.customer import Customer


def test_name_is_cleaned():
    assert Customer("  hope kathomi ", "DL-12345").name == "Hope Kathomi"


def test_empty_name_fails():
    with pytest.raises(ValueError):
        Customer("   ", "DL-12345")


def test_short_driver_id_fails():
    with pytest.raises(ValueError):
        Customer("Sandra", "12")


def test_negative_payment_fails():
    with pytest.raises(ValueError):
        Customer("Sandra", "DL-12345", -50)


def test_add_payment():
    c = Customer("Kinya", "DL-12345", 100)
    c.add_payment(50)
    assert c.payment == 150


def test_add_payment_zero_fails():
    c = Customer("Kinya", "DL-12345")
    with pytest.raises(ValueError):
        c.add_payment(0)
