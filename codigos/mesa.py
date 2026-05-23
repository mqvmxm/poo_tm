class Mesa:
    def __init__(self, material, ancho, alto, estilo, forma, color, soporte, peso, capacidad, estado):
        self.material = material
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.forma = forma
        self.color = color 
        self.soporte = soporte
        self.peso = peso
        self.capacidad = capacidad
        self.estado = estado

        print(f"Material: {self.material}")
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Estilo: {self.estilo}")
        print(f"Forma: {self.forma}")
        print(f"Color: {self.color}")
        print(f"Soporte: {self.soporte}")
        print(f"Peso: {self.peso}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Estado: {self.estado}")

    def limpiarSuperficie(self) -> None:
        """
        Se remueve la suciedad de la superficie

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: Se ha limpiado la superficie de la mesa")

    def soportarPeso(self) -> None:
        """
        Sostiene una carga sobre la superficie 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La mesa soporta X peso")

    def colocarObjeto(self) -> None:
        """
        Se añade un objeto a la superficie 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: Se le ha colocado un objeto a la mesa")

    def retirarObjeto(self) -> None:
        """
        Se quitan los objetos que se encuentran en la superficie

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: Se le ha retirado el objeto a la mesa")

    def rayarSuperficie(self) -> None:
        """
        Se realizan marcas o daños a la superficie 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: Se ha rayado la superficie de la mesa")

mi_mesa = Mesa("Madera", "80cm", "75cm", "Vintage", "Rectangular", "Café", "4 patas de madera", "25kg", "80 kg", "Nueva")





