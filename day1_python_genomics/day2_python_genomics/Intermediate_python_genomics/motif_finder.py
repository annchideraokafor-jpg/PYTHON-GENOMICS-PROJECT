import os
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
                seq_id = line[1:]  # remove '>'
                seq_lines = []
            else:
                seq_lines.append(line)
        if seq_id:
            sequences[seq_id] = "".join(seq_lines)
    return sequences
def count_motif(sequence, motif):
    sequence = sequence.upper()
    motif = motif.upper()
    return sequence.count(motif)
if __name__ == "__main__":
    fasta_file = "example.fasta"
    motif = "ATG"  # you can change this

    if not os.path.exists(fasta_file):
        print(f"File {fasta_file} not found!")
    else:
        sequences = read_fasta(fasta_file)
        print(f"Motif: {motif}\n")
        for seq_id, seq in sequences.items():
            count = count_motif(seq, motif)
            print(f"{seq_id}: {count} occurrence(s)")
