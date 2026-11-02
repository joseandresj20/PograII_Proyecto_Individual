
# Importación de librerías necesarias
from datetime import date, datetime


# Comprueba que un texto no esté vacío.
def validar_texto(valor):
    
    return valor.strip() != ""


# Comprueba que un nombre contenga únicamente letras,
# espacios, guiones o apóstrofes.
def validar_nombre(valor):

    if not valor.strip():
        return False

    for caracter in valor:

        if not (caracter.isalpha() or caracter in " -'’"):
            return False

    return True


# Comprueba que el correo tenga una estructura básica válida.
def validar_correo(correo):

    correo = correo.strip()

    if correo.count("@") != 1:
        return False

    partes = correo.split("@")

    usuario = partes[0]
    dominio = partes[1]

    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    if dominio.startswith(".") or dominio.endswith("."):
        return False

    if " " in correo:
        return False

    return True


# Comprueba que el teléfono contenga entre 8 y 15 dígitos.
# Permite espacios, guiones y el símbolo +.
def validar_telefono(telefono):

    if not validar_texto(telefono):
        return False

    if not telefono.isdigit():
        return False

    return len(telefono) == 8


# Comprueba que el año de ingreso sea válido.
def validar_anio_ingreso(anio):

    if not anio.isdigit():
        return False

    anio = int(anio)

    return 1900 <= anio <= date.today().year


# Comprueba que la fecha tenga el formato AAAA-MM-DD
# y que no sea posterior a la fecha actual.
def validar_fecha_nacimiento(fecha):

    try:

        fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()

        return fecha_convertida <= date.today()

    except ValueError:

        return False

# Valida el formato de la identificación.
def validar_formato_identificacion(idpersona):

    if not validar_texto(idpersona):
        return False

    if not idpersona.isdigit():
        return False

    return len(idpersona) in (9, 11, 12)

# Valida que el ISBN tenga 10 o 13 digitos.
def validar_isbn(isbn):

    # Elimina los guiones para comprobar los digitos.
    isbn = isbn.replace("-", "")

    # Comprueba que el ISBN contenga solamente numeros.
    if not isbn.isdigit():
        return False

    return len(isbn) == 13


# Valida que el anio de publicacion sea correcto.
def validar_anio_publicacion(anio):

    # Comprueba que el anio contenga solamente numeros.
    if not anio.isdigit():
        return False

    # Convierte el anio a entero.
    anio = int(anio)

    # Comprueba que no sea un anio futuro.
    return 1 <= anio <= date.today().year
