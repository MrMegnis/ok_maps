import requests


def get_image_by_cords_bytes(cords : tuple, zoom, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://static-maps.yandex.ru/1.x"
    map_params = {
        "ll": ",".join(map(str, cords)),
        "spn": ",".join(map(str, (zoom, zoom))),
        "l": "map"
        # "pt": f"{cords},pmwtm1"
    }
    # print(url)
    with requests.get(url, params=map_params) as response:
        data = response.content
        return data
