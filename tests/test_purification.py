"""Unit tests for the purification module."""

import os
import gzip
from mini_fastqc.purification import purification


def test_purification_creates_output(tmp_path):
    """Checks that the output file is created and contains purified data."""

    sample_path = tmp_path / "sample.fastq.gz"
    with gzip.open(sample_path, "wt") as f:
        f.write("@read1\nAGCT\n+\nIIII\n@read2\nCGTA\n+\nHHHH\n")

    output_file = f"{tmp_path / 'pure_fastq.fastq'}"
    purification(str(sample_path), min_avg_quality=0, output_file=output_file)

    assert output_file.exists()
    with open(output_file, "rt", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 8


def test_purification_quality_filter(tmp_path):
    """Checks that reads below the quality threshold are filtered out."""
    sample_path = tmp_path / "sample.fastq.gz"
    with gzip.open(sample_path, "wt") as f:
        f.write("@read1\nAGCT\n+\n!!!!\n@read2\nCGTA\n+\nHHHH\n")
    purification(str(sample_path), min_avg_quality=40)
    of = os.path.join(os.path.dirname(__file__), "..", "mini_fastqc", "results", "pure_fastq.fastq")
    with open(of, "rt", encoding="utf-8") as f:
        lines = f.readlines()
    # Only the high-quality read should remain
    assert len(lines) == 4
