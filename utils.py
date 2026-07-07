from colorama import Fore, init

# Inicializa colorama (necesario en Windows)
init(autoreset=True)

# Mensaje correcto (verde)
def ok(msg):
    print(Fore.GREEN + msg)

# Mensaje de error (rojo)
def error(msg):
    print(Fore.RED + msg)