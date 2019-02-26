import sys

def map_rna_to_amino_acid(rna):
    rna_to_protein = {
        'A': {
            'A': {
                'A': 'K',
                'C': 'N',
                'U': 'N',
                'G': 'K'
            },
            'C': {
                'A': 'T',
                'C': 'T',
                'U': 'T',
                'G': 'T'
            },
            'U': {
                'A': 'I',
                'C': 'I',
                'U': 'I',
                'G': 'M'
            },
            'G': {
                'A': 'R',
                'C': 'S',
                'U': 'S',
                'G': 'R'
            }
        },
        'C': {
            'A': {
                'A': 'Q',
                'C': 'H',
                'U': 'H',
                'G': 'Q'
            },
            'C': {
                'A': 'P',
                'C': 'P',
                'U': 'P',
                'G': 'P'
            },
            'U': {
                'A': 'L',
                'C': 'L',
                'U': 'L',
                'G': 'L'
            },
            'G': {
                'A': 'R',
                'C': 'R',
                'U': 'R',
                'G': 'R'
            }
        },
        'U': {
            'A': {
                'A': '',
                'C': 'Y',
                'U': 'Y',
                'G': ''
            },
            'C': {
                'A': 'S',
                'C': 'S',
                'U': 'S',
                'G': 'S'
            },
            'U': {
                'A': 'L',
                'C': 'F',
                'U': 'F',
                'G': 'L'
            },
            'G': {
                'A': '',
                'C': 'C',
                'U': 'C',
                'G': 'W'
            }
        },
        'G': {
            'A': {
                'A': 'E',
                'C': 'D',
                'U': 'D',
                'G': 'E'
            },
            'C': {
                'A': 'A',
                'C': 'A',
                'U': 'A',
                'G': 'A'
            },
            'U': {
                'A': 'V',
                'C': 'V',
                'U': 'V',
                'G': 'V'
            },
            'G': {
                'A': 'G',
                'C': 'G',
                'U': 'G',
                'G': 'G'
            }
        }
    }
    return rna_to_protein[rna[0]][rna[1]][rna[2]]


def convert_rna_string_to_amino_acid(rna_string):
    protein = ''
    for i in range(int(len(rna_string)/3)):
        protein += map_rna_to_amino_acid(rna_string[i*3:i*3 + 3])
    return protein

def solve_peptide_encoding(dna, peptide):
    dna_encoding_peptide = []
    slice_size = len(peptide) * 3
    for i in range(int(len(dna) - slice_size + 1)):
        dna_slice = dna[i: i + slice_size]
        dna_rc_slice = reverse_compliment(dna_slice)
        if check_dna_encodes_peptide(dna_slice, peptide):
            dna_encoding_peptide.append(dna_slice)
        if check_dna_encodes_peptide(dna_rc_slice, peptide):
            dna_encoding_peptide.append(dna_slice)
        
    return dna_encoding_peptide

def check_dna_encodes_peptide(dna_slice, peptide):
    rna = convert_dna_to_rna(dna_slice)
    protein = convert_rna_string_to_amino_acid(rna)
    if protein == peptide:
        return True
    return False

def convert_dna_to_rna(dna):
    return dna.replace('T', 'U')

def reverse_compliment(text):
    map = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }
    compliment = ''
    for nucleotide in text:
        compliment += map[nucleotide]
    return compliment[::-1]

f = open(r'C:\Users\Shane\Downloads\Bacillus_brevis.txt')

peptide = 'VKLFPWFNQY'
dna = ''.join(f.readlines())
dna = dna.replace('\n', '')

dna_encoding_peptide = solve_peptide_encoding(dna, peptide)

for dna_slice in dna_encoding_peptide:
    print(dna_slice)