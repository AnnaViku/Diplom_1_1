import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_name.return_value = "mock ingredient"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_price.return_value = 150
    return ingredient


def test_get_receipt_exact(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    expected_receipt = (
        "(==== mock bun ====)\n"
        "= filling mock ingredient =\n"
        "(==== mock bun ====)\n\n"
        "Price: 350"
    )

    actual_receipt = burger.get_receipt()
    assert actual_receipt == expected_receipt

