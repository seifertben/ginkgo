from Bio.Blast import NCBIWWW
from Bio import SeqIO, Seq
from Bio.Seq import Seq
from flask import request
from app import app


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
