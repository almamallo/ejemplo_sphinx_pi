"""
Alquiler Barcos App
===================

Aplicación para gestión de alquiler de barcos.

Módulo principal de la aplicación. Funcionalidades:

- Gestión de clientes
- Gestión de barcos
- Gestión de alquileres
"""

from model.rental import Rental
from model.client import Client
from model.boat import Boat
from exception.dni_format_exception import DNIFormatException

import test_data


class RentalManagement(object):
    """Clase que encapsula el programa de gestión de alquileres."""

    def __init__(self):
        """Inicialización de la clase para la gestión de alquileres."""
        self.clients = {}
        self.boats = {}
        self.rentals = {}
        self.menu = """
Menú de opciones

(1) Añadir cliente
(2) Borrar cliente
(3) Mostrar lista clientes
(4) Mostrar detalle cliente
(5) Añadir barco
(6) Borrar barco
(7) Añadir alquiler
(8) Terminar

Elige una opción: """

    def del_client(self):
        """
        Borra un cliente.

        Pide al usuario el número de cliente para borrarlo.
        """
        num = input("Introduce el numero del cliente que quieres borrar: ")
        client = self.clients.get(num)
        if num == None:
            print("No existe ningún cliente con ese número")
        else:
            del self.clients[num]

    def add_client(self):
        """
        Añade un cliente.

        Pide los datos de un cliente y lo añade al diccionario.
        """
        print("Introduce los datos del cliente:")

        try:
            num = input("Introduce el número de cliente: ")
            name = input("Introduce el nombre: ")
            dni = input("Introduce el dni: ")
            phone = input("Introduce el teléfono: ")

            client = Client(client_num=num, dni=dni, name=name, phone=phone)
            self.clients[client.client_num] = client
        except DNIFormatException as e:
            print(f"\n No se ha añadido el cliente: {e.message}\n")

    def show_client_list(self):
        """Muestra la lista de clientes."""
        print()
        for cli_num, cli in self.clients.items():
            print(cli)
        print()

    def show_client_details(self):
        """Muestra los detalles de un cliente.

        No implementado.
        """
        print("Opción no implementada")

    def add_boat(self):
        """Añade un barco.

        No implementado
        """
        print("Opción no implementada")

    def del_boat(self):
        """Borra un barco

        No implementado"""
        print("Opción no implementada")

    def add_rent(self):
        """Añade un alquiler.

        No implementado.
        """
        print("Opción no implementada")

    def run_app(self):
        """
        Ejecucion del programa.

        Muestra el menú y llama a la opción correspondiente en función del
        """
        option = 1
        while option != 8:
            option = int(input(self.menu))
            if option == 1:
                self.add_client()
            elif option == 2:
                self.del_client()
            elif option == 3:
                self.show_client_list()
            elif option == 4:
                self.show_client_details()
            elif option == 5:
                print("\nOpción no implementada")
            elif option == 6:
                print("\nOpción no implementada")
            elif option == 7:
                print("\nOpción no implementada")
            else:
                print(f"No existe la opción {option}")

    def load_test_data(self):
        """Carga datos de prueba."""
        self.clients = test_data.clients
        self.boats = test_data.boats


if __name__ == "__main__":
    gestion = RentalManagement()
    gestion.load_test_data()
    gestion.run_app()
