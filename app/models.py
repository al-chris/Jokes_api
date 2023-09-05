from app import db, app

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(500))
    answer = db.Column(db.String(500))
    author = db.Column(db.String(50))
