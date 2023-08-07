from to_do.schemas import UserPublic


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
            'username': f'{user.username}',
            'email': f'{user.email}',
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


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'alex',
            'email': 'teste@teste.com',
            'password': 'testando',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'id': 6,
        'username': 'alex',
        'email': 'teste@teste.com',
    }


def test_update_user_with_wrong_user_error_400(client, other_user, token):
    response = client.put(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_with_error_404(client, other_user, token):
    response = client.delete(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}
