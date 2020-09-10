"""User notification flag

Revision ID: b5e309bfc338
Revises: 25d327218c4d
Create Date: 2019-09-30 01:32:05.649595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b5e309bfc338"
down_revision = "25d327218c4d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column("notifications", sa.Boolean(), server_default="True", nullable=False),
    )
    op.alter_column(
        "user",
        "furry",
        existing_type=sa.BOOLEAN(),
        server_default=None,
        existing_nullable=False,
    )
    op.alter_column(
        "user",
        "nsfw",
        existing_type=sa.BOOLEAN(),
        server_default=None,
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "nsfw",
        existing_type=sa.BOOLEAN(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.alter_column(
        "user",
        "furry",
        existing_type=sa.BOOLEAN(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.drop_column("user", "notifications")
    # ### end Alembic commands ###
