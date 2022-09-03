# все ошибки которые будут

class BaseError(Exception):
    message = 'Какая-то ошибка'

class NotEnoughSpace(BaseError):
    message = 'Недостаточно места на складе'

class NotEnoughProducts(BaseError):
    message = 'Недостаточно товара'

class TooManyDifferentProducts(BaseError):
    message = 'Слишком много наименований разных товаров'

class InvalidRequest(BaseError):
    message = 'Неправильный запрос. Попробуйте снова'