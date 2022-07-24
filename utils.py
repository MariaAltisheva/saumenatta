import json
import requests


def get_data_from_json_file():
    """Получаем настройки из json файла new,
    где храним ссылку на json с данными."""
    with open('kolkata.geojson') as file:
        return json.load(file)


def get_questions_data_by_requests():
    """Запрашиваем из интернета,  используя requests, json с данными."""
    request_url = get_data_from_json_file()['kolkata']
    response = requests.get(request_url)
    return response.json()

#print(get_questions_data_by_requests())