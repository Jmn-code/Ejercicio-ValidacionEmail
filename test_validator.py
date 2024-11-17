import sys
import os

import unittest
from emails.validator import EmailValidator

class TestValidadorEmail(unittest.TestCase):
    def setUp(self):
        # Inicializa una instancia del validador
        self.validador = EmailValidator()

    def test_correo_valido_individual(self):
        # Prueba un único correo válido
        self.assertTrue(
            self.validador.validar("ejemplo@correo.com"),
            "El correo válido 'ejemplo@correo.com' no pasó la validación."
        )

    def test_correo_invalido_individual(self):
        # Prueba un único correo inválido
        self.assertFalse(
            self.validador.validar("correo_invalido.com"),
            "El correo inválido 'correo_invalido.com' pasó la validación."
        )

    def test_correos_validos(self):
        # Prueba múltiples correos válidos
        correos_validos = [
            "usuario.nombre@dominio.com",
            "simple@correo.co",
            "usuario-alias@sub.dominio.org",
        ]
        for correo in correos_validos:
            with self.subTest(correo=correo):
                self.assertTrue(
                    self.validador.validar(correo),
                    f"El correo válido '{correo}' no pasó la validación."
                )

    def test_correos_invalidos(self):
        # Prueba múltiples correos inválidos
        correos_invalidos = [
            "sinarroba.com",
            "usuario@dominio..com",
            "usuario@.com",
            "@dominio.com",
        ]
        for correo in correos_invalidos:
            with self.subTest(correo=correo):
                self.assertFalse(
                    self.validador.validar(correo),
                    f"El correo no válido '{correo}' pasó la validación."
                )

    def test_casos_especiales(self):
        # Prueba casos límite
        casos_especiales = [
            ("@dominio.com", False, "Falta el nombre de usuario"),
            ("usuario@dominio", False, "Falta el TLD"),
            (".usuario@dominio.com", False, "El usuario comienza con un punto"),
            ("usuario@dominio..com", False, "El dominio contiene doble punto"),
            ("usuario_valido@dominio.com", True, "Correo válido"),
        ]
        for correo, esperado, descripcion in casos_especiales:
            with self.subTest(correo=correo, descripcion=descripcion):
                self.assertEqual(
                    self.validador.validar(correo),
                    esperado,
                    f"Fallo en el caso: {descripcion} para '{correo}'"
                )

    def test_cadena_vacia_y_nula(self):
        # Prueba de cadenas vacías y valores nulos
        self.assertFalse(
            self.validador.validar(""),
            "Se permitió una cadena vacía como correo válido."
        )
        with self.assertRaises(TypeError, msg="El valor 'None' fue aceptado como correo válido."):
            self.validador.validar(None)

if __name__ == "__main__":
    unittest.main()
