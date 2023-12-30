import pytest
from src.models.dish import Dish
from src.models.ingredient import Restriction, Ingredient


def test_dish():
    # Criando pratos de exemplo
    lasanha_presunto = Dish("lasanha presunto", 25.90)
    lasanha_berinjela = Dish("lasanha berinjela", 27.00)

    # Testando a representação em string do prato
    assert lasanha_presunto.__repr__() == "Dish('lasanha presunto', R$25.90)"

    # Testando os atributos do prato
    assert lasanha_presunto.name == "lasanha presunto"
    assert lasanha_presunto.price == 25.90

    # Testando a igualdade entre pratos
    assert lasanha_presunto.__eq__(lasanha_presunto) is True
    assert lasanha_presunto.__eq__(lasanha_berinjela) is False

    # Testando o hash do prato
    assert lasanha_presunto.__hash__() == hash(lasanha_presunto.__repr__())
    assert lasanha_presunto.__hash__() != hash(lasanha_berinjela.__repr__())

    # Verificando se o preço do prato é um número float
    with pytest.raises(TypeError):
        Dish("macarrão", "25")

    # Verificando se o preço do prato é maior que zero
    with pytest.raises(ValueError):
        Dish("lasanha presunto", -25)

    # Adicionando um ingrediente ao prato
    presunto = Ingredient("presunto")
    lasanha_presunto.add_ingredient_dependency(presunto, 15)

    # Verificando se o prato possui os ingredientes esperados
    assert lasanha_presunto.get_ingredients() == {presunto}

    # Verificando se o prato possui as restrições esperadas
    expected_restrictions = {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert lasanha_presunto.get_restrictions() == expected_restrictions
