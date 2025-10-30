from collections import Counter
import pandas as pd

def count_codons(sequence):
    sequence = sequence.upper()
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]
    codon_counts = Counter(codons)
    return codon_counts

if __name__ == "__main__":
    sequence = "ATGCGTATGATGGAAATG"
    codon_counts = count_codons(sequence)

    # Convert to DataFrame
    df = pd.DataFrame(codon_counts.items(), columns=["Codon", "Count"])
    df = df.sort_values(by="Count", ascending=False)

    print(df)

    # Save results
    df.to_csv("codon_usage.csv", index=False)
