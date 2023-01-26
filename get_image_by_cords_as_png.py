import requests


def get_image_by_cords_as_png(cords : tuple, size, path, api_key="40d1649f-0493-4b70-98ba-98533de7710b"):
    url = f"https://static-maps.yandex.ru/1.x"
    print(",".join(map(str, cords)))
    map_params = {
        "ll": ",".join(map(str, cords)),
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


if __name__ == "__main__":
    get_image_by_cords_as_png((0,0), 4, "a.png")