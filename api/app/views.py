import flask
from flask import jsonify
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def save_user():
    if flask.request.method == 'POST':
        record = User("username", "email")
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        return 'Saved a new User!'
    else:
        user = User.query.get(1)
        return jsonify(user)
