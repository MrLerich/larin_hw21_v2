from typing import Dict

from classes.base_storage import BaseStorage


class Store(BaseStorage):

    def __init__(self, items: Dict, quantity: int = 100):
        super().__init__(items, quantity)

    # def __repr__(self):
    #     return f"{self.items}: {self.quantity}"


