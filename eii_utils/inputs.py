from colorama import Fore


def _imprimir_error(mensaje: str) -> None:
    print(f"{Fore.RED}✖ {mensaje}")


def _imprimir_advertencia(mensaje: str) -> None:
    print(f"{Fore.YELLOW}⚠ {mensaje}")


def _imprimir_echo(etiqueta: str, valor, imprimir_echo: bool) -> None:
    if imprimir_echo:
        print(f"{Fore.GREEN}✔ {etiqueta}: {valor}")


def leer_entero(etiqueta: str, imprimir_echo: bool = True) -> int:
    while True:
        entrada = input(f"{etiqueta}: ")
        try:
            valor = int(entrada)
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        except ValueError:
            _imprimir_error("Debe ingresar un número entero válido.")


def leer_flotante(etiqueta: str, imprimir_echo: bool = True) -> float:
    while True:
        entrada = input(f"{etiqueta}: ")
        try:
            valor = float(entrada)
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        except ValueError:
            _imprimir_error("Debe ingresar un número flotante válido.")


def leer_texto(etiqueta: str, es_obligatorio: bool = True, imprimir_echo: bool = True) -> str:
    while True:
        valor = input(f"{etiqueta}: ").strip()
        if es_obligatorio and not valor:
            _imprimir_advertencia("El texto es obligatorio y no puede estar vacío.")
            continue
        _imprimir_echo(etiqueta, valor, imprimir_echo)
        return valor


def leer_booleano(etiqueta: str, imprimir_echo: bool = True) -> bool:
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
        _imprimir_error("Debe ingresar un valor booleano válido (sí/no).")


def leer_rango_enteros(
    etiqueta: str,
    menor_inclusive: int,
    mayor_inclusive: int,
    imprimir_echo: bool = True,
) -> int:
    while True:
        valor = leer_entero(etiqueta, imprimir_echo=False)
        if menor_inclusive <= valor <= mayor_inclusive:
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        _imprimir_error(f"Debe ingresar un entero entre {menor_inclusive} y {mayor_inclusive}.")


def leer_rango_flotante(
    etiqueta: str,
    menor_inclusive: float,
    mayor_inclusive: float,
    imprimir_echo: bool = True,
) -> float:
    while True:
        valor = leer_flotante(etiqueta, imprimir_echo=False)
        if menor_inclusive <= valor <= mayor_inclusive:
            _imprimir_echo(etiqueta, valor, imprimir_echo)
            return valor
        _imprimir_error(f"Debe ingresar un flotante entre {menor_inclusive} y {mayor_inclusive}.")
