"""Unit tests for the plotting module."""

import pandas as pd
from mini_fastqc.plots import ftcp


def test_ftcp_creates_csv_and_pdf(tmp_path):
    """Checks that CSV and PDF files are created with correct content."""

    # Create a dummy FASTQ file
    fastq_file = tmp_path / "pure_fastq.fastq"
    with open(fastq_file, "w", encoding="utf-8") as f:
        f.write("@read1\nAGCT\n+\nIIII\n@read2\nCGTA\n+\nHHHH\n")

    csv_file = tmp_path / "report.csv"
    pdf_file = tmp_path / "report.pdf"

    ftcp(csv_file=str(csv_file), pdf_file=str(pdf_file))

    assert csv_file.exists()
    assert pdf_file.exists()
    df = pd.read_csv(csv_file)
    assert "Read_ID" in df.columns
    assert len(df) == 2
