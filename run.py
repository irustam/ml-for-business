import config
from load_model import load_model, get_model_features
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import os
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import warnings
# warnings.filterwarnings("ignore")

config.load_env()
app = Flask(__name__)

SECRET_API_KEY = config.get_env('SECRET_API_KEY')
model = load_model()

handler = RotatingFileHandler(filename='app.log', maxBytes=10000000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.route("/", methods=["GET"])
def general():
	return """
	Welcome to prediction process. 
	Please use 'http://your_host/api/predict' to POST. 
	Don't forget secret key!
	""", 200


@app.route("/api/predict/", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if request.method == "POST":
		#Load data
		request_json = request.get_json()
		dt = strftime("[%Y-%b-%d %H:%M:%S]")

		#Check secret API key
		get_sectret_key = request_json['SECRET_API_KEY']
		if get_sectret_key != SECRET_API_KEY:
			logger.warning(f'{dt} Exception: {config.bad_key}')
			data['predictions'] = config.bad_key
			return jsonify(data)

		#Get features values
		features_list = get_model_features(model)
		feat_values_dict = {}
		for feat in features_list:
			feat_values_dict[feat] = [request_json[feat] or np.nan]

		logger.info(f'{dt} Data: {feat_values_dict}')
		try:
			preds = model.predict(pd.DataFrame(feat_values_dict))
		except AttributeError as e:
			logger.warning(f'{dt} Exception: {str(e)}')
			data['predictions'] = str(e)
			return jsonify(data)

		data["predictions"] = preds[:, 1][0]
		# indicate that the request was a success
		data["success"] = True

	# return the data dictionary as a JSON response
	return jsonify(data)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=os.environ.get('PORT', config.app_port), use_reloader=False)