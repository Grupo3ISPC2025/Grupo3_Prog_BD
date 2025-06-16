# auth.py --> módulo de autenticación
# se incorporan funciones de inicio de sesión y registro.
# auth.py --> Autenticaciones de email y rol

def validar_email():
    dominios_validos = ["@gmail.com", "@outlook.com", "@hotmail.com"]
    while True:
        email = input("Email: ").strip()
        if any(email.endswith(dominio) for dominio in dominios_validos):
            return email
        print("\nError: el email debe finalizar con un dominio válido.")

def validar_email_unico(usuarios, email_actual=None):
    while True:
        email = validar_email()

        # Permitimos dejar el mismo email si no se quiere cambiar
        if email == email_actual:
            return email

        if any(u.email == email for u in usuarios):
            print("\nError: Este email ya está registrado. Intente nuevamente.")
        else:
            return email

def validar_rol():
    while True:
        rol = input("Rol (admin / estandar): ").strip().lower()
        if rol in ["admin", "estandar"]:
            return rol
        print("\nError: el rol solo puede ser 'admin' o 'estandar' ")

def validar_contrasena():
    while True:
        contrasena = input("Contraseña (mínimo 6 caracteres): ").strip()
        if len(contrasena) >= 6:
            return contrasena
        print("\nError: La contraseña debe tener al menos 6 caracteres.")