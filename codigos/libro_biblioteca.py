class LibroBiblioteca:
    def __init__(self, titulo, autor, editorial, paginas, version_digital, anio, genero, estado_fisico, disponible, idioma):
        self.titulo = titulo
        self.autor = autor 
        self.editorial = editorial
        self.paginas = paginas
        self.version_digital = version_digital
        self.anio = anio
        self.genero = genero
        self.estado_fisico = estado_fisico
        self.disponible = disponible
        self.idioma = idioma

        print(f"Título del libro: {self.titulo}")
        print(f"Autor del libro: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Cantida de páginas: {self.paginas}")
        print(f"Version digital: {self.version_digital}")
        print(f"Año: {self.anio}")
        print(f"Género: {self.genero}")
        print(f"Estado fisico: {self.estado_fisico}")
        print(f"Disponibilidad: {self.disponible}")
        print(f"Idioma: {self.idioma}")

    def prestar(self):
        print("Método: El libro ha sido prestado")
    
    def renovar(self):
        print("Método: El libro ha sido renovado")
    
    def extenderDias(self):
        print("Método: Se han extendido días")

    def leer(self):
        print("Método: El libro ha sido leído")

    def estudiar(self):
        print("Método: El libro es para estudiar")

mi_libro = LibroBiblioteca("Harry Potter y la Piedra Filosofal", "J.K Rowling", "Bloomsbury", 223, True, 1997, "Fantasía", "Bueno", True, "Español")