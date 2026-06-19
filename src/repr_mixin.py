"""Миксин для вывода информации о создании объекта."""


class ReprMixin:
    """Миксин, который выводит информацию о создании объекта."""

    def __init__(self, *args, **kwargs) -> None:
        """Выводит информацию о создании объекта и вызывает родительский конструктор."""
        # Получаем имя класса и параметры для красивого вывода
        class_name = self.__class__.__name__
        
        # Формируем строку параметров
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        
        # Объединяем параметры с запятой если нужно
        all_params = ", ".join(filter(None, [args_str, kwargs_str]))
        
        print(f"{class_name}({all_params})")
        
        # Пытаемся вызвать конструктор родительского класса, но если его нет, игнорируем
        try:
            super().__init__(*args, **kwargs)
        except TypeError:
            # Если родительский класс не имеет __init__ или не принимает эти параметры
            pass
