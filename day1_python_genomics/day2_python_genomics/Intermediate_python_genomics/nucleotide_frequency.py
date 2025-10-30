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
def nucleotide_frequency(sequence):
    sequence = sequence.upper()
    total = len(sequence)
    freqs = {
        "A": sequence.count("A") / total * 100,
        "T": sequence.count("T") / total * 100,
        "G": sequence.count("G") / total * 100,
        "C": sequence.count("C") / total * 100
    }
    return freqs
def plot_frequencies(freqs, seq_id):
    labels = list(freqs.keys())
    values = list(freqs.values())

    plt.bar(labels, values)
    plt.title(f"Nucleotide Composition - {seq_id}")
    plt.xlabel("Nucleotide")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.show()
if __name__ == "__main__":
    fasta_file = "example.fasta"
    sequences = read_fasta(fasta_file)

    for seq_id, seq in sequences.items():
        freqs = nucleotide_frequency(seq)
        print(f"{seq_id}: {freqs}")
        plot_frequencies(freqs, seq_id)
