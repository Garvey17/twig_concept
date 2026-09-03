from fastapi import FastAPI
from backend.app.core.config import config, setup_logging, get_logger
from contextlib import asynccontextmanager

setup_logging()
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Starting app...')
    yield
    logger.info("Stopping app ...")

app = FastAPI(lifespan=lifespan)



@app.get('/health')
async def healthcheck():
    return{
        "message": "health check passed, app is healthy",
    }