from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))
