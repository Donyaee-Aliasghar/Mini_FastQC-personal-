"""This module is for executing all the different parts of the code in one place."""

import os
import argparse

from mini_fastqc.pathes import MAIN_FILE

from mini_fastqc.purification import purification as p
from mini_fastqc.qc import analyze_clean_fastq as acf
from mini_fastqc.plots import ftcp

parser = argparse.ArgumentParser(description="FASTQ Cleaner & Analyzer: CSV + PDF report")
parser.add_argument("-c", "--csv", default="report.csv", help="Output CSV file")
parser.add_argument("-p", "--pdf", default="report.pdf", help="Output PDF file")
parser.add_argument("-q", "--min_qual", type=float, default=None, help="Min avg qual to keep read")

args = parser.parse_args()


def runner():
    """Collection location."""

    # Raw FASTA file check.
    if not os.path.isfile(MAIN_FILE):
        raise FileNotFoundError(f"[❌] Raw file not found: {MAIN_FILE}")

    print("[✅] Pure FASTA file found >> read file...")
    print("[✅] Start operations...")

    # Phace 1 : cleaning and filter readings.
    p(MAIN_FILE, min_avg_quality=args.min_quality)

    # Phace 2 : operations.
    acf()

    # Phace 3 : created PDF and CSV.
    ftcp(csv_file=args.csv, pdf_file=args.pdf)

    print("=" * 40)
