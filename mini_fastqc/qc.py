"""Modue for FASTQ calculating."""

import os

from .utils import (
    base_quality_scores,
    average_quality,
    g_count,
    c_count,
    gc_content,
    a_count,
    t_count,
    at_content,
    content_formule,
)

# Save report fastq file.
output_file = os.path.join(os.path.dirname(__file__), "..", "results", "quality_report.txt")


def analyze_clean_fastq():
    """Quality calculate."""

    with open("results/pure_fastq.fastq", "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as report:
        while True:
            header = infile.readline().strip()
            if not header:
                break
            seq = infile.readline().strip()
            quality = infile.readline().strip()

            scores = base_quality_scores(quality)
            avg = average_quality(quality)

            # Write report
            report.write("=" * 30 + " Average quality " + "=" * 30 + "\n\n")

            # quality
            report.write("-" * 30 + " Quality " + "-" * 30)
            report.write(f"\n{header}\n")
            report.write(f"Sequence: {seq}\n")
            report.write(f"Quality per base: {scores}\n")
            report.write(f"Average quality: {avg:.10f}\n")

            # content
            report.write("-" * 30 + " GC content " + "-" * 30)
            report.write(f"\nG content: {g_count(seq)} ({content_formule(g_count(seq),seq):.10f} %)\n")
            report.write(f"\nC content: {c_count(seq)} ({content_formule(c_count(seq),seq):.10f} %)\n")
            report.write(f"\nGC content: {gc_content(seq)} ({content_formule(gc_content(seq),seq):.10f} %)\n")
            report.write(f"\nA content: {a_count(seq)} ({content_formule(a_count(seq),seq):.10f} %)\n")
            report.write(f"\nT content: {t_count(seq)} ({content_formule(t_count(seq),seq):.10f} %)\n")
            report.write(f"\nAT content: {at_content(seq)} ({content_formule(at_content(seq),seq):.10f} %)\n")

            # Length
            report.write("-" * 30 + " Length sequence " + "-" * 30)
            report.write(f"\nLength sequence: {len(seq):.5f}%\n")

    print("[✅] Quality report created : ../results/quality_report.txt")
