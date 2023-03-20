"""
Rental
======

"""


class Rental:
    """
    Representa el alquier de un barco de un cliente.

    :param client: El cliente, arrendatario del alquiler.
    :param boat: El barco del client para el que se realiza el alquiler.
    :param start_date: Fecha de inicio del alquiler.
    :param end_date: Fecha de fin del alquiler.
    :param position: Posición del amarre.

    :type client: Client
    :type boat: Boat
    :type start_date: datetime
    :type end_date: datetime
    :type position: string
    """

    daily_rental_price = 50

    def __init__(self, client, boat, start_date, end_date, position):
        """Inicializa un objeto de la clase Rental."""
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.boat = boat
        self.position = position
        self.__price = self.calculate_price()

    @property
    def price(self):
        """Devuelve el precio del amarre."""
        return self.__price

    def calculate_price(self):
        """
        Calcula el precio del amarre en función de de las fechas y el precio diario.

        :return: El precio del alquiler en función de las fechas

        :rtype: float
        """
        return (self.end_date - self.start_date).days * cls.daily_price * self.boat.length

    @classmethod
    def change_daily_rental_price(cls, new_price):
        """
        Cambia el precio diario del alquiler.

        :param new_price: El nuevo precio del alquiler.

        :type new_price: float
        """
        cls.daily_rental_price = new_price
