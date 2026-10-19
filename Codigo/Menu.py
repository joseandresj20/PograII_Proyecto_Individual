from Clases import Usuario, Libro, Prestamo

def registrar_usuario():

def modificar_usuario():

def registrar_libro():

def modificar_libro():

def registrar_prestamo():

def registrar_devolucion():

def mostrar_menu_principal():
    print("Bienvenido al Sistema de Biblioteca Republica de los Cocos")
    print("1. Administrador de usuarios.")
    print("3. Administrador de libros.")
    print("5. Administrador de prestamos")
    print("7. Acerca de...")
    print("7. Salir\n")



def mostrar_menu_principal():
    
    while True:

        mostrar_menu()
        
        opcion = input("Favor ingresar la opcion deseada: ")
        
        if opcion == "1":

            
            
            
        elif opcion == "2":
            
            print("\nIngresando al sistema..... \n")
            if len(lista_conejos) > 0:
                print("\nMostrando los conejos registrados en el sistema....\nLos conejos registrados son los siguientes: \n")
                contador = 1
                for conejo in lista_conejos:
                    print(f"==========Conejo {contador}==========")
                    print(f"Nombre del conejo: {conejo.nombre_conejo}")
                    print(f"Nombre del dueno: {conejo.nombre_dueno}")
                    print(f"Edad del conejo en meses: {conejo.edad_conejo}")
                    print(f"Edad del conejo en anios humanos: {conejo.edad_humana}")
                    contador += 1
                print("==============================")
            else:
                print("No existen aun conejos registrados en el sistema.\n")
                
        elif opcion == "3":
            
            print("\nRealizando el calculo de la edad humana de los conejos....\n")
            for conejo in lista_conejos:
                conejo.calcular_edad()

            print("Las edades fueron calculadas con exito....\n")
            
        elif opcion == "4":
            print("\nIngresando al sistema de eliminacion de registro.....\n")
            invalido = True    
            while invalido:
                entrada = input("Favor ingrese el numero del conejo a eliminar: ")
                try:
                    numero_conejo = int(entrada)
                    if numero_conejo > 0 and numero_conejo <= len(lista_conejos):
                        conejo = lista_conejos.pop(numero_conejo - 1)
                        print(f"\nEl conejo llamado {conejo.nombre_conejo} fue removido del Sistema\n")
                        invalido = False
                    else:
                        print("\nEl numero ingresado no es valido, debe corresponder a un conejo de la lista. Intentelo de nuevo.\n")
                except ValueError:
                    print("\nEl numero ingresado no es valido. Intentelo de nuevo.\n")
            
        elif opcion == "5":

            print("\nEn este momento esta saliendo del sistema, gracias....\n")
            
            return
        else:
            print("\nLa opcion ingresada no es valida. Regresando al menu principal....\n")
            
      
menu_principal()
