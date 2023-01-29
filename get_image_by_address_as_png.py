import requests
from get_image_by_cords_as_png import get_image_by_cords_as_png


def get_image_by_address_as_png(addres, size : tuple, zoom, layer, path, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": api_key,
        "geocode": addres,
        "format": "json"}
    with requests.get(url, params=geocoder_params) as response:
        data = response.json()
        cords = data["response"]['GeoObjectCollection']["featureMember"][0]["GeoObject"]["Point"]["pos"]
        print(cords)
    cords = tuple(map(float, cords.split()))
    return get_image_by_cords_as_png(cords, size, zoom, layer, path, api_key)


if __name__ == "__main__":
    get_image_by_address_as_png("russia", 10, "map", "a.png")