class Silla:
    def __init__(self, alto, marca, ancho, material, color, peso_maximo, es_giratoria, cantidad_patas, estado_uso, precio):
        self.alto = alto
        self.marca = marca
        self.ancho = ancho
        self.material = material
        self.color = color
        self.peso_maximo = peso_maximo
        self.es_giratoria = es_giratoria
        self.cantidad_patas = cantidad_patas
        self.estado_uso = estado_uso
        self.precio = precio

        print(f"El alto es de: {self.alto}")
        print(f"Marca: {self.marca}")
        print(f"El ancho es de: {self.ancho}")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Peso Máximo: {self.peso_maximo}")
        print(f"¿Es giratoria? {self.es_giratoria}")
        print(f"Cantidad de patas: {self.cantidad_patas}")
        print(f"Estado de uso: {self.estado_uso}")
        print(f"Precio: ${self.precio}")

    def soportarPeso(self) -> None:
        """
        Se le coloca peso a la silla 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La silla soporta x peso")

    def limpiar(self) -> None:
        """
        Se le realiza una limpieza a la silla

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La silla se limpia")

    def desplazar(self) -> None:
        """
        La silla realiza un desplazamiento hacia otro lugar

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La silla se puede desplazar")

    def ajustarAltura(self) -> None:
        """
        La persona ajusta la altura de la silla para su comodidad

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La silla puede ajustar su altura")

    def girar(self) -> None:
        """
        La persona sentada en la silla comienza a girar 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La silla puede girar")
    
mi_silla = Silla("120 cm", "DRAKE", "60cm", "Metal", "Gris y Negro", "60 kg", True, "3", "Nueva", "600")
