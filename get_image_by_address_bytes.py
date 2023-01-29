import requests
from get_image_by_cords_bytes import get_image_by_cords_bytes
from get_cords_by_adress import get_cords_by_adress


def get_image_by_address_bytes(addres, size : tuple, layer, zoom = None, spn = None, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    cords = get_cords_by_adress(addres)
    return get_image_by_cords_bytes(cords, size, zoom, layer, api_key)


if __name__ == "__main__":
    print(get_image_by_address_bytes("russia", (450,450), "map", 10))