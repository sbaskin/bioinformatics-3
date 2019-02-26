

amino_acid_map = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'W': 186,
        'Y': 163,
    }

def score(peptide, spectrum):
    p_spectrum = None
    spec_copy = spectrum[:]
    p_spectrum = linear_spectrum(peptide)
    score = 0
    for mass in p_spectrum: 
        if mass in spec_copy:
            index = spec_copy.index(mass)
            del spec_copy[index]
            score += 1
    return score


def linear_spectrum(peptide):
    prefix_masses = get_prefix_masses(peptide)
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            mass = prefix_masses[j] - prefix_masses[i]
            spectrum.append(mass)
    spectrum.sort()
    return spectrum


def get_prefix_masses(peptide):
    prefix_masses = [0]
    total = 0
    for p in peptide:
        total += amino_acid_map[p]
        prefix_masses.append(total)
    return prefix_masses


peptide = "MAMA"
spectrum = [0, 97, 129 ,129, 129, 194, 226, 323 ,323 ,355, 452]

score = score(peptide, spectrum)
print(score)