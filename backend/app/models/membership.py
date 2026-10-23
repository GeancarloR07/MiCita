
from datetime import datetime
from enum import StrEnum

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class MembershipRole(StrEnum):
    """Roles disponibles dentro de un negocio."""

    OWNER = "owner"
    ADMIN = "admin"
    RECEPTIONIST = "receptionist"
    PROFESSIONAL = "professional"


class MembershipStatus(StrEnum):
    """Estados posibles de una pertenencia."""

    PENDING = "pending"
    ACTIVE = "active"
    SUSPENDED = "suspended"


class BusinessMembership(Base):
    """Representa la pertenencia de un usuario a un negocio."""

    __tablename__ = "business_memberships"

    # Reglas que PostgreSQL debe hacer cumplir.
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "business_id",
            name="uq_membership_user_business",
        ),
        CheckConstraint(
            "role IN ('owner', 'admin', 'receptionist', 'professional')",
            name="ck_membership_valid_role",
        ),
        CheckConstraint(
            "status IN ('pending', 'active', 'suspended')",
            name="ck_membership_valid_status",
        ),
    )

    # Identificador único de la pertenencia.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Usuario al que pertenece esta relación.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    # Negocio al que pertenece el usuario.
    business_id: Mapped[int] = mapped_column(
        ForeignKey("businesses.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    # Rol del usuario dentro de este negocio.
    role: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    # Una pertenencia nueva comienza pendiente.
    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default=MembershipStatus.PENDING.value,
        server_default=MembershipStatus.PENDING.value,
    )

    # Fecha y hora de creación generada por PostgreSQL.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
