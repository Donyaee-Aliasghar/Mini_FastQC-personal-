"""Utility functions for Mini FastQC."""


def phred_score(char):
    """Convert quality character to phred number."""
    return ord(char) - 33


def base_quality_scores(qs):
    """Calculate base quality."""
    return [phred_score(c) for c in qs]


def average_quality(qs):
    """Average quality calculate."""
    scores = base_quality_scores(qs)
    return sum(scores) / len(scores)  # return > avg


def content_formule(count, sequence):
    """Content formule."""
    return (count / len(sequence)) * 100


def g_count(sequence):
    """G countent."""
    return sequence.count("G")


def c_count(sequence):
    """C countent."""
    return sequence.count("C")


def a_count(sequence):
    """A countent."""
    return sequence.count("A")


def t_count(sequence):
    """T countent."""
    return sequence.count("T")


def gc_content(sequence):
    """GC percent calculate for per sequence."""
    gc_count = g_count(sequence) + c_count(sequence)
    return content_formule(gc_count, sequence)


def at_content(sequence):
    """AT percent calculate for per sequence."""
    at_count = a_count(sequence) + t_count(sequence)
    return content_formule(at_count, sequence)
