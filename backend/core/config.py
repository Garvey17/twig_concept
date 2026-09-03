from pydantic_settings import  BaseSettings
import logging

class config(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"


def setup_logging() ->  None:
    """Basic standard logging configuration"""

    logging.basicConfig(
        level= logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    #Reduce noise from chatty libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("google").setLevel(logging.WARNING)

def get_logger(name: str) -> logging.Logger:
    """Retrieve logger"""
    return logging.getLogger(name)