#Importacion de librerrias necesarias

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
        self.codigo: str = codigo
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
        
