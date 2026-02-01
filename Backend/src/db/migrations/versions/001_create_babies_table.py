"""
Create babies table

Revision ID: 001_babies
Revises: 000_users (dépend de la table users)
Create Date: 2026-02-01 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001_babies'
down_revision = '000_users'  # Doit pointer vers la migration qui crée la table users
branch_labels = None
depends_on = None


def upgrade():
    """
    Crée la table babies et ses index
    """
    
    # Créer l'enum pour le genre
    gender_enum = postgresql.ENUM('male', 'female', 'other', name='gender_enum')
    gender_enum.create(op.get_bind(), checkfirst=True)
    
    # Créer la table babies
    op.create_table(
        'babies',
        
        # Colonnes
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='ID unique du bébé'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='ID du parent propriétaire'),
        sa.Column('name', sa.String(length=100), nullable=False, comment='Prénom du bébé'),
        sa.Column('birth_date', sa.Date(), nullable=False, comment='Date de naissance'),
        sa.Column('gender', gender_enum, nullable=False, comment='Genre du bébé'),
        sa.Column('photo_url', sa.String(length=500), nullable=True, comment='URL de la photo de profil'),
        
        # Métadonnées
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
            comment='Date de création du profil'
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
            comment='Date de dernière modification'
        ),
        sa.Column(
            'deleted_at',
            sa.DateTime(timezone=True),
            nullable=True,
            comment='Date de suppression (soft delete)'
        ),
        
        # Contraintes
        sa.PrimaryKeyConstraint('id', name='pk_babies'),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            name='fk_babies_user_id',
            ondelete='CASCADE'  # Si l'utilisateur est supprimé, ses bébés aussi
        ),
        
        # Contraintes de validation
        sa.CheckConstraint(
            "name ~ '^[a-zA-ZÀ-ÿ\\s\\-'']+$'",
            name='ck_babies_name_valid'
        ),
        sa.CheckConstraint(
            'birth_date <= CURRENT_DATE',
            name='ck_babies_birth_date_not_future'
        ),
        sa.CheckConstraint(
            "birth_date >= CURRENT_DATE - INTERVAL '10 years'",
            name='ck_babies_birth_date_not_too_old'
        )
    )
    
    # Créer les index pour les performances
    
    # Index sur user_id (très fréquent dans les requêtes)
    op.create_index(
        'ix_babies_user_id',
        'babies',
        ['user_id'],
        unique=False
    )
    
    # Index sur birth_date (pour recherches par âge)
    op.create_index(
        'ix_babies_birth_date',
        'babies',
        ['birth_date'],
        unique=False
    )
    
    # Index composite pour requêtes fréquentes (user + actif)
    op.create_index(
        'ix_babies_user_active',
        'babies',
        ['user_id', 'deleted_at'],
        unique=False,
        postgresql_where=sa.text('deleted_at IS NULL')  # Index partiel
    )
    
    # Index pour recherche par nom (case-insensitive)
    op.execute(
        """
        CREATE INDEX ix_babies_name_lower
        ON babies (LOWER(name))
        """
    )
    
    # Index sur created_at pour tri chronologique
    op.create_index(
        'ix_babies_created_at',
        'babies',
        ['created_at'],
        unique=False
    )
    
    # Ajouter un trigger pour mettre à jour updated_at automatiquement
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )
    
    op.execute(
        """
        CREATE TRIGGER update_babies_updated_at
        BEFORE UPDATE ON babies
        FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """
    )
    
    # Commentaires sur la table
    op.execute(
        """
        COMMENT ON TABLE babies IS 'Profils des bébés (spécification 3.1 du cahier des charges)'
        """
    )


def downgrade():
    """
    Supprime la table babies et ses index
    """
    
    # Supprimer les triggers
    op.execute('DROP TRIGGER IF EXISTS update_babies_updated_at ON babies')
    op.execute('DROP FUNCTION IF EXISTS update_updated_at_column()')
    
    # Supprimer les index
    op.drop_index('ix_babies_created_at', table_name='babies')
    op.execute('DROP INDEX IF EXISTS ix_babies_name_lower')
    op.drop_index('ix_babies_user_active', table_name='babies')
    op.drop_index('ix_babies_birth_date', table_name='babies')
    op.drop_index('ix_babies_user_id', table_name='babies')
    
    # Supprimer la table
    op.drop_table('babies')
    
    # Supprimer l'enum
    gender_enum = postgresql.ENUM('male', 'female', 'other', name='gender_enum')
    gender_enum.drop(op.get_bind(), checkfirst=True)
