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


    def inscribir(self):
        print("Método: La alumna se ha inscrito")

    def aplicarBeca(self):
        print("Método: La alumna ha aplicado para la beca")

    def obtenerKardex(self):
        print("Método: La alumna ha obtenido su kárdex")

    def aprobar(self):
        print("Método: La alumnna ha aprobado todas sus materias")

    def registrarAsistencia(self):
        print("Método: La alumna ha registrado su asistencia del día")

mi_alumna = Alumno("Ariadna Aleyda", "Romero Gonzalez", 20, 1725110987, "UAEH Instituto de Artes", "Licenciatura en Música", 20,
                   77577777, "Segundo", 9.5)
