# Repositorios de Programación Orientada a Objetos con Python

Repositorio con ejercicios de Programación Orientada a Objetos

## 1. Crear .gitignore

Crear el archivo -gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el repositorio.

````shell
*.pyc
_pycache_/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de documentos nuevos. 

````shell
git add .
````

## 3. Crear un COMMIT

Crea un commit o punto de control de los cambios realizados en el proyecto. 

````shell
git commit -m "CREATED gitignore"
````

* CREATED - Se crearon nuevas carpetas.
* UPDATED - Se actualizaron o agregaron nuevas funciones.
* FIXED - Se corrigieron errores.

## 4. Realizar el COMMIT

Sincroniza los cambios realizados en el repositorio.

````shell
git push -u origin main
````

## 5. Agregar Documentación a los métodos

Agregar un **DocString** a los métodos generados.

````python 
def metodoUno(self):
    """
    Imprime el texto Método Uno

    Este método no recibe argumentos adicionales ni hace return a otro valor
    """
    
    print("Método Uno")


def metodoDos(self, variable_uno: int, variable_dos: float):
    """
    Este método recibe 2 variables enteras, la suma y regresa
    el resultado de la suma

    Args:

    variable_uno : int - Primer numero entero
    variable_dos : float - Segundo numero flotante

    Return:

    suma : int - Suma de los dos numeros enteros
    """

    suma = variable_uno + variable_dos
    return int(suma)

def metodoTres(self, variable_tres:str)->None:
    """
    Cuenta e imprime la cantidad de caracteres que tiene una cadena de texto.

    Args:
    variable_tres : str - El texto del que se desea calcular la longitud

    Return: 
    None: Este método solo imprime el resultado en consola, no devuelve valores.

    """

    print(f"Número de caracteres: {len(variable_tres)}")

