def gc_content(sequence):
    """
    Calculate the GC content (percentage of G and C) in a DNA sequence.
    """
    sequence = sequence.upper()  # convert to uppercase to avoid mismatch
    gc_count = 0
    for base in sequence:
        if base in ['G', 'C']:
            gc_count += 1
    
    gc_percentage = (gc_count / len(sequence)) * 100
    return round(gc_percentage, 2)


if __name__ == "__main__":
    seq = input("Enter a DNA sequence: ").strip()
    result = gc_content(seq)
    print(f"GC Content: {result}%")
