from typing import Dict

from classes.abstract_storage import AbstractStorage
from classes.exceptions import InvalidRequest, InvalidStorageName


class Request:

    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        self.__request = request
        splitted_request = request.lower().split(" ")  # делаем из запроса список

        if len(splitted_request) != 7:
            raise InvalidRequest
        # смотрим по шаблону запроса от пользователя что на каком месте стоит
        self.amount = int(splitted_request[1])  # количество
        self.product = splitted_request[2]  # наименований товара
        self.departure = splitted_request[4]  # откуда перемещает
        self.destination_point = splitted_request[6]  # точка назначения

        # проверяем место куда.откуда перемещаем товар
        if self.departure not in storages or self.destination_point not in storages:
            raise InvalidStorageName
