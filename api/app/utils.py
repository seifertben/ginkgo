from Bio.Blast import NCBIWWW, NCBIXML
from flask import request
from app import app, db
from app.models import Result
import re

def parse_result(sequence):
    protein_name = ""
    protein_id = ""
    match_start = 0
    match_end = 0
    match_found = False
    align_length = 0
    for record in NCBIXML.parse(open("results.xml")): 
        if record.alignments:
            for align in record.alignments:
                hit_def = align.hit_def
                # Parse protein name and protein id out of search results.
                p1 = re.compile("\[protein=([^\[]*)\]")
                p2 = re.compile("\[protein_id=([^\[]*)\]")
                result1 = p1.search(hit_def)
                result2 = p2.search(hit_def)
                protein_name = result1.group(1)
                protein_id = result2.group(1)
                for hsp in align.hsps:
                    align_length = hsp.align_length
                    if(align_length == len(sequence)):
                        match_found = True
                    match_start = hsp.sbjct_start
                    match_end = hsp.sbjct_end

    record = Result(protein_name, protein_id, match_start, match_end, sequence)
    # Only save to the DB if a match was found and it is a complete match (no substring matches allowed)
    if (match_found):
        db.session.add(record)
        db.session.commit()
    
    return match_found, record

