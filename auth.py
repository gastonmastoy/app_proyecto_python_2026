# auth.py

from config import USUARIO, PASSWORD, ERROR_LOGIN, LOGIN_EXITOSO

def login():
    """
    Solicita usuario y contraseña y valida el acceso.
    """
    print("\n Acceso al sistema del museo")

    user = input("Usuario: ")
    password = input("Contraseña: ")

    # Verificación de credenciales
    if user == USUARIO and password == PASSWORD:
        print(LOGIN_EXITOSO)
        return True
    else:
        print(ERROR_LOGIN)
        return False