import unittest

from src.car import Car


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Volkswagen Golf", 300000)

    def test_amount_of_wheels_4(self):
        self.assertEqual(self.car.wheels, 4)

    def test_str(self):
        self.assertEqual(str(self.car), "Model: Volkswagen Golf, Price: 300000")

    def test_change_model(self):
        new_model = "BMW"
        self.car.change_model(new_model)
        self.assertEqual(self.car.model, new_model)

    def test_set_price(self):
        new_price = 69420
        self.car.set_price(new_price)
        self.assertEqual(self.car.price, new_price)

    def test_age_no_args(self):
        self.car.age()
        self.assertEqual(self.car.price, 270000)

    def test_age_2_years(self):
        self.car.age(2)
        self.assertEqual(self.car.price, 243000)

    def test_age_80_percent(self):
        self.car.age(aging_factor=0.8)
        self.assertEqual(self.car.price, 240000)

    def test_age_80_percent_and_2_years(self):
        self.car.age(2, 0.8)
        self.assertEqual(self.car.price, 192000)

    def test_increase_value_no_args(self):
        self.car.increase_value()
        self.assertEqual(self.car.price, 310000)

    def test_increase_value_with_args(self):
        self.car.increase_value(394200)
        self.assertEqual(self.car.price, 694200)
