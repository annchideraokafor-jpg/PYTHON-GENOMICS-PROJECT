def calculate_at_content(dna_sequence):
    dna_sequence = dna_sequence.upper()
    a_count = dna_sequence.count("A")
    t_count = dna_sequence.count("T")
    total_bases = len(dna_sequence)

    if total_bases == 0:
        return 0

    at_content = ((a_count + t_count) / total_bases) * 100
    return at_content


# Example usage
dna = "ATGCAATGGCTT"
at_percent = calculate_at_content(dna)
print(f"AT Content: {at_percent:.2f}%")
