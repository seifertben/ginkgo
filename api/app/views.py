import flask
from flask import jsonify, request
from app import app, db
from app.models import Result
from app.utils import parse_result
from Bio.Blast.Applications import NcbiblastnCommandline

@app.route('/protein', methods=['GET'])
def find_protein():
    sequence = request.args.get('seq')
    f = open("db/queries/query.fsa", "w")
    f.write(sequence)
    f.close()
    blastn_cline = NcbiblastnCommandline(query = "db/queries/query.fsa", db = "db/out", outfmt = 5, out = "results.xml", perc_identity = 100, task="blastn-short", qcov_hsp_perc=100)
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
