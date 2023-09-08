from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    # Test valid dish creation
    dish = Dish("Spaghetti Carbonara", 15.99)
    assert dish.name == "Spaghetti Carbonara"
    assert dish.price == 15.99

    # Test __repr__
    assert repr(dish) == "Dish('Spaghetti Carbonara', R$15.99)"

    # Test equality (__eq__)
    same_dish = Dish("Spaghetti Carbonara", 15.99)
    different_dish = Dish("Lasagna", 12.99)

    assert dish == same_dish
    assert dish != different_dish

    # Test hash (__hash__)
    assert hash(dish) == hash(same_dish)
    assert hash(dish) != hash(different_dish)

    # Test adding ingredient dependencies
    tomato = Ingredient("tomato")
    bacon = Ingredient("bacon")
    cheese = Ingredient("cheese")

    dish.add_ingredient_dependency(tomato, 2)
    dish.add_ingredient_dependency(bacon, 3)
    dish.add_ingredient_dependency(cheese, 1)

    assert dish.recipe == {tomato: 2, bacon: 3, cheese: 1}

    # Test get_restrictions
    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    # Test get_ingredients
    assert dish.get_ingredients() == {tomato, bacon, cheese}

    # Test invalid dish creation
    with pytest.raises(TypeError):
        Dish("Invalid Dish", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Invalid Dish", -10.0)

    # Test accessing quantity of ingredient
    assert dish.recipe.get(tomato) == 2
    assert dish.recipe.get(bacon) == 3
    assert dish.recipe.get(cheese) == 1

    # Test that accessing a non-existent ingredient returns None
    mushroom = Ingredient("mushroom")
    assert dish.recipe.get(mushroom) is None
