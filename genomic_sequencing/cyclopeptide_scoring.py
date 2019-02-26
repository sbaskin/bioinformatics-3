import sys

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


def cyclo_score(peptide, spectrum):
    p_spectrum = cyclical_spectrum(peptide)
    score = 0
    for mass in p_spectrum: 
        if mass in spectrum:
            index = spectrum.index(mass)
            del spectrum[index]
            score += 1
    return score


def cyclical_spectrum(peptide):
    prefix_masses = get_prefix_masses(peptide)
    peptide_mass = prefix_masses[len(prefix_masses)-1]
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            mass = prefix_masses[j] - prefix_masses[i]
            spectrum.append(mass)
            if i > 0 and j < len(peptide):
                m = peptide_mass - mass
                spectrum.append(m)
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
spectrum = [0, 71, 98, 99 ,131 ,202, 202, 202, 202, 202, 299 ,333 ,333 ,333, 503]

#f = open('C:/Users/Shane/Downloads/dataset_102_3 (3).txt')

#peptide = f.readline().strip()
#spectrum = [int(x) for x in f.readline().replace('\n','').split(' ')]
score = cyclo_score(peptide, spectrum)
print(score)