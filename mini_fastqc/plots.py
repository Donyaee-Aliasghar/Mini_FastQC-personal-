"""Module for visoalization."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from .utils import gc_content, phred_score


def ftcp(csv_file="report.csv", pdf_file="report.pdf", fastq_file=None):
    """Analysis fastq to csv and pdf."""
    import os

    if fastq_file is None:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        results_dir = os.path.join(project_root, "results")
        os.makedirs(results_dir, exist_ok=True)
        fastq_file = os.path.join(results_dir, "pure_fastq.fastq")
        if csv_file == "report.csv":
            csv_file = os.path.join(results_dir, "report.csv")
        if pdf_file == "report.pdf":
            pdf_file = os.path.join(results_dir, "report.pdf")

    ids, lengths, gc_percents, avg_qualities = [], [], [], []
    record_count = 0

    with open(fastq_file, "r", encoding="utf-8") as infile:
        while True:
            header = infile.readline().strip()
            if not header:
                break
            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            quality = infile.readline().strip()

            # Calculate.
            ids.append(header)
            lengths.append(len(sequence))
            gc_percents.append(gc_content(sequence))
            from .utils import base_quality_scores

            scores = base_quality_scores(quality)
            avg_qualities.append(sum(scores) / len(scores) if scores else 0)
            record_count += 1

    print(f"[INFO] Number of records processed: {record_count}")
    if record_count == 0:
        print("[WARNING] No records found in pure_fastq.fastq. Check input and filters.")

    # Create DataFrame.
    df = pd.DataFrame({"Read_ID": ids, "Length": lengths, "GC_Content": gc_percents, "Average_Quality": avg_qualities})

    # Save CSV.
    df.to_csv(csv_file, index=False)
    print(f"[✅] CSV file created : {csv_file}")

    # Create summary report PDF.
    with PdfPages(pdf_file) as pdf:
        # Lenght sequence chart.
        plt.figure(figsize=(8, 5))
        plt.hist(df["Length"], bins=20, color="skyblue", edgecolor="black")
        plt.title("Distribution of Read Lengths")
        plt.xlabel("Length")
        plt.ylabel("Count")
        pdf.savefig()
        plt.close()

        # GC content chart.
        plt.figure(figsize=(8, 5))
        plt.hist(df["GC_Content"], bins=20, color="lightgreen", edgecolor="black")
        plt.title("GC Content Distribution")
        plt.xlabel("GC %")
        plt.ylabel("Count")
        pdf.savefig()
        plt.close()

        # Average quality chart.
        plt.figure(figsize=(8, 5))
        plt.hist(df["Average_Quality"], bins=20, color="salmon", edgecolor="black")
        plt.title("Average Quality Distribution")
        plt.xlabel("Average Quality")
        plt.ylabel("Count")
        pdf.savefig()
        plt.close()

    print(f"PDF file created : ../results/report.pdf")
