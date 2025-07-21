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
    if request.method == 'POST':
        nom = request.form.get('nom')
        prix = request.form.get('prix')
        image = request.files.get('image')

        # Sauvegarder l'image si elle existe
        image_path = ""
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(upload_path)
            image_path = os.path.join("uploads", filename).replace("\\", "/")
        else:
            image_path = ""


        nouveau_plat = Plat(nom=nom, prix=prix, image_url=image_path)
        db.session.add(nouveau_plat)
        db.session.commit()

        return redirect(url_for('accueil'))

    plats = Plat.query.all()
    return render_template("index.html", plats=plats)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)