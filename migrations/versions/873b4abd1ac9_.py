"""empty message

Revision ID: 873b4abd1ac9
Revises: 
Create Date: 2021-03-06 14:35:43.422323

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '873b4abd1ac9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audiobook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('narrator', sa.String(length=100), nullable=False),
    sa.Column('duration_seconds', sa.Integer(), nullable=False),
    sa.Column('upload_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('podcast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('duration_seconds', sa.Integer(), nullable=False),
    sa.Column('upload_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('host', sa.String(length=100), nullable=False),
    sa.Column('participants', postgresql.ARRAY(sa.String(), dimensions=1), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('duration_seconds', sa.Integer(), nullable=False),
    sa.Column('upload_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    op.drop_table('podcast')
    op.drop_table('audiobook')
    # ### end Alembic commands ###