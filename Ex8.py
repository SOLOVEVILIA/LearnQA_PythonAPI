import requests
import time
import json


create_task = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
token = json.loads(create_task.text)

check_task = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)
if check_task.text == '{"status":"Job is NOT ready"}':
    time.sleep(10)
    post_check_task = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)
    checker_from_json = json.loads(post_check_task.text)
    if (checker_from_json['result'] != 'null' and checker_from_json['status'] == 'Job is ready'):
        print(f'All done: {post_check_task.text}')
    else:
        print('Something wrong')
else:
    print(f'Status: {check_task.text}')

