import math

def get_backtrack(v,w):
    sigma = 1
    s = [[0]]
    backtrack = [[""]]
    for i in range(len(v)):
        s.append([0])
        backtrack.append(["source"])
    
    for i in range(len(v)+1):
        for j in range(len(w)):
            s[i].append(-sigma*(j+1))
            backtrack[i].append("right-insertion")

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = 1 if v[i-1] == w[j-1] else -1
            s[i][j] = max(s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + match)
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

def fitting_alignment(s1, s2):
    backtrack, values = get_backtrack(s1, s2)
    
    new_s1 = []
    new_s2 = []

    for row in backtrack:
      s = ""
      for c in row:
        s += "{}\t".format(c)
      print(s)

    sink = (-math.inf, -1, -1)
    for i, row in enumerate(values):
      if row[len(row)-1] > sink[0]:
          sink = (row[len(row)-1], i, len(row)-1)

    print(sink)
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


#v = "GTAGGCTTAAGGTTA"  # TAGGCTTA
#w = "TAGATA"  #TAGA--TA

v = "TAAAGGAAATCCCGACTTACATGTGTAATTGCAGCCCAAAATGCAAGCTTTGACTTCGATCCATGAGAGTCATTTTGTTACATTCTACCACAGGCCGCTAAATTAACACCTTACTACGATGAGACGTGCAACCAGGGTGCCCATTCGAGGTCGCGAAAACAGGCGGCTAGTGACCGTCTGCACCGCCGAATAATTCGTCTGTTTATTGACAAGCAACAGCGCATTAAATAGCCATTACGATCTGGTACGCTTTTCGCCAAGCCGTTGTATATCTCTGACGCAGAGAGTCTCAGGCGTATCGCCCTACGGACGTTATAAACCACAGCCAGACTATCAAGCATGAGGTCGTTAAACCGGAACGTGTTCGCACAGCGGACCTTTTATCAGGCGTGTTGTACTCAGTATTACGTCCAATTCACGAGCCAAAGGTTATCGCCTATGCGACGGCGCGCGATGATTACGTAGGCTTTGCGCTTACCCGCTCCTCAACAAAACTAGCTCGCAGTAACAACGGTAGTTGACCAGCTATGTCAGGAGGATCTACATAGAACAATCGCTCAGCTTGTCTTTGCTGGCAGAGAGCAGCCCCATGTCTGAACGTACACCTTGGGACGTAGTAGGTCGCATAATTAATAACGTAATGTCAGCATTAGCGGAGGGCCCAATCTGACACTCAAAGGTAGGGACGACAGTCACAAGATGGGGTATAGAGTGTTGGGTGTCGCGGGTTATAAGAATTGCTGAGGGCATCTACGAATTACAAGGAGTCCACCCCATGCGCCGATTGTCAAGCGTTTGGACAGACTACGCGAAGTCTGACATG"
w = "TCCCCATGGCTGTTTGGCGGGTGAACATGAGGTTACTGTAAAGCGCACGATCAGGCAGATGCACGACCGTTGTAAAAGAT"

av, aw = fitting_alignment(v, w)

print(''.join(av))
print(''.join(aw))
