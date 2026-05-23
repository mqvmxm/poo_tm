class Telefono:
    def __init__(self, modelo, capacidad, color, porcentaje_bateria, operador, cantidad_camaras, numero_serie, espacio_usado, version, precio):
        self.modelo = modelo
        self.capacidad = capacidad
        self.color = color
        self.porcentaje_bateria = porcentaje_bateria
        self.operador = operador
        self.cantidad_camaras = cantidad_camaras
        self.numero_serie = numero_serie
        self.espacio_usado = espacio_usado
        self.version = version
        self.precio = precio

        print(f"El modelo es: {self.modelo}")
        print(f"La capacidad es de: {self.capacidad}")
        print(f"El color es: {self.color}")
        print(f"Porcentaje de bateria {self.porcentaje_bateria}")
        print(f"Operador: {self.operador}")
        print(f"Cantidad de Cámaras: {self.cantidad_camaras}")
        print(f"Número de serie: {self.numero_serie}")
        print(f"Espacio usado: {self.espacio_usado}")
        print(f"Versión Actual: {self.version}")
        print(f"Precio: ${self.precio}")

    def sacarFotografias(self) -> None:
        """
        El usuario toma una fotografía con la cámara del celular

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El teléfono ha sacado fotografías")

    def hacerLlamada(self) -> None:
        """
        El usuario realiza una llamada telefónica 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El teléfono está haciendo llamada")

    def abrirAplicacion(self) -> None:
        """
        El usuario realiza la acción de abrir diferentes aplicaciones

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El teléfono puede abrir diferentes aplicaciones")

    def recibirNotificaciones(self) -> None:
        """
        El teléfono manda diferentes tipos de notificaciones

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El teléfono recibe muchas notificaciones")

    def apagar(self) -> None:
        """
        El teléfono o el usuario pueden apagar el teléfono 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: El teléfono se apagó")

mi_iphone = Telefono("Iphone 13", "128 GB", "Azul", "74%", "TELCEL", "3", "WYKLQ7MV90", "110.29 GB", "iOS 26.4.2", "14,000")
