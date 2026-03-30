import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0"
        })

    def _url(self, endpoint):
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint, headers=None, params=None):
        return self.session.get(
            self._url(endpoint),
            headers=headers,
            params=params
        )

    def post(self, endpoint, headers=None, json=None):
        return self.session.post(
            self._url(endpoint),
            headers=headers,
            json=json
        )

    def put(self, endpoint, headers=None, json=None):
        return self.session.put(
            self._url(endpoint),
            headers=headers,
            json=json
        )

    def delete(self, endpoint, headers=None):
        return self.session.delete(
            self._url(endpoint),
            headers=headers
        )