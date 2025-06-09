# main.py --> menú e interaccion con usuario

from usuarios import registrar_usuario, mostrar_usuarios, iniciar_sesion, modificar_usuario, eliminar_usuario
from auth import validar_email, validar_rol

def imprimir_usuarios():
    """
    Imprime lista de usuarios registrados con info básica

    Cada usuario se enumera con:
        - indice_usuario (int): representaria el num secuencial del usuario en la lista (o posicion)
        - usuario (dict): contiene nombre, apellido, email y rol del usuario.

    Ej de salida:
        3. Gloria López - gloria@gmail.com (estandar)
    """    
    print("\nUsuarios Registrados:")
    for indice_usuario, usuario in enumerate(mostrar_usuarios(), 1):
        print(f"{indice_usuario}. {usuario['nombre']} {usuario['apellido']} - {usuario['email']} ({usuario['rol']})")


def registrar_usuarios():

    """
    Crea un nuevo usuario y lo agrega a lista de usuarios

    Parameters:
        nombre (input): nombre del usuario
        apellido (input): apellido del usuario
        email (input): email del usuario
        contraseña (input): contraseña del usuario
        rol (input): rol del usuario ('admin' o 'estandar')

    Returns:
        dict: nuevo usuario registrado.
    """
    print("\n<<< Registrar nuevo usuario >>>")
    nuevo_usuario = registrar_usuario() 

def main():
    print("<<< Bienvenidos a Portfolio Inteligente >>>")

    while True:
        print("\nElegir una opción:")
        print("1. Mostrar usuarios")
        print("2. Registrar nuevo usuario")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == '1':
            mostrar_usuarios()

        elif opcion == '2':
            registrar_usuario()

        elif opcion == '3':
            usuario = iniciar_sesion()
            if usuario:
                if usuario["rol"] == "admin":
                    while True:
                        print("\n<<<  Menú Administrador  >>>")
                        print("1. Modificar usuarios")
                        print("2. Eliminar usuarios")
                        print("3. Ver usuarios")
                        print("4. Cerrar sesión")

                        opciones_de_admin = input("Seleccionar una opción: ").strip()

                        if opciones_de_admin == '1':
                            modificar_usuario(usuario)
                        elif opciones_de_admin == '2':
                            eliminar_usuario(usuario)
                        elif opciones_de_admin == '3':
                            mostrar_usuarios()
                        elif opciones_de_admin == '4':
                            print("Su sesión finalizó con éxito.")
                            break
                        else:
                            print("Opción inválida, intente nuevamente.")

                else:
                    while True:
                        print(f"\nSesión iniciada como: {usuario['nombre']} ({usuario['rol']})")
                        print("Opciones disponibles:")
                        print("1. Ver usuarios")
                        print("2. Cerrar sesión")

                        opcion_estandar = input("Elegí una opción: ").strip()

                        if opcion_estandar == '1':
                            mostrar_usuarios()
                        elif opcion_estandar == '2':
                            print("Su sesión finalizó con éxito.")
                            break
                        else:
                            print("La opción es inválida, intente de nuevo")

            else:
                print("No se pudo iniciar sesión, vuelva a intentar!")

        elif opcion == '4':
            print("Usted esta saliendo del programa")
            break

        else:
            print("Error, por favor selecciona entre las opciones: 1, 2, 3 o 4")

    print("Cerrando programa. Vuelva pronto!")

if __name__ == "__main__":
    main()
