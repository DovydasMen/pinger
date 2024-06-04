import logging
from logging import FileHandler, Formatter

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO

LOG_TO_FILE = "data.log"
file_logger = logging.getLogger("File logger")
file_logger.setLevel(LOG_LEVEL)
file_handler = FileHandler(LOG_TO_FILE)
file_formatter = Formatter(LOG_FORMAT)
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)