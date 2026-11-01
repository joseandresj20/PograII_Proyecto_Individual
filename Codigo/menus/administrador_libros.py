# Importacion de la clase Libro
from clases.libro import Libro
from utilidades.validaciones import (
    validar_texto,
    validar_nombre,
    validar_isbn,
    validar_anio_publicacion
)


# Controla las opciones del menu de administracion de libros
def control_libros():

    while True:

        mostrar_menu_libros()

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_libro()

        elif opcion == "2":
            modificar_libro()

        elif opcion == "3":
            eliminar_libro()

        elif opcion == "4":
            consultar_libros()

        elif opcion == "5":
            break

        else:
            print("\nOpcion no valida. Intente nuevamente.")


# Muestra las opciones del menu de administracion de libros
def mostrar_menu_libros():

    print("\n--- ADMINISTRACION DE LIBROS ---")
    print("1. Registrar libro")
    print("2. Modificar libro")
    print("3. Eliminar libro")
    print("4. Consultar libros")
    print("5. Regresar")

# Gestiona el registro de nuevos libros en el sistema.
def registrar_libro():

    print("\n==============================================")
    print("               REGISTRAR LIBRO")
    print("==============================================")

    # Solicita los datos del libro mediante las funciones auxiliares.
    nombre_libro = solicitar_nombre_libro()
    isbn = solicitar_isbn()
    autor = solicitar_autor()
    edicion = solicitar_edicion()
    anio_publicacion = solicitar_anio_publicacion()
    condicion = solicitar_condicion()

    # Genera automaticamente el codigo del libro.
    codigo = generar_codigo_libro()

    # Crea una instancia de la clase Libro.
    nuevo_libro = Libro(
        nombre_libro,
        codigo,
        isbn,
        autor,
        edicion,
        anio_publicacion,
        condicion
    )

    # Muestra la confirmacion del registro.
    print("\nLibro registrado correctamente.")
    print(f"Codigo asignado: {nuevo_libro.codigo}")

# Genera automaticamente el siguiente codigo disponible.
def generar_codigo_libro():

    # Comprueba si existen libros registrados.
    if not Libro.libros:
        return 1

    # Obtiene el codigo mayor entre los libros registrados.
    codigo_mayor = max(libro.codigo for libro in Libro.libros)

    # Genera el siguiente codigo consecutivo.
    return codigo_mayor + 1

    return True

# Solicita el nombre del libro.
def solicitar_nombre_libro():

    while True:
        nombre_libro = input("Ingrese el nombre del libro: ").strip()

        # Comprueba que el nombre no este vacio.
        if validar_texto(nombre_libro):
            return nombre_libro

        print("El nombre del libro no puede estar vacio.")

# Solicita un ISBN con formato valido.
def solicitar_isbn():

    while True:
        isbn = input("Ingrese el ISBN: ").strip()

        # Comprueba que el ISBN tenga un formato valido.
        if validar_isbn(isbn):
            return isbn

        print("El ISBN debe contener 13 digitos numericos. Puede poseer guiones intermedios.")

# Solicita el nombre del autor.
def solicitar_autor():

    while True:
        autor = input("Ingrese el autor del libro: ").strip()

        # Comprueba que el nombre del autor tenga un formato valido.
        if validar_nombre(autor):
            return autor

        print("El nombre del autor contiene caracteres no validos.")

# Solicita la edicion del libro.
def solicitar_edicion():

    while True:
        edicion = input("Ingrese la edicion del libro: ").strip()

        # Comprueba que la edicion no este vacia.
        if validar_texto(edicion):
            return edicion

        print("La edicion no puede estar vacia.")

# Solicita el anio de publicacion del libro.
def solicitar_anio_publicacion():

    while True:
        anio = input("Ingrese el anio de publicacion: ").strip()

        # Comprueba que el anio tenga un formato valido.
        if validar_anio_publicacion(anio):
            return int(anio)

        print("El anio de publicacion no es valido.")

# Solicita la condicion fisica del libro.
def solicitar_condicion():

    while True:

        # Muestra las condiciones disponibles.
        print("\nCondiciones del libro:")
        for clave, valor in Libro.condiciones.items():
            print(f"{clave}. {valor.capitalize()}")

        condicion = input("Seleccione la condicion: ").strip()

        # Comprueba que la opcion seleccionada sea valida.
        if condicion.isdigit() and int(condicion) in Libro.condiciones:
            return int(condicion)

        print("La condicion seleccionada no es valida.")

# Permite consultar todos los libros registrados.
def consultar_libros():

    print("\n==============================================")
    print("               CONSULTAR LIBROS")
    print("==============================================")

    # Comprueba si existen libros registrados.
    if not Libro.libros:
        print("No hay libros registrados en el sistema.")
        return

    # Recorre la lista de libros registrados.
    for libro in Libro.libros:

        print("\n----------------------------------------------")
        print(f"Codigo: {libro.codigo}")
        print(f"Nombre: {libro.nombre_libro}")
        print(f"ISBN: {libro.isbn}")
        print(f"Autor: {libro.autor}")
        print(f"Edicion: {libro.edicion}")
        print(f"Año de publicacion: {libro.anio_publicacion}")
        print(f"Estado: {libro.estado.capitalize()}")
        print(f"Condicion: {libro.condicion.capitalize()}")
        print("----------------------------------------------")

# Busca libros utilizando diferentes criterios.
def buscar_libros(criterio, valor):

    # Almacena los libros que coincidan con la busqueda.
    libros_encontrados = []

    # Recorre los libros registrados.
    for libro in Libro.libros:

        # Comprueba si el criterio corresponde al nombre.
        if criterio == "1" and valor.lower() in libro.nombre_libro.lower():
            libros_encontrados.append(libro)

        # Comprueba si el criterio corresponde al codigo.
        elif criterio == "2" and valor == str(libro.codigo):
            libros_encontrados.append(libro)

        # Comprueba si el criterio corresponde al ISBN.
        elif criterio == "3" and valor == libro.isbn:
            libros_encontrados.append(libro)

        # Comprueba si el criterio corresponde al autor.
        elif criterio == "4" and valor.lower() in libro.autor.lower():
            libros_encontrados.append(libro)

    return libros_encontrados

# Permite modificar los datos de un libro registrado.

# Permite modificar los datos de un libro registrado.
def modificar_libro():

    print("\n==============================================")
    print("               MODIFICAR LIBRO")
    print("==============================================")

    # Muestra los criterios de busqueda disponibles.
    print("\nSeleccione un criterio de busqueda:")
    print("1. Nombre")
    print("2. Codigo")
    print("3. ISBN")
    print("4. Autor")

    criterio = input("\nSeleccione una opcion: ").strip()

    # Comprueba que el criterio sea valido.
    if criterio not in ("1", "2", "3", "4"):
        print("La opcion seleccionada no es valida.")
        return

    # Solicita el valor que se utilizara para buscar.
    valor = input("Ingrese el valor de busqueda: ").strip()

    # Comprueba que se haya ingresado un valor.
    if not valor:
        print("Debe ingresar un valor para realizar la busqueda.")
        return

    # Busca los libros que coincidan con el criterio.
    libros_encontrados = buscar_libros(criterio, valor)

    # Permite seleccionar el libro que se desea modificar.
    libro = seleccionar_libro(libros_encontrados)

    # Comprueba si se selecciono un libro.
    if libro is None:
        return

    # Muestra las opciones de modificacion.
    while True:

        print("\n¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. ISBN")
        print("3. Autor")
        print("4. Edicion")
        print("5. Año de publicacion")
        print("6. Condicion")
        print("7. Estado")
        print("8. Regresar")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            libro.nombre_libro = solicitar_nombre_libro()
            print("Nombre actualizado correctamente.")

        elif opcion == "2":
            libro.isbn = solicitar_isbn()
            print("ISBN actualizado correctamente.")

        elif opcion == "3":
            libro.autor = solicitar_autor()
            print("Autor actualizado correctamente.")

        elif opcion == "4":
            libro.edicion = solicitar_edicion()
            print("Edicion actualizada correctamente.")

        elif opcion == "5":
            libro.anio_publicacion = solicitar_anio_publicacion()
            print("Año de publicacion actualizado correctamente.")

        elif opcion == "6":
            condicion = solicitar_condicion()
            libro.definir_condicion(condicion)
            print("Condicion actualizada correctamente.")

        elif opcion == "7":

            # Muestra los estados disponibles.
            for clave, valor in Libro.estados.items():
                print(f"{clave}. {valor.capitalize()}")

            estado = input("Seleccione el nuevo estado: ").strip()

            # Comprueba que el estado seleccionado sea valido.
            if estado.isdigit() and int(estado) in Libro.estados:
                libro.definir_estado(int(estado))
                print("Estado actualizado correctamente.")
            else:
                print("La opcion seleccionada no es valida.")

        elif opcion == "8":
            break

        else:
            print("La opcion seleccionada no es valida.")

# Permite seleccionar un libro de los resultados de busqueda.
def seleccionar_libro(libros_encontrados):

    # Comprueba si existen coincidencias.
    if not libros_encontrados:
        print("No se encontraron libros con el criterio indicado.")
        return None

    # Muestra los libros encontrados.
    print("\nLibros encontrados:")

    for indice, libro in enumerate(libros_encontrados, start=1):
        print(f"\n{indice}. {libro.nombre_libro}")
        print(f"   Codigo: {libro.codigo}")
        print(f"   ISBN: {libro.isbn}")
        print(f"   Autor: {libro.autor}")
        print(f"   Estado: {libro.estado}")

    # Solicita seleccionar un libro.
    while True:
        seleccion = input("\nSeleccione el libro (0 para cancelar): ").strip()

        # Comprueba que la seleccion sea numerica.
        if seleccion.isdigit():

            seleccion = int(seleccion)

            # Permite cancelar la seleccion.
            if seleccion == 0:
                return None

            # Comprueba que la seleccion exista.
            if 1 <= seleccion <= len(libros_encontrados):
                return libros_encontrados[seleccion - 1]

        print("La seleccion no es valida.")

