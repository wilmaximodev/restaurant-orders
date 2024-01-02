import csv
from models.dish import Dish
from models.ingredient import Ingredient

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._menu_data(source_path)

    def _menu_data(self, source_path: str) -> None:
        with open(source_path) as csv_file:
            reader = csv.reader(csv_file)
            
            next(reader)
            
            dishes_data = {}

            for row in reader:
                dish_name = row[0]
                price_str = row[1]
                ingredient_name = row[2]
                quantity_str = row[3]
                
                price = float(price_str)
                quantity = int(quantity_str)
                dish = dishes_data.get(dish_name)
                if not dish:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)
                    dishes_data[dish_name] = dish

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, quantity)
