class Quimera:
    def __init__(self, cabeza, habitat, velocidad, agresividad, habilidades, edad, colores, nombre, elemento, altura):
        self.cabeza = cabeza
        self.habitat = habitat
        self.velocidad = velocidad
        self.agresividad = agresividad
        self.habilidades = habilidades 
        self.edad = edad
        self.colores = colores
        self.nombre = nombre
        self.elemento = elemento
        self.altura = altura

        print(f"Tipo de cabezas: {self.cabeza}")
        print(f"Hábitat: {self.habitat}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Nivel de agresividad: {self.agresividad}")
        print(f"Tipo de habilidades: {self.habilidades}")
        print(f"Edad: {self.edad}")
        print(f"Colores: {self.colores}")
        print(f"Nombre: {self.nombre}")
        print(f"Elemento: {self.elemento}")
        print(f"Altura: {self.altura}")

    def escupirFuego(self):
        print("Método: La quimera ha escupido fuego")

    def morder(self):
        print("Método: La quimera ha mordido")

    def volar(self):
        print("Método: La quimera está volando")

    def rugir(self):
        print("Método: La quimera ha rugido")

    def morir(self):
        print("Método: La quimera ha muerto")

mi_quimera = Quimera("León, Cabra y Serpiente", "Montañas", "85 km/h", "Extrema", "Aliento de fuego", "300 años", "Rojo y Negro", "Monkey D. Luffy", "Fuego", "5 metros")

