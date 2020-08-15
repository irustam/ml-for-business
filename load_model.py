import dill
from config import model_filename


def load_model():
	# load the pre-trained model
	try:
		with open(model_filename, 'rb') as f:
			model = dill.load(f)
	except IOError as e:
		return None

	return model


def get_model_features(model):
	#Get features list from Catboost model
	return model.steps[1][1].get_feature_importance(prettified=True)['Feature Id'].to_list()


if __name__ == '__main__':
	model = load_model()
	if model:
		print(model.steps[1])