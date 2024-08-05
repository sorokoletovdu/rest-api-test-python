import requests


class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {}
        if token:
            self.headers['Authorization'] = f'Bearer {token}'

    def get(self, endpoint):
        response = requests.get(f'{self.base_url}{endpoint}', headers=self.headers)
        return response

    def post(self, endpoint, data):
        response = requests.post(f'{self.base_url}{endpoint}', json=data, headers=self.headers)
        return response

    def put(self, endpoint, data):
        response = requests.put(f'{self.base_url}{endpoint}', json=data, headers=self.headers)
        return response

    def delete(self, endpoint):
        response = requests.delete(f'{self.base_url}{endpoint}', headers=self.headers)
        return response
