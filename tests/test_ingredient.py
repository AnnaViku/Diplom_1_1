from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 250),
])
def test_ingredient_getters(type_, name, price):
    ingredient = Ingredient(type_, name, price)
    assert ingredient.get_type() == type_
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
