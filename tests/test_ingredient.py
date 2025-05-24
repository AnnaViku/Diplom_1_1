import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("type_", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def test_ingredient_get_type(type_):
    ingredient = Ingredient(type_, "Test", 100)
    assert ingredient.get_type() == type_

@pytest.mark.parametrize("name", ["hot sauce", "cutlet"])
def test_ingredient_get_name(name):
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100)
    assert ingredient.get_name() == name

@pytest.mark.parametrize("price", [100, 250])
def test_ingredient_get_price(price):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Test", price)
    assert ingredient.get_price() == price

