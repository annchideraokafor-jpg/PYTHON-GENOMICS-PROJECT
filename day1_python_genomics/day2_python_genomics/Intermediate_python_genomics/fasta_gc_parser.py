import os
print("🔍 Current working directory:", os.getcwd())
fasta_file = "example.fasta"
# fasta_gc_parser.py
# Week 1: FASTA Parsing Foundation
# -------------------------------

# Step 1: Read the FASTA file
def read_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        seq_id = None
        seq_lines = []

        for line in f:
            line = line.strip()
            if not line:
                continue  # skip blank lines

            if line.startswith(">"):  # header line
                if seq_id:
                    # Save the previous sequence
                    sequences[seq_id] = "".join(seq_lines)
                seq_id = line[1:]  # remove '>'
                seq_lines = []
            else:
                seq_lines.append(line)

        # Save the last sequence
        if seq_id:
            sequences[seq_id] = "".join(seq_lines)

    return sequences


# Step 2: Test your parser
if __name__ == "__main__":
    fasta_file = "example.fasta"
    result = read_fasta(fasta_file)

    print("Parsed FASTA sequences:\n")
    for header, seq in result.items():
        print(f"{header}: {seq} (Length: {len(seq)})")
