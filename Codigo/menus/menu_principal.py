from menus.administrador_usuarios import control_usuarios
from menus.administrador_libros import control_libros
from menus.administrador_prestamos import control_prestamos

def mostrar_menu_principal():

    while True:

        print("\n==============================================")
        print(" BIBLIOTECA REPÚBLICA DE LOS COCOS")
        print("==============================================")

        print("1. Administrador de usuarios.")
        print("2. Administrador de libros.")
        print("3. Administrador de préstamos y devoluciones.")
        print("5. Acerca de...")
        print("6. Salir")
        print("==============================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\nIngresando al administrador de usuarios...")
            control_usuarios()

        elif opcion == "2":
            print("\nIngresando al administrador de libros...")
            control_libros()

        elif opcion == "3":
            print("\nIngresando al administrador de préstamos y devoluciones...")
            control_prestamos()

        elif opcion == "5":
            mostrar_acerca_de()

        elif opcion == "6":
            print("\nGracias por utilizar nuestro sistema.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

def mostrar_acerca_de():

    print("\n=====================================================")
    print("     PROYECTO BIBLIOTECA REPÚBLICA DE LOS COCOS")
    print("=====================================================")

    print("\nINFORMACIÓN DEL CURSO")
    print("Curso: TI-131 Programación II")
    print("Docente: Róger Rodríguez López")
    print("Periodo: III Cuatrimestre 2026")
    print("Institución: Colegio Universitario de Cartago")

    print("\nINFORMACIÓN DEL ESTUDIANTE")
    print("Estudiante: Jose Andres Jimenez Coto")
    print("Carnet: 304620100")
    print("Carrera: Tecnologias de Informacion")
    
    print("\n==============================================")

