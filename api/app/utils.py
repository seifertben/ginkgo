from Bio.Blast import NCBIWWW
from Bio import SeqIO, Seq
from Bio.Seq import Seq
from flask import request
from app import app
from Bio.Blast import NCBIXML
from app import app, db, q
from app.models import Result
import re

def find_protein(sequence):
    sequence = request.args.get('seq')
    # record = SeqIO.read("m_cold.fasta", format="fasta")
    with app.app_context():
        result = NCBIWWW.qblast("blastp", "nr", Seq(sequence), 
            entrez_query = "txid10506[ORGN]",
            perc_ident = 100
        )
    with open('./results.xml', 'w') as save_file: 
        blast_results = result.read() 
        save_file.write(blast_results)
    print(sequence)


def parse_result(sequence):
    E_VALUE_THRESH = 1e-20
    protein_name = ""
    protein_id = ""
    match_start = 0
    match_end = 0
    match_found = False
    align_length = 0
    for record in NCBIXML.parse(open("results.xml")): 
        if record.alignments:
            for align in record.alignments:
                match_found = True
                hit_def = align.hit_def
                # Parse protein name and protein id out of search results.
                p1 = re.compile("\[protein=([^\[]*)\]")
                p2 = re.compile("\[protein_id=([^\[]*)\]")
                result1 = p1.search(hit_def)
                result2 = p2.search(hit_def)
                protein_name = result1.group(1)
                protein_id = result2.group(1)
                for hsp in align.hsps:
                    match_start = hsp.sbjct_start
                    match_end = hsp.sbjct_end

    record = Result(protein_name, protein_id, match_start, match_end, sequence)
    # Only save to the DB if a match was found and it is a complete match (no substring matches allowed)
    if (match_found):
        db.session.add(record)
        db.session.commit()
    
    return match_found, record

