# usuarios.py -->se definen las clases Usuario y Administrador
# usuarios.py -->se definen las clases Usuario y Administrador

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
        'email': 'marcos@hotmail.com',
        'contraseña': 'marcos123',
        'rol': 'estandar'
    },
    {
        'nombre': 'Lucas',
        'apellido': 'Martínez',
        'email': 'lucas@hotmail.com',
        'contraseña': 'lucas123',
        'rol': 'estandar'
    },
    {
        'nombre': 'Teodoro',
        'apellido': 'Ramírez',
        'email': 'teodoro@outlook.com',
        'contraseña': 'teo123',
        'rol': 'estandar'
    }
]

def registrar_usuario(nombre, apellido, email, contraseña, rol='estandar'):
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
    nuevo_usuario = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'contraseña': contraseña,
        'rol': rol
    }
    usuarios.append(nuevo_usuario)
    return nuevo_usuario

def mostrar_usuarios():
    """
    Devuelve lista actualizada c/usuarios registrados.

    Returns:
        list: lista de diccionarios c/datos de usuarios.
    """    
    return usuarios