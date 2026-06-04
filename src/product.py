"""Модель продукта для домашней работы по каталогу"""


def _format_price(price: float) -> str:
    """Форматирует цену для вывода в каталоге.
    
    Если цена целое число, возвращает её без десятичной части.
    Иначе возвращает как есть.
    """
    if float(price).is_integer():
        return str(int(price))
    return str(price)


class Product:
    """Представляет товар в каталоге магазина.
    
    Атрибуты:
        name: Название товара
        description: Описание товара
        quantity: Количество товара на складе
        price: Цена товара (приватное свойство)
    """

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует товар.
        
        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара на складе
        """
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает новую цену товара.
        
        Args:
            value: Новая цена товара
            
        Примечания:
            - Цена не может быть нулевой или отрицательной
            - При понижении цены требуется подтверждение пользователя
        """
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
        """Создаёт товар из словаря.
        
        Args:
            product_dict: Словарь с полями name, description, price, quantity
            
        Returns:
            Новый экземпляр Product
        """
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=float(product_dict["price"]),
            quantity=int(product_dict["quantity"]),
        )

    def format_for_catalog(self) -> str:
        """Строковое представление товара для геттера категории.
        
        Returns:
            Строка с информацией о товаре в формате каталога
        """
        return f"{self.name}, {_format_price(self.price)} руб. " f"Остаток: {self.quantity} шт.\n"

    def __str__(self) -> str:
        """Строковое представление продукта.
        
        Returns:
            Строка в формате: Название, X руб. Остаток: X шт.
        """
        return f"{self.name}, {_format_price(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает продукты, возвращая общую стоимость всех товаров.
        
        Args:
            other: Другой продукт для сложения
            
        Returns:
            Сумма произведений цены на количество для обоих товаров
            (цена1 * количество1 + цена2 * количество2)
        """
        return self.price * self.quantity + other.price * other.quantity
