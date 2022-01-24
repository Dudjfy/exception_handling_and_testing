"""Car Class Module"""


class Car:
    """Car class"""
    wheels = 4

    def __init__(self, model: str, price: int):
        self.model: str = model
        self.price: int = price

    def __str__(self):
        return f"Model: {self.model}, Price: {self.price}"

    def change_model(self, new_model: str):
        """Changes current model string to the given one"""
        self.model = new_model

    def set_price(self, new_price: int):
        """Sets the price to the given one"""
        self.price = new_price

    def age(self, years: int = 1, aging_factor: float = 0.9):
        """Ages the car by the amount of given years, using the aging factor.
        Defaults: years=1, aging_factor=0.9"""

        self.price = int(self.price * (aging_factor ** years))

    def increase_value(self, dif: int = 10000):
        """Increases price by given difference, default=10000"""
        self.price += dif
