def base_frequency(sequence):
    """
    Calculate the frequency (percentage) of each nucleotide in a DNA sequence.
    """
    sequence = sequence.upper()
    length = len(sequence)

    if length == 0:
        return "Sequence is empty."

    freq = {
        'A': (sequence.count('A') / length) * 100,
        'T': (sequence.count('T') / length) * 100,
        'G': (sequence.count('G') / length) * 100,
        'C': (sequence.count('C') / length) * 100
    }

    # Round percentages to 2 decimal places
    for base in freq:
        freq[base] = round(freq[base], 2)

    return freq


if __name__ == "__main__":
    dna = input("Enter a DNA sequence: ").strip()
    frequency = base_frequency(dna)

    print("\nBase Frequency (%):")
    for base, percent in frequency.items():
        print(f"{base}: {percent}%")
