# Importacion de librerias necesarias.
from datetime import date, datetime
from clases.prestamo import Prestamo
from clases.libro import Libro
from clases.usuario import Usuario
from clases.estudiante import Estudiante
from clases.docente import Docente
from manejo_xml.prestamo_xml import PrestamoXML
from manejo_xml.libro_xml import LibroXML

# Crea los objetos para administrar los archivos XML.
prestamo_xml = PrestamoXML()
libro_xml = LibroXML()

# Controla las opciones del administrador de prestamos.
def control_prestamos():

    while True:

        print("\n==============================================")
        print("           ADMINISTRAR PRESTAMOS")
        print("==============================================")
        print("1. Registrar prestamo")
        print("2. Registrar devolucion")
        print("3. Consultar prestamos pendientes")
        print("4. Regresar")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_prestamo()

        elif opcion == "2":
            registrar_devolucion()

        elif opcion == "3":
            consultar_prestamos_pendientes()

        elif opcion == "4":
            break

        else:
            print("Opcion no valida.")


# Registra un nuevo prestamo.
def registrar_prestamo():

    print("\n==============================================")
    print("               REGISTRAR PRESTAMO")
    print("==============================================")

    # Solicita la identificacion del usuario.
    identificacion = input("Ingrese la identificacion del usuario: ").strip()

    # Busca el usuario registrado.
    usuario = buscar_usuario(identificacion)

    # Comprueba si el usuario existe.
    if usuario is None:
        print("No se encontro un usuario con esa identificacion.")
        return

    # Comprueba si el usuario puede solicitar un prestamo.
    if not validar_usuario_prestamo(usuario):
        print("El usuario tiene prestamos pendientes.")
        return

    # Solicita el codigo del libro.
    codigo = input("Ingrese el codigo del libro: ").strip()

    # Comprueba que el codigo contenga solamente numeros.
    if not codigo.isdigit():
        print("El codigo debe contener solamente numeros.")
        return

    # Busca el libro registrado.
    libro = buscar_libro(int(codigo))

    # Comprueba si el libro existe.
    if libro is None:
        print("No se encontro un libro con ese codigo.")
        return

    # Comprueba si el libro esta disponible.
    if not validar_libro_prestamo(libro):
        print("El libro no se encuentra disponible.")
        return

    # Solicita la fecha tentativa de devolucion.
    fecha_devolucion = solicitar_fecha_devolucion()

    # Crea el nuevo prestamo.
    nuevo_prestamo = Prestamo(usuario, libro, fecha_devolucion)

    # Cambia el estado del libro a prestado.
    libro.definir_estado(1)

    # Guarda el prestamo en el archivo XML.
    prestamo_guardado = prestamo_xml.agregar(nuevo_prestamo)

    # Actualiza el estado del libro en el archivo XML.
    libro_actualizado = libro_xml.modificar(libro)

    # Comprueba si ambas operaciones fueron exitosas.
    if prestamo_guardado and libro_actualizado:

        # Confirma el registro del prestamo.
        print("\nPrestamo registrado correctamente.")
        print(f"Usuario: {usuario.nombre}")
        print(f"Libro: {libro.nombre_libro}")
        print(f"Codigo: {libro.codigo}")
        print(f"Fecha de prestamo: {nuevo_prestamo.fecha_prestamo}")
        print(f"Fecha de devolucion: {nuevo_prestamo.fecha_tentativa_devolucion}")

    else:
        print("\nNo fue posible completar el registro en los archivos XML.")


# Registra la devolucion de un libro.
def registrar_devolucion():

    print("\n==============================================")
    print("              REGISTRAR DEVOLUCION")
    print("==============================================")

    # Solicita la identificacion del usuario.
    identificacion = input("Ingrese la identificacion del usuario: ").strip()

    # Busca el usuario registrado.
    usuario = buscar_usuario(identificacion)

    # Comprueba si el usuario existe.
    if usuario is None:
        print("No se encontro un usuario con esa identificacion.")
        return

    # Busca el prestamo pendiente del usuario.
    prestamo = buscar_prestamo_usuario(usuario)

    # Comprueba si el usuario tiene un prestamo pendiente.
    if prestamo is None:
        print("El usuario no tiene prestamos pendientes.")
        return

    # Muestra la informacion del prestamo.
    mostrar_prestamo_pendiente(prestamo)

    # Solicita confirmacion de la devolucion.
    confirmacion = input("\n¿Desea registrar esta devolucion? (S/N): ").strip().lower()

    if confirmacion != "s":
        print("Operacion cancelada.")
        return

    # Calcula los dias de retraso y la multa.
    dias_retraso = prestamo.calcular_dias_retraso()
    multa = prestamo.calculo_multa()

    # Muestra la informacion de la multa.
    print(f"\nDias de retraso: {dias_retraso}")
    print(f"Multa correspondiente: ₡{multa}")

    # Muestra las condiciones disponibles.
    print("\nSeleccione la condicion fisica del libro:")
    print("1. Excelente")
    print("2. Dañado")
    print("3. Daños menores")

    while True:

        # Solicita la condicion del libro.
        condicion = input("Seleccione una opcion: ").strip()

        # Comprueba que la opcion sea valida.
        if condicion.isdigit() and int(condicion) in Libro.condiciones:
            break

        print("Opcion no valida. Intente nuevamente.")

    # Actualiza la condicion fisica del libro.
    prestamo.libro.definir_condicion(int(condicion))

    # Registra la devolucion del prestamo.
    prestamo.registrar_devolucion()

    # Actualiza el prestamo en el archivo XML.
    prestamo_actualizado = prestamo_xml.modificar(prestamo)

    # Actualiza el libro en el archivo XML.
    libro_actualizado = libro_xml.modificar(prestamo.libro)

    # Comprueba si ambas operaciones fueron exitosas.
    if prestamo_actualizado and libro_actualizado:

        print("\nDevolucion registrada correctamente.")
        print(f"Libro: {prestamo.libro.nombre_libro}")
        print(f"Condicion: {prestamo.libro.condicion.capitalize()}")
        print(f"Estado: {prestamo.libro.estado.capitalize()}")

    else:
        print("\nNo fue posible actualizar los archivos XML.")

# Busca un usuario mediante su identificacion.
def buscar_usuario(identificacion):

    # Recorre los usuarios registrados.
    for usuario in Usuario.usuarios:

        # Comprueba si la identificacion coincide.
        if usuario.idpersona == identificacion:
            return usuario

    # Indica que no se encontro el usuario.
    return None

# Comprueba si un usuario tiene multas pendientes.

# Busca un libro mediante su codigo.
def buscar_libro(codigo):

    # Recorre los libros registrados.
    for libro in Libro.libros:

        # Comprueba si el codigo coincide.
        if libro.codigo == codigo:
            return libro

    # Indica que no se encontro el libro.
    return None

# Valida si un usuario puede solicitar un prestamo.
def validar_usuario_prestamo(usuario):

    # Recorre los prestamos registrados.
    for prestamo in Prestamo.registro_prestamos:

        # Comprueba si el usuario tiene prestamos pendientes.
        if prestamo.usuario == usuario and not prestamo.devuelto:
            return False

    return True

def validar_libro_prestamo(libro):

    # Comprueba si el libro se encuentra disponible.
    if libro.estado == "disponible":
        return True

    return False

# Solicita y valida la fecha tentativa de devolucion.
def solicitar_fecha_devolucion():

    while True:

        # Solicita la fecha al usuario.
        fecha = input("Ingrese la fecha de devolucion (DD/MM/AAAA): ").strip()

        try:
            # Convierte el texto ingresado en una fecha.
            fecha_devolucion = datetime.strptime(fecha, "%d/%m/%Y").date()

            # Obtiene la fecha actual.
            fecha_actual = date.today()

            # Calcula la diferencia entre ambas fechas.
            dias_prestamo = (fecha_devolucion - fecha_actual).days

            # Comprueba que la fecha sea posterior a la actual.
            if dias_prestamo <= 0:
                print("La fecha debe ser posterior al dia de hoy.")
                continue

            # Comprueba que el prestamo no supere los 15 dias.
            if dias_prestamo > 15:
                print("La fecha de devolucion no puede superar los 15 dias.")
                continue

            return fecha_devolucion

        except ValueError:
            print("Formato de fecha incorrecto. Utilice DD/MM/AAAA.")

# Busca el prestamo pendiente de un usuario.
def buscar_prestamo_usuario(usuario):

    # Recorre los prestamos registrados.
    for prestamo in Prestamo.registro_prestamos:

        # Comprueba si el prestamo pertenece al usuario y no ha sido devuelto.
        if prestamo.usuario == usuario and not prestamo.devuelto:
            return prestamo

    # Indica que el usuario no tiene prestamos pendientes.
    return None

# Muestra el prestamo pendiente de un usuario.
def mostrar_prestamo_pendiente(prestamo):

    print(f"\nCodigo: {prestamo.libro.codigo}")
    print(f"Libro: {prestamo.libro.nombre_libro}")
    print(f"Fecha de prestamo: {prestamo.fecha_prestamo}")
    print(f"Fecha de devolucion: {prestamo.fecha_tentativa_devolucion}")
    print(f"Dias de retraso: {prestamo.calcular_dias_retraso()}")
    print(f"Multa: ₡{prestamo.calculo_multa()}")

# Consulta el prestamo pendiente de un usuario.
def consultar_prestamos_pendientes():

    print("\n==============================================")
    print("         CONSULTAR PRESTAMO PENDIENTE")
    print("==============================================")

    # Solicita la identificacion del usuario.
    identificacion = input("Ingrese la identificacion del usuario: ").strip()

    # Busca el usuario registrado.
    usuario = buscar_usuario(identificacion)

    # Comprueba si el usuario existe.
    if usuario is None:
        print("No se encontro un usuario con esa identificacion.")
        return

    # Busca el prestamo pendiente del usuario.
    prestamo = buscar_prestamo_usuario(usuario)

    # Comprueba si el usuario tiene un prestamo pendiente.
    if prestamo is None:
        print("El usuario no tiene prestamos pendientes.")
        return

    # Calcula los dias de retraso tomando como referencia la fecha actual.
    dias_retraso = (date.today() - prestamo.fecha_tentativa_devolucion).days

    # Evita mostrar dias negativos.
    if dias_retraso < 0:
        dias_retraso = 0

    # Identifica el tipo de usuario.
    if isinstance(usuario, Estudiante):
        tipo_usuario = "Estudiante"
    else:
        tipo_usuario = "Docente"

    # Muestra los datos del prestamo pendiente.
    print("\n==============================================")
    print("          DATOS DEL PRESTAMO")
    print("==============================================")
    print(f"Codigo del libro: {prestamo.libro.codigo}")
    print(f"ISBN: {prestamo.libro.isbn}")
    print(f"Titulo: {prestamo.libro.nombre_libro}")
    print(f"Identificacion: {usuario.idpersona}")
    print(f"Tipo de persona: {tipo_usuario}")
    print(f"Nombre: {usuario.nombre} {usuario.apellidos}")
    print(f"Fecha de devolucion: {prestamo.fecha_tentativa_devolucion.strftime('%d/%m/%Y')}")
    print(f"Dias de retraso: {dias_retraso}")

    # Consulta si desea modificar la fecha de devolucion.
    while True:
        opcion = input("\n¿Desea modificar la fecha de devolucion? (S/N): ").strip().upper()

        if opcion == "S":

            # Solicita la nueva fecha de devolucion.
            prestamo.fecha_tentativa_devolucion = solicitar_nueva_fecha_devolucion()

            # Actualiza el prestamo en el archivo XML.
            if prestamo_xml.modificar(prestamo):

                # Confirma la modificacion.
                print("\nFecha de devolucion actualizada correctamente.")
                print("Nueva fecha:", prestamo.fecha_tentativa_devolucion.strftime("%d/%m/%Y"))

                # Calcula nuevamente los dias de retraso.
                dias_retraso = prestamo.calcular_dias_retraso()

                print("Dias de retraso actualizados:", dias_retraso)

            else:
                print("\nNo fue posible actualizar la fecha en el XML.")
                print("Nueva fecha:", prestamo.fecha_tentativa_devolucion.strftime("%d/%m/%Y"))

            # Calcula nuevamente los dias de retraso.
            dias_retraso = prestamo.calcular_dias_retraso()

            print("Dias de retraso actualizados:", dias_retraso)
            break

        elif opcion == "N":
            print("\nNo se realizaron modificaciones.")
            break

        else:
            print("Opcion incorrecta. Ingrese S o N.")


# Solicita y valida una nueva fecha de devolucion.
def solicitar_nueva_fecha_devolucion():
    while True:
        # Solicita la nueva fecha.
        fecha = input("Ingrese la nueva fecha de devolucion (DD/MM/AAAA): ").strip()

        try:
            # Convierte el texto ingresado en una fecha.
            nueva_fecha = datetime.strptime(fecha, "%d/%m/%Y").date()

            # Comprueba que la fecha no sea anterior a la actual.
            if nueva_fecha < date.today():
                print("La fecha no puede ser anterior al dia de hoy.")
                continue

            return nueva_fecha

        except ValueError:
            print("Formato de fecha incorrecto. Utilice DD/MM/AAAA.")
