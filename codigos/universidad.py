class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informatico, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informatico = sistema_informatico
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres
        self.cantidad_salones = cantidad_salones
        self.rector = rector

        print(f"Logotipo de la Universidad: {self.logo}")
        print(f"Oferta Educativa: {self.oferta_educativa}")
        print(f"Localidad: {self.localidad}")
        print(f"Sistema Informático: {self.sistema_informatico}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Servicios: {self.servicios}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Talleres: {self.talleres}")
        print(f"Cantidad de Salones: {self.cantidad_salones}")
        print(f"Rector: {self.rector}")

    def matricularEstudiante(self):
        print("Método: La Universidad matriculó a todos sus estudiantes")

    def contratarProfesor(self):
        print("Método: La Universidad contrató a X profesor")

    def abrirCicloEscolar(self):
        print("Método: La Universidad abrió su nuevo ciclo escolar")

    def firmarConvenio(self):
        print("Método: La Universidad firmó nuevos convenios")

    def organizarEventos(self):
        print("Método: La Universidad está organizando futuros eventos")

unideh = Universidad ("Logo.jpg", "Ing en Software, Turismo Alternativo, Gestión Empresarial y de Proyectos", "San Miguel", 
                      "CADU", "Virtual", "Biblioteca Digital", "Santa Catarina", None, None, "Octavio Castillo")