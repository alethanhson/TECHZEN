"""seed_roles_and_users

Revision ID: ad5c96af6c2c
Revises: 4e545b5645c0
Create Date: 2026-04-01 05:44:27.737343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad5c96af6c2c'
down_revision: Union[str, Sequence[str], None] = '4e545b5645c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Insert roles
    op.bulk_insert(
        sa.table(
            "roles",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("name", sa.String()),
            sa.Column("description", sa.String()),
        ),
        [
            {"id": 1, "name": "admin", "description": "Administrator with full access"},
            {"id": 2, "name": "user", "description": "Regular user with limited access"},
        ],
    )

    # Insert users
    op.bulk_insert(
        sa.table(
            "users",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("username", sa.String()),
            sa.Column("email", sa.String()),
            sa.Column("hashed_password", sa.String()),
            sa.Column("is_active", sa.Boolean()),
            sa.Column("role_id", sa.Integer()),
        ),
        [
            {
                "id": 1,
                "username": "admin_techzen",
                "email": "admin@techzen.com",
                "hashed_password": "$2b$12$FFdbZixSNaJlOrYv7kIRXedkx7NQVeSkBpVsE/MmgUGcUL/ucW7mW",
                "is_active": True,
                "role_id": 1,
            },
            {
                "id": 2,
                "username": "user_techzen",
                "email": "user@techzen.com",
                "hashed_password": "$2b$12$FFdbZixSNaJlOrYv7kIRXedkx7NQVeSkBpVsE/MmgUGcUL/ucW7mW",
                "is_active": True,
                "role_id": 2,
            },
        ],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM users WHERE id IN (1, 2)")
    op.execute("DELETE FROM roles WHERE id IN (1, 2)")
