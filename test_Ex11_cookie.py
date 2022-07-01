import requests

response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
print(response.cookies)
cookie = 'HomeWork'
assert cookie in response.cookies, f'Cannot find cookie with name {cookie} in the cookies'
