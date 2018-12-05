#Written by Sian Bray on 7th March 2018
#This code takes a sample sheet with the sample name in the first column and the index location in the second column and fills in the adapters
#It fills in Illumina Adapter Plate Dual-Index indicies(described here: https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/samplepreps_truseq/truseqsampleprep/truseq-library-prep-pooling-guide-15042173-01.pdf)
#It uses a sample sheet saved as SampleSheet.csv for use with bcl2fastq (described here:https://www.illumina.com/content/dam/illumina-marketing/documents/products/technotes/sequencing-sheet-format-specifications-technical-note-970-2017-004.pdf)
#Under [data] (on line 18) the sample sheet must have the following column headers (on line 19): Sample_ID, Sample_Name, Sample_Plate, Sample_Well, I7_Index_ID, index, I5_Index_ID, index2, Sample_Project, Description
#The list of samples must start on line 20
#Put sample name (e.g. Sample1) under Sample_ID and adapter plate location (e.g. A1) under Sample_Name
#Make sure all the letters in Sample_Name are capitalized (i.e. H12 not h12). They can only contain one letter (A-H) and on number (1-12) with no spaces.
#Make sure the file is saved as a comma delaminated file (.csv)

#These are the index IDs and indicies using the row/column axis of the table as a key. This works because all the I7 indexes in row 1 are D701 and all the I5 indexes in column A areD501.
x_axis_numbers_D7_adapters={"1":"D701,ATTACTCG", "2":"D702,TCCGGAGA", "3":"D703,CGCTCATT", "4":"D704,GAGATTCC", "5":"D705,ATTCAGAA", "6":"D706,GAATTCGT", "7":"D707,CTGAAGCT", "8":"D708,TAATGCGC", "9":"D709,CGGCTATG", "10":"D710,TCCGCGAA", "11":"D711,TCTCGCGC", "12":"D712,AGCGATAG"}
y_axis_letters_D5_adapters_reverse_complimented={"A":"D501,AGGCTATA", "B":"D502,GCCTCTAT", "C":"D503,AGGATAGG", "D":"D504,TCAGAGCC", "E":"D505,CTTCGCCT", "F":"D506,TAAGATTA", "G":"D507,ACGTCCTG", "H":"D508,GTCAGTAC"}

input_file=open("SampleSheet.csv", "r") #This is your input file, make sure it is the same as below (line 17)
new_SampleSheet=open("SampleSheet_new.csv", "w+") #This will create a new file, rename as you like
number_of_lines = len(open("SampleSheet.csv", "r").readlines()) #This is also your input file, make sure it is the same as above (line 15)
line_number_count=0

while line_number_count<number_of_lines: #This reads through each line in turn
	current_line=input_file.readline()
	if line_number_count<19: #This simply rewrites the file until it reaches the samples
		new_SampleSheet.write(current_line)
		line_number_count=line_number_count+1
	elif line_number_count>=19: #When it reaches the samples...
		current_line_list=current_line.split(",") #...it splits the line by column...
		adapter_position=list(current_line_list[1]) #...and reads the index plate location (e.g. A1).
		if len(adapter_position)>2: #If the number is double digits...
			adapter_position[1]=adapter_position[1]+adapter_position[2] #...it puts them back together (they are still strings so "1"+"1"="11" not 2).
		new_SampleSheet.write(current_line_list[0])#This then rewrites what was in the old file into the new one
		new_SampleSheet.write(",")
		new_SampleSheet.write(current_line_list[1])
		new_SampleSheet.write(",")
		new_SampleSheet.write(current_line_list[2])
		new_SampleSheet.write(",")
		new_SampleSheet.write(current_line_list[3])
		new_SampleSheet.write(",")
		new_SampleSheet.write(x_axis_numbers_D7_adapters[adapter_position[1]]) #Until it reaches the index ID and sequence, where it uses the adapter plate location you gave in SampleSheet.csv as a dictionary key to identify and write the correct barcode.
		new_SampleSheet.write(",")
		new_SampleSheet.write(y_axis_letters_D5_adapters_reverse_complimented[adapter_position[0]])
		new_SampleSheet.write(",")
		new_SampleSheet.write(current_line_list[8])
		new_SampleSheet.write(",")
		new_SampleSheet.write(current_line_list[9])
		line_number_count=line_number_count+1
		#While loop ends here
		
input_file.close()
new_SampleSheet.close()

print("New sample sheet created! :)")