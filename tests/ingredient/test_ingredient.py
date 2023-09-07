from src.models.ingredient import Ingredient, Restriction, restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    beef_ingredient = Ingredient("beef")
    chicken_ingredient = Ingredient("chicken")

    assert beef_ingredient.name == "beef"
    assert chicken_ingredient.name == "chicken"

    expected_beef_restrictions = restriction_map().get("beef", set())
    assert beef_ingredient.restrictions == expected_beef_restrictions

    assert hash(beef_ingredient) == hash("beef")
    assert hash(chicken_ingredient) == hash("chicken")

    assert beef_ingredient.__eq__(beef_ingredient) is True
    assert beef_ingredient.__eq__(chicken_ingredient) is False
    assert beef_ingredient == beef_ingredient
    assert beef_ingredient != chicken_ingredient

    assert repr(beef_ingredient) == "Ingredient('beef')"
    assert repr(chicken_ingredient) == "Ingredient('chicken')"
