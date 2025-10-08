def is_valid_dna(sequence):
    valid_bases = {"A", "T", "G", "C"}
    for base in sequence:
        if base not in valid_bases:
            return False
    return True

dna_seq = "ATGCGTAACGT"
print(f"Sequence: {dna_seq}")
print("Valid DNA?" , is_valid_dna(dna_seq))
