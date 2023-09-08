from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("Spaghetti Carbonara", 15.99)
    assert dish.name == "Spaghetti Carbonara"
    assert dish.price == 15.99

    assert repr(dish) == "Dish('Spaghetti Carbonara', R$15.99)"

    same_dish = Dish("Spaghetti Carbonara", 15.99)
    different_dish = Dish("Lasagna", 12.99)

    assert dish == same_dish
    assert dish != different_dish

    assert hash(dish) == hash(same_dish)
    assert hash(dish) != hash(different_dish)

    tomato = Ingredient("tomato")
    bacon = Ingredient("bacon")
    cheese = Ingredient("cheese")

    dish.add_ingredient_dependency(tomato, 2)
    dish.add_ingredient_dependency(bacon, 3)
    dish.add_ingredient_dependency(cheese, 1)

    assert dish.recipe == {tomato: 2, bacon: 3, cheese: 1}

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert dish.get_ingredients() == {tomato, bacon, cheese}

    with pytest.raises(TypeError):
        Dish("Invalid Dish", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Invalid Dish", -10.0)

    assert dish.recipe.get(tomato) == 2
    assert dish.recipe.get(bacon) == 3
    assert dish.recipe.get(cheese) == 1

    mushroom = Ingredient("mushroom")
    assert dish.recipe.get(mushroom) is None
