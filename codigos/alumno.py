class Alumno:
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
        """Registra formalmente a la alumna en el ciclo escolar actual.

        Args:
            Ninguno.

        Return:
            None: Este método solo imprime el resultado en consola, no devuelve valores.
        """
        print("Método: La alumna se ha inscrito")

    def aplicarBeca(self) -> None:
        """Inicia el proceso de solicitud para un apoyo económico o beca estudiantil.

        Args:
            Ninguno.

        Return:
            None: Este método solo imprime el resultado en consola, no devuelve valores.
        """
        print("Método: La alumna ha aplicado para la beca")

    def obtenerKardex(self) -> None:
        """Consulta y despliega el historial académico detallado de la alumna.

        Args:
            Ninguno.

        Return:
            None: Este método solo imprime el resultado en consola, no devuelve valores.
        """
        print("Método: La alumna ha obtenido su kárdex")

    def aprobar(self) -> None:
        """Verifica y confirma que la alumna ha acreditado la totalidad de sus asignaturas.

        Args:
            Ninguno.

        Return:
            None: Este método solo imprime el resultado en consola, no devuelve valores.
        """
        print("Método: La alumna ha aprobado todas sus materias")

    def registrarAsistencia(self) -> None:
        """Registra la presencia de la alumna en la bitácora escolar del día actual.

        Args:
            Ninguno.

        Return:
            None: Este método solo imprime el resultado en consola, no devuelve valores.
        """
        print("Método: La alumna ha registrado su asistencia del día")

mi_alumna = Alumno("Ariadna Aleyda", "Romero Gonzalez", 20, 1725110987, "UAEH Instituto de Artes", "Licenciatura en Música", 20,
                   77577777, "Segundo", 9.5)
