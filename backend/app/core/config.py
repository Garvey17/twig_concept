from pydantic_settings import  BaseSettings, SettingsConfigDict
from pathlib import Path
import logging

class Setings(BaseSettings):
    openai_api_key: str
    openai_model: str
    embedding_model: str
    github_webhook_secret: str
    github_app_id: int
    github_private_key_path: str
    qdrant_url: str
    qdrant_api_key: str
    qdrant_collection_name: str


    model_config = SettingsConfigDict(env_file=".env")

    @property
    def github_private_key(self) -> str:
        """Reads the private key path and returns the path"""
        return Path(self.github_private_key_path).read_text

settings = Setings()

def setup_logging() ->  None:
    """Basic standard logging configuration"""

    logging.basicConfig(
        level= logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    #Reduce noise from chatty libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    # logging.getLogger("google").setLevel(logging.WARNING)

def get_logger(name: str) -> logging.Logger:
    """Retrieve logger"""
    return logging.getLogger(name)