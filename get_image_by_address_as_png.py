import requests
from get_image_by_cords_as_png import get_image_by_cords_as_png
from get_cords_by_adress import get_cords_by_adress


def get_image_by_address_as_png(addres, size : tuple, layer, path, zoom = None, spn = None, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    cords = get_cords_by_adress(addres)
    return get_image_by_cords_as_png(cords, size, layer, path, zoom, spn, api_key)


if __name__ == "__main__":
    get_image_by_address_as_png("russia", (450,450), "map", "a.png", 10)