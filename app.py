import tensorflow as tf
from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
from recomendator import recomender
import numpy as np
import pandas as pd
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = pd.read_csv('./data/photoDf.csv')
vectors = np.load('vectorsnp.npy')
names = [f for f in data.Path]

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './uploadphotos'


@app.route("/")
def upload_file():
    # renderiamos la plantilla "formulario.html"
    return render_template('index3.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        res = recomender(vectors, names, './uploadphotos/{}'.format(filename))
        return res

    # Iniciamos la aplicación
    app.run(debug=True)


if __name__ == "__main__":
    app.run()
