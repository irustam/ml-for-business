from config import get_env, model_url
import json
import requests
import numpy as np


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
    MODEL_URL = get_env('MODEL_URL')
    body['SECRET_API_KEY'] = get_env('SECRET_API_KEY')

    jsondata = json.dumps(body, cls=NpEncoder)
    response = requests.post(MODEL_URL, json=jsondata)
    return response.json()['predictions']