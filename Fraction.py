#%%
from math import gcd
import unittest
import pydoc

class Fraction:
    """Class representing a fraction and operations on it.

    Author : Sean VERGAUWEN
    Date : November 2024
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE:
            - den != 0 (division by zero is not allowed)
        POST:
            - Fraction is always in reduced form.
            - If den < 0, both numerator and denominator are adjusted to ensure the denominator is positive.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        if den < 0:
            num = -num
            den = -den

        common_divisor = gcd(num, den)
        self._num = num // common_divisor
        self._den = den // common_divisor

    @property
    def numerator(self) -> int:
        """Numerator of the fraction."""
        return self._num

    @property
    def denominator(self) -> int:
        """Denominator of the fraction."""
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction.

        PRE:
            - None
        POST:
            - Returns a string of the form 'a/b' for non-integer fractions or 'a' for integers.
        """
        if self._den == 1:
            return f"{self._num}"
        return f"{self._num}/{self._den}"

    def as_mixed_number(self) -> str:
        """Return a textual representation of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRE:
            - None
        POST:
            - Returns a string like 'n a/b' if applicable or just 'n' for integers.
        """
        integer_part = self._num // self._den
        remainder = abs(self._num) % self._den
        if remainder == 0:
            return f"{integer_part}"
        return f"{integer_part} {remainder}/{self._den}" if integer_part != 0 else f"{self._num}/{self._den}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the + operator for fractions.

        PRE:
            - other must be a Fraction instance.
        POST:
            - Returns a new Fraction that is the sum of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be a Fraction.")
        new_num = self._num * other._den + self._den * other._num
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the - operator for fractions.

        PRE:
            - other must be a Fraction instance.
        POST:
            - Returns a new Fraction that is the difference of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be a Fraction.")
        new_num = self._num * other._den - self._den * other._num
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the * operator for fractions.

        PRE:
            - other must be a Fraction instance.
        POST:
            - Returns a new Fraction that is the product of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be a Fraction.")
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Overloading of the / operator for fractions.

        PRE:
            - other must be a Fraction instance.
            - other.numerator != 0
        POST:
            - Returns a new Fraction that is the quotient of self and other.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be a Fraction.")
        if other._num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Fraction(new_num, new_den)

    def __pow__(self, power: int) -> 'Fraction':
        """Overloading of the ** operator for fractions.

        PRE:
            - power must be an integer.
        POST:
            - Returns the fraction raised to the given power.
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")
        return Fraction(self._num ** power, self._den ** power)

    def __eq__(self, other: 'Fraction') -> bool:
        """Overloading of the == operator for fractions.

        PRE:
            - other must be a Fraction instance.
        POST:
            - Returns True if self and other are equal, False otherwise.
        """
        if not isinstance(other, Fraction):
            return False
        return self._num == other._num and self._den == other._den

    def __float__(self) -> float:
        """Returns the decimal value of the fraction.

        PRE:
            - None
        POST:
            - Returns the float representation of the fraction.
        """
        return self._num / self._den

    # ------------------ Properties checking ------------------

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0.

        PRE:
            - None
        POST:
            - Returns True if the fraction is 0, False otherwise.
        """
        return self._num == 0

    def is_integer(self) -> bool:
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2, ...).

        PRE:
            - None
        POST:
            - Returns True if the fraction is an integer, False otherwise.
        """
        return self._num / self._den == int(self._num / self._den)

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1.

        PRE:
            - None
        POST:
            - Returns True if the fraction is proper, False otherwise.
        """
        return abs(self._num) < self._den

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE:
            - None
        POST:
            - Returns True if the numerator is 1, False otherwise.
        """
        return self._num == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Check if two fractions differ by a unit fraction.

        PRE:
            - other must be a Fraction instance.
        POST:
            - Returns True if self and other are adjacent, False otherwise.
        """
        diff = abs(self._num * other._den - other._num * self._den)
        return diff == 1


if __name__ == '__main__':
    pydoc.writedoc(Fraction)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)