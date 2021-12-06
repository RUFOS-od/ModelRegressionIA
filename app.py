import pickle

import numpy as np
from flask import Flask, render_template, request

model = pickle.load(open('modelel.pk', 'rb'))


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post_login', methods=['post', 'get'])
def post_page():
    for x in request.form.values():

        if not x:
            erreur = 'Veuillez Renseignez Tout les champs'
            return render_template('index.html', erreur=erreur)

    recup_data = [int(x) for x in request.form.values()]
    features = np.array(recup_data)
    features = features.reshape(1, -1)
    prediction = model.predict(features)

    return render_template('index.html', predict=prediction)


if __name__ == "__main__":
    app.run(debug=True)
