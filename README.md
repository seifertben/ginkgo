# FastBlast

### Introduction

FastBlast assists in searching for specific DNA sequences within proteins. Simply type your query in the search bar and hit enter and if there is a match, you will see it. There is also a history table to view the results of past searches.

### How to Run

Run `docker-compose up` from the root directory. This will launch the API and webapp and you can immediately begin querying. Queries must be 10 or longer for the Blast algorithm to find matches. I discuss this in the limitations section.

### Implementation Details

The application consists of a React UI with a Flask API. All data is stored in a sqlite DB. The application also makes use of a local BLAST DB to get around the ridiculous slowness of the NCBI API.

### Limitations and Time Constraints

The Blast Algorithm seems to require a minimum query length of 10 (this is also dependent on the settings passed in). I would like to research this more and see if searching on shorter sequences can be accomodated.

If the amount of data were to expand, it might become neceessary to implement a queue system to process jobs. I had started with a Redis cache to queue these jobs but I realized it would not be necessary with a local DB, givn the good performance. I found the NCBI API to be so slow it was practically worthless.
