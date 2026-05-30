import io
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from colorama import Fore

from eii_utils.inputs import (
    leer_booleano,
    leer_booleano_opcional,
    leer_entero,
    leer_entero_opcional,
    leer_flotante_opcional,
    leer_rango_enteros,
    leer_texto,
    leer_texto_opcional,
    mostrar_menu,
)
from eii_utils.outputs import (
    generar_titulo_decorado,
    imprimir_advertencia,
    imprimir_echo,
    imprimir_error,
    imprimir_mensaje,
    imprimir_titulo_decorado,
    limpiar_consola,
    pausar,
)


class TestInputs(unittest.TestCase):
    @patch("builtins.input", side_effect=["abc", "15"])
    def test_leer_entero_reintenta_hasta_valido(self, _mock_input):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            valor = leer_entero("Edad")
        self.assertEqual(valor, 15)
        self.assertIn(Fore.RED, buffer.getvalue())
        self.assertIn(Fore.GREEN, buffer.getvalue())

    @patch("builtins.input", side_effect=["", "Ana"])
    def test_leer_texto_obligatorio_muestra_advertencia(self, _mock_input):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            valor = leer_texto("Nombre")
        self.assertEqual(valor, "Ana")
        self.assertIn(Fore.YELLOW, buffer.getvalue())

    @patch("builtins.input", side_effect=["tal vez", "sí"])
    def test_leer_booleano(self, _mock_input):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            valor = leer_booleano("Activo")
        self.assertTrue(valor)
        self.assertIn(Fore.RED, buffer.getvalue())

    @patch("builtins.input", side_effect=["100", "10"])
    def test_leer_rango_enteros(self, _mock_input):
        valor = leer_rango_enteros("Nota", 0, 20, imprimir_echo=False)
        self.assertEqual(valor, 10)

    @patch("builtins.input", side_effect=["", "nuevo"])
    def test_leer_texto_opcional(self, _mock_input):
        self.assertEqual(leer_texto_opcional("Nombre", "actual"), "actual")
        self.assertEqual(leer_texto_opcional("Nombre", "actual"), "nuevo")

    @patch("builtins.input", side_effect=["", "42", "abc", "3.5"])
    def test_leer_numericos_opcionales(self, _mock_input):
        self.assertEqual(leer_entero_opcional("Edad", 20), 20)
        self.assertEqual(leer_entero_opcional("Edad", 20), 42)
        self.assertEqual(leer_flotante_opcional("Promedio", 2.0), 3.5)

    @patch("builtins.input", side_effect=[""])
    def test_leer_entero_opcional_muestra_valor_actual_en_prompt(self, mock_input):
        valor = leer_entero_opcional("Edad", 78)
        self.assertEqual(valor, 78)
        mock_input.assert_called_once_with("Edad [78]: ")

    @patch("builtins.input", side_effect=["", "si", "tal vez", "no"])
    def test_leer_booleano_opcional(self, _mock_input):
        self.assertTrue(leer_booleano_opcional("Activo", True))
        self.assertTrue(leer_booleano_opcional("Activo", False))
        self.assertFalse(leer_booleano_opcional("Activo", True))

    @patch("builtins.input", side_effect=["3", "2"])
    def test_mostrar_menu(self, _mock_input):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            opcion = mostrar_menu("Menu principal", ["A", "B"], etiqueta_salir="Volver")
        salida = buffer.getvalue()
        self.assertEqual(opcion, 2)
        self.assertIn("MENU PRINCIPAL", salida)
        self.assertIn("   1 - A", salida)
        self.assertIn("   0 - Volver", salida)


class TestOutputs(unittest.TestCase):
    @patch("eii_utils.outputs.os.system")
    def test_limpiar_consola(self, mock_system):
        limpiar_consola()
        mock_system.assert_called_once_with("cls" if os.name == "nt" else "clear")

    def test_imprimir_titulo_decorado(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            imprimir_titulo_decorado("hola", largo=8)
        salida = buffer.getvalue().strip().splitlines()
        self.assertEqual(salida[0], "********")
        self.assertEqual(salida[1], "**HOLA**")
        self.assertEqual(salida[2], "********")

    def test_generar_titulo_decorado(self):
        salida = generar_titulo_decorado("hola", largo=8).splitlines()
        self.assertEqual(salida[0], "********")
        self.assertEqual(salida[1], "**HOLA**")
        self.assertEqual(salida[2], "********")

    def test_imprimir_mensaje(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            imprimir_mensaje("Correcto")
            imprimir_mensaje("Error", es_error=True)
        salida = buffer.getvalue()
        self.assertIn(Fore.GREEN, salida)
        self.assertIn(Fore.RED, salida)
        self.assertIn("✔ Correcto", salida)
        self.assertIn("✖ Error", salida)

    def test_imprimir_metodos_publicos(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            imprimir_error("error")
            imprimir_advertencia("ojo")
            imprimir_echo("Edad", 18)
        salida = buffer.getvalue()
        self.assertIn(Fore.RED, salida)
        self.assertIn(Fore.YELLOW, salida)
        self.assertIn(Fore.GREEN, salida)

    @patch("builtins.input", return_value="")
    def test_pausar(self, _mock_input):
        pausar()
        _mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main()
