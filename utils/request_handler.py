import requests


class RequestHandler:

    def __init__(self, base_url, headers=None, timeout=10):
        self.session = requests.Session()
        self.session.base_url = base_url
        if headers:
            self.session.headers = headers
        self.timeout = timeout

    def set_header(self, key, value):
        self.session.headers.update({key: value})

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f'{self.session.base_url}{endpoint}',
            timeout=self.timeout,
            **kwargs
        )

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.session.post(
            f'{self.session.base_url}{endpoint}',
            data=data,
            json=json,
            timeout=self.timeout,
            **kwargs
        )

    def close(self):
        self.session.close()
