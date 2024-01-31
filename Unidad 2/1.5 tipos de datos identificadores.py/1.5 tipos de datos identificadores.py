# Programa de conversión de unidades de temperatura
# Este programa convierte unidades de temperatura entre Celsius, Fahrenheit y Kelvin,
# utilizando diferentes tipos de datos (int, float, str, bool) de manera adecuada.

def celsius_to_fahrenheit(celsius):
    """Convierte temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convierte temperatura de Celsius a Kelvin."""
    return celsius + 273.15

# Función principal
def main():
    # Solicitar al usuario la temperatura en Celsius
    celsius_str = input("Ingrese la temperatura en grados Celsius: ")

    # Validar la entrada del usuario
    try:
        # Convertir la entrada a float
        celsius = float(celsius_str)

        # Realizar las conversiones
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)

        # Mostrar los resultados
        print("\nResultados:")
        print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
        print(f"{celsius} grados Celsius son {kelvin:.2f} Kelvin.")

        # Ejemplo de uso de diferentes tipos de datos
        # bool para verificar si la temperatura en Celsius es mayor que 0
        es_positiva = celsius > 0
        print(f"\n¿La temperatura en Celsius es positiva? {es_positiva}")

    except ValueError:
        print("Error: Ingrese un número válido para la temperatura en Celsius.")

if __name__ == "__main__":
    main()