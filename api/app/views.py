import flask
from flask import jsonify, request
from app import app, db, q
from app.models import User, Result
from rq.job import Job
from worker import conn
from app.utils import find_protein, parse_result

from Bio.Blast import NCBIWWW
from Bio import SeqIO, Seq
from Bio.Seq import Seq
from Bio.Blast.Applications import NcbiblastnCommandline

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

@app.route('/protein', methods=['GET'])
def find_protein():
    sequence = request.args.get('seq')
    f = open("db/queries/query.fsa", "w")
    f.write(sequence)
    f.close()
    print(sequence)
    blastn_cline = NcbiblastnCommandline(query = "db/queries/query.fsa", db = "db/out", outfmt = 5, out = "results.xml", perc_identity = 100, max_target_seqs = 1)
    stdout, stderr = blastn_cline()
    result = parse_result(sequence)
    match_found = result[0]
    record = result[1]
    if (match_found):
        return jsonify(record.serialize())
    else:
        return jsonify(None)


@app.route("/searches", methods=['GET'])
def get_searches():
    searches = Result.query.all()
    return jsonify([search.serialize() for search in searches])
