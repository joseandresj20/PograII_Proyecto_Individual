# Importacion de librerias necesarias.
import xml.etree.ElementTree as ET
from pathlib import Path
from clases.estudiante import Estudiante
from clases.docente import Docente
from clases.usuario import Usuario
from datetime import datetime

# Definicion de la clase UsuarioXML.
class UsuarioXML:

    # Ruta del archivo XML de usuarios.
    ruta_archivo = Path("usuarios.xml")
    
        # Constructor de la clase.
    def __init__(self):

        # Comprueba si el archivo XML existe.
        if not UsuarioXML.ruta_archivo.is_file():

            # Crea el elemento raiz del XML.
            raiz = ET.Element("Usuarios")

            # Crea el arbol XML.
            arbol = ET.ElementTree(raiz)

            # Guarda el archivo XML.
            arbol.write(UsuarioXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

    # Lee el archivo XML y obtiene su elemento raiz.
    def _leer_raiz(self):

        # Carga el archivo XML.
        arbol = ET.parse(UsuarioXML.ruta_archivo)

        # Obtiene el elemento raiz.
        raiz = arbol.getroot()

        return raiz

    # Busca un usuario mediante su identificacion.
    def buscar(self, identificacion):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Recorre los usuarios registrados.
        for usuario in raiz.findall("Usuario"):

            # Comprueba si la identificacion coincide.
            if usuario.find("idpersona").text == identificacion:
                return usuario

        # Indica que no se encontro el usuario.
        return None

    # Consulta todos los usuarios registrados en el XML.
    def consultar_todos(self):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Obtiene todos los usuarios registrados.
        usuarios = raiz.findall("Usuario")

        return usuarios
    
    # Agrega un usuario al archivo XML.
    def agregar(self, usuario):

        # Comprueba si el usuario ya existe.
        if self.buscar(usuario.idpersona) is not None:
            return False

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Crea el elemento Usuario.
        elemento_usuario = ET.SubElement(raiz, "Usuario")

        # Determina el tipo de usuario.
        if isinstance(usuario, Estudiante):
            tipo = "Estudiante"
        elif isinstance(usuario, Docente):
            tipo = "Docente"
        else:
            return False

        # Guarda el tipo de usuario.
        ET.SubElement(elemento_usuario, "tipo_usuario").text = tipo

        # Guarda los atributos del usuario.
        ET.SubElement(elemento_usuario, "nombre").text = usuario.nombre
        ET.SubElement(elemento_usuario, "apellidos").text = usuario.apellidos
        ET.SubElement(elemento_usuario, "idpersona").text = usuario.idpersona
        ET.SubElement(elemento_usuario, "nacionalidad").text = usuario.nacionalidad

        # Crea el elemento para almacenar las carreras.
        elemento_carreras = ET.SubElement(elemento_usuario, "carreras")

        # Guarda cada carrera del usuario.
        for carrera in usuario.carreras:
            ET.SubElement(elemento_carreras, "carrera").text = carrera

        # Guarda los atributos restantes.
        ET.SubElement(elemento_usuario, "estado_civil").text = usuario.estado_civil
        ET.SubElement(elemento_usuario, "anio_ingreso").text = str(usuario.anio_ingreso)
        ET.SubElement(elemento_usuario, "fecha_nacimiento").text = usuario.fecha_nacimiento.strftime("%Y-%m-%d")
        ET.SubElement(elemento_usuario, "telefono").text = usuario.telefono
        ET.SubElement(elemento_usuario, "correo").text = usuario.correo

        # Crea el arbol XML.
        arbol = ET.ElementTree(raiz)

        # Guarda los cambios en el archivo XML.
        arbol.write(UsuarioXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

        return True
    
    # Modifica los datos de un usuario existente en el XML.
    def modificar(self, usuario):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Busca el usuario mediante su identificacion.
        elemento_usuario = None

        # Recorre los usuarios registrados.
        for elemento in raiz.findall("Usuario"):

            # Comprueba si la identificacion coincide.
            if elemento.find("idpersona").text == usuario.idpersona:
                elemento_usuario = elemento
                break

        # Comprueba si el usuario existe.
        if elemento_usuario is None:
            return False

        # Determina el tipo de usuario.
        if isinstance(usuario, Estudiante):
            tipo = "Estudiante"
        elif isinstance(usuario, Docente):
            tipo = "Docente"
        else:
            return False

        # Actualiza el tipo de usuario.
        elemento_usuario.find("tipo_usuario").text = tipo

        # Actualiza los atributos del usuario.
        elemento_usuario.find("nombre").text = usuario.nombre
        elemento_usuario.find("apellidos").text = usuario.apellidos
        elemento_usuario.find("nacionalidad").text = usuario.nacionalidad
        elemento_usuario.find("estado_civil").text = usuario.estado_civil
        elemento_usuario.find("anio_ingreso").text = str(usuario.anio_ingreso)
        elemento_usuario.find("fecha_nacimiento").text = usuario.fecha_nacimiento.strftime("%Y-%m-%d")
        elemento_usuario.find("telefono").text = usuario.telefono
        elemento_usuario.find("correo").text = usuario.correo

        # Actualiza la lista de carreras.
        elemento_carreras = elemento_usuario.find("carreras")

        # Elimina las carreras anteriores.
        elemento_carreras.clear()

        # Agrega las carreras actualizadas.
        for carrera in usuario.carreras:
            ET.SubElement(elemento_carreras, "carrera").text = carrera

        # Crea el arbol XML.
        arbol = ET.ElementTree(raiz)

        # Guarda los cambios en el archivo XML.
        arbol.write(UsuarioXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

        return True

    # Elimina un usuario del archivo XML mediante su identificacion.
    def eliminar(self, identificacion):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Busca el usuario que se desea eliminar.
        elemento_usuario = None

        # Recorre los usuarios registrados.
        for elemento in raiz.findall("Usuario"):

            # Comprueba si la identificacion coincide.
            if elemento.find("idpersona").text == identificacion:
                elemento_usuario = elemento
                break

        # Comprueba si el usuario existe.
        if elemento_usuario is None:
            return False

        # Elimina el usuario de la raiz.
        raiz.remove(elemento_usuario)

        # Crea el arbol XML.
        arbol = ET.ElementTree(raiz)

        # Guarda los cambios en el archivo XML.
        arbol.write(UsuarioXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

        return True

 # Carga los usuarios almacenados en el archivo XML.
    def cargar_todos(self):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Lista para almacenar los usuarios recuperados.
        usuarios = []

        # Recorre los usuarios registrados en el XML.
        for elemento in raiz.findall("Usuario"):

            # Obtiene la identificacion del usuario.
            identificacion = elemento.find("idpersona").text

            # Comprueba si el usuario ya existe en memoria.
            usuario_existente = False

            # Recorre los usuarios almacenados en memoria.
            for usuario in Usuario.usuarios:

                # Comprueba si la identificacion coincide.
                if usuario.idpersona == identificacion:
                    usuario_existente = True
                    break

            # Evita cargar usuarios duplicados.
            if usuario_existente:
                continue

            # Obtiene el tipo de usuario.
            tipo = elemento.find("tipo_usuario").text

            # Obtiene las carreras del usuario.
            carreras = []

            # Recorre las carreras almacenadas.
            for carrera in elemento.find("carreras").findall("carrera"):
                carreras.append(carrera.text)

            # Convierte el año de ingreso a entero.
            anio_ingreso = int(elemento.find("anio_ingreso").text)

            # Convierte la fecha de nacimiento a date.
            fecha_nacimiento = datetime.strptime(
                elemento.find("fecha_nacimiento").text, "%Y-%m-%d"
            ).date()

            # Obtiene los datos restantes.
            nombre = elemento.find("nombre").text
            apellidos = elemento.find("apellidos").text
            nacionalidad = elemento.find("nacionalidad").text
            estado_civil = elemento.find("estado_civil").text
            telefono = elemento.find("telefono").text
            correo = elemento.find("correo").text

            # Crea el objeto correspondiente.
            if tipo == "Estudiante":
                usuario = Estudiante(
                    nombre, apellidos, identificacion, nacionalidad,
                    carreras, estado_civil, anio_ingreso,
                    fecha_nacimiento, telefono, correo
                )

            elif tipo == "Docente":
                usuario = Docente(
                    nombre, apellidos, identificacion, nacionalidad,
                    carreras, estado_civil, anio_ingreso,
                    fecha_nacimiento, telefono, correo
                )

            else:
                continue

            # Agrega el usuario a la lista de recuperados.
            usuarios.append(usuario)

        return usuarios
