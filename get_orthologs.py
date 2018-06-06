##AUTHORS: Jordi Busoms & Mariana Quiroga 

import os
import sys
from Bio import SeqIO

with open(sys.argv[1]) as out: #sys.argv[1] that will contain the Blast results
	IDS={}
	try:
		Orthologs_num = sys.argv[3] #sys.argv[3] is the number of hits from which you will take a sequence per each.
                #If it does not find anything, it will take 20 sequences by default.

	except:
		Orthologs_num = 20
	for line in out:
		if line.split()[0] not in IDS:
			IDS[line.split()[0]] = []
		if len(IDS[line.split()[0]])<Orthologs_num:
			if line.split()[0] != line.split()[1]:
				IDS[line.split()[0]].append(line.split()[1])

line=""
records = list(SeqIO.parse("blast_database_FCG2018.fasta","fasta"))
All_ids=set()

for ID2 in IDS[sys.argv[2]]: #The target sequence from which you want to print the hits.
	All_ids.add(ID2)
		
#This is how we do the parsing of the fasta format
for record in records:
    ID= record.id
    if ID in All_ids:
		print('>'+record.id)
		print(record.seq)
    


