
from logging.config import fileConfig
from pathlib import Path
import sys

from alembic import context
from sqlalchemy import engine_from_config, pool

# Añadir backend a las rutas de importación de Python.
# Esto permite importar el paquete app al ejecutar Alembic desde la raíz.
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))

from app.config import settings
from app.database import Base
from app.models.business import Business

# Configuración principal de Alembic.
config = context.config

# Cargar la configuración de logging definida en alembic.ini.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Obtener los metadatos de SQLAlchemy.
# Alembic los utilizará más adelante para detectar cambios en los modelos.
target_metadata = Base.metadata

# Leer la URL desde .env, sin guardar credenciales en alembic.ini.
# Duplicar % evita problemas con la interpolación de ConfigParser.
config.set_main_option(
    "sqlalchemy.url",
    settings.database_url.replace("%", "%%"),
)


def run_migrations_offline() -> None:
    """Preparar migraciones sin abrir una conexión directa."""
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecutar migraciones utilizando una conexión a la base de datos."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    try:
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                compare_type=True,
            )

            with context.begin_transaction():
                context.run_migrations()
    finally:
        connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

