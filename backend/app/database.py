
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

# Crear el motor que administra las conexiones a PostgreSQL.
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)

# Crear sesiones para ejecutar operaciones con la base de datos.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """Clase base para los futuros modelos de SQLAlchemy."""

    pass
