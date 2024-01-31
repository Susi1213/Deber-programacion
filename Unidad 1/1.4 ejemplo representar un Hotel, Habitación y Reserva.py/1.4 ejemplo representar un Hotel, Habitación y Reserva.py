class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones_disponibles = []

    def agregar_habitacion(self, numero, tipo, precio):
        habitacion = Habitacion(numero, tipo, precio)
        self.habitaciones_disponibles.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print(f"Habitaciones disponibles en {self.nombre}:")
        for habitacion in self.habitaciones_disponibles:
            print(habitacion)

    def realizar_reserva(self, habitacion, cliente, noches):
        habitacion.reservar(cliente, noches)


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False
        self.cliente_actual = None
        self.noches_reservadas = 0

    def reservar(self, cliente, noches):
        if not self.reservada:
            self.reservada = True
            self.cliente_actual = cliente
            self.noches_reservadas = noches
            print(f"Habitación {self.numero} reservada por {cliente} por {noches} noches.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def __str__(self):
        estado_reserva = "Reservada" if self.reservada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}): {estado_reserva}, Precio: ${self.precio} por noche"


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


# Ejemplo de uso del sistema de reservas
if __name__ == "__main__":
    # Crear un hotel
    mi_hotel = Hotel("Hotel Ejemplo")

    # Agregar habitaciones al hotel
    mi_hotel.agregar_habitacion(101, "Doble", 120)
    mi_hotel.agregar_habitacion(102, "Individual", 80)
    mi_hotel.agregar_habitacion(103, "Suite", 200)

    # Mostrar habitaciones disponibles
    mi_hotel.mostrar_habitaciones_disponibles()

    # Crear un cliente
    cliente1 = Cliente("Juan")

    # Realizar una reserva
    mi_hotel.realizar_reserva(mi_hotel.habitaciones_disponibles[0], cliente1, 3)

    # Mostrar habitaciones disponibles después de la reserva
    mi_hotel.mostrar_habitaciones_disponibles()