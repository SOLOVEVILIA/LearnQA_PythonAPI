import requests

class TestCookie:
    def test_for_cookie(self):
        response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        print(response.cookies)
        cookie = 'HomeWork'
        assert cookie in response.cookies, f'Cannot find cookie with name {cookie} in the cookies'