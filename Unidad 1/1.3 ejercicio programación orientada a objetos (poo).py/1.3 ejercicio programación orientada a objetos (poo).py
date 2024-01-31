# Programación Orientada a Objetos (POO)

class ClimaDiario:
    def __init__(self):
        self.temperaturas = [ ]

    def ingresar_temperaturas_diarias(self):
        for i in range ( 7 ):
            temp = float ( input ( f"Ingrese la temperatura del día {i + 1}: " ) )
            self.temperaturas.append ( temp )

    def calcular_promedio_semanal(self):
        promedio = sum ( self.temperaturas ) / len ( self.temperaturas )
        return promedio


def main():
    clima = ClimaDiario ()
    clima.ingresar_temperaturas_diarias ()
    promedio_semanal = clima.calcular_promedio_semanal ()

    print ( f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}" )


if __name__ == "__main__":
    main ()