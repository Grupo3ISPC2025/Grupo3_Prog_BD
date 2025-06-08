# usuarios.py -->se definen las clases Usuario y Administrador
# usuarios.py -->se definen las clases Usuario y Administrador

from auth import validar_email, validar_rol 

usuarios = [
    {
        'nombre': 'Florencia',
        'apellido': 'Lorenzati',
        'email': 'florencia@gmail.com',
        'contraseña': 'flor123',
        'rol': 'admin'
    },
    {
        'nombre': 'Ignacio',
        'apellido': 'Bentivoglio',
        'email': 'ignacio@gmail.com',
        'contraseña': 'nacho123',
        'rol': 'admin'
    },
    {
        'nombre': 'Gloria',
        'apellido': 'López',
        'email': 'gloria@gmail.com',
        'contraseña': 'gloria123',
        'rol': 'estandar'
    },
    {
        'nombre': 'Marcos',
        'apellido': 'Fernández',
        'email': 'marcos@gmail.com',
        'contraseña': 'marcos123',
        'rol': 'estandar'
    },
    {
        'nombre': 'Lucas',
        'apellido': 'Martínez',
        'email': 'lucas@gmail.com',
        'contraseña': 'lucas123',
        'rol': 'estandar'
    },
    {
        'nombre': 'Teodoro',
        'apellido': 'Ramírez',
        'email': 'teodoro@gmail.com',
        'contraseña': 'teo123',
        'rol': 'estandar'
    }
]


def iniciar_sesion():
    """Permite que iniciar sesion"""
    email = validar_email()
    contraseña = input("Contraseña:")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["contraseña"] == contraseña:
            print(f"\nBienvenido, {usuario['nombre']} ({usuario['rol']})")
            return usuario

    print("\nError: Mail o contraseña incorrectas.")
    return None

def registrar_usuario():
    """
    Crea y agrega un nuevo usuario a la lista.

    Parameters:
        nombre (str): nombre del usuario
        apellido (str): apellido del usuario
        email (str): email del usuario
        contraseña (str): contraseña del usuario
        rol (str): rol del usuario ('admin' o 'estandar')

    Returns:
        dict: usuario recién creado.
    """
    print("\n<<< Registro de usuario >>>")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = validar_email()
    contraseña = input("Contraseña: ")
    rol = validar_rol()

    nuevo_usuario = {'nombre': nombre, 'apellido': apellido, 'email': email, 'contraseña': contraseña, 'rol': rol}
    usuarios.append(nuevo_usuario)

    print(f"\nUsuario registrado: {nuevo_usuario['nombre']} {nuevo_usuario['apellido']} ({nuevo_usuario['rol']})")
    return nuevo_usuario




def modificar_usuario(admin):
    """Para que solo los administradores puedan modificar a otors usuarios"""
    if admin["rol"] != "admin":
        print("\nError: Solo los administradores pueden modificar usuarios.")
        return
    
    print("\nUsuarios:")
    mostrar_usuarios()

    id_usuario = int(input("Elgi el numero del usuario a cambiar: ")) -1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario]["rol"] == "estandar":
        usuarios[id_usuario]["nombre"] = input ("Nuevo nombre: ")
        usuarios[id_usuario]["email"] = input ("Nuevo mail: ")
        usuarios[id_usuario]["contraseña"] = input ("Nueva contraseña: ")
        print ("\nUsuario modificado")
    else:
        print ("\nNo se puede modificar admins")

def eliminar_usuario(admin):
    """para que solo los admins puedan borrar usuarios"""
    if admin["rol"] != "admin":
        print("\nError: Solo un administrador puede eliminar usuarios.")
        return

    print("\nUsuarios:")
    for indice_usuario, usuario in enumerate(usuarios, 1):
        print(f"{indice_usuario}. {usuario['nombre']} {usuario['apellido']} - {usuario['email']} ({usuario['rol']})")

    id_usuario = int(input("\nElegí el número del usuario que quiere eliminar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario]["rol"] == "estandar":
        usuarios.pop(id_usuario)
        print("\nUsuario eliminado con éxito.")
    else:
        print("\nError: no se puede eliminar a un admin")

def mostrar_usuarios():
    """
    Devuelve lista actualizada c/usuarios registrados.

    Returns:
        list: lista de diccionarios c/datos de usuarios.
        Ahora cada vez que necesitemos que se vean los usuarios directamente llamamos a mostrar_usuarios
    """    
    print("\nLista de Usuarios: ")
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u['nombre']} {u['apellido']} - {u['email']} ({u['rol']})")