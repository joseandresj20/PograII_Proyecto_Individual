# Importacion de la clases
from menus.menu_principal import mostrar_menu_principal
from manejo_xml.usuario_xml import UsuarioXML
from manejo_xml.libro_xml import LibroXML
from manejo_xml.prestamo_xml import PrestamoXML

def main():
    # Crea el objeto para administrar el XML de usuarios.
    usuario_xml = UsuarioXML()

    # Carga los usuarios almacenados en el archivo XML.
    usuario_xml.cargar_todos()

    # Crea el objeto para administrar el XML de libros.
    libro_xml = LibroXML()

    # Carga los libros almacenados en el archivo XML.
    libro_xml.cargar_todos()

    # Crea el objeto para administrar el XML de prestamos.
    prestamo_xml = PrestamoXML()

    # Carga los prestamos almacenados en el archivo XML.
    prestamo_xml.cargar_todos()

    # Muestra el menu principal.
    mostrar_menu_principal()

if __name__ == "__main__":
    main()
