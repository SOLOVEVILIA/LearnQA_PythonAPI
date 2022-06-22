import requests

response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True) # Кладем в переменную все данные которые вернулись после запроса
first_response = response.history[0]                                     # Обращаемся к history - это массив в котором хранится информация о всех предыдущих запросах (выбираем первый элемент)
second_response = response                                               # Информация по последнему запросу уже лежит в переменной, но для наглядности мы перекладываем её в другую переменную

print(first_response.url)
print(second_response.url)
print(response.status_code)
