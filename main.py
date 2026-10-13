def calculate_gc_content(sequence: str):
    """calculates the GC-content percentage of DNA sequences"""
    if not sequence:
        return 0.0

    sequence = sequence.upper()
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    return round(((g_count + c_count) / len(sequence)) * 100, 2)

def parse_fasta(file_path: str) -> list[dir]:
    """reads a multi-sequence fasta to return a list containing parsed dictionaries"""
    records = []
    current_header = None
    current_seq_lines = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_header is not None:
                    full_seq = "".join(current_seq_lines)
                    records.append({
                        "header": current_header,
                        "length": len(full_seq),
                        "gc-content": calculate_gc_content(full_seq),
                        "sequence": full_seq
                    })

                current_header = line[1:]
                current_seq_lines = []

            else:
                current_seq_lines.append(line)
                