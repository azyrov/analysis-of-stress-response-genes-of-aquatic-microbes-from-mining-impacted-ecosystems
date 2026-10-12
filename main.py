def calculate_gc_content(sequence: str):
    """calculates the GC-content percentage of DNA sequences"""
    if not sequence:
        return 0.0

    sequence = sequence.upper()
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    return round(((g_count + c_count) / len(sequence)) * 100, 2)