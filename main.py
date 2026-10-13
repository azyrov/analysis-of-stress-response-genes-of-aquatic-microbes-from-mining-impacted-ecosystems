import csv

def calculate_gc_content(sequence: str):
    """calculates the GC-content percentage of DNA sequences"""
    if not sequence:
        return 0.0

    sequence = sequence.upper()
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    return round(((g_count + c_count) / len(sequence)) * 100, 2)

def parse_fasta(file_path: str) -> list[dict]:
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

        if current_header is not None:
            full_seq = "".join(current_seq_lines)
            records.append({
                "header": current_header,
                "length": len(full_seq),
                "gc-content": calculate_gc_content(full_seq),
                "sequence": full_seq
            })

    return records


def export_to_csv(records: list[dict], output_path: str) -> None:
    """Takes a list of parsed record dictionaries and writes them to a CSV file."""
    if not records:
        print("No records found to export.")
        return

    fieldnames = ["header", "length", "gc-content", "sequence"]

    with open(output_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for record in records:
            writer.writerow(record)
            
    print(f"Successfully exported {len(records)} records to {output_path}")