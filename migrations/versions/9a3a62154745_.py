"""empty message

Revision ID: 9a3a62154745
Revises: 72e7a2838b7f
Create Date: 2021-01-09 19:46:08.115815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a3a62154745'
down_revision = '72e7a2838b7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rickshaw',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rickshaw_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rickshaw')
    # ### end Alembic commands ###
