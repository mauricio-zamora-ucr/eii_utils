"""Utilidades de lectura de datos por consola.

Este modulo ofrece funciones de entrada robustas para leer tipos basicos,
rangos validos, valores opcionales y menus numerados.
"""

from .outputs import (
    imprimir_advertencia,
    imprimir_echo as _imprimir_echo,
    imprimir_error,
    imprimir_titulo_decorado,
)


def leer_entero(etiqueta: str, imprimir_echo: bool = True) -> int:
    """Lee un numero entero valido desde consola.

    Args:
        etiqueta: Texto mostrado antes de la lectura.
        imprimir_echo: Si es True, imprime una confirmacion del valor leido.

    Returns:
        El entero capturado.
    """
    while True:
        entrada = input(f"{etiqueta}: ")
        try:
            valor = int(entrada)
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        except ValueError:
            imprimir_error("Debe ingresar un numero entero valido.")


def leer_flotante(etiqueta: str, imprimir_echo: bool = True) -> float:
    """Lee un numero flotante valido desde consola.

    Args:
        etiqueta: Texto mostrado antes de la lectura.
        imprimir_echo: Si es True, imprime una confirmacion del valor leido.

    Returns:
        El flotante capturado.
    """
    while True:
        entrada = input(f"{etiqueta}: ")
        try:
            valor = float(entrada)
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        except ValueError:
            imprimir_error("Debe ingresar un numero flotante valido.")


def leer_texto(etiqueta: str, es_obligatorio: bool = True, imprimir_echo: bool = True) -> str:
    """Lee texto desde consola con opcion de obligatoriedad.

    Args:
        etiqueta: Texto mostrado antes de la lectura.
        es_obligatorio: Si es True, no acepta texto vacio.
        imprimir_echo: Si es True, imprime una confirmacion del valor leido.

    Returns:
        El texto capturado.
    """
    prompt = f"{etiqueta}: "
    while True:
        valor = input(prompt).strip()
        if es_obligatorio and not valor:
            imprimir_advertencia("El texto es obligatorio y no puede estar vacio.")
            continue
        _imprimir_echo(etiqueta, valor, imprimir_echo)
        return valor


def leer_booleano(etiqueta: str, imprimir_echo: bool = True) -> bool:
    """Lee un valor booleano usando variantes de si/no.

    Args:
        etiqueta: Texto mostrado antes de la lectura.
        imprimir_echo: Si es True, imprime una confirmacion del valor leido.

    Returns:
        True o False segun la entrada interpretada.
    """
    valores_verdaderos = {"si", "sí", "s", "true", "1", "y", "yes"}
    valores_falsos = {"no", "n", "false", "0"}

    while True:
        entrada = input(f"{etiqueta} (sí/no): ").strip().lower()
        if entrada in valores_verdaderos:
            _imprimir_echo(etiqueta, True, imprimir_echo)
            return True
        if entrada in valores_falsos:
            _imprimir_echo(etiqueta, False, imprimir_echo)
            return False
        imprimir_error("Debe ingresar un valor booleano valido (si/no).")


def leer_rango_enteros(
    etiqueta: str,
    menor_inclusive: int,
    mayor_inclusive: int,
    imprimir_echo: bool = True,
) -> int:
    """Lee un entero dentro de un rango inclusivo.

    Args:
        etiqueta: Texto mostrado antes de la lectura.
        menor_inclusive: Limite inferior permitido.
        mayor_inclusive: Limite superior permitido.
        imprimir_echo: Si es True, imprime una confirmacion del valor leido.

    Returns:
        El entero capturado dentro del rango.
    """
    while True:
        valor = leer_entero(etiqueta, imprimir_echo=False)
        if menor_inclusive <= valor <= mayor_inclusive:
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        imprimir_error(f"Debe ingresar un entero entre {menor_inclusive} y {mayor_inclusive}.")


def leer_rango_flotante(
    etiqueta: str,
    menor_inclusive: float,
    mayor_inclusive: float,
    imprimir_echo: bool = True,
) -> float:
    """Lee un flotante dentro de un rango inclusivo.

    Args:
        etiqueta: Texto mostrado antes de la lectura.
        menor_inclusive: Limite inferior permitido.
        mayor_inclusive: Limite superior permitido.
        imprimir_echo: Si es True, imprime una confirmacion del valor leido.

    Returns:
        El flotante capturado dentro del rango.
    """
    while True:
        valor = leer_flotante(etiqueta, imprimir_echo=False)
        if menor_inclusive <= valor <= mayor_inclusive:
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        imprimir_error(f"Debe ingresar un flotante entre {menor_inclusive} y {mayor_inclusive}.")


def leer_flotante_opcional(mensaje: str, valor_actual: float) -> float:
    """Lee un flotante editable; vacio conserva el valor actual.

    Args:
        mensaje: Etiqueta de lectura.
        valor_actual: Valor retornado cuando la entrada queda vacia.

    Returns:
        Un flotante nuevo o el valor actual.
    """
    while True:
        texto = leer_texto(f"{mensaje} [{valor_actual}]", False, False).strip()
        if texto == '':
            return valor_actual
        try:
            return float(texto)
        except ValueError:
            imprimir_error('Debe digitar un numero valido')


def leer_entero_opcional(mensaje: str, valor_actual: int) -> int:
    """Lee un entero editable; vacio conserva el valor actual.

    Args:
        mensaje: Etiqueta de lectura.
        valor_actual: Valor retornado cuando la entrada queda vacia.

    Returns:
        Un entero nuevo o el valor actual.
    """
    while True:
        texto = leer_texto(f"{mensaje} [{valor_actual}]", False, False).strip()
        if texto == '':
            return valor_actual
        try:
            return int(texto)
        except ValueError:
            imprimir_error('Debe digitar un numero entero valido')


def leer_booleano_opcional(mensaje: str, valor_actual: bool) -> bool:
    """Lee un booleano editable; vacio conserva el valor actual.

    Args:
        mensaje: Etiqueta de lectura.
        valor_actual: Valor retornado cuando la entrada queda vacia.

    Returns:
        Un booleano nuevo o el valor actual.
    """
    valores_verdaderos = {"si", "sí", "s", "true", "1", "y", "yes"}
    valores_falsos = {"no", "n", "false", "0"}

    while True:
        texto = leer_texto(f"{mensaje} [{valor_actual}]", False, False).strip().lower()
        if texto == '':
            return valor_actual
        if texto in valores_verdaderos:
            return True
        if texto in valores_falsos:
            return False
        imprimir_error('Debe digitar un valor booleano valido (si/no)')


def leer_texto_opcional(mensaje: str, valor_actual: str) -> str:
    """Lee un texto editable; vacio conserva el valor actual.

    Args:
        mensaje: Etiqueta de lectura.
        valor_actual: Valor retornado cuando la entrada queda vacia.

    Returns:
        Un texto nuevo o el valor actual.
    """
    texto = leer_texto(f"{mensaje} [{valor_actual}]", False, False).strip()
    return valor_actual if texto == '' else texto


def mostrar_menu(
    titulo_menu: str,
    opciones: list[str],
    etiqueta_salir: str = "Salir",
    ancho_titulo: int = 60,
    etiqueta_lectura: str = "Digite opcion",
) -> int:
    """Muestra un menu numerado y devuelve la opcion elegida.

    El indice inicia en 1 para las opciones de la lista y siempre incluye
    la opcion 0 para salir (o etiqueta equivalente).

    Args:
        titulo_menu: Titulo decorado del menu.
        opciones: Lista de opciones del menu.
        etiqueta_salir: Etiqueta para la opcion 0.
        ancho_titulo: Ancho minimo usado al imprimir el titulo.
        etiqueta_lectura: Etiqueta usada para solicitar la opcion.

    Returns:
        La opcion seleccionada dentro del rango 0..len(opciones).
    """
    imprimir_titulo_decorado(titulo_menu, ancho_titulo)
    for indice, opcion in enumerate(opciones, start=1):
        print('{:4d} - {:40}'.format(indice, opcion))
    print('{:4d} - {:40}'.format(0, etiqueta_salir))
    return leer_rango_enteros(f"{etiqueta_lectura}: ", 0, len(opciones))


