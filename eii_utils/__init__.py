"""API publica del paquete eii_utils.

Agrupa utilidades de entrada y salida para aplicaciones de consola.
"""

from colorama import init

try:
    init(auto_reset=True)
except TypeError:
    init(autoreset=True)

from .inputs import (
    leer_booleano,
    leer_booleano_opcional,
    leer_entero,
    leer_entero_opcional,
    leer_flotante,
    leer_flotante_opcional,
    leer_rango_enteros,
    leer_rango_flotante,
    leer_texto,
    leer_texto_opcional,
    mostrar_menu,
)
from .outputs import (
    generar_titulo_decorado,
    imprimir_advertencia,
    imprimir_echo,
    imprimir_error,
    imprimir_mensaje,
    imprimir_titulo_decorado,
    limpiar_consola,
    pausar,
)

__all__ = [
    "leer_booleano",
    "leer_booleano_opcional",
    "leer_entero",
    "leer_entero_opcional",
    "leer_flotante",
    "leer_flotante_opcional",
    "leer_rango_enteros",
    "leer_rango_flotante",
    "leer_texto",
    "leer_texto_opcional",
    "mostrar_menu",
    "generar_titulo_decorado",
    "imprimir_advertencia",
    "imprimir_echo",
    "imprimir_error",
    "limpiar_consola",
    "imprimir_mensaje",
    "imprimir_titulo_decorado",
    "pausar",
]
