import pytest


@pytest.mark.positive
def test_edit_project(api, created_project_id):
    updated_data = {
        "title": "Это не то что вы подумали",
        "users": {
            "982d0603-249a-4b4e-a0c0-06a208f7a820": "admin"
        },
        "deleted": False
    }
    resp = api.update_project(created_project_id, updated_data)
    assert resp.status_code == 200


@pytest.mark.positive
def test_get_project(api, created_project_id):
    resp = api.get_project(created_project_id)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Это не то что вы подумали"


@pytest.mark.positive
def test_create_project(api):
    data = {
        "title": "Тестовый проект",
        "users": {
            "982d0603-249a-4b4e-a0c0-06a208f7a820": "admin"
        }
    }
    resp = api.create_project(data)
    assert resp.status_code == 201
    assert "id" in resp.json()
