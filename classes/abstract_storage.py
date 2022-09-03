from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, name: str, amount: int) -> None:  # добавляет товар
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:   #вычитатет товар со склада при заказе на магазин
        pass

    @abstractmethod
    def get_free_space(self) -> int:    # проверка свободного места
        pass

    @abstractmethod
    def get_items(self):    #список товара в местах хранения
        pass

    @abstractmethod
    def get_unique_items_count(self):   #проверка количество уникальных товаров
        pass
