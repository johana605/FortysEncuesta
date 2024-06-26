"""Initial migration

Revision ID: 6bc2d7fed700
Revises: 
Create Date: 2024-05-19 19:13:54.819377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bc2d7fed700'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('satisfaction', sa.Integer(), nullable=False),
    sa.Column('recommendation', sa.String(length=3), nullable=False),
    sa.Column('product_type', sa.String(length=50), nullable=False),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('survey')
    # ### end Alembic commands ###
