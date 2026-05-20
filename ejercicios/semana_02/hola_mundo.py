class NombreClase: 

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Método Uno")

    def metodoDos(self, variable_uno: int, variable_dos: float):
        """
        Este método redibe 2 variables enteras, la suma y regresa
        el resultado de la suma

        Args:

        variable_uno : int - Primer numero entero
        variable_dos : int - Segundo numero entero

        Return:

        suma : int - Suma de los dos numeros enteros
        """

        suma = variable_uno + variable_dos
        return int(suma)
    
    def metodoTres(self, variable_tres:str)->None:
        print(f"Número de caracteres: {len(variable_tres)}")

    

nombre_objeto = NombreClase()
nombre_objeto.metodoUno()

