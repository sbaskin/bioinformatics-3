import numpy as np

amino_acid_map = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        #'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        #'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'W': 186,
        'Y': 163,
    }

def cyclopeptide_sequencing_BB(spectrum):
    sequences = []
    parent_mass = spectrum[len(spectrum)-1]
    peptides = [""]
    while peptides:
        peptides = expand(peptides)
        next_peptides = []
        for peptide in peptides:
            cyc_spectrum = cyclical_spectrum(peptide)
            lin_spectrum = linear_spectrum(peptide)
            if lin_spectrum[len(lin_spectrum)-1] == parent_mass:
                if consistent(cyc_spectrum, spectrum):
                    sequences.append(peptide)
            elif consistent(lin_spectrum, spectrum):
                next_peptides.append(peptide)
        peptides = next_peptides
    return sequences

def consistent(peptide_spectrum, spectrum):
    for mass in peptide_spectrum:
        if mass not in spectrum:
            return False
    return True

def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for amino_acid in amino_acid_map:
            new_peptide = peptide + amino_acid
            new_peptides.append(new_peptide)
    return new_peptides


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


spectrum = [0, 71, 87, 87, 131, 158, 174, 202 ,218 ,245, 289 ,289 ,305 ,376]
sequences = cyclopeptide_sequencing_BB(spectrum)

output = ""
for j, sequence in enumerate(sequences):
    if j:
        output += ' '
    for i, peptide in enumerate(sequence):
        if i:
            output += '-'
        output += str(amino_acid_map[peptide])
print(output)