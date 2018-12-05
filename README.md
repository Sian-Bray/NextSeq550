# NextSeq550
A few simple scripts to help with demultiplexing NextSeq550 data.
NextSeq_check_SampleSheet_illumina_barcodes.py will check that there are no typos in the Illumina barcoded you have input into your demultiplexing sample sheet (SampleSheet.csv). This is useful to catch human errors in barcode entry.
NextSeq_create_SampleSheet.py will turn Illumina Adapter Plate Dual-Index indicies (e.g. A1, B7, E3) into barcodes in your demultiplexing sample sheet (SampleSheet.csv). This makes the whole process less painful and avoids human errors in barcode entry.
demultiplex_NextSeq_combine_statistics.py combines demultiplexing statistics for the same samples from multiple sequencing runs. This is useful if you want an overview of your sequencing from multiple attempts.
Notes on use are in the comments at the top of the files.
