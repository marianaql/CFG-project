# This is our CFG-project


Bachelor's Degree in Bioinformatics <br />
Comparative and Functional Genomics <br />
**Authors: Mariana Quiroga & Jordi Busoms** <br />


The project focus on the functional characterization of unknown proteins using different tools based on comparative genomics and differential gene expression.<br />

- `sequences.txt`contains 10 unknown proteins.
- `get_orthologs.py`contains a `Python` code that reads bastn results on format 6 and searches for the sequences of the n best hits for every queried sequences on the database file.<br /> 
We used `Biopython`to parse fasta format . <br />
Optional arguments: Desired_number_of_hits_retrieved, blast_results_file, database_file. To specify a file all arguments must be given.<br />
If no arguments are giben default values are taken as 20, results.out, blast_database_FCG2018.fasta.<br />
If only one argument is given it's taken as Desired_number_of_hits_retrieved. blast_results_file and database_file are set to results.out and blast_database_FCG2018.fasta respectively.


