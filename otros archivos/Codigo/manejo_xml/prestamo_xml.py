# Importacion de librerias necesarias.
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Importacion de las clases necesarias.
from clases.prestamo import Prestamo
from clases.usuario import Usuario
from clases.libro import Libro


# Definicion de la clase para administrar el XML de prestamos.
class PrestamoXML:

    # Define la ruta del archivo XML.
    ruta_archivo = Path("prestamos.xml")

    # Constructor de la clase.
    def __init__(self):

        # Comprueba si el archivo XML existe.
        if not self.ruta_archivo.exists():

            # Crea la estructura inicial del XML.
            raiz = ET.Element("Prestamos")

            # Genera el archivo XML.
            arbol = ET.ElementTree(raiz)
            arbol.write(self.ruta_archivo, encoding="utf-8", xml_declaration=True)

    # Lee el contenido del archivo XML.
    def _leer_raiz(self):

        # Obtiene el arbol XML.
        arbol = ET.parse(self.ruta_archivo)

        # Retorna el elemento principal.
        return arbol.getroot()

    # Agrega un prestamo al archivo XML.
    def agregar(self, prestamo):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Crea el elemento correspondiente al prestamo.
        elemento = ET.SubElement(raiz, "Prestamo")

        # Almacena la identificacion del usuario.
        ET.SubElement(elemento, "idpersona").text = prestamo.usuario.idpersona

        # Almacena el codigo del libro.
        ET.SubElement(elemento, "codigo_libro").text = str(prestamo.libro.codigo)

        # Almacena la fecha en que se realizo el prestamo.
        ET.SubElement(elemento, "fecha_prestamo").text = prestamo.fecha_prestamo.isoformat()

        # Almacena la fecha tentativa de devolucion.
        ET.SubElement(elemento, "fecha_tentativa_devolucion").text = prestamo.fecha_tentativa_devolucion.isoformat()

        # Almacena el estado de devolucion.
        ET.SubElement(elemento, "devuelto").text = str(prestamo.devuelto)

        # Guarda los cambios en el archivo XML.
        arbol = ET.ElementTree(raiz)
        arbol.write(self.ruta_archivo, encoding="utf-8", xml_declaration=True)

        # Confirma que el registro fue almacenado.
        return True

    # Busca un prestamo mediante el usuario y el libro.
    def buscar(self, idpersona, codigo_libro):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Recorre los prestamos registrados.
        for elemento in raiz.findall("Prestamo"):

            # Comprueba si coinciden la identificacion y el codigo.
            if (elemento.find("idpersona").text == str(idpersona)
                    and elemento.find("codigo_libro").text == str(codigo_libro)):

                # Retorna el prestamo encontrado.
                return elemento

        # Retorna None si no encuentra coincidencias.
        return None

    # Consulta todos los prestamos almacenados en el XML.
    def consultar_todos(self):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Retorna todos los elementos de prestamos.
        return raiz.findall("Prestamo")

    # Carga todos los prestamos almacenados en el XML.
    def cargar_todos(self):

        # Obtiene todos los prestamos del archivo XML.
        prestamos_xml = self.consultar_todos()

        # Inicializa la lista de prestamos recuperados.
        prestamos_cargados = []

        # Recorre los prestamos almacenados.
        for elemento in prestamos_xml:

            # Recupera la identificacion del usuario y el codigo del libro.
            idpersona = elemento.find("idpersona").text
            codigo_libro = int(elemento.find("codigo_libro").text)

            # Inicializa las referencias al usuario y al libro.
            usuario = None
            libro = None

            # Busca el usuario correspondiente.
            for persona in Usuario.usuarios:
                if persona.idpersona == idpersona:
                    usuario = persona
                    break

            # Busca el libro correspondiente.
            for ejemplar in Libro.libros:
                if ejemplar.codigo == codigo_libro:
                    libro = ejemplar
                    break

            # Comprueba que existan el usuario y el libro.
            if usuario is None or libro is None:
                continue

            # Recupera la fecha tentativa de devolucion.
            fecha_devolucion = datetime.strptime(
                elemento.find("fecha_tentativa_devolucion").text,
                "%Y-%m-%d"
            ).date()

            # Recupera la fecha original del prestamo.
            fecha_prestamo = datetime.strptime(
                elemento.find("fecha_prestamo").text,
                "%Y-%m-%d"
            ).date()

            # Comprueba si el prestamo ya existe en memoria.
            prestamo_existente = False

            for prestamo in Prestamo.registro_prestamos:
                if (prestamo.usuario == usuario
                        and prestamo.libro == libro
                        and prestamo.fecha_prestamo == fecha_prestamo):
                    prestamo_existente = True
                    break

            # Evita cargar prestamos duplicados.
            if prestamo_existente:
                continue

            # Crea el objeto prestamo.
            nuevo_prestamo = Prestamo(usuario, libro, fecha_devolucion)

            # Recupera la fecha original del prestamo.
            nuevo_prestamo.fecha_prestamo = datetime.strptime(
                elemento.find("fecha_prestamo").text,
                "%Y-%m-%d"
            ).date()

            # Recupera el estado de devolucion.
            nuevo_prestamo.devuelto = (
                elemento.find("devuelto").text == "True"
            )

            # Agrega el prestamo a la lista recuperada.
            prestamos_cargados.append(nuevo_prestamo)

        # Retorna los prestamos recuperados.
        return prestamos_cargados

    # Modifica un prestamo almacenado en el archivo XML.
    def modificar(self, prestamo):

        # Obtiene la raiz del archivo XML.
        raiz = self._leer_raiz()

        # Recorre los prestamos registrados.
        for elemento in raiz.findall("Prestamo"):

            # Comprueba que coincidan el usuario, el libro y la fecha del prestamo.
            if (elemento.find("idpersona").text == str(prestamo.usuario.idpersona)
                    and elemento.find("codigo_libro").text == str(prestamo.libro.codigo)
                    and elemento.find("fecha_prestamo").text == prestamo.fecha_prestamo.isoformat()):

                # Actualiza la fecha tentativa de devolucion.
                elemento.find("fecha_tentativa_devolucion").text = (
                    prestamo.fecha_tentativa_devolucion.isoformat()
                )

                # Actualiza el estado de devolucion.
                elemento.find("devuelto").text = str(prestamo.devuelto)

                # Guarda los cambios en el archivo XML.
                arbol = ET.ElementTree(raiz)
                arbol.write(
                    self.ruta_archivo,
                    encoding="utf-8",
                    xml_declaration=True
                )

                # Confirma que el prestamo fue actualizado.
                return True

        # Indica que no se encontro el prestamo.
        return False
