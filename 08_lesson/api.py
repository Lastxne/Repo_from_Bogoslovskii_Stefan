import requests


class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def create_project(self, data):
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            headers=self.headers,
            json=data
        )

    def update_project(self, project_id, data):
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers,
            json=data
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
