import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 150
    ingredient.get_name.return_value = "mock ingredient"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient

def test_set_buns(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun.get_name() == "mock bun"

def test_add_remove_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

def test_move_ingredient(mock_ingredient):
    burger = Burger()
    burger.add_ingredient(MagicMock(get_name=lambda: "a", get_type=lambda: INGREDIENT_TYPE_SAUCE, get_price=lambda: 10))
    burger.add_ingredient(MagicMock(get_name=lambda: "b", get_type=lambda: INGREDIENT_TYPE_FILLING, get_price=lambda: 10))
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0].get_name() == "b"

def test_get_price(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert burger.get_price() == 100 * 2 + 150

def test_get_receipt(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    receipt = burger.get_receipt()
    assert "mock bun" in receipt
    assert "mock ingredient" in receipt
    assert "Price: 350" in receipt
