import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Union
import sys
import os

APP_DIR = Path(__file__).parent.parent.resolve()
base_dir = os.path.abspath(os.getcwd())


class CustomFormatter(logging.Formatter):
    def format(self, record):
        full_path = record.pathname
        relative_path = os.path.relpath(full_path, base_dir)
        record.pathname = relative_path
        return super().format(record)


def setup_logger(
    name: str = 'bunker',
    log_level: int = logging.DEBUG,
    log_to_file: Union[str, None] = None,
) -> logging.Logger:
    logger = logging.getLogger(name=name)
    logger.setLevel(log_level)

    log_format = CustomFormatter(
        '%(asctime)s | %(pathname)s | %(funcName)s - %(lineno)d | %(levelname)s | %(message)s', '%m-%d-%Y %H:%M:%S' # noqa
    )

    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setFormatter(log_format)

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    logger.propagate = False

    logger.addHandler(stdout_handler)

    if log_to_file:
        path = Path(APP_DIR / log_to_file).resolve().parent
        path.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(
            log_to_file,
            maxBytes=1000000,
            backupCount=1,
        )
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    telegram_logger = logging.getLogger("httpx")
    telegram_logger.setLevel(logging.WARNING)

    return logger
