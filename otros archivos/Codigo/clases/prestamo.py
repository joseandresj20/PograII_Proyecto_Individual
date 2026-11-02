#Importacion de librerias necesarias
from clases.usuario import Usuario
from clases.libro import Libro
from datetime import date

#Definicion de clase Prestamo con sus atributos y metodos
class Prestamo():

    #Varible que alojara todos los prestamos
    registro_prestamos = []

    #Constructor de la clase Prestamo
    def __init__(self, usuario, libro, fecha_tentativa_devolucion):

        self.usuario: Usuario = usuario
        self.libro: Libro = libro
        self.fecha_prestamo: date = date.today()
        self.fecha_tentativa_devolucion: date = fecha_tentativa_devolucion
        self.devuelto = False

        Prestamo.registro_prestamos.append(self) 

    # Calcula los dias naturales de retraso.
    def calcular_dias_retraso(self):

        # Calcula los dias transcurridos desde la fecha de devolucion establecida.
        dias_retraso = (date.today() - self.fecha_tentativa_devolucion).days

        # Comprueba si existe un retraso.
        if dias_retraso > 0:
            return dias_retraso
        else:
            return 0

    # Calcula el monto de la multa por retraso.
    def calculo_multa(self):

        return self.calcular_dias_retraso() * 525

    # Registra la devolucion de un libro.
    def registrar_devolucion(self):

        # Comprueba si el libro ya fue devuelto.
        if self.devuelto:
            raise ValueError("Este libro ya fue devuelto.")

        # Marca el prestamo como devuelto.
        self.devuelto = True

        # Cambia el estado del libro a disponible.
        self.libro.definir_estado(2)
