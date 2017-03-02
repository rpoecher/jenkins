'''
@author: Rene Poecher
'''

class Bruch(object):
    """
    Bruch

    :param int zaehler: Der Zaehler
    :param int nenner: Der Nenner
    """

    def __iter__(self):
        """
        Macht zeahler und nenner iterable
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=1, nenner=1):
        """
        Konstructor

        :raise TypeError: wenn kein Bruch oder kein int
        :param zaehler: Bruch oder int
        :param nenner: int darf nicht 0 sein!
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('Zeahler ist kein int:')
        elif type(nenner) is not int:
            raise TypeError('Nenner ist kein int:')
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):
        """
        Gibt zeahler/nenner aus

        :return: float
        """
        return self.zaehler / self.nenner

    def __int__(self):
        """
        Gibt zeahler/nenner als int aus

        :return: float
        """
        return int(self.__float__())

    def __neg__(self):
        """
        Setzt den Bruch auf Minus

        :return: Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __complex__(self):
        """
        Gibt float als  complex zurück

        :return: complex
        """
        return complex(self.__float__())

    def __pow__(self, pow):
        """
        Multipliziert zeahler und Nenner mit pow

        :raise TypeError: inkompatible typen
        :param int pow: power
        :return: Bruch
        """
        if type(pow) is int:
            return Bruch(self.zaehler ** pow, self.nenner ** pow)
        else:
            raise TypeError('inkompatible typen:')

    def __invert__(self):
        """
        invert den Bruch ~

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):
        """
        kuerzt den Bruch gibt den repreentanten zurueck

        :return str
        """

        """ggt berrechnen"""
        x=self.zaehler
        y=self.nenner
        while y != 0:
            g = x % y
            x, y = y, g
        kuerzen=x

        """kuezren"""
        self.zaehler //= kuerzen
        self.nenner //= kuerzen

        if self.nenner < 0:
            self.nenner=abs(self.nenner)
            self.zaehler=abs(self.zaehler)

        if self.nenner == 1:
            return "(%d)" % self.zaehler

        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __makeBruch(other):
        """
        erstellt einen Bruch

        :raise TypeError: inkompatible typen
        :param other: Bruch oder int
        :return: Bruch
        """

        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('inkompatible typen')

    def __eq__(self, other):
        """
        Evaluirt ob Bruch gleich ist

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner

    def __abs__(self):
        """
        Erstellt den Positiven Bruch

        :return: Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))




