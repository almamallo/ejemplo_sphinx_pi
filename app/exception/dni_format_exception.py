"""
DNIFormatException module
=========================

"""


class DNIFormatException(IOError):
    """
    Excepción que se lanza cuando se detecta un error en el formato del DNI

    Attributes:
        dni -- dni con el error
        message -- explanation of the error
    """

    def __init__(self, dni):
        """
        Inicializa la excepción

        :param dni: El dni que provocó que se lanzara la excepción.

        :type dni: string
        """
        self.expression = dni
        self.message = "Formato de dni incorrecto"