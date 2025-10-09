def count_bases(sequence):
    """
    Count how many times A, T, G, and C appear in a DNA sequence.
    """
    sequence = sequence.upper()
    base_count = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }
    return base_count


if __name__ == "__main__":
    dna = input("Enter a DNA sequence: ").strip()
    counts = count_bases(dna)

    print("\nBase Count:")
    for base, count in counts.items():
        print(f"{base}: {count}")
