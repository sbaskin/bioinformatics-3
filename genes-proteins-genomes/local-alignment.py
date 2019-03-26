import math

pam250 = {'A': {'A': 2, 'C': -2, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': -1, 'M': -1, 'L': -2, 'N': 0, 'Q': 0, 'P': 1, 'S': 1, 'R': -2, 'T': 1, 'W': -6, 'V': 0, 'Y': -3}, 'C': {'A': -2, 'C': 12, 'E': -5, 'D': -5, 'G': -3, 'F': -4, 'I': -2, 'H': -3, 'K': -5, 'M': -5, 'L': -6, 'N': -4, 'Q': -5, 'P': -3, 'S': 0, 'R': -4, 'T': -2, 'W': -8, 'V': -2, 'Y': 0}, 'E': {'A': 0, 'C': -5, 'E': 4, 'D': 3, 'G': 0, 'F': -5, 'I': -2, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'D': {'A': 0, 'C': -5, 'E': 3, 'D': 4, 'G': 1, 'F': -6, 'I': -2, 'H': 1, 'K': 0, 'M': -3, 'L': -4, 'N': 2, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'G': {'A': 1, 'C': -3, 'E': 0, 'D': 1, 'G': 5, 'F': -5, 'I': -3, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -3, 'T': 0, 'W': -7, 'V': -1, 'Y': -5}, 'F': {'A': -3, 'C': -4, 'E': -5, 'D': -6, 'G': -5, 'F': 9, 'I': 1, 'H': -2, 'K': -5, 'M': 0, 'L': 2, 'N': -3, 'Q': -5, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -1, 'Y': 7}, 'I': {'A': -1, 'C': -2, 'E': -2, 'D': -2, 'G': -3, 'F': 1, 'I': 5, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -2, 'S': -1, 'R': -2, 'T': 0, 'W': -5, 'V': 4, 'Y': -1}, 'H': {'A': -1, 'C': -3, 'E': 1, 'D': 1, 'G': -2, 'F': -2, 'I': -2, 'H': 6, 'K': 0, 'M': -2, 'L': -2, 'N': 2, 'Q': 3, 'P': 0, 'S': -1, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': 0}, 'K': {'A': -1, 'C': -5, 'E': 0, 'D': 0, 'G': -2, 'F': -5, 'I': -2, 'H': 0, 'K': 5, 'M': 0, 'L': -3, 'N': 1, 'Q': 1, 'P': -1, 'S': 0, 'R': 3, 'T': 0, 'W': -3, 'V': -2, 'Y': -4}, 'M': {'A': -1, 'C': -5, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 2, 'H': -2, 'K': 0, 'M': 6, 'L': 4, 'N': -2, 'Q': -1, 'P': -2, 'S': -2, 'R': 0, 'T': -1, 'W': -4, 'V': 2, 'Y': -2}, 'L': {'A': -2, 'C': -6, 'E': -3, 'D': -4, 'G': -4, 'F': 2, 'I': 2, 'H': -2, 'K': -3, 'M': 4, 'L': 6, 'N': -3, 'Q': -2, 'P': -3, 'S': -3, 'R': -3, 'T': -2, 'W': -2, 'V': 2, 'Y': -1}, 'N': {'A': 0, 'C': -4, 'E': 1, 'D': 2, 'G': 0, 'F': -3, 'I': -2, 'H': 2, 'K': 1, 'M': -2, 'L': -3, 'N': 2, 'Q': 1, 'P': 0, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -2, 'Y': -2}, 'Q': {'A': 0, 'C': -5, 'E': 2, 'D': 2, 'G': -1, 'F': -5, 'I': -2, 'H': 3, 'K': 1, 'M': -1, 'L': -2, 'N': 1, 'Q': 4, 'P': 0, 'S': -1, 'R': 1, 'T': -1, 'W': -5, 'V': -2, 'Y': -4}, 'P': {'A': 1, 'C': -3, 'E': -1, 'D': -1, 'G': 0, 'F': -5, 'I': -2, 'H': 0, 'K': -1, 'M': -2, 'L': -3, 'N': 0, 'Q': 0, 'P': 6, 'S': 1, 'R': 0, 'T': 0, 'W': -6, 'V': -1, 'Y': -5}, 'S': {'A': 1, 'C': 0, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': -1, 'P': 1, 'S': 2, 'R': 0, 'T': 1, 'W': -2, 'V': -1, 'Y': -3}, 'R': {'A': -2, 'C': -4, 'E': -1, 'D': -1, 'G': -3, 'F': -4, 'I': -2, 'H': 2, 'K': 3, 'M': 0, 'L': -3, 'N': 0, 'Q': 1, 'P': 0, 'S': 0, 'R': 6, 'T': -1, 'W': 2, 'V': -2, 'Y': -4}, 'T': {'A': 1, 'C': -2, 'E': 0, 'D': 0, 'G': 0, 'F': -3, 'I': 0, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -1, 'T': 3, 'W': -5, 'V': 0, 'Y': -3}, 'W': {'A': -6, 'C': -8, 'E': -7, 'D': -7, 'G': -7, 'F': 0, 'I': -5, 'H': -3, 'K': -3, 'M': -4, 'L': -2, 'N': -4, 'Q': -5, 'P': -6, 'S': -2, 'R': 2, 'T': -5, 'W': 17, 'V': -6, 'Y': 0}, 'V': {'A': 0, 'C': -2, 'E': -2, 'D': -2, 'G': -1, 'F': -1, 'I': 4, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -1, 'S': -1, 'R': -2, 'T': 0, 'W': -6, 'V': 4, 'Y': -2}, 'Y': {'A': -3, 'C': 0, 'E': -4, 'D': -4, 'G': -5, 'F': 7, 'I': -1, 'H': 0, 'K': -4, 'M': -2, 'L': -1, 'N': -2, 'Q': -4, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -2, 'Y': 10}}

def backtrack(v,w):
    sigma = 5
    s = [[0]]
    backtrack = [[""]]
    for i in range(len(v)):
        s.append([0])
        backtrack.append(["down-deletion"])
    for i in range(len(v)+1):
        for j in range(len(w)):
            s[i].append(0)
            backtrack[i].append("right-insertion")
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = pam250[v[i-1]][w[j-1]]
            s[i][j] = max(0, s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j] - sigma: #deletion
                backtrack[i][j] = 'down-deletion'
            elif s[i][j] == s[i][j-1] - sigma: #insertion
                backtrack[i][j] = 'right-insertion'
            elif s[i][j] == s[i-1][j-1] + match:
                if v[i-1] == w[j-1]: #match
                    backtrack[i][j] = 'diagonal'
                else: #mismatch
                    backtrack[i][j] = 'diagonal'
            elif s[i][j] == 0:
                backtrack[i][j] = 'source'
    return (backtrack, s)

def local_alignment(map, s1, s2):
    backtrack = map[0]
    values = map[1]
    
    new_s1 = []
    new_s2 = []

    sink = (-math.inf, -1, -1)
    for i, row in enumerate(values):
        for j, cell in enumerate(row):
            if cell > sink[0]:
                sink = (cell, i, j)

    print(sink[0])
    i = sink[1]
    j = sink[2]

    while i>=0 and j>=0 and backtrack[i][j] != '' and backtrack[i][j] != 'source':
        if backtrack[i][j] == "diagonal":
            new_s1.append(s1[i-1])
            new_s2.append(s2[j-1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == "down-deletion":
            new_s1.append(s1[i-1])
            new_s2.append('-')
            i -= 1
        elif backtrack[i][j] == 'right-insertion':
            new_s1.append('-')
            new_s2.append(s2[j-1])
            j -= 1
        else:
            raise Exception("Unknown backtrack: {}".format(backtrack[i][j]))
    new_s1.reverse()
    new_s2.reverse()
    return [new_s1, new_s2]


s1 = "QQITVINAVCKGAQGFVACHEHDHNYWWQPDQIMCPHDKNVKFKYIERALVACVHHVNLWLPWQPRQEYHFFMLFQQAEMFDCTGRWDWAIKSQMCKFMWICMGGIEGNDCTCGHKSLCSCQWSGMLNNKDDEIFEALASYLTEQPRAWTLVEDDCKYVDDQKAQALLVPSCCIRAETQLWSAKISTNCWQMWSAKRHWEQERSCVYRNHEQHMIRQTDMHSGFKMFSKPKQIDKYLEMETQDNTDLHKNAHHDHTMDKYDGLFGAYDWAKQSLQHFVTLEAEMNVQIDESAGALIFMFGVGSFYIECGNADWHWRISRQHLTCSHFKPDIKDNALEHCEEQCTNAKHKWGDVFNTSFRLYTGRFIVCDTSAMHNTRNFSENKAAVHRWVTQRVTLANASYEAWDFGLTLSPDMLYDGEIEWDHHAQVTRYLALYEIQDKATSKSCKKACSMNHNMRNAATNALHFRVFIENLHNDFEELKYERNKDEGYRRHIQIWDCMRDQMRGNEKHCCTNQPMWGAKCKNPNKMCTGWQPVDNQWCHNYWAGKINLVASYHHRWCGGLACRGLVNVAFRFVNAWLWRDADENPQKDRGKHFQVPVLDHCGQKHEVLPKNCSWWGMQYDGWSMCAIRFPTKGTCHSGRRWKQFQKHARCTKSWDHHIKCRAVDTLGIMRLGYTEMWPVYNDYNPWFVIQTFMPMRVKAGDLADGIKCHHDPGFMIMMDETNYGVYRAVTKACGYPVFFYYKPKLTFSAMRAVHREKIICQQLEVKQDAFFVDPMDTCWDYFSTSQYGQWSYPGATGDWPFKGYWQTEAPRIMQDKSDYRPANCKPPIKSNIIEWVETQKFEQTTPYTQPSAEKEPWSQNQLYKLCRWLCPITLHMWWRTNNPIKSKSETGEQKCKDW" 
s2 = "HWCFFARPKKAEQTNWSDNPIAETHFDKSNDTKHWYLEPDTADGTVVYNFCPEVDMDFVKLTRIEHPEKGGLHDYQGMTWLIMTISPFLWNHNYDNPPVNGGSVEHKCGGPYTSESQTMGVSQASKVMSALWGGSYKWLKMHCYERSMIVTEQIPLSQPIQVNNKMNPSWIISLLIFNNILDQSLKLMKKPCPRNWSYCCSAQIWVVGMDGRCARCRSDVDVNPFIYHFIGCATVVSTGEINQSLTIAFSRHAETLNKCQCEDRYHASRFRAYFFNADWHWRISRQHLTCSHFRGAKEHCEEQCTNAKHKWGDVFNHSFRLYTGRFIGLDTSAMHNTMCCNSHFNKAAVETRWRGHTYMYMFTASSDLHPPAGAEAWDFDMLMWSRDTLTESKAYPFQVCPDMLYDGERAQVTRYLAKAASMNHNMRFIENLHNDFEECKMEGVLVWERDTACNKDEGYRRHIEIWDCMNKDHRCICCMLDLSAGNEKHSYKAKCKNPNLHMCTAMGQSDQPVDTRDSDLSVWYHHRWRGTQVNVAFRFVNAWLWRDADDRGKHHGQVPVVDHVLPKNCSWWYMQFKMFNKDHLGIRFPTKGTCHSGRRWKQFQKFAHIKAGTDHDSQYHCDFLNPQYEHGPVPMGQMFCSIKNPHLTTVPNMCAFTNRQELVCWRSKPTNCSWWDEDLDCYIRKVDNLCTPVAIIQYREMLVAYAWMGCMCPWQLPAPNDNWCFKQFCGTTFNTGMSHPAMHGITMSCKDIAPDYATSDGMLLPAANCGVVDVSGAYFCMHCEIDYGQKWKMVKTARASAISNPVCMQMNYRHEGHLQATSRLYHVAHNVTHYNPMERDDMMQGYA"

b = backtrack(s1, s2)

output = local_alignment(b, s1, s2)


print(''.join(output[0]))
print(''.join(output[1]))


