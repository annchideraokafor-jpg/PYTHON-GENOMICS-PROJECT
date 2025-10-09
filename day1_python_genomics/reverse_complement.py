def reverse_complement(sequence):
    """
    Return the reverse complement of a DNA sequence.
    Example: 'ATGC' → 'GCAT'
    """
    # Convert to uppercase
    sequence = sequence.upper()

    # Dictionary for base pairing
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    # Generate complement sequence
    comp_seq = ''
    for base in sequence:
        comp_seq += complement.get(base, 'N')  # 'N' for unknown bases

    # Reverse the complemented sequence
    rev_comp = comp_seq[::-1]

    return rev_comp


if __name__ == "__main__":
    dna = input("Enter a DNA sequence: ").strip()
    result = reverse_complement(dna)
    print(f"Reverse Complement: {result}")
