# auth.py --> módulo de autenticación
# se incorporan funciones de inicio de sesión y registro.
# auth.py --> Autenticaciones de email y rol


def validar_email():
    """Verificacion de mail, tiene que ser si o si '@gmail.com'"""
    while True:
        email = input("Email: ").strip()
        if "@gmail.com" in email:
            return email 
        print("\nError: El mail debe contener '@gmail.com' ")

def validar_rol():
    """Verificacion de rol, solo puede ser admin o estandar"""
    while True:
        rol = input("Rol (admin / estandar): ").strip().lower()
        if rol in ["admin", "estandar"]:
            return rol
        print("\nError: el rol solo puede ser 'admin' o 'estandar' ")