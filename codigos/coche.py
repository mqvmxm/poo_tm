class Coche: 
    def __init__(self, numero_puertas, transmision, numero_asientos, camara_reversa, tipo_frenos, gps, volumen_cajuela, placa, traccion, ventanas_electricas):
        self.numero_puertas = numero_puertas
        self.transmision = transmision
        self.numero_asientos = numero_asientos
        self.camara_reversa = camara_reversa
        self.tipo_frenos = tipo_frenos
        self.gps = gps
        self.volumen_cajuela = volumen_cajuela
        self.placa = placa
        self.traccion = traccion
        self.ventanas_electricas = ventanas_electricas

        print(f"Numero de puertas: {self.numero_puertas}")
        print(f"Transmisión: {self.transmision}")
        print(f"Número de Asientos: {self.numero_asientos}")
        print(f"¿Tiene cámara reversa? {self.camara_reversa}")
        print(f"Tipo de frenos: {self.tipo_frenos}")
        print(f"¿Tiene GPS? {self.gps}")
        print(f"Volúmen de la cajuela: {self.volumen_cajuela}")
        print(f"Placa: {self.placa}")
        print(f"Tracción: {self.traccion}")
        print(f"¿Tiene ventanas eléctricas? {self.ventanas_electricas}")

    def estacionarse(self) -> None:
        """
        El coche realiza el movimiento para estacionarse

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print(f"Método: El coche se ha estacionado")

    def activarSeguros(self) -> None:
        """
        Bloquea las puertas por seguridad

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print(f"Método: El coche ha activado los seguros")

    def conectarBluetooth(self) -> None:
        """
        Se establece una conexión inalámbrica con algún otro dispositivo

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print(f"Metodo: Dispositivo bluetooth conectado")

    def activarLimpiaParabrisas(self) -> None:
        """
        Se activan los Limpia Parabrisas para mejorar la visibilidad

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print(f"Se ha activado el limpia parabrisas")

    def prenderLuces(self) -> None:
        """
        Se encienden las luces principales del coche 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print(f"Se han prendido las luces")

mi_coche = Coche(4, "Automática", 5, True, "ABS", True, "450 lts", "REY-20-06", "Delantera", True)