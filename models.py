from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
GENERIC_IMAGE = "https://tse3.mm.bing.net/th?id=OIP.bpcFDYoSrCuxUx4-wCI5wAAAAA&pid=Api&P=0&h=220"
db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    species = db.Column(db.String(50),nullable=False)
    photo_url = db.Column(db.String(500),nullable=True)
    age = db.Column(db.Integer,nullable=True)
    notes = db.Column(db.String(500),nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)

    def image_url(self):
        
        return self.photo_url or GENERIC_IMAGE
