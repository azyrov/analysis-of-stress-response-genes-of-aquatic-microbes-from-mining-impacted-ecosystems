import csv
import os

def calculate_gc_content(sequence: str):
    """calculates the GC-content percentage of DNA sequences"""
    if not sequence:
        return 0.0

    sequence = sequence.upper()
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    return round(((g_count + c_count) / len(sequence)) * 100, 2)

def parse_fasta(file_path: str, organism_name: str, group_label: str) -> list[dict]:
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
                        "organism": organism_name,
                        "group": group_label,
                        "sequence": full_seq
                    })

                current_header = line[1:].split()[0]
                current_seq_lines = []

            else:
                current_seq_lines.append(line)

        if current_header is not None:
            full_seq = "".join(current_seq_lines)
            records.append({
                "header": current_header,
                "length": len(full_seq),
                "gc-content": calculate_gc_content(full_seq),
                "organism": organism_name,
                "group": group_label,
                "sequence": full_seq
            })

    return records


def export_to_csv(records: list[dict], output_path: str) -> None:
    """Takes a list of parsed record dictionaries and writes them to a CSV file."""
    if not records:
        print("No records found to export.")
        return

    fieldnames = ["header", "length", "gc-content", "organism", "group", "sequence"]

    with open(output_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for record in records:
            writer.writerow(record)
            
    print(f"Successfully exported {len(records)} records to {output_path}")

if __name__ == "__main__":
    group_directories = {
        "control": "./data/control",
        "treatment": "./data/treatment"
    }

    output_csv = "microbial_metrics.csv"
    
    all_parsed_records = []

    for group_label, dir_path in group_directories.items():
        if not os.path.exists(dir_path):
            print(f"Notice: Directory '{dir_path}' does not exist yet. Skipping...")
            continue
            
        print(f"\nScanning group directory [{group_label}] -> {dir_path}")

        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith((".fna", ".fasta", ".fa")):
                    file_path = os.path.join(root, file)
                    organism_name = os.path.splitext(file)[0]
                    
                    print(f"  -> Processing: {file} (Organism tag: {organism_name})")
                    records = parse_fasta(file_path, organism_name, group_label)
                    all_parsed_records.extend(records)

    print("\n--- Finalizing Export ---")
    export_to_csv(all_parsed_records, output_csv)