import unittest
from odd_numbers import OddNumbers
from faker import Faker


class TestMath(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_should_not_pass_when_is_none(self):
        number = self.fake.random_number()
        self.assertIsNotNone(OddNumbers.is_even(number))

    def test_should_return_true_when_number_is_even(self):
        even_number = self.fake.random_number() * 2 + 1
        self.assertTrue(OddNumbers.is_even(even_number))
