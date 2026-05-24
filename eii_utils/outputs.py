import os

from colorama import Fore


def limpiar_consola() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_titulo_decorado(texto: str, largo: int = 0) -> None:
    texto_mayuscula = texto.upper().strip()
    ancho = len(texto_mayuscula) if largo == 0 else max(largo, len(texto_mayuscula))
    linea = "*" * ancho
    print(linea)
    print(texto_mayuscula.center(ancho, "*"))
    print(linea)


def imprimir_mensaje(mensaje: str, es_error: bool = False) -> None:
    if es_error:
        print(f"{Fore.RED}✖ {mensaje}")
    else:
        print(f"{Fore.GREEN}✔ {mensaje}")
