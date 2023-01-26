import requests


def get_image_bytes(addres, size, path, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://geocode-maps.yandex.ru/1.x?geocode={addres}&apikey={api_key}&format=json"
    geocoder_params = {
        "apikey": api_key,
        "geocode": addres,
        "format": "json"}
    with requests.get(url) as response:
        data = response.json()
        cords = data["response"]['GeoObjectCollection']["featureMember"][0]["GeoObject"]["Point"]["pos"]
        # print(cords)

    url = f"https://static-maps.yandex.ru/1.x/?l=sat&ll={cords.split()[0]},{cords.split()[1]}&z=4"
    map_params = {
        "ll": cords,
        "spn": ",".join(size),
        "l": "map"
        # "pt": f"{cords},pmwtm1"
    }
    # print(url)
    with requests.get(url) as response:
        data = response.content
        return data
