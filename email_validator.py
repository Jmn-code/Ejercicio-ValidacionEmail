import re
import logging
import os

class EmailValidator:
    def __init__(self):
        """
        Inicializa el validador 
        """
        # Expresión regular para validar correos electrónicos
        self.regex = re.compile(
            r'^[A-Za-z0-9]+[._-]*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$'
        )

        # Crear carpeta de logs si no existe
        os.makedirs("logs", exist_ok=True)

        # Configuración del logger
        self.logger = logging.getLogger("EmailValidator")
        self.logger.setLevel(logging.DEBUG)

        # Configuración de un handler para archivo
        file_handler = logging.FileHandler("logs/validation.log")
        file_handler.setLevel(logging.INFO)

        # Configuración de un handler para consola
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.WARNING)

        # Formato para los logs
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Asignar handlers al logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def validar(self, correo: str) -> bool:
        """
        Valida un correo electrónico 
        Registra los resultados en el logger.
        
        :param correo: Correo electrónico a validar.
        :return: True si si, False si no.
        """
        try:
            if not correo:
                raise ValueError("El correo está vacío o es nulo.")

            if re.fullmatch(self.regex, correo):
                self.logger.info(f"Correo válido: {correo}")
                return True
            else:
                raise ValueError(f"Correo inválido: '{correo}' incumple las reglas.")

        except ValueError as e:
            self.logger.error(str(e))
            return False
        except Exception as e:
            self.logger.exception(f"Error inesperado '{correo}': {e}")
            return False
