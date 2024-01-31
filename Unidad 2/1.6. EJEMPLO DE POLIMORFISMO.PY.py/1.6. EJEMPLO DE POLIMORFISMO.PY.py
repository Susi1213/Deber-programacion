# Definición de la clase base
class ProductoElectronico:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Encapsulación
        self.__precio = precio

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def mostrar_informacion(self):
        print(f"Producto: {self.__nombre}, Precio: ${self.__precio}")


# Clase derivada que hereda de ProductoElectronico
class Smartphone(ProductoElectronico):
    def __init__(self, nombre, precio, modelo):
        # Llamamos al constructor de la clase base usando super()
        super().__init__(nombre, precio)
        self.__modelo = modelo  # Encapsulación

    def obtener_modelo(self):
        return self.__modelo

    # Sobrescritura de método de la clase base
    def mostrar_informacion(self):
        # Llamamos al método de la clase base usando super()
        super().mostrar_informacion()
        print(f"Modelo: {self.__modelo}")


# Función que demuestra polimorfismo
def imprimir_info_producto(producto):
    producto.mostrar_informacion()


# Crear instancias de las clases
producto_generico = ProductoElectronico("Cargador USB", 15.99)
smartphone1 = Smartphone("iPhone 13", 999.99, "A2483")
smartphone2 = Smartphone("Samsung Galaxy S21", 799.99, "G910F")

# Usar polimorfismo al llamar a la función con diferentes tipos de objetos
imprimir_info_producto(producto_generico)
imprimir_info_producto(smartphone1)
imprimir_info_producto(smartphone2)