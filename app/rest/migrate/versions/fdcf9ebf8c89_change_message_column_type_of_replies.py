"""change message column type of replies

Revision ID: fdcf9ebf8c89
Revises: 60e230cb9b17
Create Date: 2016-09-15 16:01:56.378347

"""

# revision identifiers, used by Alembic.
revision = 'fdcf9ebf8c89'
down_revision = '60e230cb9b17'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        table_name='replies',
        column_name='message',
        type_=sa.Text
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        table_name='replies',
        column_name='message',
        type_=sa.String(1000)
    )
    ### end Alembic commands ###
