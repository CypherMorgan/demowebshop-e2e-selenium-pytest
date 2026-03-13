import json
import os


def load_json(file_name):

    path = os.path.join("data", file_name)

    with open(path) as f:
        return json.load(f)
