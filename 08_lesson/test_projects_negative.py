import pytest


@pytest.mark.negative
def test_create_project_without_title(api):
    data = {
        "title": "",
        "users": {
            "982d0603-249a-4b4e-a0c0-06a208f7a820": "admin"
        }
    }
    resp = api.create_project(data)
    assert resp.status_code == 400
    body = resp.json()
    assert body["message"] == ["title should not be empty"]
    assert body["error"] == "Bad Request"


@pytest.mark.negative
def test_update_nonexistent_project(api):
    project_id = "0a983608-0166-49fc-a304-bfcaf1959bc3"
    data = {
        "title": "Тестовое обновление",
        "users": {
            "982d0603-249a-4b4e-a0c0-06a208f7a820": "admin"
        },
        "deleted": False
    }
    resp = api.update_project(project_id, data)
    assert resp.status_code == 404
    body = resp.json()
    assert body["message"] == "Проект не найден"
    assert body["error"] == "Not Found"


@pytest.mark.negative
def test_get_nonexistent_project(api):
    project_id = "0a983608-0166-49fc-a304-bfcaf1959bc3"
    resp = api.get_project(project_id)
    assert resp.status_code == 404
    body = resp.json()
    assert body["message"] == "Проект не найден"
    assert body["error"] == "Not Found"
