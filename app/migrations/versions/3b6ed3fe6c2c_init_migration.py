"""init migration

Revision ID: 3b6ed3fe6c2c
Revises: 2c333341bcb8
Create Date: 2015-12-26 09:47:46.810000

"""

# revision identifiers, used by Alembic.
revision = '3b6ed3fe6c2c'
down_revision = '2c333341bcb8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activitys', sa.Column('likenumber', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('timestamp', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'timestamp')
    op.drop_column('activitys', 'likenumber')
    ### end Alembic commands ###
