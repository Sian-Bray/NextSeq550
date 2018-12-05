#Written by Sian Bray on 8th March 2018
#This script checks a demultiplexing sample sheet for correct barcodes.
#It looks for Illumina Adapter Plate Dual-Index indicies(described here: https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/samplepreps_truseq/truseqsampleprep/truseq-library-prep-pooling-guide-15042173-01.pdf)
#It uses a sample sheet saved as SampleSheet.csv for use with bcl2fastq (described here:https://www.illumina.com/content/dam/illumina-marketing/documents/products/technotes/sequencing-sheet-format-specifications-technical-note-970-2017-004.pdf)
#Under [data] (on line 18) the sample sheet must have the following column headers (on line 19): Sample_ID, Sample_Name, Sample_Plate, Sample_Well, I7_Index_ID, index, I5_Index_ID, index2, Sample_Project, Description
#The indexes must start on line 20
#It checks index sequence and orientation (i.e. reverse complemented I5 index, but not I7 index).
#It also checks that the index IDs entered match the barcodes entered
#results are printed to the terminal, errors are indicated with <---

#These are the index sequences and index IDs
I7_adapter_sequence=("ATTACTCG", "TCCGGAGA", "CGCTCATT", "GAGATTCC", "ATTCAGAA", "GAATTCGT", "CTGAAGCT", "TAATGCGC", "CGGCTATG", "TCCGCGAA", "TCTCGCGC", "AGCGATAG")
I7_adapter_sequence_reverse_complimented=("CGAGTAAT", "TCTCCGGA", "AATGAGCG", "GGAATCTC", "TTCTGAAT", "ACGAATTC", "AGCTTCAG", "GCGCATTA", "CATAGCCG", "TTCGCGGA", "GCGCGAGA", "CTATCGCT")
I7_adapter_name=("D701", "D702", "D703", "D704", "D705", "D706", "D707", "D708", "D709", "D710", "D711", "D712")
I5_adapter_sequence=("TATAGCCT", "ATAGAGGC", "CCTATCCT", "GGCTCTGA", "AGGCGAAG", "TAATCTTA", "CAGGACGT", "GTACTGAC")
I5_adapter_sequence_reverse_complimented=("AGGCTATA", "GCCTCTAT", "AGGATAGG", "TCAGAGCC", "CTTCGCCT", "TAAGATTA", "ACGTCCTG", "GTCAGTAC")
I5_adapter_name=("D501", "D502", "D503", "D504", "D505", "D506", "D507", "D508")

input_file=open("SampleSheet.csv", "r") #This is your input file
number_of_lines = len(open("SampleSheet.csv", "r").readlines()) #This is your input file too, make sure they are the same
line_number_count=0

while line_number_count<number_of_lines:
	current_line=input_file.readline()
	if line_number_count<19: #This skips all of the details/headers on the first 19 lines
		line_number_count=line_number_count+1
	elif line_number_count>=19:
		current_line_list=current_line.split(",")
		I7_list_position_count=0
		while I7_list_position_count<12: #This cycles through all of the I7 indexes
			if current_line_list[5]==I7_adapter_sequence[I7_list_position_count]: #This checks the index sequences (not reverse complimented)
				print(current_line_list[0]+ " I7 adapter is "+ I7_adapter_name[I7_list_position_count]) #When the index sequence is found it is printed
				if current_line_list[4]!=I7_adapter_name[I7_list_position_count]: #The index ID is then checked
					print(current_line_list[0]+" I7_index_ID does not match index! Double check that this is the correct adapter sequence!   <---") #If the index ID is wrong a warning is printed
				break #The while loop stops once an index is found
			if current_line_list[5]==I7_adapter_sequence_reverse_complimented[I7_list_position_count]: #This checks the reverse complimented index sequences
				print(current_line_list[0]+ " I7 adapter is "+ I7_adapter_name[I7_list_position_count]+ " reverse complemented, you need to fix this!   <---") #If the index is reverse complimented a warning is printed
				if current_line_list[4]!=I7_adapter_name[I7_list_position_count]:
					print(current_line_list[0]+" I7_index_ID does not match index! Double check that this is the correct adapter sequence!   <---") #If the index ID is wrong a warning is printed
				break #The while loop stops once an index is found
			I7_list_position_count=I7_list_position_count+1
		if I7_list_position_count==12: #If the index sequence does not match any of the illumina I7 indexes a warning is printed
			print(current_line_list[0]+ " I7 adapter is not recognised! You need to fix this!   <---")
		I5_list_position_count=0
		while I5_list_position_count<8: #This does the same (as the while loop starting line 30) for all the I5 indexes, except that the I5 indexes SHOULD be reverse complimented
			if current_line_list[7]==I5_adapter_sequence[I5_list_position_count]:
				print(current_line_list[0]+ " I5 adapter is "+ I5_adapter_name[I5_list_position_count]+ ". You need to reverse complement this!   <---") #If the I5 index is NOT reverse complimented a warning is printed
				if current_line_list[6]!=I5_adapter_name[I5_list_position_count]:
					print(current_line_list[0]+" I5_index_ID does not match index! Double check that this is the correct adapter sequence!   <---")
				break
			if current_line_list[7]==I5_adapter_sequence_reverse_complimented[I5_list_position_count]:
				print(current_line_list[0]+ " I5 adapter is "+ I5_adapter_name[I5_list_position_count])
				if current_line_list[6]!=I5_adapter_name[I5_list_position_count]:
					print(current_line_list[0]+" I5_index_ID does not match index! Double check that this is the correct adapter sequence!   <---")
				break
			I5_list_position_count=I5_list_position_count+1
		if I5_list_position_count==8:
			print(current_line_list[0]+ " I5 adapter is not recognised! You need to fix this!   <---")
		line_number_count=line_number_count+1

input_file.close()