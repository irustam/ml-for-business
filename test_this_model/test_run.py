import config
import pandas as pd
import requests
import json
import numpy as np

config.load_env()
SECRET_API_KEY = config.get_env('SECRET_API_KEY')

X_test = pd.read_csv("hw8_X_test.csv")
y_test = pd.read_csv("hw8_y_test.csv")


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def get_prediction(body):
    myurl = "http://localhost:5000/api/predict/"
    body['SECRET_API_KEY'] = SECRET_API_KEY
    jsondata = json.dumps(body, cls=NpEncoder)
    response = requests.post(myurl, json=jsondata)
    return response.json()['predictions']


for n in range(10):
    print(int(get_prediction(X_test.iloc[n].to_dict())), y_test.iloc[n][0])