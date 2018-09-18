import json

import pytest

from .factories import StudentFactory


@pytest.mark.django_db
def test_endpoint(client):
    student = StudentFactory()
    response = client.get(f'/api/{student.id}', follow=True)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content['name'] == student.first_name
