# main.py --> menú e interaccion con usuario

from usuarios import registrar_usuario, mostrar_usuarios

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
        nombre (str): nombre del usuario
        apellido (str): apellido del usuario
        email (str): email del usuario
        contraseña (str): contraseña del usuario
        rol (str): rol del usuario ('admin' o 'estandar')

    Returns:
        dict: nuevo usuario registrado.
    """    
    print("\n<<< Registrar nuevo usuario >>>")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("email: ")
    contraseña = input("Contraseña: ")
    rol = input("Rol (admin / estandar): ")
    nuevo = registrar_usuario(nombre, apellido, email, contraseña, rol)
    print(f"\nUsuario registrado: {nuevo['nombre']} {nuevo['apellido']} ({nuevo['rol']})")

def main():
    print("<<< Bienvenidos a Portfolio Inteligente >>>")

    while True:
        print("\nElige una opción:")
        print("1. Mostrar usuarios")
        print("2. Registrar nuevo usuario")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == '1':
            imprimir_usuarios()
        elif opcion == '2':
            registrar_usuarios()
        elif opcion == '3':
            print("Estás saliendo del programa...")
            break
        else:
            print("La opción no es válida. Por favor ingresá 1, 2 o 3.")

    print("Programa finalizado. Vuelva pronto!")

if __name__ == "__main__":
    main()
