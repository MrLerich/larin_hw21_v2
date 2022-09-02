from typing import Any, Dict

from classes.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], quantity: int):

        self.__items = items
        self.__quantity = quantity

    def add(self, name: str, amount: int):

