def dna_to_rna(sequence):
    """
    Convert a DNA sequence to its RNA equivalent.
    Example: DNA 'ATCG' → RNA 'AUCG'
    """
    sequence = sequence.upper()  # ensure consistent format
    rna_sequence = sequence.replace("T", "U")
    return rna_sequence


if __name__ == "__main__":
    dna = input("Enter a DNA sequence: ").strip()
    rna = dna_to_rna(dna)
    print(f"RNA Sequence: {rna}")
