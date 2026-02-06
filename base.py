from sqlalchemy.ext.declarative import declarative_base

# Créer la classe Base pour tous les modèles
Base = declarative_base()

# Tu peux ajouter des mixins ou des méthodes communes ici si besoin
class BaseModel:
    """Mixin avec des méthodes communes pour tous les modèles"""
    
    def to_dict(self):
        """Convertit l'objet en dictionnaire"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
