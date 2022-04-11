# FastBlast

### Introduction

FastBlast assists in searching for specific DNA sequences within proteins. Simply type your query in the search bar and hit enter and if there is a match, you will see it. There is also a history table to view the results of past searches.

### Implementation Details

The application consists of a React UI with a Flask API. All data is stored in a sqlite DB. The application also makes use of a local BLAST DB to get around the ridiculous slowness of the NCBI API.
