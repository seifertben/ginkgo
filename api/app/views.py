import flask
from flask import jsonify, request
from app.utils import find_protein
from app import app, db, q
from app.models import User
from rq.job import Job
from app.worker import conn


@app.route('/user', methods=['GET', 'POST'])
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

@app.route('/', methods=['POST'])
def index():
    sequence = request.args.get('seq')
    job = q.enqueue_call(
        func=find_protein, args=(sequence,), result_ttl=10
    )
    print(job.get_id())
    return jsonify(sequence)

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202
