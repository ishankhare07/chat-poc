"""add user details

Revision ID: 28f60d1d0a71
Revises: 
Create Date: 2016-09-02 11:19:46.946301

"""

# revision identifiers, used by Alembic.
revision = '28f60d1d0a71'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    ### end Alembic commands ###
