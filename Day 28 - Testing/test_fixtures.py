import pytest

@pytest.fixture
def database():
    """Fixture providing test database connection"""
    db = connect_to_test_db()
    yield db
    db.disconnect()

def test_user_count(database):
    assert database.get_user_count() == 0

@pytest.fixture
def sample_user():
    return {"name": "Alice", "email": "alice@example.com"}

def test_user_creation(sample_user):
    assert "@" in sample_user["email"]