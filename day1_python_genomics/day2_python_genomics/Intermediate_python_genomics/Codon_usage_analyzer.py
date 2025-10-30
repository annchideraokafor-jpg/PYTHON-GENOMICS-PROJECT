from collections import Counter
import matplotlib.pyplot as plt
def read_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        seq_id = None
        seq_lines = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = "".join(seq_lines)
                seq_id = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line)
        if seq_id:
            sequences[seq_id] = "".join(seq_lines)
    return sequences
def count_codons(sequence):
    sequence = sequence.upper()
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]
    codon_counts = Counter(codons)
    return codon_counts
def plot_top_codons(codon_counts, seq_id, top_n=10):
    most_common = codon_counts.most_common(top_n)
    codons, counts = zip(*most_common)

    plt.bar(codons, counts)
    plt.title(f"Top {top_n} Codons - {seq_id}")
    plt.xlabel("Codon")
    plt.ylabel("Frequency")
    plt.show()
if __name__ == "__main__":
    fasta_file = "example.fasta"
    sequences = read_fasta(fasta_file)

    for seq_id, seq in sequences.items():
        codon_counts = count_codons(seq)
        print(f"\nTop codons for {seq_id}:")
        for codon, count in codon_counts.most_common(10):
            print(f"{codon}: {count}")
        plot_top_codons(codon_counts, seq_id)
