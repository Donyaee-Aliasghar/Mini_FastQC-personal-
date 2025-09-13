import os
import gzip
import pytest
from mini_fastqc.purification import purification


def test_purification_creates_output(tmp_path):
    import gzip
    from mini_fastqc.purification import purification

    sample_path = tmp_path / "sample.fastq.gz"
    with gzip.open(sample_path, "wt") as f:
        f.write("@read1\nAGCT\n+\nIIII\n@read2\nCGTA\n+\nHHHH\n")

    output_file = tmp_path / "pure_fastq.fastq"
    purification(str(sample_path), min_avg_quality=0, output_file=str(output_file))

    assert output_file.exists()
    with open(output_file) as f:
        lines = f.readlines()
    assert len(lines) == 8


def test_purification_quality_filter(tmp_path):
    sample_path = tmp_path / "sample.fastq.gz"
    with gzip.open(sample_path, "wt") as f:
        f.write("@read1\nAGCT\n+\n!!!!\n@read2\nCGTA\n+\nHHHH\n")
    purification(str(sample_path), min_avg_quality=40)
    output_file = os.path.join(os.path.dirname(__file__), "..", "mini_fastqc", "results", "pure_fastq.fastq")
    with open(output_file) as f:
        lines = f.readlines()
    # فقط رکورد دوم باید باقی بماند
    assert len(lines) == 4
