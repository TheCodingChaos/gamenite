import pytest
from server.app import app, db
from models import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_signup_success(client):
    response = client.post('/signup', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'testpass'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['email'] == 'test@example.com'

def test_signup_existing_email(client):
    client.post('/signup', json={
        'name': 'User One',
        'email': 'dupe@example.com',
        'password': 'testpass'
    })
    response = client.post('/signup', json={
        'name': 'User Two',
        'email': 'dupe@example.com',
        'password': 'testpass'
    })
    assert response.status_code == 409

def test_login_success(client):
    client.post('/signup', json={
        'name': 'Log Me In',
        'email': 'login@example.com',
        'password': 'secret'
    })
    response = client.post('/login', json={
        'email': 'login@example.com',
        'password': 'secret'
    })
    assert response.status_code == 200

def test_login_fail(client):
    response = client.post('/login', json={
        'email': 'nonexistent@example.com',
        'password': 'nope'
    })
    assert response.status_code == 401