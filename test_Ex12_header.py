import requests
import json

class TestHeader:
    def test_for_headers(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_header')
        secret_header = "x-secret-homework-header"
        print(response.headers)

        assert secret_header in response.headers, f'There is no secret values. Only: {response.headers}'