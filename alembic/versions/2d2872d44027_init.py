"""init

Revision ID: 2d2872d44027
Revises: 
Create Date: 2023-01-05 19:04:10.458467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d2872d44027'
down_revision = None
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
