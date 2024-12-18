from Fraction import Fraction
import unittest
import coverage


class TestFraction(unittest.TestCase):
    def test_creation_fraction(self):
        fraction = Fraction(3, 4)
        fraction1 = Fraction(2, 4)
        fraction2 = Fraction(1, -3)
        fraction3 = Fraction(-3, -4)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(4, 2)
        self.assertEqual(fraction.numerator, 3)
        self.assertEqual(fraction.denominator, 4)
        with self.assertRaises(ValueError):
            Fraction(1, 0)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
        self.assertEqual(fraction2.numerator, -1)
        self.assertEqual(fraction2.denominator, 3)
        self.assertEqual(fraction3.numerator, 3)
        self.assertEqual(fraction3.denominator, 4)
        self.assertEqual(fraction4.numerator, 0)
        self.assertEqual(fraction4.denominator, 1)
        self.assertEqual(fraction5.numerator, 2)
        self.assertEqual(fraction5.denominator, 1)

    def test_textual_repr(self):
        fraction1 = Fraction(5, 2)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(4, 2)
        fraction4 = Fraction(1, -2)
        fraction6 = Fraction(10, 1)
        # __str__
        self.assertEqual(str(fraction1), '5/2')
        self.assertEqual(str(fraction2), '3/4')
        self.assertEqual(str(fraction3), '2')
        self.assertEqual(str(fraction4), '-1/2')
        # as_mixed_number
        self.assertEqual(fraction2.as_mixed_number(), '3/4')
        self.assertEqual(fraction1.as_mixed_number(), '2 + 1/2')
        self.assertEqual(fraction6.as_mixed_number(), '10')

    def test_operations_mathematiques(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(2, 3)
        fraction3 = Fraction(1, -3)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(0, 4)
        fraction6 = Fraction(4, 2)
        fraction7 = Fraction(9, 3)
        fraction8 = Fraction(-4, 2)
        fraction9 = Fraction(-9,3)
        # __add__
        resultat_addition = fraction1 + fraction2
        self.assertEqual(resultat_addition.numerator, 17)
        self.assertEqual(resultat_addition.denominator, 12)
        resultat_addition1 = fraction1 + fraction3
        self.assertEqual(resultat_addition1.numerator, 5)
        self.assertEqual(resultat_addition1.denominator, 12)
        resultat_addition2 = fraction2 + fraction4
        self.assertEqual(resultat_addition2.numerator, 2)
        self.assertEqual(resultat_addition2.denominator, 3)
        resultat_addition3 = fraction4 + fraction5
        self.assertEqual(resultat_addition3.numerator, 0)
        self.assertEqual(resultat_addition3.denominator, 1)
        resultat_addition4 = fraction6 + fraction7
        self.assertEqual(resultat_addition4.numerator, 5)
        self.assertEqual(resultat_addition4.denominator, 1)
        with self.assertRaises(TypeError):
            fraction1 + "string"

        # __sub__
        resultat_soustraction = fraction1 - fraction2
        self.assertEqual(resultat_soustraction.numerator, 1)
        self.assertEqual(resultat_soustraction.denominator, 12)
        resultat_soustraction1 = fraction1 - fraction3
        self.assertEqual(resultat_soustraction1.numerator, 13)
        self.assertEqual(resultat_soustraction1.denominator, 12)
        resultat_soustraction2 = fraction2 - fraction4
        self.assertEqual(resultat_soustraction2.numerator, 2)
        self.assertEqual(resultat_soustraction2.denominator, 3)
        resultat_soustraction3 = fraction4 - fraction5
        self.assertEqual(resultat_soustraction3.numerator, 0)
        self.assertEqual(resultat_soustraction3.denominator, 1)
        resultat_soustraction4 = fraction8 - fraction9
        self.assertEqual(resultat_soustraction4.numerator, 1)
        self.assertEqual(resultat_soustraction4.denominator, 1)
        with self.assertRaises(TypeError):
            fraction1 - "string"

        # __mul__
        resultat_multiplication = fraction1 * fraction2
        self.assertEqual(resultat_multiplication.numerator, 1)
        self.assertEqual(resultat_multiplication.denominator, 2)
        resultat_multiplication1 = fraction6 * fraction3
        self.assertEqual(resultat_multiplication1.numerator, -2)
        self.assertEqual(resultat_multiplication1.denominator, 3)
        resultat_multiplication2 = fraction3 * fraction9
        self.assertEqual(resultat_multiplication2.numerator, 1)
        self.assertEqual(resultat_multiplication2.denominator, 1)
        resultat_multiplication3 = fraction1 * fraction4
        self.assertEqual(resultat_multiplication3.numerator, 0)
        self.assertEqual(resultat_multiplication3.denominator, 1)
        resultat_multiplication4 = fraction6 * fraction7
        self.assertEqual(resultat_multiplication4.numerator, 6)
        self.assertEqual(resultat_multiplication4.denominator, 1)
        with self.assertRaises(TypeError):
            fraction1 * "string"

        # __truediv__
        resultat_division = fraction1 / fraction2
        self.assertEqual(resultat_division.numerator, 9)
        self.assertEqual(resultat_division.denominator, 8)
        resultat_division1 = fraction1 / fraction3
        self.assertEqual(resultat_division1.numerator, -9)
        self.assertEqual(resultat_division1.denominator, 4)
        resultat_division2 = fraction8 / fraction3
        self.assertEqual(resultat_division2.numerator, 6)
        self.assertEqual(resultat_division2.denominator, 1)
        with self.assertRaises(ZeroDivisionError):
            fraction6 / fraction4
        with self.assertRaises(TypeError):
            fraction1 / "string"

        resultat_division3 = fraction4 / fraction7
        self.assertEqual(resultat_division3.numerator, 0)
        self.assertEqual(resultat_division3.denominator, 1)


        # __pow__
        resultat_puissance = fraction1 ** 2
        self.assertEqual(resultat_puissance.numerator, 9)
        self.assertEqual(resultat_puissance.denominator, 16)
        resultat_puissance1 = fraction3 ** 2
        self.assertEqual(resultat_puissance1.numerator, 1)
        self.assertEqual(resultat_puissance1.denominator, 9)
        resultat_puissance2 = fraction1 ** 1
        self.assertEqual(resultat_puissance2.numerator, 3)
        self.assertEqual(resultat_puissance2.denominator, 4)
        resultat_puissance3 = fraction1 ** 0
        self.assertEqual(resultat_puissance3.numerator, 1)
        self.assertEqual(resultat_puissance3.denominator, 1)
        with self.assertRaises(TypeError):
            fraction1 ** "string"

        # __eq__
        self.assertTrue(fraction1 == fraction1)
        self.assertFalse(fraction8 == fraction6)
        self.assertFalse(1.2 == fraction1)


    def test_propriete_fraction(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(4, 3)
        fraction3 = Fraction(5, 1)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(1, 1)

        # is_zero
        self.assertFalse(fraction1.is_zero())
        self.assertTrue(fraction4.is_zero())

        # is_integer
        self.assertFalse(fraction1.is_integer())
        self.assertTrue(fraction3.is_integer())

        # is_proper
        self.assertTrue(fraction1.is_proper())
        self.assertFalse(fraction2.is_proper())

        # is_unit
        self.assertFalse(fraction1.is_unit())
        self.assertTrue(fraction5.is_unit())

        # is_adjacent_to
        self.assertFalse(fraction1.is_adjacent_to(Fraction(7, 4)))
        self.assertTrue(fraction1.is_adjacent_to(Fraction(2, 3)))

    def test_conversion_decimal(self):
        fraction = Fraction(3, 4)
        fraction1 = Fraction(4,2)
        fraction3 = Fraction(-9,3)
        self.assertEqual(float(fraction), 0.75)
        self.assertEqual(float(fraction1), 2)
        self.assertEqual(float(fraction3), -3)


if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    cov.stop()
    cov.report()