import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

for i in range(len(response.history)):
    r = response.history[i]
    print(f'Redirected URL: {r.url}')
else:
    print(f'Destination URL: {response.url}')