"""Database

Revision ID: 7a4c09d987fa
Revises: 
Create Date: 2021-11-24 13:07:42.535579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a4c09d987fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('actor_id')
    )
    op.create_table('director',
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('director_id')
    )
    op.create_table('movie',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.Text(), nullable=True),
    sa.Column('movie_genre', sa.Text(), nullable=True),
    sa.Column('movie_release_date', sa.Date(), nullable=True),
    sa.Column('movie_status', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('movie_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('booking',
    sa.Column('booking_id', sa.Integer(), nullable=False),
    sa.Column('booking_date_time', sa.Date(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Confirmation', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.movie_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('booking_id')
    )
    op.create_table('schedule',
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.movie_id'], ),
    sa.PrimaryKeyConstraint('schedule_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    op.drop_table('booking')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('movie')
    op.drop_table('director')
    op.drop_table('actor')
    # ### end Alembic commands ###