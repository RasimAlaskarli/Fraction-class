class Fraction:
    def __init__(self, numerator, denominator):
        if denominator < 0:
            denominator *= -1
            numerator *= -1
        max = 0
        if numerator > denominator:
            max = int(numerator)
        else:
            max = int(denominator)
        for i in range(max, 0, -1):
            if numerator % i == 0 and denominator % i == 0:
                numerator /= i
                denominator /= i
                break
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        if self.denominator == 0:
            raise ZeroDivisionError

    def __str__(self):
        if self.numerator % self.denominator == 0:
                self.numerator = int(self.numerator/self.denominator)
                return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        denominator = self.denominator * other.denominator
        numerator = (self.numerator*(denominator/self.denominator))+(other.numerator*(denominator/other.denominator))

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        denominator = self.denominator * other.denominator
        numerator = (self.numerator*(denominator/self.denominator))-(other.numerator*(denominator/other.denominator))

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return Fraction(numerator, denominator)

    def __eq__(self, other):
        denominator = self.denominator * other.denominator
        numerator1 = self.numerator*(denominator/self.denominator)
        numerator2 = other.numerator*(denominator/other.denominator)
        return numerator1 == numerator2

    def __lt__(self, other):
        denominator = self.denominator * other.denominator
        numerator1 = self.numerator*(denominator/self.denominator)
        numerator2 = other.numerator*(denominator/other.denominator)
        return numerator1 < numerator2

    def __le__(self, other):
        denominator = self.denominator * other.denominator
        numerator1 = self.numerator*(denominator/self.denominator)
        numerator2 = other.numerator*(denominator/other.denominator)
        return numerator1 <= numerator2

    def __gt__(self, other):
        denominator = self.denominator * other.denominator
        numerator1 = self.numerator*(denominator/self.denominator)
        numerator2 = other.numerator*(denominator/other.denominator)
        return numerator1 > numerator2

    def __ge__(self, other):
        denominator = self.denominator * other.denominator
        numerator1 = self.numerator*(denominator/self.denominator)
        numerator2 = other.numerator*(denominator/other.denominator)
        return numerator1 >= numerator2