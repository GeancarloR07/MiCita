
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Obtener la carpeta raíz del proyecto MiCita.
# Este archivo está dentro de backend/app/.
PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """Configuración central de la aplicación."""

    app_env: str = "development"
    api_host: str = "127.0.0.1"
    api_port: int = 8000

    # Se obtiene del archivo .env; no guardamos la URL aquí.
    database_url: str

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Crear una instancia para reutilizar la configuración.
settings = Settings()
