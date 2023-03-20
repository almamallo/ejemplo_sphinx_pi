"""
Boat
=====

"""


class Boat:
    """Representa un barco de un cliente.

    :param client: El cliente, dueño del barco.
    :param registration_number: Matrícula del barco.
    :param length_m: Metros de eslora.
    :param manufacturing_year: Año de fabricación.

    :type client: Client
    :type registration_number: string
    :type length_m: float
    :type manufacturing_year: int
    """

    def __init__(self, cliente, registration_number, length_m, manufacturing_year):
        """Inicializa un objeto de la clase Boat."""
        self.registration_number = registration_number
        self.length = length_m
        self.manufacturing_year = manufacturing_year