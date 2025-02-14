from abc import ABC, abstractmethod


class Pasta(ABC):
    """Абстрактный класс пасты."""

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_topping(self):
        pass

    @abstractmethod
    def get_additives(self):
        pass


class Carbonara(Pasta):
    """Класс пасты Карбонара."""

    def get_type(self):
        return "Спагетти"

    def get_sauce(self):
        return "Сырный соус"

    def get_topping(self):
        return "Бекон"

    def get_additives(self):
        return "Пармезан, яйцо"


class Bolognese(Pasta):
    """Класс пасты Болоньезе."""

    def get_type(self):
        return "Феттучини"

    def get_sauce(self):
        return "Томатный соус"

    def get_topping(self):
        return "Фарш"

    def get_additives(self):
        return "Базилик, чеснок"


class Alfredo(Pasta):
    """Класс пасты Альфредо."""

    def get_type(self):
        return "Феттучини"

    def get_sauce(self):
        return "Сливочный соус"

    def get_topping(self):
        return "Курица"

    def get_additives(self):
        return "Пармезан, петрушка"


class PastaFactory:
    """Фабрика пасты."""

    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "Carbonara":
            return Carbonara()
        elif pasta_type == "Bolognese":
            return Bolognese()
        elif pasta_type == "Alfredo":
            return Alfredo()
        else:
            raise ValueError("Неизвестный тип пасты.")