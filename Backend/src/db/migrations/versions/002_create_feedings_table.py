# 📁 backend/src/db/migrations/versions/002_create_feedings_table.py
"""Create feedings table

Revision ID: xxxx
Revises: previous_migration
Create Date: 2024-01-01 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = 'previous_migration'
branch_labels = None
depends_on = None

def upgrade():
    # Create enum types
    feeding_type = postgresql.ENUM(
        'breast_milk', 'formula', 'solid_food', 'water', 'mixed',
        name='feedingtype'
    )
    feeding_type.create(op.get_bind())
    
    breastside = postgresql.ENUM(
        'left', 'right', 'both', 'not_applicable',
        name='breastside'
    )
    breastside.create(op.get_bind())
    
    solidfoodtype = postgresql.ENUM(
        'puree', 'cereals', 'fruits', 'vegetables', 'meat', 'fish', 'dairy', 'other',
        name='solidfoodtype'
    )
    solidfoodtype.create(op.get_bind())
    
    # Create table
    op.create_table('feedings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('baby_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('type', feeding_type, nullable=False),
        sa.Column('start_time', sa.DateTime(), nullable=False),
        sa.Column('end_time', sa.DateTime(), nullable=True),
        sa.Column('duration_minutes', sa.Integer(), nullable=True),
        sa.Column('quantity_ml', sa.Float(), nullable=True),
        sa.Column('quantity_grams', sa.Float(), nullable=True),
        sa.Column('breast_side', breastside, nullable=True),
        sa.Column('breast_empty', sa.Boolean(), nullable=True),
        sa.Column('solid_food_type', solidfoodtype, nullable=True),
        sa.Column('food_name', sa.String(length=255), nullable=True),
        sa.Column('formula_brand', sa.String(length=100), nullable=True),
        sa.Column('formula_type', sa.String(length=100), nullable=True),
        sa.Column('water_ml', sa.Float(), nullable=True),
        sa.Column('formula_scoops', sa.Integer(), nullable=True),
        sa.Column('notes', sa.String(length=1000), nullable=True),
        sa.Column('was_refused', sa.Boolean(), nullable=True),
        sa.Column('vomiting', sa.Boolean(), nullable=True),
        sa.Column('reflux', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['baby_id'], ['babies.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feedings_baby_id'), 'feedings', ['baby_id'], unique=False)
    op.create_index(op.f('ix_feedings_id'), 'feedings', ['id'], unique=False)
    op.create_index(op.f('ix_feedings_start_time'), 'feedings', ['start_time'], unique=False
