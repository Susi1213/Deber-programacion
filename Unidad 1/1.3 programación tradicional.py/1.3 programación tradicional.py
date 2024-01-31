# Programación Tradicional

def ingresar_temperaturas_diarias():
    temperaturas = [ ]
    for i in range ( 7 ):
        temp = float ( input ( f"Ingrese la temperatura del día {i + 1}: " ) )
        temperaturas.append ( temp )
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    promedio = sum ( temperaturas ) / len ( temperaturas )
    return promedio


def main():
    temperaturas_diarias = ingresar_temperaturas_diarias ()
    promedio_semanal = calcular_promedio_semanal ( temperaturas_diarias )

    print ( f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}" )


if __name__ == "__main__":
    main ()