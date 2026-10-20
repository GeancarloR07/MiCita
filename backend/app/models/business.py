
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Business(Base):
    """Representa un negocio registrado en TurnoPro."""

    __tablename__ = "businesses"

    # Identificador único del negocio.
    id: Mapped[int] = mapped_column(
    primary_key=True,
)
    
    

    # Nombre comercial del negocio.
    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    # Correo de contacto del negocio.
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    # Indica si el negocio está activo en la plataforma.
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    # Fecha y hora de creación del registro.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
