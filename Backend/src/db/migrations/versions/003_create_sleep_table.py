# 📁 backend/src/db/migrations/versions/003_create_sleep_table.py
"""Create sleep_sessions table

Revision ID: xxxx
Revises: previous_migration
Create Date: 2024-01-01 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'xxxx'
down_revision = 'previous_migration'
branch_labels = None
depends_on = None

def upgrade():
    # Create enum types
    sleeptype = postgresql.ENUM(
        'nap', 'night_sleep', 'bedtime', 'wakeup',
        name='sleeptype'
    )
    sleeptype.create(op.get_bind())
    
    sleepquality = postgresql.ENUM(
        'excellent', 'good', 'fair', 'poor', 'restless',
        name='sleepquality'
    )
    sleepquality.create(op.get_bind())
    
    sleepenvironment = postgresql.ENUM(
        'crib', 'bassinet', 'parent_bed', 'swing', 'car_seat', 'stroller', 'other',
        name='sleepenvironment'
    )
    sleepenvironment.create(op.get_bind())
    
    # Create table
    op.create_table('sleep_sessions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('baby_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('type', sleeptype, nullable=False),
        sa.Column('start_time', sa.DateTime(), nullable=False),
        sa.Column('end_time', sa.DateTime(), nullable=True),
        sa.Column('duration_minutes', sa.Integer(), nullable=True),
        sa.Column('quality', sleepquality, nullable=True),
        sa.Column('environment', sleepenvironment, nullable=True),
        sa.Column('room_temperature', sa.Float(), nullable=True),
        sa.Column('was_swaddled', sa.Boolean(), nullable=True),
        sa.Column('used_white_noise', sa.Boolean(), nullable=True),
        sa.Column('used_pacifier', sa.Boolean(), nullable=True),
        sa.Column('sleep_position', sa.String(length=50), nullable=True),
        sa.Column('wakeups_count', sa.Integer(), nullable=True),
        sa.Column('longest_stretch_minutes', sa.Integer(), nullable=True),
        sa.Column('fed_before_sleep', sa.Boolean(), nullable=True),
        sa.Column('feeding_minutes_before', sa.Integer(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('dreams_observed', sa.Boolean(), nullable=True),
        sa.Column('snoring', sa.Boolean(), nullable=True),
        sa.Column('breathing_issues', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['baby_id'], ['babies.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sleep_sessions_baby_id'), 'sleep_sessions', ['baby_id'], unique=False)
    op.create_index(op.f('ix_sleep_sessions_id'), 'sleep_sessions', ['id'], unique=False)
    op.create_index(op.f('ix_sleep_sessions_start_time'), 'sleep_sessions', ['start_time'], unique=False)
    op.create_index(op.f('ix_sleep_sessions_user_id'), 'sleep_sessions', ['user_id'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_sleep_sessions_user_id'), table_name='sleep_sessions')
    op.drop_index(op.f('ix_sleep_sessions_start_time'), table_name='sleep_sessions')
    op.drop_index(op.f('ix_sleep_sessions_id'), table_name='sleep_sessions')
    op.drop_index(op.f('ix_sleep_sessions_baby_id'), table_name='sleep_sessions')
    op.drop_table('sleep_sessions')
    
    # Drop enum types
    op.execute('DROP TYPE sleeptype')
    op.execute('DROP TYPE sleepquality')
    op.execute('DROP TYPE sleepenvironment')
