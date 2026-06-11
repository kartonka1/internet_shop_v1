"""Модель продукта для домашней работы по каталогу."""


def _format_price(price: float) -> str:
    """Форматирует цену для вывода в каталоге."""
    if float(price).is_integer():
        return str(int(price))
    return str(price)


class Product:
    """Представляет товар в каталоге магазина."""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if hasattr(self, "_Product__price") and value < self.__price:
            answer = input("Цена понижается. Согласны? (y/n): ")
            if answer != "y":
                return
        self.__price = value

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=float(product_dict["price"]),
            quantity=int(product_dict["quantity"]),
        )

    def format_for_catalog(self) -> str:
        return f"{self.name}, {_format_price(self.price)} руб. Остаток: {self.quantity} шт.\n"

    def __str__(self) -> str:
        return f"{self.name}, {_format_price(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        # В этом задании можно складывать только товары одного конкретного класса.
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного класса")
        return self.price * self.quantity + other.price * other.quantity
