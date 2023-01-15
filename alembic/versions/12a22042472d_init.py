"""init

Revision ID: 12a22042472d
Revises: 3c6b49e59e8d
Create Date: 2023-01-15 19:08:15.794242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12a22042472d'
down_revision = '3c6b49e59e8d'
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