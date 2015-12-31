"""init migration

Revision ID: 1c02358c36ce
Revises: None
Create Date: 2015-12-30 21:24:18.316000

"""

# revision identifiers, used by Alembic.
revision = '1c02358c36ce'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attentactivitys', sa.Column('state', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attentactivitys', 'state')
    ### end Alembic commands ###