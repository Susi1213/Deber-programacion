import csv


class Producto:
    def __init__(self , id , nombre , cantidad , precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self , producto):
        self.productos [ producto.id ] = producto

    def eliminar_producto(self , id):
        if id in self.productos:
            del self.productos [ id ]

    def actualizar_producto(self , id , cantidad=None , precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos [ id ].cantidad = cantidad
            if precio is not None:
                self.productos [ id ].precio = precio

    def buscar_producto_por_nombre(self , nombre):
        resultados = [ ]
        for producto in self.productos.values ():
            if producto.nombre == nombre:
                resultados.append ( producto )
        return resultados

    def mostrar_productos(self):
        for producto in self.productos.values ():
            print ( producto )

    def guardar_inventario(self , nombre_archivo):
        with open ( nombre_archivo , 'w' , newline = '' ) as archivo:
            escritor_csv = csv.writer ( archivo )
            for producto in self.productos.values ():
                escritor_csv.writerow ( [ producto.id , producto.nombre , producto.cantidad , producto.precio ] )

    def cargar_inventario(self , nombre_archivo):
        with open ( nombre_archivo , 'r' ) as archivo:
            lector_csv = csv.reader ( archivo )
            for linea in lector_csv:
                id , nombre , cantidad , precio = linea
                self.agregar_producto ( Producto ( id , nombre , int ( cantidad ) , float ( precio ) ) )


def menu():
    print ( "1. Agregar producto" )
    print ( "2. Eliminar producto" )
    print ( "3. Actualizar producto" )
    print ( "4. Buscar producto por nombre" )
    print ( "5. Mostrar todos los productos" )
    print ( "6. Guardar inventario en archivo" )
    print ( "7. Cargar inventario desde archivo" )
    print ( "8. Salir" )
    return input ( "Seleccione una opción: " )


if __name__ == "__main__":
    inventario = Inventario ()

    while True:
        opcion = menu ()

        if opcion == '1':
            id = input ( "Ingrese ID del producto: " )
            nombre = input ( "Ingrese nombre del producto: " )
            cantidad = int ( input ( "Ingrese cantidad del producto: " ) )
            precio = float ( input ( "Ingrese precio del producto: " ) )
            inventario.agregar_producto ( Producto ( id , nombre , cantidad , precio ) )

        elif opcion == '2':
            id = input ( "Ingrese ID del producto a eliminar: " )
            inventario.eliminar_producto ( id )

        elif opcion == '3':
            id = input ( "Ingrese ID del producto a actualizar: " )
            cantidad = input ( "Ingrese nueva cantidad (deje en blanco para mantener): " )
            precio = input ( "Ingrese nuevo precio (deje en blanco para mantener): " )
            inventario.actualizar_producto ( id , int ( cantidad ) if cantidad else None ,
                                             float ( precio ) if precio else None )

        elif opcion == '4':
            nombre = input ( "Ingrese nombre del producto a buscar: " )
            resultados = inventario.buscar_producto_por_nombre ( nombre )
            if resultados:
                for producto in resultados:
                    print ( producto )
            else:
                print ( "Producto no encontrado." )

        elif opcion == '5':
            inventario.mostrar_productos ()

        elif opcion == '6':
            nombre_archivo = input ( "Ingrese el nombre del archivo para guardar el inventario: " )
            inventario.guardar_inventario ( nombre_archivo )
            print ( "Inventario guardado correctamente." )

        elif opcion == '7':
            nombre_archivo = input ( "Ingrese el nombre del archivo para cargar el inventario: " )
            inventario.cargar_inventario ( nombre_archivo )
            print ( "Inventario cargado correctamente." )

        elif opcion == '8':
            print ( "Saliendo del programa..." )
            break


if __name__ == "__main__":
    menu()
