from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu = []
        for dish in self.menu_data.dishes:
            dish_restrictions = dish.get_restrictions()
            dish_ingredients = dish.get_ingredients()

            if (
                restriction is None or restriction not in dish_restrictions
            ) and all(
                ingredient in self.inventory.inventory
                for ingredient in dish_ingredients
            ):
                menu.append(
                    {
                        "ingredients": dish_ingredients,
                        "price": dish.price,
                        "dish_name": dish.name,
                        "restrictions": list(dish_restrictions),
                    }
                )
        return menu
