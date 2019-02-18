import requests
import pandas as pd
import json
from pandas.io.json import json_normalize

def get_and_flatten():
    res = requests.get("https://polisen.se/api/events")

    if res.status_code == requests.codes.ok:
        print(flatten_data(res.json()))

def flatten_from_file(file_path):
    with open(file_path) as f:
        json_data = json.load(f)
        print(flatten_data(json_data))

def flatten_data(json_data):
    flattened_data = [json_normalize(d) for d in json_data]
    df = pd.concat(flattened_data)
    return df.to_json(orient='records', force_ascii=False)
