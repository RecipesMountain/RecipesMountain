"""first revision

Revision ID: e1d5e99cfb13
Revises: 
Create Date: 2021-11-18 17:20:01.952896

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "e1d5e99cfb13"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True),
        sa.Column("full_name", sa.String(), nullable=False, index=True),
        sa.Column("email", sa.String(), nullable=False, unique=True, index=True),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("is_superuser", sa.Boolean, nullable=False, default=False),
    )


def downgrade():
    op.drop_table("users")
