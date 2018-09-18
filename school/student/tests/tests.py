import json

import pytest

from .factories import StudentFactory

@pytest.fixture
def user():
    return StudentFactory()


@pytest.mark.django_db
def test_endpoint(client, user):
    response = client.get(f'/api/{user.id}', follow=True)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content['name'] == student.first_name
