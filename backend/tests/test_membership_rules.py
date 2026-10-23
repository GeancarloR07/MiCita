
from app.models.membership import (
    BusinessMembership,
    MembershipRole,
    MembershipStatus,
)


def test_all_membership_roles_are_defined():
    """Comprueba que existan los cuatro roles permitidos."""

    roles = {role.value for role in MembershipRole}

    assert roles == {
        "owner",
        "admin",
        "receptionist",
        "professional",
    }


def test_all_membership_statuses_are_defined():
    """Comprueba que existan los tres estados permitidos."""

    statuses = {status.value for status in MembershipStatus}

    assert statuses == {
        "pending",
        "active",
        "suspended",
    }


def test_membership_has_unique_user_business_constraint():
    """Comprueba que no se permitan pertenencias duplicadas."""

    constraint_names = {
        constraint.name
        for constraint in BusinessMembership.__table__.constraints
    }

    assert "uq_membership_user_business" in constraint_names


def test_membership_has_role_and_status_constraints():
    """Comprueba que el modelo declare las restricciones de validación."""

    constraint_names = {
        constraint.name
        for constraint in BusinessMembership.__table__.constraints
    }

    assert "ck_membership_valid_role" in constraint_names
    assert "ck_membership_valid_status" in constraint_names


def test_membership_has_required_foreign_keys():
    """Comprueba que la pertenencia apunte a usuario y negocio."""

    foreign_keys = {
        foreign_key.target_fullname
        for foreign_key in BusinessMembership.__table__.foreign_keys
    }

    assert "users.id" in foreign_keys
    assert "businesses.id" in foreign_keys
