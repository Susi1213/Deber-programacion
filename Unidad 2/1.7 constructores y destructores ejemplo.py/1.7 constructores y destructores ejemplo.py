class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        Parameters:
        - nombre (str): El nombre de la persona.
        - edad (int): La edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva persona llamada {self.nombre} de {self.edad} años.")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Este método se llama automáticamente cuando el objeto es destruido.
        """
        print(f"La persona llamada {self.nombre} ha sido destruida.")

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Imprimir información de las personas
print(f"{persona1.nombre} tiene {persona1.edad} años.")
print(f"{persona2.nombre} tiene {persona2.edad} años.")

# Eliminar una instancia, lo que activará el destructor
del persona1

# Algunas acciones más...

# Al final del programa, cuando las variables dejan de referenciar a las instancias,
# el recolector de basura se encargará de llamar a los destructores restantes.