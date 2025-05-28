import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Car(Prototype):
    def __init__(self, brand, model, options):
        self.brand = brand
        self.model = model
        self.options = options

    def __str__(self):
        return f"{self.brand} {self.model}, options: {', '.join(self.options)}"

# Демонстрація
if __name__ == "__main__":
    original_car = Car("Tesla", "Model S", ["Autopilot", "Electric"])
    print("Original:", original_car)

    # Клонування
    cloned_car = original_car.clone()
    cloned_car.options.append("Sunroof")
    print("Cloned:  ", cloned_car)
    print("Original after clone:", original_car)  # перевіримо, чи оригінал не змінився
