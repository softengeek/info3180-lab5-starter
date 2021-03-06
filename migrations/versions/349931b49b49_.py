"""empty message

Revision ID: 349931b49b49
Revises: bd6dddedfab5
Create Date: 2017-02-25 21:58:23.913859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349931b49b49'
down_revision = 'bd6dddedfab5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
