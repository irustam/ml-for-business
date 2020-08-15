import os
from dotenv import load_dotenv


def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), 'local.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    return True


def get_env(key):
    return os.environ.get(key)

# App port
app_port = 5000

#Model
model_filename = './models/hw8_pipeline_model2.dill'


# Texts:
bad_key = 'Wrong secret API key'

