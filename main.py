from classes.courier import Courier
from classes.exceptions import BaseError
from classes.request import Request
from classes.shop import Shop
from classes.store import Store

store = Store({
    "печенька": 25,
    "собачка": 25,
    "елка": 25,
    "крокодил": 10,
    "жратва": 10,
    "чебурашка": 4
})
shop = Shop({
    "печенька": 2,
    "собачка": 2,
    "елка": 2,
    "крокодил": 1,
    "чебурашка": 1
})
storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print("\nДобро пожаловать!\n")

    while True:
        # выводим все товары для всех хранилищ
        for storage_name in storages:
            print(f"Сейчас на {storage_name}:\n {storages[storage_name].get_items()}")

        # забираем у пользователя запрос
        user_typing = input(
            "Введите запрос вида 'Доставить 3 печенька из склад в магазин'\n"
            "(для выхода:'стоп' или 'stop'\n"
        )
        if user_typing.lower() in ('стоп', 'stop'):
            print("До свидания!")
            break

        # формируем запрос на перемещение
        try:
            request = Request(request=user_typing, storages=storages)
        except BaseError as error:     #InvalidRequest, InvalidStorageName
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        # перемещение товара
        try:
            courier.move()

        except BaseError as error:
            print(error.message)
            courier.cancel()
            continue

if __name__ == "__main__":
    main()
