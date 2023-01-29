import requests


def get_image_by_cords_bytes(cords : tuple, size : tuple, layer, marks, zoom = None, spn = 10, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://static-maps.yandex.ru/1.x"
    zoom_param = ""
    zoom_arg = ""
    if isinstance(zoom, type(None)):
        zoom_param = "spn"
        zoom_arg = spn
    else:
        zoom_param = "z"
        zoom_arg = zoom
    map_params = {
        "ll": ",".join(map(str, cords)),
        # "spn": ",".join(map(str, (zoom, zoom))),
        zoom_param: zoom_arg,
        "size" : ",".join(map(str, size)),
        "l": layer,
        "pt": "~".join(marks)
    }
    # print(url)
    with requests.get(url, params=map_params) as response:
        data = response.content
        return data
