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
    """Permite iniciar sesion"""
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
        dict: usuario recién creado. None si existe algún error.
    """
    print("\n<<< Registro de usuario >>>")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    while True:
        email = validar_email()
        if any(usuario["email"] == email for usuario in usuarios):
            print("\nError: Este email ya se encuentra registrado.")
        else:
            break

    while True:
        contraseña = input("Contraseña (ingresa mínimo 6 caracteres): ")
        if len(contraseña) >= 6:
            break
        print("\nError: la contraseña debe tener al menos 6 caracteres.")

    rol = validar_rol()

    nuevo_usuario = {'nombre': nombre, 'apellido': apellido, 'email': email, 'contraseña': contraseña, 'rol': rol}
    usuarios.append(nuevo_usuario)

    print(f"\nUsuario registrado: {nuevo_usuario['nombre']} {nuevo_usuario['apellido']} ({nuevo_usuario['rol']})")
    return nuevo_usuario

def modificar_usuario(admin):
    """Permite que los administradores puedan modificar usuarios estándar
    
    Parameters:
        admin (dict): Usuario administrador que realiza la acción.

    Returns:
        - muestra usuarios y permite seleccionar 1 p/editar.
        - valida que el nuevo email no este en uso.
        - valida que la nueva contraseña tenga minimo 6 caracteres.
        - no permite modificar usuarios administradores.   
    """
    if admin["rol"] != "admin":
        print("\nError: Solo los administradores pueden modificar usuarios.")
        return
    
    print("\nUsuarios:")
    mostrar_usuarios()

    id_usuario = int(input("Elegi el número del usuario a editar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario]["rol"] == "estandar":
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        nuevo_email = validar_email()

        for i, usuario in enumerate(usuarios):
            if i != id_usuario and usuario["email"] == nuevo_email:
                print("\nError: Este email ya se encuentra registrado.")
                return
        
        while True:
            nueva_contraseña = input("Nueva contraseña: ")
            if len(nueva_contraseña) >= 6:
                break
            print("\nError: La contraseña debe tener al menos 6 caracteres.")

        # Asignar nuevos valores
        usuarios[id_usuario]["nombre"] = nuevo_nombre
        usuarios[id_usuario]["apellido"] = nuevo_apellido
        usuarios[id_usuario]["email"] = nuevo_email
        usuarios[id_usuario]["contraseña"] = nueva_contraseña

        print("\nUsuario modificado con éxito")
    else:
        print("\nError: No se puede modificar a un usuario Administrador o el número es inválido")

def eliminar_usuario(admin):
    """Solo los admins pueden borrar usuarios"""
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