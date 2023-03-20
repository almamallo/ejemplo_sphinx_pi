"""
Saling Boat
===========

"""

from model.boat import Boat


class SailingBoat(Boat):
    """
    Representa un barco velero.

    :param sail_length: Longitud de la vela

    :type sail_length: float
    """

    def __init__(self, cliente, registration_number, length_m, manufacturing_year, sail_length):
        """Inicializa un objeto de la clase Boat."""
        super().__init__(cliente, registration_number, length_m, manufacturing_year)
        self.sail_length = sail_length
