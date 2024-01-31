<<<<<<< HEAD
=======
import csv

>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}
<<<<<<< HEAD
=======
        self.archivo = "inventario.txt"

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r', newline='') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                for linea in lector_csv:
                    id_producto, nombre, cantidad, precio = linea
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print("Permiso denegado para acceder al archivo de inventario.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                for producto in self.productos.values():
                    escritor_csv.writerow([producto.id_producto, producto.nombre, producto.cantidad, producto.precio])
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Permiso denegado para guardar el archivo de inventario.")
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
<<<<<<< HEAD
=======
            self.guardar_inventario()
            print("Producto agregado al inventario.")
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
<<<<<<< HEAD
=======
            self.guardar_inventario()
            print("Producto eliminado del inventario.")
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
<<<<<<< HEAD
=======
            self.guardar_inventario()
            print("Producto actualizado en el inventario.")
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

<<<<<<< HEAD
    def mostrar_productos_(self):
        pass

    def mostrar_productos(self):
        pass


def mostrar_productos(self):
    if self.productos:
        for producto in self.productos:
            print ( producto )


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
=======
# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    inventario.cargar_inventario()  # Cargar el inventario al iniciar el programa
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
<<<<<<< HEAD
            break
        elif opcion == '1':
            id = input ( "Ingrese el ID del producto: " )
            nombre = input ( "Ingrese el nombre del producto: " )
            cantidad = int ( input ( "Ingrese la cantidad del producto: " ) )
            precio = float ( input ( "Ingrese el precio del producto: " ) )
            producto = Producto ( id , nombre , cantidad , precio )
            inventario.agregar_producto ( producto )
        elif opcion == '2':
            id = input ( "Ingrese el ID del producto a eliminar: " )
            inventario.eliminar_producto ( id )
        elif opcion == '3':
            id = input ( "Ingrese el ID del producto a actualizar: " )
            cantidad = input ( "Ingrese la nueva cantidad (deje en blanco si no desea actualizar): " )
            precio = input ( "Ingrese el nuevo precio (deje en blanco si no desea actualizar): " )
            if cantidad:
                cantidad = int ( cantidad )
            if precio:
                precio = float ( precio )
            inventario.actualizar_producto ( id , cantidad , precio )
=======
            inventario.guardar_inventario()  # Guardar el inventario antes de salir
            break
        elif opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea actualizar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea actualizar): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)
        elif opcion == '4':
            nombre = input("Ingrese el nombre o parte del nombre del producto:")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_productos()

            inventario.mostrar_inventario()
=======

if __name__ == "__main__":
    menu()
if __name__ == "__main__":
    <<<<<<< HEAD
    menu()
>>>>>>> 24a03fb (PROGRAMACION ORIENTADA A OBJETOS.iml)
