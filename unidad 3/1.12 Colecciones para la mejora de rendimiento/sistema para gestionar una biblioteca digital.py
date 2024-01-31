class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def añadir_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.usuario_id)

    def dar_de_baja_usuario(self, usuario):
        if usuario.usuario_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.usuario_id)

    def prestar_libro(self, libro, usuario):
        if libro.isbn in self.libros_disponibles and usuario.usuario_id in self.usuarios_registrados:
            self.libros_disponibles.pop(libro.isbn)
            usuario.libros_prestados.append(libro)

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            self.libros_disponibles[libro.isbn] = libro

    def buscar_libros_por_titulo(self, titulo):
        return [libro for libro in self.libros_disponibles.values() if titulo.lower() in libro.titulo_autor[0].lower()]

    def buscar_libros_por_autor(self, autor):
        return [libro for libro in self.libros_disponibles.values() if autor.lower() in libro.titulo_autor[1].lower()]

    def buscar_libros_por_categoria(self, categoria):
        return [libro for libro in self.libros_disponibles.values() if categoria.lower() == libro.categoria.lower()]

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados


# Ejemplo de uso:
if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "978-0307474728")
    libro2 = Libro("El nombre del viento", "Patrick Rothfuss", "Fantasía", "978-8401352836")
    libro3 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Misterio", "978-0307743915")

    usuario1 = Usuario("Juan", 1)
    usuario2 = Usuario("María", 2)

    biblioteca = Biblioteca()
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    biblioteca.prestar_libro(libro1, usuario1)
    biblioteca.prestar_libro(libro2, usuario2)

    print("Libros prestados a Juan:", [libro.titulo_autor[0] for libro in biblioteca.listar_libros_prestados(usuario1)])
    print("Libros prestados a María:", [libro.titulo_autor[0] for libro in biblioteca.listar_libros_prestados(usuario2)])

    print("Busqueda por título 'soledad':", [libro.titulo_autor[0] for libro in biblioteca.buscar_libros_por_titulo("soledad")])
    print("Busqueda por autor 'García Márquez':", [libro.titulo_autor[0] for libro in biblioteca.buscar_libros_por_autor("García Márquez")])
    print("Busqueda por categoría 'Fantasía':", [libro.titulo_autor[0] for libro in biblioteca.buscar_libros_por_categoria("Fantasía")])