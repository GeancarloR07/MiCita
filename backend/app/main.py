
from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title="TurnoPro API",
    description="API para la gestión de citas de múltiples negocios.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    """Devuelve información básica de la API."""
    return {
        "message": "Bienvenido a TurnoPro",
        "status": "running",
        "environment": settings.app_env,
    }


@app.get("/health")
def health_check():
    """Comprueba que la API responde."""
    return {"status": "ok"}
