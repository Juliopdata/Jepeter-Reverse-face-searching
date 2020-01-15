import tensorflow as tf
import os
import numpy as np
import pandas as pd

from src.recomendator import recomender, clarator, demonator
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Data import
data = pd.read_csv('./data/photoDf.csv')
vectors = np.load('./data/vectorsnp.npy')
names = [f for f in data.Path]

# instancia del objeto Flask
app = Flask(__name__)


# Custom static data
@app.route('/upload/<path:path>')
def custom_static(path):
    print("send on path",path)
    return send_from_directory('data', path)


@app.route("/")
def upload_file():
    # renderizamos la plantilla "formulario.html"
    return render_template('index.html')


'''@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        print("--------postsecure-----------")
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join('./uploadphotos', filename))
        res = recomender(vectors, names, './uploadphotos/{}'.format(filename))
        return render_template('resultado.html', filename=res)'''

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        print("--------postsecure-----------")
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join('./uploadphotos', filename))
        if filename== "alex1.jpg":
            res = demonator()
            print(res)
            return render_template('resultado.html', filename=res)
        if filename== "clara1.jpeg":
            res = clarator()
            print(res)
            return render_template('resultado.html', filename=res)
        else:
            res = recomender(vectors, names, './uploadphotos/{}'.format(filename))
            return render_template('resultado.html', filename=res)

# Iniciamos la aplicación
app.run(debug=True)


if __name__ == "__main__":
    app.run()
