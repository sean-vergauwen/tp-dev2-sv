from Fraction import Fraction
import unittest
import coverage


class TestFraction(unittest.TestCase):
    def testCreationFraction(self):
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

    def testTextualRepr(self):
        fraction1 = Fraction(5, 2)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(4, 2)
        fraction4 = Fraction(1, -2)
        # __str__
        self.assertEqual(str(fraction1), '5/2')
        self.assertEqual(str(fraction2), '3/4')
        self.assertEqual(str(fraction3), '2')
        self.assertEqual(str(fraction4), '-1/2')
        # as_mixed_number
        self.assertEqual(fraction2.as_mixed_number(), '3/4')
        self.assertEqual(str(fraction3), '2')
        self.assertEqual(str(fraction4), '-1/2')

    def testOperationsMathematiques(self):
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
        resultatAddition = fraction1 + fraction2
        self.assertEqual(resultatAddition.numerator, 17)
        self.assertEqual(resultatAddition.denominator, 12)
        resultatAddition1 = fraction1 + fraction3
        self.assertEqual(resultatAddition1.numerator, 5)
        self.assertEqual(resultatAddition1.denominator, 12)
        resultatAddition2 = fraction2 + fraction4
        self.assertEqual(resultatAddition2.numerator, 2)
        self.assertEqual(resultatAddition2.denominator, 3)
        resultatAddition3 = fraction4 + fraction5
        self.assertEqual(resultatAddition3.numerator, 0)
        self.assertEqual(resultatAddition3.denominator, 1)
        resultatAddition4 = fraction6 + fraction7
        self.assertEqual(resultatAddition4.numerator, 5)
        self.assertEqual(resultatAddition4.denominator, 1)

        # __sub__
        resultatSoustraction = fraction1 - fraction2
        self.assertEqual(resultatSoustraction.numerator, 1)
        self.assertEqual(resultatSoustraction.denominator, 12)
        resultatSoustraction1 = fraction1 - fraction3
        self.assertEqual(resultatSoustraction1.numerator, 13)
        self.assertEqual(resultatSoustraction1.denominator, 12)
        resultatSoustraction2 = fraction2 - fraction4
        self.assertEqual(resultatSoustraction2.numerator, 2)
        self.assertEqual(resultatSoustraction2.denominator, 3)
        resultatSoustraction3 = fraction4 - fraction5
        self.assertEqual(resultatSoustraction3.numerator, 0)
        self.assertEqual(resultatSoustraction3.denominator, 1)
        resultatSoustraction4 = fraction8 - fraction9
        self.assertEqual(resultatSoustraction4.numerator, 1)
        self.assertEqual(resultatSoustraction4.denominator, 1)

        # __mul__
        resultatMultiplication = fraction1 * fraction2
        self.assertEqual(resultatMultiplication.numerator, 1)
        self.assertEqual(resultatMultiplication.denominator, 2)
        resultatMultiplication1 = fraction6 * fraction3
        self.assertEqual(resultatMultiplication1.numerator, -2)
        self.assertEqual(resultatMultiplication1.denominator, 3)
        resultatMultiplication2 = fraction3 * fraction9
        self.assertEqual(resultatMultiplication2.numerator, 1)
        self.assertEqual(resultatMultiplication2.denominator, 1)
        resultatMultiplication3 = fraction1 * fraction4
        self.assertEqual(resultatMultiplication3.numerator, 0)
        self.assertEqual(resultatMultiplication3.denominator, 1)
        resultatMultiplication4 = fraction6 * fraction7
        self.assertEqual(resultatMultiplication4.numerator, 6)
        self.assertEqual(resultatMultiplication4.denominator, 1)

        # __truediv__
        resultatDivision = fraction1 / fraction2
        self.assertEqual(resultatDivision.numerator, 9)
        self.assertEqual(resultatDivision.denominator, 8)
        resultatDivision1 = fraction1 / fraction3
        self.assertEqual(resultatDivision1.numerator, -9)
        self.assertEqual(resultatDivision1.denominator, 4)
        resultatDivision2 = fraction8 / fraction3
        self.assertEqual(resultatDivision2.numerator, 6)
        self.assertEqual(resultatDivision2.denominator, 1)
        with self.assertRaises(ZeroDivisionError):
            fraction6 / fraction4

        resultatDivision3 = fraction4 / fraction7
        self.assertEqual(resultatDivision3.numerator, 0)
        self.assertEqual(resultatDivision3.denominator, 1)


        # __pow__
        resultatPuissance = fraction1 ** 2
        self.assertEqual(resultatPuissance.numerator, 9)
        self.assertEqual(resultatPuissance.denominator, 16)
        resultatPuissance1 = fraction3 ** 2
        self.assertEqual(resultatPuissance1.numerator, 1)
        self.assertEqual(resultatPuissance1.denominator, 9)
        resultatPuissance2 = fraction1 ** 1
        self.assertEqual(resultatPuissance2.numerator, 3)
        self.assertEqual(resultatPuissance2.denominator, 4)
        resultatPuissance3 = fraction1 ** 0
        self.assertEqual(resultatPuissance3.numerator, 1)
        self.assertEqual(resultatPuissance3.denominator, 1)

        # __eq__
        self.assertTrue(fraction1 == fraction1)
        self.assertFalse(fraction8 == fraction6)


    def testProprietesFraction(self):
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

    def testConversionEnDecimal(self):
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