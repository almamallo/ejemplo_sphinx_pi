"""
Datos iniciales para pruebas
============================

Datos de barcos y clientes para pruebas.

"""

from model.client import Client
from model.boat import Boat

clients = {
    "123": Client(client_num="123", dni="32123456B", name="Pedro Rodríguez López", phone="123456789"),
    "456": Client(client_num="456", dni="72333444B", name="María Martínez Pérez", phone="654789412"),
    "789": Client(client_num="789", dni="22123456B", name="Lucía González Martín", phone="555236485"),
}

boats = {
    "123": Boat(clients["123"], "12345", 10, 2015),
    "456": Boat(clients["123"], "23456", 5, 2010),
    "789": Boat(clients["456"], "55566", 12, 2018),
}
