"""Remove username unique constraint

Revision ID: e948b90172ab
Revises: 9503a8aea135
Create Date: 2019-06-06 23:46:09.743975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e948b90172ab"
down_revision = "9503a8aea135"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("unique_user_username", "user", type_="unique")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("unique_user_username", "user", ["username"])
    # ### end Alembic commands ###
