
# Importación de librerías necesarias
from datetime import datetime
from utilidades.validaciones import (
    validar_texto,
    validar_nombre,
    validar_formato_identificacion,
    validar_anio_ingreso,
    validar_fecha_nacimiento,
    validar_telefono,
    validar_correo
)
from clases.usuario import Usuario
from clases.estudiante import Estudiante
from clases.docente import Docente


# Controla el funcionamiento del menú de administración de usuarios.
# Mantiene el menú activo hasta que el usuario seleccione regresar.
def control_usuarios():

    # Ciclo que permite mostrar nuevamente el menú después de cada operación.
    while True:

        # Muestra las opciones disponibles para administrar usuarios.
        mostrar_menu_usuarios()

        # Captura la opción seleccionada y elimina espacios innecesarios.
        opcion = input("Favor ingresar la opción deseada: ").strip()

        # Evalúa la opción seleccionada y ejecuta la función correspondiente.
        if opcion == "1":

            registrar_usuario()

        elif opcion == "2":

            modificar_usuario()

        elif opcion == "3":

            eliminar_usuario()

        elif opcion == "4":

            consultar_usuario()

        # Finaliza el ciclo y regresa al menú principal.
        elif opcion == "5":

            print("\nRegresando al menú principal...")
            break

        # Informa cuando se introduce una opción que no está contemplada.
        else:

            print("\nLa opción indicada es inválida. Inténtelo nuevamente.")


# Muestra las opciones disponibles en el módulo de administración de usuarios.
def mostrar_menu_usuarios():

    print("\n==============================================")
    print("       ADMINISTRACIÓN DE USUARIOS")
    print("==============================================")

    print("1. Registrar usuario.")
    print("2. Modificar usuario.")
    print("3. Eliminar usuario.")
    print("4. Consultar usuarios.")
    print("5. Regresar al menú principal.")

    print("==============================================")


# Gestiona el registro de nuevos usuarios en el sistema, ya sean estudiantes o profesores.
# Su implementación permitirá capturar los datos y crear objetos Usuario.
def registrar_usuario():

    #Solicita el tipo de usuario que desea registrar
    while True:
        print("\n--- Tipo de usuario ---")
        print("1. Estudiante")
        print("2. Docente")

        tipo_usuario = input("Seleccione una opcion: ").strip()
        
        #Valida que solo sean las opciones 1 o 2
        if tipo_usuario == "1" or tipo_usuario == "2":
            break
        else:
            print("Opcion incorrecta. Intente nuevamente.")

    #Solicita los datos personales del usuario
    nombre = solicitar_nombre("Ingrese el nombre del usuario: ")
    apellidos = solicitar_nombre("Ingrese los apellidos: ")
    idpersona = solicitar_identificacion()
    nacionalidad = solicitar_nacionalidad()
    carreras = solicitar_carreras()
    estado_civil = solicitar_estado_civil()
    anio_ingreso = solicitar_anio_ingreso()
    fecha_nacimiento = solicitar_fecha_nacimiento()
    telefono = solicitar_telefono()
    correo = solicitar_correo()

    #Crea una instancia segun el tipo de usuario seleccionado
    if tipo_usuario == "1":
        nuevo_usuario = Estudiante(
            nombre, apellidos, idpersona, nacionalidad, carreras,
            estado_civil, anio_ingreso, fecha_nacimiento, telefono, correo
        )
    else:
        nuevo_usuario = Docente(
            nombre, apellidos, idpersona, nacionalidad, carreras,
            estado_civil, anio_ingreso, fecha_nacimiento, telefono, correo
        )

    #Muestra un mensaje de confirmacion
    print("\nUsuario registrado correctamente.")


# Gestiona la modificación de la información de un usuario existente.
def modificar_usuario():

    # Solicita la identificacion del usuario que desea modificar.
    idpersona = solicitar_identificacion_existente()

    # Busca el usuario en la lista de usuarios registrados.
    usuario = buscar_usuario(idpersona)

    # Comprueba si el usuario existe.
    if usuario is None:
        print("\nNo se encontro un usuario con esa identificacion.")
        return

    # Mantiene activo el menu hasta seleccionar regresar.
    while True:

        # Muestra las opciones disponibles para modificar.
        mostrar_menu_modificacion()

        # Solicita la opcion que desea modificar.
        opcion = input("Seleccione el dato que desea modificar: ").strip()

        # Modifica el nombre.
        if opcion == "1":
            usuario.nombre = solicitar_nombre("Ingrese el nuevo nombre: ")

        # Modifica los apellidos.
        elif opcion == "2":
            usuario.apellidos = solicitar_nombre("Ingrese los nuevos apellidos: ")

        # Modifica la nacionalidad.
        elif opcion == "3":
            usuario.nacionalidad = solicitar_nacionalidad()

        # Modifica las carreras.
        elif opcion == "4":
            usuario.carreras = solicitar_carreras()

        # Modifica el estado civil.
        elif opcion == "5":
            usuario.estado_civil = solicitar_estado_civil()

        # Modifica el año de ingreso.
        elif opcion == "6":
            usuario.anio_ingreso = solicitar_anio_ingreso()

        # Modifica la fecha de nacimiento.
        elif opcion == "7":
            usuario.fecha_nacimiento = solicitar_fecha_nacimiento()

        # Modifica el telefono.
        elif opcion == "8":
            usuario.telefono = solicitar_telefono()

        # Modifica el correo electronico.
        elif opcion == "9":
            usuario.correo = solicitar_correo()

        # Regresa al menu de administracion de usuarios.
        elif opcion == "10":
            break

        # Informa cuando se selecciona una opcion incorrecta.
        else:
            print("\nLa opcion seleccionada no es valida.")
            continue

        # Confirma que la modificacion se realizo correctamente.
        print("\nLa informacion del usuario fue actualizada correctamente.")


# Gestiona la eliminación de un usuario registrado en el sistema.
def eliminar_usuario():

    # Comprueba que existan usuarios registrados.
    if not Usuario.usuarios:
        print("\nNo hay usuarios registrados.")
        return

    # Solicita una identificacion con formato valido.
    idpersona = solicitar_identificacion_existente()

    # Busca el usuario en la lista de usuarios registrados.
    usuario = buscar_usuario(idpersona)

    # Comprueba que el usuario exista.
    if usuario is None:
        print("\nNo se encontro ningun usuario con esa identificacion.")
        return

    # Solicita confirmacion antes de eliminar el usuario.
    confirmacion = input(
        f"\n¿Desea eliminar a {usuario.nombre} {usuario.apellidos}? (S/N): "
    ).strip().upper()

    # Comprueba la respuesta del usuario.
    if confirmacion == "S":

        # Elimina el usuario de la lista de usuarios registrados.
        Usuario.usuarios.remove(usuario)

        print("\nEl usuario fue eliminado correctamente.")

    elif confirmacion == "N":
        print("\nOperacion cancelada.")

    else:
        print("\nOpcion no valida. No se elimino el usuario.")


# Permite consultar la información de los usuarios registrados.
def consultar_usuario():

    # Comprueba si existen usuarios registrados.
    if not Usuario.usuarios:
        print("\nNo hay usuarios registrados en el sistema.")
        return

    # Muestra el encabezado de la consulta.
    print("\n==============================================")
    print("             USUARIOS REGISTRADOS")
    print("==============================================")

    # Recorre la lista de usuarios registrados.
    for usuario in Usuario.usuarios:

        # Identifica el tipo de usuario.
        if isinstance(usuario, Estudiante):
            tipo_usuario = "Estudiante"
        elif isinstance(usuario, Docente):
            tipo_usuario = "Docente"

        # Muestra la información del usuario.
        print("\n----------------------------------------------")
        print(f"Tipo de usuario: {tipo_usuario}")
        print(f"Nombre: {usuario.nombre}")
        print(f"Apellidos: {usuario.apellidos}")
        print(f"Identificación: {usuario.idpersona}")
        print(f"Nacionalidad: {usuario.nacionalidad}")
        print(f"Carreras: {', '.join(usuario.carreras)}")
        print(f"Estado civil: {usuario.estado_civil}")
        print(f"Año de ingreso: {usuario.anio_ingreso}")
        print(f"Fecha de nacimiento: {usuario.fecha_nacimiento}")
        print(f"Teléfono: {usuario.telefono}")
        print(f"Correo: {usuario.correo}")

    print("\n==============================================")


# Solicita información mediante consola y devuelve el valor ingresado.
# Recibe como parámetro el texto que describe el dato solicitado.
def insertar_datos(valor_escrito):

    entrada = input(f"Favor digite {valor_escrito}")

    # Devuelve el dato capturado para utilizarlo en otras funciones.


#Solicita el nombre del usuario y lo valida.
def solicitar_nombre(mensaje):

    while True:
        nombre = input(mensaje).strip()

        if validar_nombre(nombre):
            return nombre

        print("El nombre ingresado no es válido. Inténtelo nuevamente.")

# Solicita una identificación hasta que cumpla con el formato
# establecido y no esté registrada previamente.
def solicitar_identificacion():

    while True:
        idpersona = input("Ingrese el número de identificación: ").strip()

        # Comprueba el formato y que no exista otro usuario con esa identificación.
        if validar_identificacion_no_registrada(idpersona):
            return idpersona

        print("La identificación no es válida o ya se encuentra registrada.")

#Valida que la identificacion de la persona no se vacia y que el usuario no exista
def validar_identificacion_no_registrada(idpersona):

    if not validar_formato_identificacion(idpersona):
        return False

    for usuario in Usuario.usuarios:
        if usuario.idpersona == idpersona:
            return False

    return True

def solicitar_nacionalidad():

    while True:
        nacionalidad = input("Ingrese la nacionalidad: ").strip()

        # Comprueba que el texto ingresado no esté vacío.
        if validar_texto(nacionalidad):
            return nacionalidad

        print("La nacionalidad no puede estar vacía. Inténtelo nuevamente.")

# Solicita el estado civil mediante un menú de opciones.
def solicitar_estado_civil():

    # Opciones permitidas para el estado civil.
    estados_civiles = {
        "1": "Soltero(a)",
        "2": "Casado(a)",
        "3": "Divorciado(a)",
        "4": "Viudo(a)",
        "5": "Unión libre"
    }

    while True:
        print("\n--- ESTADO CIVIL ---")
        print("1. Soltero(a)")
        print("2. Casado(a)")
        print("3. Divorciado(a)")
        print("4. Viudo(a)")
        print("5. Unión libre")

        # Solicita una opción al usuario.
        opcion = input("Seleccione su estado civil: ").strip()

        # Comprueba que la opción exista y devuelve su descripción.
        if opcion in estados_civiles:
            return estados_civiles[opcion]

        print("Opción inválida. Inténtelo nuevamente.")

# Solicita el año de ingreso y comprueba que sea válido.
def solicitar_anio_ingreso():

    while True:
        # Solicita el año como texto para poder validarlo.
        anio = input("Ingrese el año de ingreso al CUC: ").strip()

        # Comprueba que el año contenga números y esté dentro del rango permitido.
        if validar_anio_ingreso(anio):
            return int(anio)

        print("El año ingresado no es válido. Inténtelo nuevamente.")

# Solicita una fecha de nacimiento y comprueba que sea válida.
def solicitar_fecha_nacimiento():

    while True:
        # Solicita la fecha en formato año-mes-día.
        fecha = input("Ingrese la fecha de nacimiento (AAAA-MM-DD): ").strip()

        # Comprueba que la fecha tenga un formato y valor válidos.
        if validar_fecha_nacimiento(fecha):

            # Convierte el texto en un objeto de tipo date.
            return datetime.strptime(fecha, "%Y-%m-%d").date()

        print("La fecha ingresada no es válida. Inténtelo nuevamente.")

# Solicita un número telefónico y comprueba que tenga 8 dígitos.
def solicitar_telefono():

    while True:
        # Solicita el número telefónico y elimina espacios externos.
        telefono = input("Ingrese el número de teléfono: ").strip()

        # Comprueba que el número contenga exactamente 8 dígitos.
        if validar_telefono(telefono):
            return telefono

        print("El teléfono debe contener exactamente 8 dígitos numéricos.")

# Solicita un correo electrónico y comprueba que tenga un formato válido.
def solicitar_correo():

    while True:
        # Solicita el correo y elimina espacios externos.
        correo = input("Ingrese el correo electrónico: ").strip()

        # Comprueba que el correo tenga una estructura válida.
        if validar_correo(correo):
            return correo

        print("El correo electrónico ingresado no es válido. Inténtelo nuevamente.")

# Solicita una o varias carreras y las almacena en una lista.
def solicitar_carreras():

    while True:
        # Solicita las carreras separadas por comas.
        carreras_ingresadas = input(
            "Ingrese la carrera o carreras(separar por comas) a las qeu pertenece: "
        ).strip()

        # Comprueba que se haya ingresado algún dato.
        if validar_texto(carreras_ingresadas):

            carreras = []

            # Separa las carreras utilizando la coma como delimitador.
            for carrera in carreras_ingresadas.split(","):

                # Elimina los espacios innecesarios de cada carrera.
                carrera = carrera.strip()

                # Evita agregar elementos vacíos a la lista.
                if validar_texto(carrera):
                    carreras.append(carrera)

            # Devuelve la lista si contiene al menos una carrera.
            if carreras:
                return carreras

        print("Debe ingresar al menos una carrera válida.")

def buscar_usuario(idpersona):

    # Recorre la lista de usuarios registrados.
    for usuario in Usuario.usuarios:

        # Comprueba si la identificacion coincide.
        if usuario.idpersona == idpersona:
            return usuario

    # Devuelve None si no encuentra coincidencias.
    return None

# Muestra las opciones disponibles para modificar un usuario.
def mostrar_menu_modificacion():

    print("\n==============================================")
    print("             MODIFICAR USUARIO")
    print("==============================================")

    print("1. Nombre")
    print("2. Apellidos")
    print("3. Nacionalidad")
    print("4. Carreras")
    print("5. Estado civil")
    print("6. Año de ingreso")
    print("7. Fecha de nacimiento")
    print("8. Teléfono")
    print("9. Correo electrónico")
    print("10. Regresar")

    print("==============================================")

# Solicita una identificacion con formato valido.
def solicitar_identificacion_existente():

    while True:
        idpersona = input("Ingrese el numero de identificacion: ").strip()

        # Comprueba que la identificacion tenga un formato valido.
        if validar_formato_identificacion(idpersona):
            return idpersona

        print("La identificacion no tiene un formato valido.")
