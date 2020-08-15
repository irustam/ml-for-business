import os
from dotenv import load_dotenv


def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), 'local.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    return True


def get_env(key):
    return os.environ.get(key)

#App port
app_port = 5001

#Model
model_url = 'http://localhost:5000/api/predict/'
model_features = {'Make': 'str',
                  'Model': 'str',
                  'Year': 'int',
                  'Engine Fuel Type': 'str',
                  'Engine HP': 'int',
                  'Engine Cylinders': 'int',
                  'Transmission Type': 'str',
                  'Driven_Wheels': 'str',
                  'Number of Doors': 'int',
                  'Market Category': 'str',
                  'Vehicle Size': 'str',
                  'Vehicle Style': 'str',
                  'highway MPG': 'int',
                  'city mpg': 'int',
                  'Popularity': 'int',
}

#Texts:
