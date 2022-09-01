from classes.shop import Shop
from classes.store import Store
from classes.request import Request

if __name__ == "__main__":
    # store = Store()
    # shop = Shop()
    store = Store({
        "печенька": 25,
        "собачка": 25,
        "елка": 25
    })
    shop = Shop({
        "печенька": 2,
        "собачка": 2,
        "елка": 2
    })
    storages = {
        "магазин": shop,
        "склад": store
    }
    # todo: доделать логику

    print("Добро пожаловать!")
    while True:
        print(f"Сейчас на складе:\n{store}")
        print(f"Сейчас в магазине:\n{shop}")
        action = input("Забрать товар со склада или добавить на склад? ('забрать' или 'добавить', для выхода:'стоп'\n")
        if action.lower() == 'стоп':
            print("До свидания!")
            break

        product = input("Введите наименование товара: ")
        quantity = int(input("Введите количество товара: "))

        if action.lower == "забрать":
            request = Request("магазин", "склад", quantity, product)
            if not store.check_remove(request.product, request.amount):
                print("Такого товара нет на складе или количество меньше запрошенного")
                continue
            if not shop.check_add(request.product, request.amount):
                print("В магазине недостаточно места, попробуйте что-то другое")
                continue

            store.remove(request.product, request.amount)
            shop.add(request.product, request.amount)
            print("Нужное количество есть на складе")
            print("На складе храниться:")

            for item in store.get_items().items():
                print(f"{item[1]: {item[0]}}")

            print("В магазине храниться: ")
            for item in shop.get_items().items():
                print(f"{item[1]: {item[0]}}")

        elif action.lower() == "добавить":
            request = Request("магазин", "склад", quantity, product)
            if store.check_add(request.amount):
                store.add(request.product, request.amount)
            else:
                print("Не хватает на складе, попробуйте заказать меньше")
        else:
            print("Вы ввели неверное действие")
