# Abstracción: Clase Base Fruta
class Fruta:
    def __init__(self, nombre, color, sabor):
        # Atributos que representan características esenciales de una fruta
        self.nombre = nombre
        self.color = color
        self.sabor = sabor

    def descripcion(self):
        # Método que proporciona una descripción básica de la fruta
        return f"Nombre: {self.nombre}\nColor: {self.color}\nSabor: {self.sabor}"

    # Encapsulación: Método Privado para Actualizar Stock
    def __actualizar_stock(self, nuevo_stock):
        # Método privado para cambiar el stock (no accesible desde fuera de la clase)
        if nuevo_stock >= 0:
            print(f"Stock actualizado a {nuevo_stock}")
        else:
            print("Stock no válido")

    def agregar_stock(self, cantidad_stock):
        # Método público que utiliza el método privado __actualizar_stock
        self.__actualizar_stock(cantidad_stock)

# Demostración de Frutas
manzana = Fruta("Manzana", "Rojo", "Dulce")
platano = Fruta("Plátano", "Amarillo", "Ligeramente dulce")

print(manzana.descripcion())
print(platano.descripcion())