import logging
from pathlib import Path


class AcessLogger:
    def __init__(self):

        self.logger = logging.getLogger("Acessibilidade")
        self.logger.setLevel(logging.DEBUG)

        # Formato
        self.formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
        )

        # Registro de log - salvando também
        log_path_dir = self.logger_dir()
        self.file_handler = logging.FileHandler(
            log_path_dir / "sistema.log", encoding="utf-8"
        )
        self.file_handler.setLevel(logging.ERROR)
        self.file_handler.setFormatter(self.formatter)

        # Terminal
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.INFO)
        self.console_handler.setFormatter(self.formatter)

        # Add
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    def logger_dir(self) -> Path:
        base_dir = Path(__file__).parent.parent.parent
        log_path = base_dir / Path("logs")

        log_path.mkdir(parents=True, exist_ok=True)

        return log_path
