class Builder:
    """Базовый класс строителя."""

    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_putty(self):
        pass

    def plaster_walls(self):
        pass

    def prime_wall(self):
        pass

    def paint_wall(self):
        pass


class TileWorker(Builder):
    """Плиточник."""

    def prepare_floor(self):
        print("Подготовка пола для укладки плитки.")

    def lay_tiles(self):
        print("Укладка плитки на пол.")


class Finisher(Builder):
    """Отделочник."""

    def apply_putty(self):
        print("Нанесение шпаклевки на стены.")

    def plaster_walls(self):
        print("Оштукатуривание стен.")


class Painter(Builder):
    """Маляр."""

    def prime_wall(self):
        print("Грунтовка стен.")

    def paint_wall(self):
        print("Покраска стен.")


class Foreman:
    """Прораб (Директор)."""

    def __init__(self, builder):
        self.builder = builder

    def make_floors(self):
        """Сделать полы."""
        self.builder.prepare_floor()
        self.builder.lay_tiles()

    def level_walls(self):
        """Выровнять стены."""
        self.builder.apply_putty()
        self.builder.plaster_walls()

    def paint_walls(self):
        """Покрасить стены."""
        self.builder.prime_wall()
        self.builder.paint_wall()

    def turnkey_work(self):
        """Работы под ключ."""
        self.make_floors()
        self.level_walls()
        self.paint_walls()