import requests
from get_image_by_cords_bytes import get_image_by_cords_bytes

def get_image_by_address_bytes(addres, size, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://geocode-maps.yandex.ru/1.x?geocode={addres}&apikey={api_key}&format=json"
    geocoder_params = {
        "apikey": api_key,
        "geocode": addres,
        "format": "json"}
    with requests.get(url) as response:
        data = response.json()
        cords = data["response"]['GeoObjectCollection']["featureMember"][0]["GeoObject"]["Point"]["pos"]
        # print(cords)

    cords = tuple(map(float, cords.split()))
    return get_image_by_cords_bytes(cords, size, api_key)


if __name__ == "__main__":
    print(get_image_by_address_bytes("russia", 4))