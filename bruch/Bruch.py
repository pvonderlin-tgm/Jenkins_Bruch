class Bruch(object):

    """
    Class Bruch is the equivalent to a mathematical fraction.
    You can create a fraction by passing another fraction to the
    :func:`__init__` constructor, or by providing a nominator and a denominator.

    You can also use a static method called :func:`_Bruch_makeBruch` to create
    a fraction simply from a nominator.
    """

    zaehler = 0
    nenner = 0

    def __init__(self, fractionOrNominator, denom=1):
        """
        The Basic Constructor.
        Checks which type of arguments if has received (only var or var and standard)
        and calls the equivalent method for procession.

        :param fractionOrNominator: Is either a nominator integer or a Bruch object.
        :param denom: The optional denominator as kwargs, Standart value is one,
        because you can also create a fraction from just one value.
        """
        if type(fractionOrNominator) is Bruch:
            self.is_fraction(fractionOrNominator)
        else:
            self.is_two_values(fractionOrNominator, denom)

    def is_two_values(self, nomi, denom):
        """
        Gets called when there are two parameters given to the constructor.
        :param nomi: The nomincator for the fraction.
        :param denom: The denominator for the fraction.
        """
        if type(nomi) is not int or type(denom) is not int:
            raise TypeError("You cannot create a fraction with floats!")

        if denom == 0:
            raise ZeroDivisionError("You cannot divide through zero!")

        self.zaehler = nomi
        self.nenner = denom

    def is_fraction(self, fraction):
        """
        Gets called when the paramter of the constructor is a Bruchh object.
        :param fraction: The fraction that should be written to this object.
        """
        if type(fraction.nenner) is float or type(fraction.zaehler) is float:
            raise TypeError("You cannot create a fraction with floats!")

        if fraction.nenner == 0:
            raise ZeroDivisionError("You cannot divide through zero!")

        self.zaehler = fraction.zaehler
        self.nenner = fraction.nenner

    def __eq__(self, other):
        """
        Checks if two fractions are equal in their value,
        meaning that the nominator and denominator match.
        :param other: The fraction that is compared to this object.
        :return: Returns a boolean value which is set true, if both fractions match.
        """
        if type(other) is int:
            return int(self) == other

        return self.zaehler == other.zaehler and self.nenner == other.nenner

    def __gt__(self, other):
        """
        Checks if the objects value in float is greater than the given fractions.
        :param other: The fraction that is compared to this object.
        :return: Returns a boolean value that is true if this objects value is greater.
        """
        return float(self) > float(other)

    def __lt__(self, other):
        """
        Checks if the objects value in float is less than the given fractions.
        :param other: The fraction that is compared to this object.
        :return: Returns a boolean value that is true if this objects value is less.
        """
        return float(self) < float(other)

    def __ge__(self, other):
        """
        Checks if this object is NOT less than the given fraction.
        :param other: The fraction that is compared to this object.
        :return: Returns a boolean value that is true if this objects is not less.
        """
        return not (self > other)

    def __le__(self, other):
        """
        Checks if this object is not greater than the given fraction.
        :param other: The fraction that is compared to this object.
        :return: Returns a boolean value that is true if this object is not greater.
        """
        return not (self > other)

    def __float__(self):
        """
        Show this objects value in float value.
        :return: Returns the equivalent float value for the fraction.
        """
        return self.zaehler / self.nenner

    def __int__(self):
        """
        Show this objects value in int value.
        :return: Returns the rounded equivalent int value for the fraction.
        """
        return round(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Shows the objects value in complex value.
        :return: Returns the equivalent complex value for the fraction.
        """
        return complex(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Creates a fraction that contains the reciprocal value of this object.
        :return: Returns a fraction that hast the reciprocal values of this object.
        """
        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):
        """
        Shows the objects value in string with the format ( integer value of fraction ).
        :return: Returns a string containing the equivalent of the int value of this object.
        """
        return '('+str(round(self.zaehler / self.nenner))+')'

    def __abs__(self):
        """
        Shows this objects absolute values.
        :return: Returns a fraction with the absolute equivalent of this object.
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        Shows this objects negation.
        :return: Returns a fraction with the equivalent values of this objects negation.
        """
        return Bruch(-self.zaehler, self.nenner)

    def __str__(self):
        """
        Shows this object as a string.
        Whole fraction will be displayed in their int equivalent.
        Other fractions will be schon in (nominator/denominator) like format.
        :return: Returns a string with this objects equivalent sting values.
        """
        if self.nenner == 1:
            return '(%s)' % self.zaehler
        elif self.zaehler < 0 and self.nenner < 0:
            return '(%s/%s)' % (abs(self.zaehler), abs(self.nenner))
        else:
            return '(%s/%s)' % (self.zaehler, self.nenner)

    def __iter__(self):
        """
        Generates a iterable object from this object (list, tuple, ...).
        :return: Returns a iterable object from containing this objects values.
        """
        yield  self.zaehler
        yield  self.nenner

    @staticmethod
    def _Bruch__makeBruch(value):
        """
        Generates a simple fraction with a the given value as nominator.
        :param value: The nominator for the fraction.
        :return: Returns a fraction with the given value as denominator.
        """
        if type(value) is int:
            return Bruch(value, 1)
        else:
            raise TypeError("You cannot create a fraction with this value!")

    def __pow__(self, power, modulo=None):
        """
        Returns this objects to the power of the given value.
        :param power: The power that this object should be empowered with.
        :param modulo: The modulo value, standard value is none
        :return: Returns a fraction that is empowered to power,
        with the equivalent values of this object.
        """
        if type(power) is not int:
            raise TypeError("Cannot power the fraction with this value!")
        else:
            z = self.zaehler ** power
            n = self.nenner ** power
            return Bruch(z, n)

    def __add__(self, other):
        """
        Checks if the parameter is an int or a fraction and processes
        it accordingly, meaning it adds them to this object.
        For this, the least common factor has to be found.
        :param other: Can be either an int value or a fraction.
        :return: Returns the value of the parameter added to this object
        """
        if type(other) is Bruch:
            newnenner = self.nenner * other.nenner
            zaehlers = self.zaehler * other.nenner
            zaehlero = self.nenner * other.zaehler

            return Bruch(zaehlers + zaehlero, newnenner)

        if type(other) == int:
            newz = other * self.nenner + self.zaehler
            return Bruch(newz, self.nenner)
        else:
            raise TypeError("No floats allowed!")

    def __iadd__(self, other):
        """
        Called when the incremental operator for + is used (+=).
        Add given parameter to this object.
        :param other: The value that should be added to this object.
        :return: Returns the addition of this object and the parameter.
        """
        return self + other

    def __radd__(self, other):
        """
        Called when reverse addition is used, meaning and int value plus a fraction.
        :param other: The value that should be added to this object.
        :return: Returns the added value of this object and the parameter.
        """
        return self + other

    def __sub__(self, other):
        """
        Utilizes the negated addition to subtract the given parameter
        from this object.
        :param other: The value that should be subtracted from this object.
        :return: Returns the subtracted value of this object and the parameter.
        """
        return self + (-other)

    def __rsub__(self, other):
        """
        Called when reverse subtraction is used, meaning and int value minus a fraction.
        :param other: The value to be subtracted from this object.
        :return: Returns the subtracted value of this object and the parameter.
        """
        return Bruch(other) - self

    def __isub__(self, other):
        """
        Called when the incremental paramter for - is used (-=).
        Subtracts given parameter from this objects.
        :param other: The value that should be subtracted from this object.
        :return: Returns the subtracted value of this object and the parameter.
        """
        return self - other

    def __mul__(self, other):
        """
        Checks if the parameter is an int or a fraction and processes the outcome
        accordingly.
        :param other: The value with which this object should be multiplied with.
        :return: Returns the multiplied values of this object and the parameter.
        """
        if type(other) is Bruch:
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        elif type(other) is int:
            return Bruch(self.zaehler * other, self.nenner)
        else:
            raise TypeError("No other than int allowed!")

    def __rmul__(self, other):
        """
        Called when reverse multiplication is used, meaning a int times a fraction.
        :param other: The value that this object should be multiplied with.
        :return: Returns the multiplied value of this object and the parameter.
        """
        return self * other

    def __imul__(self, other):
        """
        Called when the incremental parameter for * is used (*=).
        Multiplies given parameter with this object.
        :param other: The value with which this object should be multiplied with.
        :return: Retuns the multiplied value of this object and the parameter.
        """
        return self * other

    def __truediv__(self, other):
        """
        Checks if the parameter is an int or a fraction and processes the outcome
        accordingly.
        :param other: The value that this object should be divided with.
        :return:
        """
        if self.zaehler == 0:
            raise ZeroDivisionError("Cannot use the cross product when nominator is zero!")
        elif type(other) is Bruch:
            return self * ~other
        else:
            return Bruch(self.zaehler, self.nenner * other)

    def __rtruediv__(self, other):
        """
        Called when reverse division is used, meaning a int divided by a fraction.
        :param other: The value with which this object should be divided with.
        :return: Returns the divided value of this object and the parameter.
        """
        return self/other

    def __itruediv__(self, other):
        """
        Called when the incremental parameter for / is used (/=).
        Divides this object by the given parameter.
        :param other: The value with which this object should be divided with.
        :return: Returns the divided value of this object and the parameter.
        """
        return self/other


