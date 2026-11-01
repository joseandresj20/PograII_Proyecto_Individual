#Importacion de la clase Usuario
from clases.usuario import Usuario


#Definicion de clase Estudiante que hereda de Usuario
class Estudiante(Usuario):

    #Constructor de la clase Estudiante
    def __init__(self, nombre, apellidos, idpersona, nacionalidad, carreras,
                 estado_civil, anio_ingreso, fecha_nacimiento, telefono, correo):

        #Llama al constructor de la clase padre Usuario
        super().__init__(nombre, apellidos, idpersona, nacionalidad, carreras,
                         estado_civil, anio_ingreso, fecha_nacimiento, telefono, correo)
