# usuarios.py -->se definen las clases Usuario y Administrador
# usuarios.py -->se definen las clases Usuario y Administrador

from auth import validar_email, validar_rol, validar_contrasena, validar_email_unico 
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    apellido: str
    email: str
    contrasena: str
    rol: str

class Administrador(Usuario):
    def __init__(self, nombre, apellido, email, contrasena):
        super().__init__(nombre, apellido, email, contrasena, rol="admin")

usuarios = [
    Administrador('Florencia', 'Lorenzati', 'florencia@gmail.com', 'flor123'),
    Administrador('Ignacio', 'Bentivoglio', 'ignacio@gmail.com', 'nacho123'),
    Usuario('Gloria', 'López', 'gloria@gmail.com', 'gloria123', 'estandar'),
    Usuario('Marcos', 'Fernández', 'marcos@gmail.com', 'marcos123', 'estandar'),
    Usuario('Lucas', 'Martínez', 'lucas@gmail.com', 'lucas123', 'estandar'),
    Usuario('Teodoro', 'Ramírez', 'teodoro@gmail.com', 'teo123', 'estandar')
    ]

def iniciar_sesion():
    email = validar_email()
    contrasena = input("Contraseña:")

    for usuario in usuarios:
        if usuario.email == email and usuario.contrasena == contrasena:
            print(f"\nBienvenido, {usuario.nombre} ({usuario.rol})")
            return usuario

    print("\nError: Mail o contraseña incorrectas.")
    return None

def registrar_usuario():
    print("\n<<< Registro de usuario >>>")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = validar_email_unico(usuarios)
    contrasena = validar_contrasena()

    rol = validar_rol()
    if rol == "admin":
        nuevo_usuario = Administrador(nombre, apellido, email, contrasena)
    else:
        nuevo_usuario = Usuario(nombre, apellido, email, contrasena, rol)

    usuarios.append(nuevo_usuario)
    print(f"\nUsuario registrado: {nuevo_usuario.nombre} {nuevo_usuario.apellido} ({nuevo_usuario.rol})")
    return nuevo_usuario

def modificar_usuario(admin):
    if admin.rol != "admin":
        print("\nError: Solo los administradores pueden modificar usuarios.")
        return
    
    print("\nUsuarios:")
    mostrar_usuarios()

    id_usuario = int(input("Elegi el número del usuario a editar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario].rol == "estandar":
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        email_actual = usuarios[id_usuario].email
        nuevo_email = validar_email_unico(usuarios, email_actual)

        nueva_contrasena = validar_contrasena()

        for indice_usuario, usuario in enumerate(usuarios):
            if any(i != id_usuario and u.email == nuevo_email for i, u in enumerate(usuarios)):
                print("\nError: Este email ya se encuentra registrado.")
                return

        usuarios[id_usuario].nombre = nuevo_nombre
        usuarios[id_usuario].apellido = nuevo_apellido
        usuarios[id_usuario].email = nuevo_email
        usuarios[id_usuario].contrasena = nueva_contrasena

        print("\nUsuario modificado con éxito")
    else:
        print("\nError: No se puede modificar a un usuario Administrador o el número es inválido")

def eliminar_usuario(admin):
    if admin.rol != "admin":
        print("\nError: Solo un administrador puede eliminar usuarios.")
        return

    print("\nUsuarios:")
    for indice_usuario, usuario in enumerate(usuarios, 1):
        print(f"{indice_usuario}. {usuario}")

    id_usuario = int(input("\nElegí el número del usuario que quiere eliminar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario].rol == "estandar":
        usuarios.pop(id_usuario)
        print("\nUsuario eliminado con éxito.")
    else:
        print("\nError: no se puede eliminar a un admin")

def mostrar_usuarios():
    print("\nLista de Usuarios: ")
    for indice_usuario, usuario in enumerate(usuarios, 1):
        print(f"{indice_usuario}. {usuario.nombre} {usuario.apellido} - {usuario.email} ({usuario.rol})")