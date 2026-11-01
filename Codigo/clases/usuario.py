# Importación de librerías necesarias.
from datetime import date

#Definicion de clase Usuario con sus atributos y metodos
class Usuario():

    #Varible que alojara todos los usuarios
    usuarios = []

    #Constructor de la clase Usario
    def __init__(self, nombre, apellidos, idpersona, nacionalidad, carreras, estado_civil,
                 anio_ingreso, fecha_nacimiento, telefono, correo):

        #Atributos
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.idpersona: str = idpersona
        self.nacionalidad: str = nacionalidad
        self.carreras: list[str] = carreras
        self.estado_civil: str = estado_civil
        self.anio_ingreso: int = anio_ingreso
        self.fecha_nacimiento: date = fecha_nacimiento
        self.telefono: str = telefono
        self.correo: str = correo

        #Guarda la instancia creada en la variable de clase llamada usarios
        Usuario.usuarios.append(self)

