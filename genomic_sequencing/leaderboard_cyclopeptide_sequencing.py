

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

scores_dict_cyc = {}
scores_dict_lin = {}

def lcs(spectrum, n):
    parent_mass = spectrum[len(spectrum)-1]
    leaderboard = ['']
    leaderpeptide = ''
    while leaderboard:
        leaderboard = expand(leaderboard)
        p_remove = []
        for i, peptide in enumerate(leaderboard):
            lin_spectrum = linear_spectrum(peptide)
            cyc_spectrum = cyclical_spectrum(peptide)
            if lin_spectrum[len(lin_spectrum)-1] == parent_mass:
                p_score = get_score(peptide, spectrum)
                l_score = get_score(leaderpeptide, spectrum)
                if p_score > l_score:
                    leaderpeptide = peptide
            elif lin_spectrum[len(lin_spectrum)-1] > parent_mass:
                p_remove.append(i)
        p_remove.reverse()
        for i in p_remove:
            del leaderboard[i]
        leaderboard = trim(leaderboard, spectrum, n)
    return leaderpeptide


def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for amino_acid in amino_acid_map:
            new_peptide = peptide + amino_acid
            new_peptides.append(new_peptide)
    return new_peptides


def get_score(peptide, spectrum, cyclical=True):
    p_score = 0
    if cyclical:
        if peptide in scores_dict_cyc:
            p_score = scores_dict_cyc[peptide]
        else:
            p_score = score(peptide, spectrum)
            scores_dict_cyc[peptide] = p_score
    else:
        if peptide in scores_dict_lin:
            p_score = scores_dict_lin[peptide]
        else:
            p_score = score(peptide, spectrum, False)
            scores_dict_lin[peptide] = p_score
    return p_score


def trim(leaderboard, spectrum, n):
    i = 0
    leaderboard.sort(key=lambda x: get_score(x, spectrum, False), reverse=True)
    new_leaders = []
    while i < len(leaderboard) and (i < n or (i >= n and get_score(leaderboard[i], spectrum, False) == get_score(leaderboard[i-1], spectrum, False))):
        new_leaders.append(leaderboard[i])
        i += 1
    return new_leaders
        


def score(peptide, spectrum, cyclical=True):
    p_spectrum = None
    spec_copy = spectrum[:]
    if cyclical:
        p_spectrum = cyclical_spectrum(peptide)
    else:
        p_spectrum = linear_spectrum(peptide)
    score = 0
    for mass in p_spectrum: 
        if mass in spec_copy:
            index = spec_copy.index(mass)
            del spec_copy[index]
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


n = 1000
spectrum = [0, 71, 113, 129, 147,200,218,260,313,331,347,389,460]

f = open('C:/Users/Shane/Downloads/dataset_102_10 (1).txt')

n = int(f.readline().strip())
spectrum = [int(x) for x in f.readline().replace('\n','').split(' ')]
#print(n, spectrum)

winner = lcs(spectrum, n)

output = ''
for i, peptide in enumerate(winner):
    if i:
        output += '-'
    output += str(amino_acid_map[peptide])
print(output)