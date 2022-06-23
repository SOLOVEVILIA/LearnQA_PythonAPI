import requests

def first():
    print('_____Task 1_____')
    response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
    print(response.text)
    print(response.status_code)

def second():
    print('_____Task 2_____')
    response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': 'HEAD'})
    print(response.text)            # Описания к ошибке нет, не предусмотрена данная ситуация?
    print(response.status_code)     # Ошибка 400 - со стороны клиента?

def third():
    print('_____Task 3_____')
    method = {'method': 'POST'}
    response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data=method)
    print(response.text)
    print(response.status_code)

def fourth():
    print('_____Task 4_____')
    method = [{'method': 'GET'}, {'method': 'POST'}, {'method': 'PUT'}, {'method': 'DELETE'}]
    url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

    for m in method:
        response = requests.get(url, params=m)
        response_post = requests.post(url, data=m)
        response_put = requests.put(url, data=m)
        response_del = requests.delete(url, data=m)

        re = [response, response_post, response_put, response_del]

        for r in re:
            print(f'{r.request}, given method in params/data: {m}')
            print(f'Status_code: {r.status_code}')
            print(f'Text: {r.text}''\n')

first()
second()
third()
fourth()