# Importacion de librerias necesarias.
import xml.etree.ElementTree as ET
from pathlib import Path

# Importacion de la clase Libro.
from clases.libro import Libro

# Definicion de la clase LibroXML.
class LibroXML:

    # Ruta del archivo XML de libros.
    ruta_archivo = Path("libros.xml")

    # Constructor de la clase.
    def __init__(self):

        # Comprueba si el archivo XML existe.
        if not LibroXML.ruta_archivo.is_file():

            # Crea el elemento raiz del XML.
            raiz = ET.Element("Libros")

            # Crea el arbol XML.
            arbol = ET.ElementTree(raiz)

            # Guarda el archivo XML.
            arbol.write(LibroXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

    # Lee el archivo XML y obtiene su elemento raiz.
    def _leer_raiz(self):
        # Carga el archivo XML.
        arbol = ET.parse(LibroXML.ruta_archivo)

        # Obtiene el elemento raiz.
        raiz = arbol.getroot()

        return raiz

    # Busca un libro mediante su codigo.
    def buscar(self, codigo):
        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Recorre los libros registrados.
        for libro in raiz.findall("Libro"):

            # Compara el codigo del libro.
            if int(libro.find("codigo").text) == codigo:
                return libro

        return None

    # Obtiene el siguiente codigo disponible.
    def obtener_codigo_siguiente(self):
        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Inicializa el codigo mayor.
        codigo_mayor = 0

        # Recorre los libros registrados.
        for libro in raiz.findall("Libro"):

            # Obtiene el codigo del libro.
            codigo = int(libro.find("codigo").text)

            # Comprueba si es el codigo mayor.
            if codigo > codigo_mayor:
                codigo_mayor = codigo

        # Retorna el siguiente codigo.
        return codigo_mayor + 1

    # Agrega un libro al archivo XML.
    def agregar(self, libro):

        # Comprueba si el libro ya existe.
        if self.buscar(libro.codigo) is not None:
            return False

        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Crea el elemento del libro.
        elemento_libro = ET.SubElement(raiz, "Libro")

        # Agrega los datos del libro.
        ET.SubElement(elemento_libro, "nombre_libro").text = libro.nombre_libro
        ET.SubElement(elemento_libro, "codigo").text = str(libro.codigo)
        ET.SubElement(elemento_libro, "isbn").text = libro.isbn
        ET.SubElement(elemento_libro, "autor").text = libro.autor
        ET.SubElement(elemento_libro, "edicion").text = libro.edicion
        ET.SubElement(elemento_libro, "anio_publicacion").text = str(libro.anio_publicacion)
        ET.SubElement(elemento_libro, "estado").text = str(libro.estado)
        ET.SubElement(elemento_libro, "condicion").text = str(libro.condicion)

        # Guarda los cambios en el archivo XML.
        arbol = ET.ElementTree(raiz)
        arbol.write(LibroXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

        return True

    # Modifica los datos de un libro en el archivo XML.
    def modificar(self, libro):

        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Busca el libro mediante su codigo.
        elemento_libro = None

        # Recorre los libros registrados.
        for elemento in raiz.findall("Libro"):
            if int(elemento.find("codigo").text) == libro.codigo:
                elemento_libro = elemento
                break

        # Comprueba si el libro existe.
        if elemento_libro is None:
            return False

        # Actualiza los datos del libro.
        elemento_libro.find("nombre_libro").text = libro.nombre_libro
        elemento_libro.find("isbn").text = libro.isbn
        elemento_libro.find("autor").text = libro.autor
        elemento_libro.find("edicion").text = libro.edicion
        elemento_libro.find("anio_publicacion").text = str(libro.anio_publicacion)
        elemento_libro.find("estado").text = str(libro.estado)
        elemento_libro.find("condicion").text = str(libro.condicion)

        # Guarda los cambios en el archivo XML.
        arbol = ET.ElementTree(raiz)
        arbol.write(LibroXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

        return True

    # Elimina un libro del archivo XML.
    def eliminar(self, codigo):

        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Busca el libro mediante su codigo.
        for libro in raiz.findall("Libro"):

            # Comprueba si el codigo coincide.
            if int(libro.find("codigo").text) == codigo:

                # Elimina el libro de la raiz.
                raiz.remove(libro)

                # Guarda los cambios en el archivo XML.
                arbol = ET.ElementTree(raiz)
                arbol.write(LibroXML.ruta_archivo, encoding="utf-8", xml_declaration=True)

                return True

        return False

    # Consulta todos los libros registrados en el XML.
    def consultar_todos(self):

        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Obtiene todos los elementos Libro.
        libros = raiz.findall("Libro")

        # Retorna la lista de libros encontrados.
        return libros

        # Carga todos los libros almacenados en el XML.
    def cargar_todos(self):

        # Obtiene la raiz del XML.
        raiz = self._leer_raiz()

        # Inicializa la lista de libros recuperados.
        libros_cargados = []

        # Recorre los libros registrados en el XML.
        for elemento in raiz.findall("Libro"):

            # Obtiene el codigo del libro.
            codigo = int(elemento.find("codigo").text)

            # Comprueba si el libro ya existe en memoria.
            libro_existente = False

            for libro in Libro.libros:
                if libro.codigo == codigo:
                    libro_existente = True
                    break

            # Evita cargar libros duplicados.
            if libro_existente:
                continue

            # Obtiene la condicion almacenada en el XML.
            condicion_xml = elemento.find("condicion").text

            # Busca el numero correspondiente a la condicion.
            for numero, condicion in Libro.condiciones.items():
                if condicion == condicion_xml:
                    condicion = numero
                    break

            # Crea el objeto Libro con los datos recuperados.
            nuevo_libro = Libro(
                elemento.find("nombre_libro").text,
                codigo,
                elemento.find("isbn").text,
                elemento.find("autor").text,
                elemento.find("edicion").text,
                int(elemento.find("anio_publicacion").text),
                condicion
            )

            # Recupera el estado almacenado en el XML.
            nuevo_libro.estado = elemento.find("estado").text

            # Agrega el libro a la lista de recuperados.
            libros_cargados.append(nuevo_libro)

        # Retorna los libros recuperados.
        return libros_cargados
