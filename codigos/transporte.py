class Transporte:
    def __init__(self, tipo, capacidad_gente, capacidad_carga, velocidad_maxima, marca, modelo, color, precio, peso, combustible):
        self.tipo = tipo
        self.capacidad_gente = capacidad_gente
        self.capacidad_carga = capacidad_carga
        self.velocidad_maxima = velocidad_maxima
        self.marca = marca
        self.modelo = modelo 
        self.color = color
        self.precio = precio
        self.peso = peso
        self.combustible = combustible

        print(f"Tipo de Transporte: {self.tipo}")
        print(f"Capacidad de gente: {self.capacidad_gente}")
        print(f"Capacidad de carga: {self.capacidad_carga}")
        print(f"Velocidad Máxima: {self.velocidad_maxima}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        print(f"Peso: {self.peso}")
        print(f"Combustible: {self.combustible}")

        def encender(self) -> None:
            """
            Se activa el motor del transporte

            Este método no recibe argumentos adicionales ni hace return hacia otro valor
            """
            print("Método: El transporte se ha encendido")

        def apagar(self) -> None:
            """
            El transporte se ha apagado automáticamente

            Este método no recibe argumentos adicionales ni hace return hacia otro valor
            """
            print("Método: El transporte se ha apagado")

        def avanzar(self) -> None:
            """
            Inicia el movimiento del transporte hacia adelanta

            Este método no recibe argumentos adicionales ni hace return hacia otro valor
            """
            print("Método: El transporte está avanzando")

        def detener(self) -> None:
            """
            Se aplican los frenos para detener el movimiento del transporte 

            Este método no recibe argumentos adicionales ni hace return hacia otro valor
            """
            print("Método: El transporte se ha detenido")

        def cargarCombustible(self) -> None:
            """
            Se carga el tanque del transporte con el combustible exacto 

            Este método no recibe argumentos adicionales ni hace return hacia otro valor
            """
            print("Método: Se ha cargado combustible al transporte")

mi_transporte = Transporte("Terrestre", 3, "20 Toneladas", "110 km/h", "Kenworth", "T680", "Azul", 250000, "8 Toneladas", "Diesel")

