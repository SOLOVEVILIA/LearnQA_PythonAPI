import requests
import pytest
import json.decoder


class TestUserAgent:
    user_agent_and_expected_params = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", '"platform": "Mobile", "browser": "No", "device": "Android"'),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", '"platform": "Mobile", "browser": "Chrome", "device": "iOS"'),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", '"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"'),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", '"platform": "Web", "browser": "Chrome", "device": "No"'),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", '"platform": "Mobile", "browser": "No", "device": "iPhone"')
    ]

    @pytest.mark.parametrize('ua_params, expected_params', user_agent_and_expected_params)
    def test_user_agent_check(self, ua_params, expected_params):
        response = requests.get(
            'https://playground.learnqa.ru/ajax/api/user_agent_check',
            headers={"User-Agent": ua_params}
            )

        response_as_dict = response.json()

        del response_as_dict["user_agent"] # Удаляем по ключу лишнюю пару ключ/значение для более удобного сравнения
        response_as_dict_back_to_str = json.dumps(response_as_dict) # Конвертируем назад в строку

        new_exp_params = '{' + expected_params + '}' # Конкатинируем сиволы '{' и '}' так как в ответе останутся скобки после преобразований

        # Сравниваем значения полученные в результате работы метода и ожидаемые значения, которые мы сами передали через параметры
        assert response_as_dict_back_to_str == new_exp_params, f'Strings are not equal, was expected = {new_exp_params}, but response {response_as_dict_back_to_str}'
