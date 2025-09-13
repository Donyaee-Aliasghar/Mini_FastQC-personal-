"""Module for routing throughout the application."""

import os

# Find current path.
current_dir = os.path.dirname(__file__)

# Get raw file.
# =================== ! =========================
# my system path.
RAW_FILE = os.path.join(
    current_dir,
    "..",
    "..",
    "..",
    "..",
    "Raw_datas",
    "Bioinformatics",
    "FASTQ",
    "100k_reads_hiseq",
    "TESTX",
    "TESTX_H7YRLADXX_S1_L001_R1_001.fastq.gz",
)

# program path.
# RAW_FILE = os.path.join(current_dir, "..", "data", "*.fq")  # or *.fastq
# ============================================

# Normalization path.
MAIN_FILE = os.path.abspath(RAW_FILE)
