
"""add membership role and status constraints

Revision ID: 00bcbba48cda
Revises: 401b09fdc1af
"""

from typing import Sequence, Union

from alembic import op


revision: str = "00bcbba48cda"
down_revision: Union[str, Sequence[str], None] = "401b09fdc1af"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Añadir restricciones para roles y estados válidos."""

    op.create_check_constraint(
        "ck_membership_valid_role",
        "business_memberships",
        "role IN ('owner', 'admin', 'receptionist', 'professional')",
    )

    op.create_check_constraint(
        "ck_membership_valid_status",
        "business_memberships",
        "status IN ('pending', 'active', 'suspended')",
    )


def downgrade() -> None:
    """Eliminar las restricciones si se revierte la migración."""

    op.drop_constraint(
        "ck_membership_valid_status",
        "business_memberships",
        type_="check",
    )

    op.drop_constraint(
        "ck_membership_valid_role",
        "business_memberships",
        type_="check",
    )
