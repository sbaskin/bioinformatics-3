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


rna_string = 'CCUCGUACUGAUAUUAAU'
print(convert_rna_string_to_amino_acid(rna_string))