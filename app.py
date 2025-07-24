import os
from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from werkzeug.utils import secure_filename
from models.database import db, Plat
import pytesseract
from PIL import Image
import re

app = Flask(__name__)
app.secret_key = "ma_cle_secrete"

# Connexion à MySQL (via XAMPP)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/menu_restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration dossier d’upload
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_text():
    file = request.files['image']
    if file:
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        # Extraction brute du texte
        image = Image.open(path)
        extracted_text = pytesseract.image_to_string(image)

        return jsonify({"text": extracted_text})
    return jsonify({"error": "No file uploaded"}), 400

if __name__ == '__main__':
    app.run(debug=True)