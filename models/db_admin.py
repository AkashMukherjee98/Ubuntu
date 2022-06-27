#from Apps import db
from db_con import db

class Admin(db.Model):
    __tablename__ = 'admin'
    aid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    adminName = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)