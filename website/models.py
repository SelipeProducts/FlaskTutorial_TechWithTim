#from package import db var in __init__.py
from . import db

#gives user object tools for logging in
from flask_login import UserMixin
from sqlalchemy import func

#db.Model is a blueprint of db object
class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  firstname = db.Column(db.String(150))

  #each time user make note. Note is added to list
  note = db.relationship('Notes')

