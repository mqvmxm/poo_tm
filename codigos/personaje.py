class Personaje:
    def __init__(self, nombre, nivel, defensa, ataque, habilidades, tp_maximo, debilidad, hp_actual, rango_estiramiento, inmunidad_electricidad):
        self.nombre = nombre
        self.nivel = nivel
        self.defensa = defensa
        self.ataque = ataque
        self.habilidades = habilidades
        self.tp_maximo = tp_maximo
        self.debilidad = debilidad
        self.hp_actual = hp_actual
        self.rango_estiramiento = rango_estiramiento
        self.inmunidad_electricidad = inmunidad_electricidad

        print(f"Nombre del personaje: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Defensa: {self.defensa}")
        print(f"Ataque: {self.ataque}")
        print(f"Habilidades: {self.habilidades}")
        print(f"TP Máximo: {self.tp_maximo}")
        print(f"Debilidad: {self.debilidad}")
        print(f"HP Actual: {self.hp_actual}")
        print(f"Rango de Estiramiento: {self.rango_estiramiento}")
        print(f"Inmunidad a la Electricidad: {self.inmunidad_electricidad}")

    def atacar(self) -> None:
        """
        El personaje realiza un ataque al oponente

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El personaje ataca")

    def ejecutarHabilidad(self) -> None:
        """
        El personaje ejecuta sus habilidades de ataque 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El personaje ejecuta su habilidad")

    def recibirDaño(self) -> None:
        """
        El personaje recibe un ataque por parte del otro jugador

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El personaje ha recibido daño")
        
    def ganarExperiencia(self) -> None:
        """
        Conforme avanza el personaje va aumentando su experiencia 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El personaje ha ganado experiencia")
    
    def equiparAccesorios(self) -> None:
        """
        El personaje equipa sus accesorios necesarios 

        Este método recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El personaje ha equipado sus accesorios")

mi_personaje = Personaje("Luffy", 40, 410, 580, "Pistol", 500, 2.0, 2450, 15.5, True)
