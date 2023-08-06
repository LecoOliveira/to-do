from to_do.schemas import UserPublic


def test_root_deve_retornar_200_e_hello_world(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Hello world'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_create_user_with_error_400(client, user):
    response = client.post(
        '/users',
        json={
            'username': 'Teste',
            'email': 'teste@test.com',
            'password': 'testtest',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Username already registered'}


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'alex',
            'email': 'teste@teste.com',
            'password': 'testando',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'alex',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_update_user_with_error_404(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'alex',
            'email': 'teste@teste.com',
            'password': 'testando',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_with_error_404(client):
    response = client.delete('/users/1')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
