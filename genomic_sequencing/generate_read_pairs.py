
def generate_read_pairs(text, k, d):
    read_pairs = []
    for i in range(len(text) - (k * 2 + d) + 1):
        read_pairs.append((text[i:i + k], text[i+k+d: i+k+d + k]))
    return read_pairs

read_pairs = generate_read_pairs("TAATGCCATGGGATGTT", 3, 2)
print(read_pairs)