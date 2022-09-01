from classes.abstract_storage import AbstractStorage


class Shop(AbstractStorage):
    def __init__(self, capacity: int = 20):
        self._capacity = capacity
        self._items = {}

    def __repr__(self):
        return f"{self._items}: {self._capacity}"


    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title: str, quantity: int):
        if self._items.get(title):
            self._items[title] += quantity
        else:
            self._items[title] = quantity

    def remove(self, title: str, quantity: int):
        self._items[title] -= quantity

    def get_free_space(self):
        busy_space = 0
        for item in self._items.items():
            busy_space += item[1]

        return self._capacity - busy_space

    def get_items(self):
        """"""
        return self._items

    def get_unique_items_count(self):
        return len(self._items)

    def check_add(self, title: str, quantity: int):
        if ((self.get_unique_items_count() < 6 or title in self._items.keys())
                and self.get_free_space() >= quantity):
            return True
        else:
            return False
