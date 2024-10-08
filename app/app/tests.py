"""Sample tests"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc model"""

    def test_add_numbers(self):
        """Test adding number together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting number together"""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)
