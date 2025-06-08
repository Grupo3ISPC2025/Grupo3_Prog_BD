# auth.py --> módulo de autenticación
# se incorporan funciones de inicio de sesión y registro.
# auth.py --> Autenticaciones de email y rol


def validar_email():
    """Verificacion de mail, solo se permite los siguientes dominios: @gmail.com - @outlook.com - @hotmail.com"""
    dominios_validos = ["@gmail.com", "@outlook.com", "@hotmail.com"]
    while True:
        email = input("Email: ").strip()
        for dominio in dominios_validos:
            if email.endswith(dominio):
                return email
        print("\nError: el email debe finalizar con un dominio válido")

def validar_rol():
    """Verificacion de rol, solo puede ser admin o estandar"""
    while True:
        rol = input("Rol (admin / estandar): ").strip().lower()
        if rol in ["admin", "estandar"]:
            return rol
        print("\nError: el rol solo puede ser 'admin' o 'estandar' ")