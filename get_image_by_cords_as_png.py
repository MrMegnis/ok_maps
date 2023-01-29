import sys
from io import BytesIO
import requests
from PIL import Image

def get_image_by_cords_as_png(cords : tuple, size : tuple, layer, marks, path, zoom = None, spn = 10, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://static-maps.yandex.ru/1.x"
    zoom_param = ""
    zoom_arg = ""
    print("~".join(marks))
    if isinstance(zoom, type(None)):
        zoom_param = "spn"
        zoom_arg = ",".join(map(str, (spn, spn))),
    else:
        zoom_param = "z"
        zoom_arg = zoom
    print(zoom_param, zoom_arg)
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
        with open(path, "wb") as f:
            f.write(data)
            Image.open(BytesIO(data)).save(path)
    return path


if __name__ == "__main__":
    get_image_by_cords_as_png((37.620070 + 0.002,55.753630), (450, 450), "sat", "a.png", spn=10)