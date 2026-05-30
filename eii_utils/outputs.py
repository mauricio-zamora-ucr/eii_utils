"""Utilidades de salida para aplicaciones de consola.

Este modulo contiene funciones para:
- Limpiar la consola.
- Generar e imprimir titulos decorados.
- Imprimir mensajes con color para exito, error y advertencia.
- Pausar la ejecucion hasta que la persona usuaria presione ENTER.
"""

import os

from colorama import Fore


def limpiar_consola() -> None:
    """Limpia la consola de forma portable para Windows y Unix."""
    os.system("cls" if os.name == "nt" else "clear")


def generar_titulo_decorado(texto: str, largo: int = 0) -> str:
    """Genera un titulo en mayuscula enmarcado por lineas de asteriscos.

    Args:
        texto: Texto base del titulo.
        largo: Ancho minimo del bloque decorado. Si es 0, usa el largo del texto.

    Returns:
        Un string multilinea listo para imprimirse o guardarse en archivo.
    """
    texto_mayuscula = texto.upper().strip()
    ancho = len(texto_mayuscula) if largo == 0 else max(largo, len(texto_mayuscula))
    linea = "*" * ancho
    return "\n".join((linea, texto_mayuscula.center(ancho, "*"), linea))


def imprimir_titulo_decorado(texto: str, largo: int = 0) -> None:
    """Imprime un titulo decorado usando el generador de string interno."""
    print(generar_titulo_decorado(texto, largo))


def imprimir_mensaje(mensaje: str, es_error: bool = False) -> None:
    """Imprime un mensaje de exito o de error con color.

    Args:
        mensaje: Texto a imprimir.
        es_error: Si es True imprime formato de error, si es False de exito.
    """
    if es_error:
        print(f"{Fore.RED}✖ {mensaje}")
    else:
        print(f"{Fore.GREEN}✔ {mensaje}")


def imprimir_error(mensaje: str) -> None:
    """Imprime un mensaje de error en color rojo."""
    print(f"{Fore.RED}✖ {mensaje}")


def imprimir_advertencia(mensaje: str) -> None:
    """Imprime un mensaje de advertencia en color amarillo."""
    print(f"{Fore.YELLOW}⚠ {mensaje}")


def imprimir_echo(etiqueta: str, valor, habilitado: bool = True) -> None:
    """Imprime una confirmacion de lectura si esta habilitado.

    Args:
        etiqueta: Etiqueta del dato leido.
        valor: Valor capturado.
        habilitado: Controla si se imprime o no el echo.
    """
    if habilitado:
        print(f"{Fore.GREEN}✔ {etiqueta}: {valor}")


def pausar(mensaje: str = "Digite <ENTER> para continuar...") -> None:
    """Pausa la ejecucion hasta que se presione ENTER.

    Args:
        mensaje: Texto mostrado antes de esperar ENTER.
    """
    input(mensaje)


# Compatibilidad hacia atras para codigo que aun usa nombres privados.
def _imprimir_error(mensaje: str) -> None:
    """Alias de compatibilidad para imprimir_error."""
    imprimir_error(mensaje)


def _imprimir_advertencia(mensaje: str) -> None:
    """Alias de compatibilidad para imprimir_advertencia."""
    imprimir_advertencia(mensaje)


def _imprimir_echo(etiqueta: str, valor, imprimir_echo_flag: bool) -> None:
    """Alias de compatibilidad para imprimir_echo."""
    imprimir_echo(etiqueta, valor, imprimir_echo_flag)
