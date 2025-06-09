# auth.py --> módulo de autenticación
# se incorporan funciones de inicio de sesión y registro.
# auth.py --> Autenticaciones de email y rol


def validar_email():
    dominios_validos = ["@gmail.com", "@outlook.com", "@hotmail.com"]
    while True:
        email = input("Email: ").strip()
        for dominio in dominios_validos:
            if email.endswith(dominio):
                return email
        print("\nError: el email debe finalizar con un dominio válido")

def validar_rol():
    while True:
        rol = input("Rol (admin / estandar): ").strip().lower()
        if rol in ["admin", "estandar"]:
            return rol
        print("\nError: el rol solo puede ser 'admin' o 'estandar' ")


def validar_email_unico(usuarios):
    while True:
        email = validar_email()
        if any(u.email == email for u in usuarios):
            print("\nError: Este email ya está registrado. Intente nuevamente.")
        else:
            return email

def validar_contraseña():
    while True:
        contraseña = input("Contraseña (mínimo 6 caracteres): ").strip()
        if len(contraseña) >= 6:
            return contraseña
        print("\nError: La contraseña debe tener al menos 6 caracteres.")
