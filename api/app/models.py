from app         import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protein_name = db.Column(db.String(500), nullable=False)
    protein_id = db.Column(db.String(50), nullable=True)
    match_start = db.Column(db.Integer, nullable=False)
    match_end = db.Column(db.Integer, nullable=False)
    search_string = db.Column(db.String(1000), nullable=False)
    created_dttm = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.protein_name

    def __init__(self, protein_name, protein_id, match_start, match_end, search_string):
        self.protein_name = protein_name
        self.protein_id = protein_id
        self.match_start = match_start
        self.match_end = match_end
        self.search_string = search_string
    
    def serialize(self):
        return {
            'id': self.id,
            'protein_name': self.protein_name, 
            'protein_id': self.protein_id,
            'match_start': self.match_start,
            'match_end': self.match_end,
            'search_string': self.search_string,
            'created_dttm': self.created_dttm
        }
