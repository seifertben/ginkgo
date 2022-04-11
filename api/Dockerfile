FROM python:3.8-slim-buster

WORKDIR /python-docker

RUN apt-get update
RUN apt-get -y install ncbi-blast+

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN makeblastdb -in db/mydb.fasta -dbtype nucl -out db/out

CMD python3 -m flask run --host=0.0.0.0 --port=$PORT
# CMD python3 -m flask run --host=0.0.0.0 --port=5000
