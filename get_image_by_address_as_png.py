import requests


def get_image_by_address_as_png(addres, size, path, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://geocode-maps.yandex.ru/1.x"
    geocoder_params = {
        "apikey": api_key,
        "geocode": addres,
        "format": "json"}
    with requests.get(url, params=geocoder_params) as response:
        data = response.json()
        cords = data["response"]['GeoObjectCollection']["featureMember"][0]["GeoObject"]["Point"]["pos"]
        # print(cords)

    url = f"https://static-maps.yandex.ru/1.x"
    map_params = {
        "ll": cords,
        "z": size,
        "l": "map"
        # "pt": f"{cords},pmwtm1"
    }
    # print(url)
    with requests.get(url, params=map_params) as response:
        data = response.content
        with open(path, "wb") as f:
            f.write(data)
    return path
