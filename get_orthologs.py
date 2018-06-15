###################################################################

#Authors: Mariana Quiroga, Jordi Busoms

###################################################################

#Used libraries:

import os
import sys
from Bio import SeqIO

#Optional arguments: Desired_number_of_hits_retrieved, blast_results_file, database_file. To specify a file all arguments must be given
#Default values: 20, results.out, blast_database_FCG2018.fasta
try:
	Orthologs_num= sys.argv[1]
except:
	Orthologs_num=20
try:
	results_file=sys.argv[2]
	database_file=sys.argv[3]
except:
	results_file="results.out"
	database_file = "blast_database_FCG2018.fasta"


with open(results_file) as out:
	IDS={}			# IDS will contain all the target IDs asociated with its list of orthologs

	for line in out:
		if line.split()[0] not in IDS:
			IDS[line.split()[0]]=[]
		if len(IDS[line.split()[0]])<Orthologs_num+1:	#number of horthologs+ itself
			#if line.split()[0] != line.split()[1]:		#uncomment if do not want to find the target sequence itself.
			IDS[line.split()[0]].append(line.split()[1])


records = list(SeqIO.parse(database_file,"fasta"))

All_ids={}			# All_ids will contain all horthologs id associated with the querry it is hortholog to.

for ID1 in IDS:
	for ID2 in IDS[ID1]:
		All_ids[ID2]=ID1
		


###PARSING THE FASTA FILE
files={}			# will contain all taret ids with its file names.
for ID in IDS:
	files[ID]=open((str(ID)+'.ortho'), 'w')
print(files)
for record in records:
    ID= record.id
    if ID in All_ids:
        print(All_ids[ID])
        files[All_ids[ID]].write(('>'+record.id+'\n'))
        files[All_ids[ID]].write(str(record.seq +'\n'))
