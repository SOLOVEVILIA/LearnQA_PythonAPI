import requests

response = requests.get('https://playground.learnqa.ru/api/hello') #создаём get-запрос на адрес указанный в скобках
print(response.text) #из всего ответа распечатываем только текст (json-объект)

