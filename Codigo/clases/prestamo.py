#Importacion de librerrias necesarias

from datetime import date

#Definicion de clase Prestamo con sus atributos y metodos
class Prestamo():

    #Varible que alojara todos los prestamos
    registro_prestamos = []
    
    def __init__(self, usuario, libro, fecha_tentativa_devolucion):

        self.usuario: Usuario = usuario
        self.libro: Libro = libro
        self.fecha_prestamo: date = date.today()
        self.fecha_tentativa_devolucion: date = fecha_tentativa_devolucion
        self.devuelto = False

        Prestamo.registro_prestamos.append(self) 

    def calcular_dias_retraso(self):
        
        dias_prestamo = date.today().toordinal() - self.fecha_prestamo.toordinal()
        
        if dias_prestamo > 15:
            return (dias_prestamo - 15)
        else:
            return 0

    def calculo_multa(self):

        return self.calcular_dias_retraso() * 525