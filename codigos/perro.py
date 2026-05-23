class Perro:
    def __init__(self, nombre, raza, edad, peso, color_pelaje, tipo_pelo, genero, es_estirilizado, temperamento, alergias):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color_pelaje = color_pelaje
        self.tipo_pelo = tipo_pelo
        self.genero = genero
        self.es_esterilizado = es_estirilizado
        self.temperamento = temperamento
        self.alergias = alergias

        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"Color de pelo: {self.color_pelaje}")
        print(f"Tipo de pelo: {self.tipo_pelo}")
        print(f"Género: {self.genero}")
        print(f"¿Está esterilizado? {self.es_esterilizado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"¿Tiene alergias? {self.alergias}")

    def morder(self) -> None:
        """
        Simula la acción en la que el perro muerde x objeto

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El perro ha mordido")

    def ladrar(self) -> None:
        """
        Simula que el perro emite un ladrido

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El perro ha ladrado")

    def correr(self) -> None:
        """
        Simula que el perro se desplaza corriendo

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El perro está corriendo")

    def jugar(self) -> None:
        """
        Simula que el perro se encuentra jugando

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El perro quiere jugar")

    def comer(self) -> None:
        """
        Simula el momento en el que el perro consume sus alimentos

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El perro quiere comer")

mi_perro = Perro("Zansón", "Pastor Alemán", "9 años", "35 kg", "Negro con Marrón", "Corto", "Macho", False, "Agresivo", False)
