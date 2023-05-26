"""example table

Revision ID: d89cc55295ec
Revises: 
Create Date: 2023-05-25 21:20:51.061155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd89cc55295ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('example_table',
    sa.Column('test_field', sa.Integer(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('test_field', name=op.f('example_table_pkey'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('example_table')
    # ### end Alembic commands ###
