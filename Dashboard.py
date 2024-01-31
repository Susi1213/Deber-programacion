import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1':'Unidad 1/0.1 Ejercicios técnicas de programación.py',
        '2':'Unidad 1/1.1 programación tradicional.py',
        '3':'Unidad 1/1.3 ejercicio programación orientada a objetos (poo).py',
        '4':'Unidad 1/1.3 programación tradicional.py',
        '5':'Unidad 1/1.4 ejemplo representar un Hotel, Habitación y Reserva.py',
        '6':'Unidad 2/1.5 tipos de datos identificadores.py',
        '7':'Unidad 2/1.6. EJEMPLO DE POLIMORFISMO.PY.',
        '8':'Unidad 2/1.7 constructores y destructores ejemplo.py',

# Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
