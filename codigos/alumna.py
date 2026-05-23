class Alumna:
    def __init__(self, nombre, apellidos, edad, matricula, universidad, carrera, grupo, telefono, semestre, promedio_general):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.matricula = matricula
        self.universidad = universidad
        self.carrera = carrera
        self.grupo = grupo
        self.telefono = telefono
        self.semestre = semestre
        self.promedio_general = promedio_general

        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")
        print(f"Universidad: {self.universidad}")
        print(f"Carrera: {self.carrera}")
        print(f"Grupo: {self.grupo}")
        print(f"Teléfono: {self.telefono}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio General: {self.promedio_general}")


    def inscribir(self) -> None:
        """
        Registra la inscripción de la alumna a su nuevo ciclo escolar

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La alumna se ha inscrito")

    def aplicarBeca(self) -> None:
        """
        Inicia el proceso de solicitud para beca estudiantil

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La alumna ha aplicado para la beca")

    def obtenerKardex(self) -> None:
        """
        Consulta o solicita su historial académico 

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La alumna ha obtenido su kárdex")

    def aprobar(self):
        """
        Verifica que la alumna ha acreditado sus asignaturas

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La alumnna ha aprobado todas sus materias")

    def registrarAsistencia(self):
        """
        Se registra la asistencia de la alumna en la lista

        Este método no recibe argumentos adicionales ni hace return hacia otro valor
        """
        print("Método: La alumna ha registrado su asistencia del día")

mi_alumna = Alumna("Ariadna Aleyda", "Romero Gonzalez", 20, 1725110987, "UAEH Instituto de Artes", "Licenciatura en Música", 20,
                   77577777, "Segundo", 9.5)