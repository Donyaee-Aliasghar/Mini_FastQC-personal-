"""Module to collect all FASTQ file purification operations."""

import os
import gzip

from .utils import average_quality

# Save pure fastq file.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_dir = os.path.join(project_root, "results")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "pure_fastq.fastq")


def purification(input_file, min_avg_quality=20):
    """Main function."""

    valid_base = set("ACGTN")
    written_count = 0
    if output_file is None:
        os.makedirs(output_dir, exist_ok=True)
    else:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with gzip.open(input_file, "rt") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        while True:
            header = infile.readline().strip()
            if not header:
                break  # End file.
            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            quality = infile.readline().strip()

            # Sequence check
            if not set(sequence).issubset(valid_base):
                continue

            # Quality check.
            if average_quality(quality) < min_avg_quality:
                continue

            # Write output file.
            outfile.write(f"{header}\n{sequence}\n{plus}\n{quality}\n")
            written_count += 1
    print(f"[INFO] Written records: {written_count}")
    if written_count == 0:
        print("[WARNING] No records passed filters. Check input and filter values.")
