"""Added score field

Revision ID: 7d328e988377
Revises: e8282244a701
Create Date: 2021-11-27 01:15:33.740169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d328e988377'
down_revision = 'e8282244a701'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'score')
    # ### end Alembic commands ###
