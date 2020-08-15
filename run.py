import config
from get_predict import get_prediction
import os
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired
import json


class ModelForm(FlaskForm):
    fields = {}
    for feat, feat_type in config.model_features.items():
        if feat_type == 'str':
            fields[feat] = StringField(feat, validators=[DataRequired()])
        elif feat_type == 'int':
            fields[feat] = IntegerField(feat, validators=[DataRequired()])
    locals().update(fields)


config.load_env()
app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess'
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    data = {}
    if request.method == 'POST':
        for feat in config.model_features.keys():
            data[feat] = request.form.get(feat)

        try:
            response = str(get_prediction(data))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        except json.decoder.JSONDecodeError as e:
            response = json.dumps({"error": str(e)})
        return redirect(url_for('predicted', response=response))

    form = ModelForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT', config.app_port), use_reloader=False)