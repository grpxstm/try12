from flask import flask
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import warnings
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
warnings.filterwarnings("ignore", category=DeprecationWarning) 


def import_and_predict(image_data, model):
image = ImageOps.fit(image_data, (100,100),Image.ANTIALIAS)
    image = image.convert('RGB')
    image = np.asarray(image)
    flask.image(image, channels='RGB')
    image = (image.astype(np.float32) / 255.0)
    img_reshape = image[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction

model = tf.keras.models.load_model('my_model2.h5')
print('****GLAUCOMA DETECTOR GROUP 10')



UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    if request.method == 'POST':
     
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
      
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
