#Importacion de librerrias necesarias

#from datetime import date

#Definicion de clase Libro con sus atributos y metodos
class Libro():

    #Varible que alojara todos los libros
    libros = []

    #Corresponde a los valores de estado de un libro ya establecidos
    estados = {
        1:"prestado",
        2:"disponible",
        3:"inactivo"
    }

    #Corresponde a los valores de estado de un libro ya establecidos
    condiciones = {
        1:"excelente",
        2:"daniado",
        3:"danios menores"
    }

    #Constructor de la clase Libro
    def __init__(self, nombre_libro, codigo, isbn, autor, edicion, anio_publicacion, condicion):

        self.nombre_libro: str = nombre_libro
        self.codigo: int = codigo
        self.isbn: str = isbn
        self.autor: str = autor
        self.edicion: str = edicion
        self.anio_publicacion: int = anio_publicacion
        self.estado: str = "disponible"
        self.definir_condicion(condicion)

        Libro.libros.append(self)

    #Determina un estado de libro que sea valida al ingresarlo, usando un variable de clase
    def definir_estado(self, estado):
        if estado in Libro.estados:
            self.estado = Libro.estados[estado]
        else:
            raise ValueError("La opcion indicada no es valida")

    #Determina un condicion de libro que sea valida al ingresarlo, usando un variable de clase    
    def definir_condicion(self, condicion):
        if condicion in Libro.condiciones:
            self.condicion = Libro.condiciones[condicion]
        else:
            raise ValueError("La opcion indicada no es valida")


        
