"""Обновил дефолтный тип editDatе

Revision ID: 67cfd20f167f
Revises: f4cdf15f954f
Create Date: 2022-06-21 19:05:51.323357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cfd20f167f'
down_revision = 'f4cdf15f954f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'isRead',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'isRead',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
