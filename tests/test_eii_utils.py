import io
import os
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from colorama import Fore

from eii_utils.inputs import leer_booleano, leer_entero, leer_rango_enteros, leer_texto
from eii_utils.outputs import limpiar_consola, imprimir_mensaje, imprimir_titulo_decorado


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


if __name__ == "__main__":
    unittest.main()
