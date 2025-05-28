from abc import ABC, abstractmethod

# ----- SRP: Клас товару -----
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

# ----- SRP: Клас замовлення -----
class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def total_price(self):
        return sum(p.price for p in self.items)

# ----- OCP: Абстрактна стратегія знижки -----
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

# ----- OCP: Реалізація знижок -----
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        return max(0, total - self.amount)

# ----- SRP: Клас для виводу результату -----
class ReportPrinter:
    def print(self, order: Order, final_price: float):
        print("Замовлення:")
        for p in order.items:
            print(f"- {p.name}: {p.price} грн")
        print(f"Разом зі знижкою: {final_price:.2f} грн")

# ----- Основна програма -----
if __name__ == "__main__":
    order = Order()
    order.add_product(Product("Книга", 250))
    order.add_product(Product("Флешка", 150))

    # Можна легко змінити стратегію знижки, не змінюючи Order
    # discount = NoDiscount()
    # discount = FixedDiscount(100)
    discount = PercentageDiscount(10)  # 10% знижка

    total = order.total_price()
    final_price = discount.apply_discount(total)

    printer = ReportPrinter()
    printer.print(order, final_price)
