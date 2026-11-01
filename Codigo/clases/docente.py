#Importacion de la clase Usuario
from clases.usuario import Usuario


#Definicion de clase Docente que hereda de Usuario
class Docente(Usuario):

    #Constructor de la clase Docente
    def __init__(self, nombre, apellidos, idpersona, nacionalidad, carreras, estado_civil,
                 anio_ingreso, fecha_nacimiento, telefono, correo):

        #Llama al constructor de la clase padre Usuario
        super().__init__(nombre, apellidos, idpersona, nacionalidad, carreras, estado_civil,
                         anio_ingreso, fecha_nacimiento, telefono, correo)
