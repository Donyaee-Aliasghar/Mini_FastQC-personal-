<!-- About project -->
    FASTQ Cleaner & Analyzer
    This program is a command-line tool (CLI) for cleaning and analyzing FASTQ files.

    Features:
    1.Read Cleaning: Removes sequences with invalid characters and reads below a configurable quality threshold.
    2.Sequence Analysis: Computes read length, GC content, average quality, and per-base Phred scores.
    3.Professional Outputs:
        3-1.CSV: Contains detailed information for each read for downstream analysis.
        3-2.PDF: Visualizations including read length distribution, GC content, and average quality.
    4.Easy CLI: Run the program from the command line with configurable input/output options.

<!-- Initial configuration -->
    1.Go to the data directory and add complete FASTQ file(.gz).
    2.Go to the mini_fastqc > pathes.py and add fastq data name to program path part(uncomment this and command my system path codes). 

<!-- How to run -->
    1.GO to directory Mini_FastQC(personal)
    2.Run > python3 main.py -c(CSV) <name>.csv -p(PDF) <name>.pdf -q(min guality) <...>
