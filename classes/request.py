class Request:

    def __init__(self, from_: str, to_: str, amount: int = 3, product: str = "печеньки"):
        self.from_=from_
        self.to_ = to_
        self.amount = amount
        self.product = product

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to_}"

