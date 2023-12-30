from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 1
def test_ingredient():
    carne = "carne"
    queijo = "queijo"
    presunto = "presunto"
    bacon = "bacon"

    assert Ingredient(presunto).name == presunto

    response = f"Ingredient('{presunto}')"
    assert str(Ingredient(presunto)) == response

    assert Ingredient(presunto) == Ingredient(presunto)
    assert Ingredient(presunto) != Ingredient(bacon)
    assert Ingredient(presunto) != Ingredient(carne)

    assert hash(Ingredient(presunto)) == hash(Ingredient(presunto))
    assert hash(Ingredient(presunto)) != hash(Ingredient(bacon))
    assert hash(Ingredient(presunto)) != hash(Ingredient(carne))

    restrict_item_presunto = Ingredient(presunto).restrictions
    assert "ANIMAL_DERIVED" in {
        restriction.value for restriction in restrict_item_presunto
    }

    restrict_item_carne = Ingredient(carne).restrictions
    assert "ANIMAL_DERIVED" in {
        restriction.value for restriction in restrict_item_carne
    }

    restrict_item_bacon = Ingredient(bacon).restrictions
    assert "ANIMAL_DERIVED" in {
        restriction.value for restriction in restrict_item_bacon
    }

    restrict_item_queijo = Ingredient(queijo).restrictions
    assert len(restrict_item_queijo) == 0