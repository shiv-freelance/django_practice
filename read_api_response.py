import json


def find_rating_info(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "ratingInfo":
                print(f"Key: {key}, Value: {value}")
            elif isinstance(value, (dict, list)):
                find_rating_info(value)
    elif isinstance(data, list):
        for item in data:
            find_rating_info(item)


with open("api_response.json", "r") as f:
    data = json.load(f)

find_rating_info(data)
