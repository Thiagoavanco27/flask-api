import pytest
from app import agendaApp

@pytest.fixture
def client():
    agendaApp.testing = True
    return agendaApp.test_client()

def test_get_contacts(client):
    response = client.get('/contacts')
    assert response.status_code == 200

def test_get_contact(client):
    response = client.get('/contacts/1')
    assert response.status_code == 200

def test_get_contact_not_found(client):
    response = client.get('/contacts/999')
    assert response.status_code == 404

def test_add_contact(client):
    new_contact_data = {
        'nome': 'Novo Contato',
        'email': 'novo_contato@example.com',
        'telefone': '123456789',
        'idade': 30
    }
    response = client.post('/contacts', json=new_contact_data)
    assert response.status_code == 201

def test_update_contact(client):
    updated_contact_data = {
        'nome': 'Nome Atualizado',
        'email': 'email_atualizado@example.com',
        'telefone': '987654321',
        'idade': 40
    }
    response = client.put('/contacts/1', json=updated_contact_data)
    assert response.status_code == 200

def test_check_contact_exists(client):
    existing_contact_data = {
        'nome': 'Maria',
        'email': 'maria@email.com'
    }
    response = client.post('/contacts/check', json=existing_contact_data)
    assert response.status_code == 200

def test_check_contact_not_found(client):
    non_existing_contact_data = {
        'nome': 'Não Existente',
        'email': 'naoexistente@email.com'
    }
    response = client.post('/contacts/check', json=non_existing_contact_data)
    assert response.status_code == 404
