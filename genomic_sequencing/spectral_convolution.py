

def spectral_convolution(spectrum):
    convo_spectrum = []
    spectrum.sort(reverse=True)
    for i in range(len(spectrum) -1):
        for j in range(i+1, len(spectrum)):
            mass = spectrum[i] - spectrum[j]
            if mass > 0:
                convo_spectrum.append(mass)
    return convo_spectrum


spectrum = [0, 86, 160, 234, 308 ,320 ,382]

#f = open('C:/Users/Shane/Downloads/dataset_104_4 (1).txt')
#spectrum = [int(x) for x in f.readline().replace('\n','').split(' ')]


convolution_spectrum = spectral_convolution(spectrum)

mass_counts = {}
for mass in convolution_spectrum:
    if mass in mass_counts:
         mass_counts[mass] += 1
    else:
        mass_counts[mass] = 1
print(mass_counts)


output = ''
for i, mass in enumerate(convolution_spectrum):
    if i:
        output += ' '
    output += str(mass)
print(output)