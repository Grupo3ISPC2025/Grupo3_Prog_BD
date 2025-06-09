# usuarios.py -->se definen las clases Usuario y Administrador
# usuarios.py -->se definen las clases Usuario y Administrador

from auth import validar_email, validar_rol, validar_contraseña, validar_email_unico

class Usuario:

    def __init__(self, nombre, apellido, email, contraseña, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email} ({self.rol})"
    
class Administrador (Usuario):
    def __init__(self, nombre, apellido, email, contraseña):
        super().__init__(nombre, apellido, email, contraseña, rol="admin")

usuarios = [
    Administrador('Florencia', 'Lorenzati', 'florencia@gmail.com', 'flor123'),
    
    Administrador('Ignacio', 'Bentivoglio', 'ignacio@gmail.com', 'nacho123'),
    
    Usuario('Gloria', 'López', 'gloria@gmail.com', 'gloria123', 'estandar'),

    Usuario('Marcos', 'Fernández', 'marcos@gmail.com','marcos123', 'estandar'),

    Usuario('Lucas', 'Martínez', 'lucas@gmail.com', 'lucas123', 'estandar'),

    Usuario('Teodoro', 'Ramírez', 'teodoro@gmail.com', 'teo123', 'estandar')
]


def iniciar_sesion():
    """Permite que iniciar sesion"""
    email = validar_email()
    contraseña = input("Contraseña:")

    for usuario in usuarios:
        if usuario.email == email and usuario.contraseña == contraseña:
            print(f"\nBienvenido, {usuario.nombre} ({usuario.rol})")
            return usuario

    print("\nError: Mail o contraseña incorrectas.")
    return None

def registrar_usuario():
<<<<<<< Updated upstream
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
=======
>>>>>>> Stashed changes
    print("\n<<< Registro de usuario >>>")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
<<<<<<< Updated upstream
    email = validar_email()
    contraseña = input("Contraseña: ")
=======
    email = validar_email_unico(usuarios)
    contraseña = validar_contraseña()
>>>>>>> Stashed changes
    rol = validar_rol()

    if rol == "admin":
        nuevo_usuario = Usuario (nombre, apellido, email, contraseña)
    else:
        nuevo_usuario = Usuario (nombre, apellido, email, contraseña, rol)

    usuarios.append(nuevo_usuario)

    print(f"\nUsuario registrado: {nuevo_usuario.nombre} {nuevo_usuario.apellido} ({nuevo_usuario.rol})")
    return nuevo_usuario

<<<<<<< Updated upstream



def modificar_usuario(admin):
    """Para que solo los administradores puedan modificar a otors usuarios"""
    if admin["rol"] != "admin":
=======
def modificar_usuario(admin):

    if admin.rol != "admin":
>>>>>>> Stashed changes
        print("\nError: Solo los administradores pueden modificar usuarios.")
        return
    
    print("\nUsuarios:")
    mostrar_usuarios()

    id_usuario = int(input("Elgi el numero del usuario a cambiar: ")) -1

<<<<<<< Updated upstream
    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario]["rol"] == "estandar":
        usuarios[id_usuario]["nombre"] = input ("Nuevo nombre: ")
        usuarios[id_usuario]["email"] = input ("Nuevo mail: ")
        usuarios[id_usuario]["contraseña"] = input ("Nueva contraseña: ")
        print ("\nUsuario modificado")
=======
    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario].rol == "estandar":
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        nuevo_email = validar_email()

        for i, u in enumerate(usuarios):
            if i != id_usuario and u.email == nuevo_email:
                print("\nError: Este email ya se encuentra registrado.")
                return
        
        while True:
            nueva_contraseña = input("Nueva contraseña: ")
            if len(nueva_contraseña) >= 6:
                break
            print("\nError: La contraseña debe tener al menos 6 caracteres.")

        # Asignar nuevos valores
        usuarios[id_usuario].nombre = nuevo_nombre
        usuarios[id_usuario].apellido = nuevo_apellido
        usuarios[id_usuario].email = nuevo_email
        usuarios[id_usuario].contraseña = nueva_contraseña

        print("\nUsuario modificado con éxito")
>>>>>>> Stashed changes
    else:
        print ("\nNo se puede modificar admins")

def eliminar_usuario(admin):
<<<<<<< Updated upstream
    """para que solo los admins puedan borrar usuarios"""
    if admin["rol"] != "admin":
        print("\nError: Solo un administrador puede eliminar usuarios.")
=======
    if admin.rol != "admin":
        print("\nError: Sólo los administradores pueden eliminar usuarios.")
>>>>>>> Stashed changes
        return

    print("\nUsuarios:")
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u}")

    id_usuario = int(input("\nElegí el número del usuario que quiere eliminar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario].rol == "estandar":
        usuarios.pop(id_usuario)
        print("\nUsuario eliminado con éxito.")
    else:
        print("\nError: no se puede eliminar a un administrador")

def mostrar_usuarios():
    print("\nLista de Usuarios: ")
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u.nombre} {u.apellido} - {u.email} ({u.rol})")