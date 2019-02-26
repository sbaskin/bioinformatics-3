
def cyclical_spectrum(peptide, map):
    prefix_masses = get_prefix_masses(peptide, map)
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


def linear_spectrum(peptide, map):
    prefix_masses = get_prefix_masses(peptide, map)
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            mass = prefix_masses[j] - prefix_masses[i]
            spectrum.append(mass)
    spectrum.sort()
    return spectrum


def get_prefix_masses(peptide, map):
    prefix_masses = [0]
    total = 0
    for p in peptide:
        total += map[p]
        prefix_masses.append(total)
    return prefix_masses


#peptide = 'LEQN'
#spectrum = generate_theoretical_spectrum(peptide)

#output = ""
#for mass in spectrum:
#    output += str(mass) + ' '
#output.strip()

map = {
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
        'Y': 163,
        'W': 186
    }
answer = cyclical_spectrum("MTAI", map)
output = ""
for a in answer:
    output += str(a) + ' '
print(output)