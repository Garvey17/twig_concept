from fastapi import FastAPI
from app.core.config import settings, setup_logging, get_logger
from contextlib import asynccontextmanager

setup_logging()
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Starting app...')
    logger.info(f"OpenAI model: {settings.openai_model}")
    logger.info(f"Qdrant collection: {settings.qdrant_collection_name}")
    yield
    logger.info("Stopping app ...")

app = FastAPI(lifespan=lifespan)



@app.get('/health')
async def healthcheck():
    return{
        "message": "health check passed, app is healthy",
    }