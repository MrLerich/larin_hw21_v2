from typing import Dict

from classes.base_storage import BaseStorage
from classes.exceptions import TooManyDifferentProducts


class Shop(BaseStorage):
    def __init__(self, items: Dict, quantity: int = 20):
        super().__init__(items, quantity)

    # def __repr__(self):
    #     return f"{self.items}: {self.quantity}"

    def add(self, name: str, amount: int):
        # может быть в магазиен 5 уник товаров
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts  # ошибка слишком много униктоваров

        super().add(name, amount)  # остальное как в родительксом классе
