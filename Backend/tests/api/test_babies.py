"""
Tests for Baby Profile API
Tests unitaires et d'intégration pour les endpoints /api/v1/babies
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import date, timedelta
from typing import Dict

from app.main import app
from app.db.models.baby_model import Baby
from app.db.models.user_model import User


# ==================== FIXTURES ====================

@pytest.fixture
def client():
    """Client de test FastAPI"""
    return TestClient(app)


@pytest.fixture
def test_user(db: Session) -> User:
    """Crée un utilisateur de test"""
    user = User(
        email="test@example.com",
        hashed_password="hashed_password",
        first_name="Test",
        last_name="User"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def other_user(db: Session) -> User:
    """Crée un second utilisateur pour tester l'isolation"""
    user = User(
        email="test2@example.com",
        hashed_password="hashed_password",
        first_name="Other",
        last_name="User"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def auth_headers(test_user: User) -> Dict[str, str]:
    """Headers d'authentification pour test_user"""
    # Note: Adapter selon votre implémentation JWT
    token = create_access_token(test_user.id)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def other_auth_headers(other_user: User) -> Dict[str, str]:
    """Headers d'authentification pour other_user"""
    token = create_access_token(other_user.id)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def sample_baby_data() -> dict:
    """Données de test pour créer un bébé"""
    return {
        "name": "Lina",
        "birth_date": "2025-12-01",
        "gender": "female",
        "photo_url": "https://cdn.pixabay.com/photo/2023/06/11/14/38/baby-8056153_1280.jpg"
    }


@pytest.fixture
def test_baby(db: Session, test_user: User) -> Baby:
    """Crée un bébé de test en base"""
    baby = Baby(
        user_id=test_user.id,
        name="Lina",
        birth_date=date(2025, 12, 1),
        gender="female"
    )
    db.add(baby)
    db.commit()
    db.refresh(baby)
    return baby


# ==================== TESTS CREATION ====================

class TestCreateBaby:
    """Tests pour POST /api/v1/babies/"""
    
    def test_create_baby_success(self, client, auth_headers, sample_baby_data):
        """Test création réussie d'un profil bébé"""
        response = client.post(
            "/api/v1/babies/",
            json=sample_baby_data,
            headers=auth_headers
        )
        
        assert response.status_code == 201
        data = response.json()
        
        # Vérifier les champs retournés
        assert data["name"] == sample_baby_data["name"]
        assert data["birth_date"] == sample_baby_data["birth_date"]
        assert data["gender"] == sample_baby_data["gender"]
        assert data["photo_url"] == sample_baby_data["photo_url"]
        assert "id" in data
        assert "age" in data
        assert "created_at" in data
        
        # Vérifier le calcul d'âge
        assert "days" in data["age"]
        assert "weeks" in data["age"]
        assert "months" in data["age"]
        assert data["age"]["months"] >= 0
    
    def test_create_baby_without_auth(self, client, sample_baby_data):
        """Test création sans authentification → 401"""
        response = client.post("/api/v1/babies/", json=sample_baby_data)
        assert response.status_code == 401
    
    def test_create_baby_invalid_name(self, client, auth_headers):
        """Test avec nom invalide → 422"""
        invalid_data = {
            "name": "123",  # Nom avec chiffres
            "birth_date": "2025-12-01",
            "gender": "female"
        }
        response = client.post(
            "/api/v1/babies/",
            json=invalid_data,
            headers=auth_headers
        )
        assert response.status_code == 422
    
    def test_create_baby_future_birth_date(self, client, auth_headers):
        """Test avec date de naissance future → 422"""
        tomorrow = (date.today() + timedelta(days=1)).isoformat()
        invalid_data = {
            "name": "Lina",
            "birth_date": tomorrow,
            "gender": "female"
        }
        response = client.post(
            "/api/v1/babies/",
            json=invalid_data,
            headers=auth_headers
        )
        assert response.status_code == 422
        assert "future" in response.json()["detail"][0]["msg"].lower()
    
    def test_create_baby_too_old(self, client, auth_headers):
        """Test avec date trop ancienne → 422"""
        old_date = (date.today() - timedelta(days=365 * 11)).isoformat()
        invalid_data = {
            "name": "Lina",
            "birth_date": old_date,
            "gender": "female"
        }
        response = client.post(
            "/api/v1/babies/",
            json=invalid_data,
            headers=auth_headers
        )
        assert response.status_code == 422
    
    def test_create_baby_invalid_gender(self, client, auth_headers):
        """Test avec genre invalide → 422"""
        invalid_data = {
            "name": "Lina",
            "birth_date": "2025-12-01",
            "gender": "unknown"
        }
        response = client.post(
            "/api/v1/babies/",
            json=invalid_data,
            headers=auth_headers
        )
        assert response.status_code == 422
    
    def test_create_baby_missing_required_fields(self, client, auth_headers):
        """Test avec champs obligatoires manquants → 422"""
        incomplete_data = {"name": "Lina"}
        response = client.post(
            "/api/v1/babies/",
            json=incomplete_data,
            headers=auth_headers
        )
        assert response.status_code == 422
    
    def test_create_baby_without_photo(self, client, auth_headers):
        """Test création sans photo (optionnelle) → 201"""
        data = {
            "name": "Lina",
            "birth_date": "2025-12-01",
            "gender": "female"
        }
        response = client.post(
            "/api/v1/babies/",
            json=data,
            headers=auth_headers
        )
        assert response.status_code == 201
        assert response.json()["photo_url"] is None


# ==================== TESTS LECTURE ====================

class TestGetBabies:
    """Tests pour GET /api/v1/babies/"""
    
    def test_get_babies_empty(self, client, auth_headers):
        """Test récupération avec aucun bébé"""
        response = client.get("/api/v1/babies/", headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 0
        assert data["items"] == []
    
    def test_get_babies_with_data(self, client, auth_headers, test_baby):
        """Test récupération avec des bébés"""
        response = client.get("/api/v1/babies/", headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert len(data["items"]) == 1
        assert data["items"][0]["name"] == test_baby.name
    
    def test_get_babies_pagination(self, client, auth_headers, db, test_user):
        """Test pagination"""
        # Créer plusieurs bébés
        for i in range(15):
            baby = Baby(
                user_id=test_user.id,
                name=f"Baby{i}",
                birth_date=date(2025, 1, 1),
                gender="female"
            )
            db.add(baby)
        db.commit()
        
        # Page 1
        response = client.get(
            "/api/v1/babies/?skip=0&limit=10",
            headers=auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 15
        assert len(data["items"]) == 10
        assert data["skip"] == 0
        assert data["limit"] == 10
        
        # Page 2
        response = client.get(
            "/api/v1/babies/?skip=10&limit=10",
            headers=auth_headers
        )
        data = response.json()
        assert len(data["items"]) == 5
    
    def test_get_babies_isolation(self, client, auth_headers, other_auth_headers, 
                                  test_baby, db, other_user):
        """Test que chaque utilisateur voit seulement ses bébés"""
        # Créer un bébé pour other_user
        other_baby = Baby(
            user_id=other_user.id,
            name="OtherBaby",
            birth_date=date(2025, 1, 1),
            gender="male"
        )
        db.add(other_baby)
        db.commit()
        
        # test_user voit seulement son bébé
        response = client.get("/api/v1/babies/", headers=auth_headers)
        data = response.json()
        assert data["total"] == 1
        assert data["items"][0]["name"] == test_baby.name
        
        # other_user voit seulement son bébé
        response = client.get("/api/v1/babies/", headers=other_auth_headers)
        data = response.json()
        assert data["total"] == 1
        assert data["items"][0]["name"] == "OtherBaby"


class TestGetBabyById:
    """Tests pour GET /api/v1/babies/{baby_id}"""
    
    def test_get_baby_success(self, client, auth_headers, test_baby):
        """Test récupération réussie d'un bébé"""
        response = client.get(
            f"/api/v1/babies/{test_baby.id}",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == test_baby.id
        assert data["name"] == test_baby.name
    
    def test_get_baby_not_found(self, client, auth_headers):
        """Test récupération d'un bébé inexistant → 404"""
        response = client.get("/api/v1/babies/99999", headers=auth_headers)
        assert response.status_code == 404
    
    def test_get_baby_not_owned(self, client, other_auth_headers, test_baby):
        """Test accès au bébé d'un autre utilisateur → 404"""
        response = client.get(
            f"/api/v1/babies/{test_baby.id}",
            headers=other_auth_headers
        )
        assert response.status_code == 404


class TestSearchBabies:
    """Tests pour GET /api/v1/babies/search"""
    
    def test_search_babies_success(self, client, auth_headers, db, test_user):
        """Test recherche par nom"""
        # Créer plusieurs bébés
        babies = [
            Baby(user_id=test_user.id, name="Lina", birth_date=date(2025, 1, 1), gender="female"),
            Baby(user_id=test_user.id, name="Ali", birth_date=date(2025, 1, 1), gender="female"),
            Baby(user_id=test_user.id, name="Sofia", birth_date=date(2025, 1, 1), gender="male"),
        ]
        for baby in babies:
            db.add(baby)
        db.commit()
        
        # Rechercher "Em"
        response = client.get(
            "/api/v1/babies/search?q=Em",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2  # Emma et Emily
        names = [baby["name"] for baby in data]
        assert "Lina" in names
        assert "Ali" in names
    
    def test_search_babies_case_insensitive(self, client, auth_headers, test_baby):
        """Test recherche insensible à la casse"""
        response = client.get(
            "/api/v1/babies/search?q=EMMA",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == "Emma"
    
    def test_search_babies_no_results(self, client, auth_headers):
        """Test recherche sans résultats"""
        response = client.get(
            "/api/v1/babies/search?q=NonExistent",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        assert response.json() == []


# ==================== TESTS MISE A JOUR ====================

class TestUpdateBaby:
    """Tests pour PUT /api/v1/babies/{baby_id}"""
    
    def test_update_baby_name(self, client, auth_headers, test_baby):
        """Test mise à jour du nom"""
        update_data = {"name": "Lina Rose"}
        response = client.put(
            f"/api/v1/babies/{test_baby.id}",
            json=update_data,
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Lina Rose"
        assert data["id"] == test_baby.id
    
    def test_update_baby_multiple_fields(self, client, auth_headers, test_baby):
        """Test mise à jour de plusieurs champs"""
        update_data = {
            "name": "Lina Rose",
            "gender": "other"
        }
        response = client.put(
            f"/api/v1/babies/{test_baby.id}",
            json=update_data,
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Lina Rose"
        assert data["gender"] == "other"
    
    def test_update_baby_not_found(self, client, auth_headers):
        """Test mise à jour d'un bébé inexistant → 404"""
        response = client.put(
            "/api/v1/babies/99999",
            json={"name": "Test"},
            headers=auth_headers
        )
        assert response.status_code == 404
    
    def test_update_baby_not_owned(self, client, other_auth_headers, test_baby):
        """Test mise à jour du bébé d'un autre → 404"""
        response = client.put(
            f"/api/v1/babies/{test_baby.id}",
            json={"name": "Hacked"},
            headers=other_auth_headers
        )
        assert response.status_code == 404
    
    def test_update_baby_no_fields(self, client, auth_headers, test_baby):
        """Test mise à jour sans champs → 400"""
        response = client.put(
            f"/api/v1/babies/{test_baby.id}",
            json={},
            headers=auth_headers
        )
        assert response.status_code == 400
    
    def test_update_baby_invalid_data(self, client, auth_headers, test_baby):
        """Test mise à jour avec données invalides → 422"""
        response = client.put(
            f"/api/v1/babies/{test_baby.id}",
            json={"birth_date": "2030-01-01"},  # Date future
            headers=auth_headers
        )
        assert response.status_code == 422


# ==================== TESTS SUPPRESSION ====================

class TestDeleteBaby:
    """Tests pour DELETE /api/v1/babies/{baby_id}"""
    
    def test_soft_delete_baby(self, client, auth_headers, test_baby, db):
        """Test suppression soft (par défaut)"""
        response = client.delete(
            f"/api/v1/babies/{test_baby.id}",
            headers=auth_headers
        )
        
        assert response.status_code == 204
        
        # Vérifier que le bébé est marqué comme supprimé
        db.refresh(test_baby)
        assert test_baby.deleted_at is not None
    
    def test_hard_delete_baby(self, client, auth_headers, test_baby, db):
        """Test suppression définitive"""
        baby_id = test_baby.id
        
        response = client.delete(
            f"/api/v1/babies/{baby_id}?permanent=true",
            headers=auth_headers
        )
        
        assert response.status_code == 204
        
        # Vérifier que le bébé n'existe plus en BDD
        baby = db.query(Baby).filter(Baby.id == baby_id).first()
        assert baby is None
    
    def test_delete_baby_not_found(self, client, auth_headers):
        """Test suppression d'un bébé inexistant → 404"""
        response = client.delete(
            "/api/v1/babies/99999",
            headers=auth_headers
        )
        assert response.status_code == 404
    
    def test_delete_baby_not_owned(self, client, other_auth_headers, test_baby):
        """Test suppression du bébé d'un autre → 404"""
        response = client.delete(
            f"/api/v1/babies/{test_baby.id}",
            headers=other_auth_headers
        )
        assert response.status_code == 404


class TestRestoreBaby:
    """Tests pour POST /api/v1/babies/{baby_id}/restore"""
    
    def test_restore_baby_success(self, client, auth_headers, test_baby, db):
        """Test restauration d'un bébé supprimé"""
        # Soft delete d'abord
        test_baby.soft_delete()
        db.commit()
        
        # Restaurer
        response = client.post(
            f"/api/v1/babies/{test_baby.id}/restore",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == test_baby.id
        
        # Vérifier en BDD
        db.refresh(test_baby)
        assert test_baby.deleted_at is None
    
    def test_restore_baby_not_deleted(self, client, auth_headers, test_baby):
        """Test restauration d'un bébé non supprimé → 404"""
        response = client.post(
            f"/api/v1/babies/{test_baby.id}/restore",
            headers=auth_headers
        )
        assert response.status_code == 404


# ==================== TESTS STATISTIQUES ====================

# class TestBabyStatistics:
#     """Tests pour GET /api/v1/babies/statistics/overview"""
    
#     def test_get_statistics(self, client, auth_headers, db, test_user):
#         """Test récupération des statistiques"""
#         # Créer plusieurs bébés
#         babies = [
#             Baby(user_id=test_user.id, name="Emma", birth_date=date(2025, 12, 1), gender="female"),
#             Baby(user_id=test_user.id, name="Lucas", birth_date=date(2024, 6, 1), gender="male"),
#             Baby(user_id=test_user.id, name="Olivia", birth_date=date(2025, 11, 1), gender="female"),
#         ]
#         for baby in babies:
#             db.add(baby)
#         db.commit()
        
#         response = client.get(
#             "/api/v1/babies/statistics/overview",
#             headers=auth_headers
#         )
        
#         assert response.status_code == 200
#         data = response.json()
        
#         assert data["total"] == 3
#         assert data["by_gender"]["female"] == 2
#         assert data["by_gender"]["male"] == 1
#         assert "youngest" in data
#         assert "oldest" in data


# # ==================== HELPERS ====================

# def create_access_token(user_id: int) -> str:
#     """
#     Crée un JWT token pour les tests
#     Note: À adapter selon votre implémentation réelle
#     """
#     # TODO: Implémenter selon votre système d'auth
#     from app.core.security import create_token
#     return create_token({"sub": str(user_id)})
