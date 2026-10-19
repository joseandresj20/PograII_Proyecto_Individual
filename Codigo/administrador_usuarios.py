def from datetime import datetime

control_usuarios():
    while True:

        mostrar_menu_usuarios()

        opcion = input("Favor ingresar la opcion deseada: ")
        
        if opcion == "1":

            registrar_usuario()
            print("\nEl usuario fue registrado de manera existosa.\n")
            break

        elif opcion == "2":
            modificar_usuario()
            print("\nEl usuario fue modifcado de manera existosa.\n")
            break

        elif opcion == "3":
            eliminar_usario()
            print("\nEl usuario fue eliminado de manera existosa.\n")
            break
        
        elif opcion == "4":
            consultar_usuario()
            break

        else:
            print("La opcion indicada es invalida. Intentelo nuevamente./n")

def mostrar_menu_usuarios():
    print("\nIngresando al apartado de administracion de usuarios....\n")
    print("Sistema de Administracion de usuarios")
    print("1. Registrar usuario.")
    print("2. Modificar usuario.")
    print("3. Eliminar ususario.")
    print("4. Consultar usario")

def registrar_usuario():
    
    while True:
        
            nombre = insertar_datos("el nombre de usario: ")
            apellidos = insertar_datos("los apellidos: ")
            idpersona = insertar_datos("el numero de identificacion: ")
            stado_civil = insertar_datos("el estado civil: ")
            nacionalidad = insertar_datos("la nacionalidad: ")
            anio_ingreso = insertar_datos("el anio de ingreso: ")
            telefono = insertar_datos("el numero de telefono: ")
            correo = insertar_datos("el correo electronico: ")
            carreras = (insertar_datos("Ingrese la o las carreras a las que pertenece usando las siglas. "
                                           + "Separelo por comas ',' .\n")).split(",")
        try:
            fecha_nacimiento = datetime.strptime(insertar_datos("la fecha de nacimiento en formato AAAA-MM-DD: "),"%Y-%m-%d").date()
        except ValueError:
            print("La fecha ingresada no es valida")

#def modificar_usuario():

#def eliminar_usario():

#def consultar_usuario():

def insertar_datos(valor_escrito):
    entrada = input(f"Favor digite {valor_escrito}")
    return entrada

registrar_usuario()
