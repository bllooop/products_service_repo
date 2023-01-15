"""init

Revision ID: 3c6b49e59e8d
Revises: 2d2872d44027
Create Date: 2023-01-05 19:12:14.337603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c6b49e59e8d'
down_revision = '2d2872d44027'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'product',
        sa.Column('id',sa.Integer, primary_key=True, index=True),
        sa.Column('name',sa.String),
        sa.Column('price',sa.String),
        sa.Column('shopid',sa.String)

    )

def downgrade() -> None:
    op.drop_table('product')