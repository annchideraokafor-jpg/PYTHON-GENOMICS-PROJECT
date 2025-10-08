"""Small utility to check whether a sequence contains only DNA bases.

This module provides `is_valid_dna(sequence)` which returns True when the
sequence contains only the canonical DNA bases: A, T, C, G. The check is case-
insensitive and ignores surrounding whitespace.
"""

from typing import Iterable


def is_valid_dna(sequence: str) -> bool:
    """Return True if `sequence` contains only A, T, C, G characters.

    The check is case-insensitive and treats an empty sequence as False.
    Non-string inputs will raise a TypeError.
    """
    if not isinstance(sequence, str):
        raise TypeError("sequence must be a string")

    seq = sequence.strip().upper()
    if not seq:
        return False

    valid_bases = {'A', 'T', 'C', 'G'}
    return all(base in valid_bases for base in seq)


if __name__ == "__main__":
    # simple smoke test
    default_sequence = "ATGCGTAACGO"
    print(f"sequence: {default_sequence}")
    print("Valid DNA?", is_valid_dna(default_sequence))