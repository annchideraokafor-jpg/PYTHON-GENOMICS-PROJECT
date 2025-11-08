def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(complement[base] for base in reversed(seq.upper()))
def find_orfs(seq):
    stop_codons = ['TAA', 'TAG', 'TGA']
    orfs = []
    for frame in range(3):  # three reading frames
        for i in range(frame, len(seq)-2, 3):
            codon = seq[i:i+3]
            if codon == 'ATG':  # start codon
                for j in range(i, len(seq)-2, 3):
                    codon2 = seq[j:j+3]
                    if codon2 in stop_codons:
                        orfs.append((i+1, j+3, seq[i:j+3]))  # positions are 1-based
                        break
    return orfs

def read_fasta(path):
    """
    Simple FASTA reader that returns a dict {header: sequence}.
    Sequences are concatenated and returned in uppercase.
    """
    sequences = {}
    with open(path, 'r') as f:
        seq_id = None
        seq_lines = []
        for line in f:
            line = line.rstrip('\n')
            if not line:
                continue
            if line.startswith('>'):
                if seq_id is not None:
                    sequences[seq_id] = ''.join(seq_lines).upper()
                seq_id = line[1:].strip()
                seq_lines = []
            else:
                seq_lines.append(line.strip())
        if seq_id is not None:
            sequences[seq_id] = ''.join(seq_lines).upper()
    return sequences
if __name__ == "__main__":
    fasta_file = "example.fasta"
    sequences = read_fasta(fasta_file)  # reuse your FASTA reader

    for seq_id, seq in sequences.items():
        rev_comp = reverse_complement(seq)
        print(f"\nSequence ID: {seq_id}")
        print(f"Reverse Complement: {rev_comp}")

        orfs = find_orfs(seq)
        print(f"Found {len(orfs)} ORFs:")
        for start, end, orf_seq in orfs:
            print(f"Start: {start}, End: {end}, ORF: {orf_seq}")
