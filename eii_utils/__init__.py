from colorama import init

try:
    init(auto_reset=True)
except TypeError:
    init(autoreset=True)

from .inputs import (
    leer_booleano,
    leer_entero,
    leer_flotante,
    leer_rango_enteros,
    leer_rango_flotante,
    leer_texto,
)
from .outputs import limpiar_consola, imprimir_mensaje, imprimir_titulo_decorado

__all__ = [
    "leer_booleano",
    "leer_entero",
    "leer_flotante",
    "leer_rango_enteros",
    "leer_rango_flotante",
    "leer_texto",
    "limpiar_consola",
    "imprimir_mensaje",
    "imprimir_titulo_decorado",
]
