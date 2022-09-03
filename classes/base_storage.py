from typing import Dict

from classes.abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProducts


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], quantity: int):

        self.__items = items
        self.__quantity = quantity

    def add(self, name: str, amount: int):
        """добавляет товар"""
        # если места на складе меньше чем товара
        if self.get_free_space() < amount
            raise NotEnoughSpace  # если места нет ошибка недостаточно места

        if name in self.__items:  # если уже был товар плюсуем количество
            self.__items[name] += amount

        else:  # если товара не было раньше просто заводим количество
            self.__items[name] += amount

    def remove(self, name: str, amount: int) -> None:
        """проверяет что товара достаточно на складе"""
        if name not in self.__items or self.__items[name] < amount:
            # если товара нет вообще либо товара не хватает
            raise NotEnoughProducts  # ошибка недостаточно товара

        # если товара хватает вычитаем количество требуемого товара
        self.__items[name] -= amount
        # если количество товара становиться 0 выводим из списка доступных
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_items(self) -> Dict[str, int]:
        """получает список товара через ф-ю"""
        return self.__items

    def get_free_space(self) -> int:
        """проверяет достаточно ли места"""
        current_space = 0
        for value in self.__items.values():
            current_space += value  # уже занято

        return self.__quantity - current_space  # считаем свободное место, из емкости храна вычитаем что уже есть

    def get_unique_items_count(self):
        """получает количество уникальных товаров"""
        return len(self.__items) #количество ключей в словаре