import tensorflow as tf
from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
import os
from recomendator import recomender, demonator, clarator
import numpy as np
import pandas as pd
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = pd.read_csv('./data/photoDf.csv')
vectors = np.load('vectorsnp.npy')
names = [f for f in data.Path]

# instancia del objeto Flask
app = Flask(__name__)

# Carpeta static alternativa
# Carpeta de subida

# Custom static data
@app.route('/upload/<path:path>')
def custom_static(path):
    print("send on path",path)
    return send_from_directory('data', path)


@app.route("/")
def upload_file():
    # renderiamos la plantilla "formulario.html"
    return render_template('index.html')


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
