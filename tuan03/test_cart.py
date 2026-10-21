import pytest

from tuan03.cart import calculate_total


def test_empty_cart():
    assert calculate_total([]) == 0


def test_one_item():
    assert calculate_total([(25000, 2)]) == 50000


def test_multiple_items():
    assert calculate_total([(25000, 2), (10000, 3)]) == 80000


def test_free_item():
    assert calculate_total([(0, 2)]) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total([(-1000, 1)])


@pytest.mark.parametrize("quantity", [0, -1])
def test_invalid_quantity(quantity):
    with pytest.raises(ValueError):
        calculate_total([(25000, quantity)])


@pytest.mark.parametrize("price", [12.5, "25000", True])
def test_price_must_be_integer(price):
    with pytest.raises(TypeError):
        calculate_total([(price, 1)])


@pytest.mark.parametrize("quantity", [1.5, "2", True])
def test_quantity_must_be_integer(quantity):
    with pytest.raises(TypeError):
        calculate_total([(25000, quantity)])
