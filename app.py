import os
from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from models.database import db, Plat

app = Flask(__name__)
app.secret_key = "ma_cle_secrete"

# Connexion à MySQL (via XAMPP)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/menu_restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration dossier d’upload
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

db.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def accueil():
    return render_template("index.html")
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)