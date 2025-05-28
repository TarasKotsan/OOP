from abc import ABC, abstractmethod

# Базовий абстрактний клас
class Tvaryna(ABC):
    def __init__(self, imya):
        self._imya = imya  # Інкапсуляція

    @abstractmethod
    def zvuk(self):
        pass  # Абстрактний метод

    def info(self):
        return f"Я тварина на ім'я {self._imya}"

# Похідні класи
class Pes(Tvaryna):
    def __init__(self, imya):
        super().__init__(imya)

    def zvuk(self):
        return f"{self._imya} каже: Гав!"

class Kit(Tvaryna):
    def __init__(self, imya):
        super().__init__(imya)

    def zvuk(self):
        return f"{self._imya} каже: Няв!"

class Korova(Tvaryna):
    def __init__(self, imya):
        super().__init__(imya)

    def zvuk(self):
        return f"{self._imya} каже: Муу!"

# Колекція тварин (поліморфізм)
zoo = [
    Pes("Рекс"),
    Kit("Барсік"),
    Korova("Белла")
]

# Виклик абстрактного методу
for tvaryna in zoo:
    print(tvaryna.zvuk())
