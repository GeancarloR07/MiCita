
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    """Representa una cuenta de usuario global en TurnoPro."""

    __tablename__ = "users"

    # Identificador único de la persona.
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    # Nombre que se mostrará en la plataforma.
    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    # Correo único para identificar la cuenta.
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    # Aquí se almacenará un hash seguro, nunca la contraseña original.
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Permite desactivar una cuenta sin eliminarla.
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )

    # Fecha y hora de creación generada por PostgreSQL.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
