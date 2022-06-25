import requests
import unittest


class YandexApiTest:
    def __init__(self, token_ya: str):
        self.token_ya = token_ya

    def token_ya(self):
        with open('token_YaDisk.txt', 'r') as file:
            token_ya = file.read().strip()
        return token_ya

    def create_yadisk_folder(folder_path):
        token = YandexApiTest.token_ya(YandexApiTest)
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        HEADERS = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        PARAMS = {'path': folder_path}
        create_dir = requests.api.put(url, headers=HEADERS, params=PARAMS)
        return create_dir.status_code



class TestApiYand(unittest.TestCase):
    def test_success_create_folder(self):
        self.assertEqual(YandexApiTest.create_yadisk_folder('api_yandex_testing'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(YandexApiTest.create_yadisk_folder('test_passed'), 409)


if __name__ == '__main__':
    unittest.main()