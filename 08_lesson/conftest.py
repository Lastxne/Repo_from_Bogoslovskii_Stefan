import pytest
from api import ProjectAPI


@pytest.fixture(scope="session")
def api():
    base_url = "https://ru.yougile.com"
    token = "ТОКЕН_ДЛЯ_АВТОРИЗАЦИИ"  # Замените на ваш токен
    return ProjectAPI(base_url, token)


@pytest.fixture(scope="session")
def created_project_id(api):
    data = {
        "title": "Ночные услуги",
        "users": {
            "982d0603-249a-4b4e-a0c0-06a208f7a820": "admin"
        }
    }
    resp = api.create_project(data)
    assert resp.status_code == 201
    return resp.json()["id"]
