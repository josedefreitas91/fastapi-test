from typing import Any
import logging

def get_logger(file_name: str) -> Any:
    logging.basicConfig(
        filename=f"./app/logs/{file_name}.log",
        level=logging.WARNING,
        format="[%(asctime)s] [%(levelname)s] %(message)s"
        # format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    )
    return logging.getLogger(__name__)

class Logger():
    def __init__(self, APP_NAME: str, logger_name: str) -> None:
        self.APP_NAME = APP_NAME
        self.logger = get_logger(logger_name)
        
    
    def info(self, message: str) -> None:
        self.logger.info(f'[{self.APP_NAME}] {message}')
    
    
    def warning(self, message: str) -> None:
        self.logger.warning(f'[{self.APP_NAME}] {message}')
        
        
    def error(self, message: str) -> None:
        self.logger.error(f'[{self.APP_NAME}] {message}')