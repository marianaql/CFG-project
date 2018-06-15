# This is our CFG-project


Bachelor's Degree in Bioinformatics <br />
Comparative and Functional Genomics <br />
**Authors: Mariana Quiroga & Jordi Busoms** <br />


The project focus on the functional characterization of unknown proteins using different tools based on comparative genomics and differential gene expression.<br />

- `sequences.txt`contains 10 unknown proteins from the species *Penicillium polonicum*.
- `get_orthologs.py`contains a `Python` code that reads `blastp` results on 6 format and searches for the sequences of the  best hits for every queried sequences on the database file you want to use. <br /> 
- We used `Biopython` to parse fasta format. <br />
1. **Optional arguments**: *Desired_number_of_hits_retrieved, blast_results_file, database_file*. To specify a file all arguments must be given. Notice that: <br />
    - If no new arguments are given, default values are taken as `20`, `results.out`, `blast_database_FCG2018.fasta`.
    - If only one argument is given, it is taken as *Desired_number_of_hits_retrieved*, *blast_results_file* and *database_file* are set to `results.out` and `blast_database_FCG2018.fasta`, respectively.
2. **Expected output:**: a file per each of the 10 sequences with its corresponding 20 orthologs sequences, in fasta format.


