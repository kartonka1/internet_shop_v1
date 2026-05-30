"""Модель продукта для домашней работы по каталогу"""


class Product:
    """Представляет товар в каталоге магазина"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
