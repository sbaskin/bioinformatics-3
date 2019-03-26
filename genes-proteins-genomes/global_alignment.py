
blosum = {
    'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 
    'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 
    'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
    'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 
    'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 
    'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 
    'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 
    'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 
    'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
    'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 
    'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 
    'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 
    'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 
    'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 
    'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 
    'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 
    'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 
    'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 
    'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 
    'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}
}

def get_backtrack(v,w):
    sigma = 5
    s = [[0]]
    backtrack = [[""]]
    for i in range(len(v)):
        s.append([-sigma*(i+1)])
        backtrack.append(["down-deletion"])
    for i in range(len(v)+1):
        for j in range(len(w)):
            s[i].append(-sigma*(j+1))
            backtrack[i].append("right-insertion")
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = blosum[v[i-1]][w[j-1]]
            s[i][j] = max(s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j] - sigma: #deletion
                backtrack[i][j] = 'down-deletion'
            elif s[i][j] == s[i][j-1] - sigma: #insertion
                backtrack[i][j] = 'right-insertion'
            elif v[i-1] == w[j-1]: #match
                backtrack[i][j] = 'diagonal'
            else: #mismatch
                backtrack[i][j] = 'diagonal'
    #print(s[len(v)][len(w)])
    return backtrack

def global_alignment(s1, s2):
    backtrack = get_backtrack(s1, s2)
    new_s1 = []
    new_s2 = []
    i=len(backtrack)-1
    j=len(backtrack[0])-1
    while i>=0 and j>=0 and backtrack[i][j] != '':
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
    new_s1.reverse()
    new_s2.reverse()
    return [new_s1, new_s2]

#s1 = "MPAQCRGVEVHYGPGDMLWQLGKDLFHWCHQVARYSQSGNYQTYKKMPSSKLHSVDHPYTNRISCLETMKPRICQKMYAWKNYQKGHWNRTNDERRLKCRAWWRMFIPTVSGLHNVPERYLMKLTTWVEPLMSKLETPTEWNHIPITCGDPVHVFFIVSCLIQVNGESVFATYYSKVPTWFSVNCYADVDVGMMRLCPDGCAQMYNCPERALPNKQIDTNAESSIEIFTCSSAMMDNDTFVRGGYFPKVHSGSWEAVGMDWAQCGICYTQAAIIGMWYIKMSLEDMPVQDVIAETHAELECDFFHSVFDAIMEGADGTQYAGMDPHKQKMCHPYRHLMQLEPFYHMKSQEYCTRALAPASMQLDSGEKGFLTNTYHDRKNMMFYRMSPEECNQWGVDHGTSCIKLPGYATGRRPPTMAHMQQNAFLTQTTQQNMNGEKRNEKVSDVSWDSFNMVFWHHFISCPIWHEGMFLLRHMNMFCKYWMHLHDVSQEGYKCIMGIEWQAATWETNVVGKENNVIDIDVLVIMYNLRVIYERMPHKPKCFPDRQYHMSHASVMHFSSGWRQSVSQACENWYMPGVDLPKKSPECNDACTAECGTVAYPYKHWHYCDHEKQDGQVGKYKAYQIIMWYPIKDLSCGDDTMWEPLKCYWMGQPYHWKPIEGDMHKFTGAHNICTVCCCSGPNQLFPISMDHDVHSPQPIDVNCNPNQAWVWSDQQFAHLEMTQEPHRDWWPWPQMSHICPCRRHHVRPEFHATGCPTEISIKPYSSCPPPHHIWPCEKASNPKVLLGLVCMESHLCCSIMLGPYQCDDCQLLWDIRTWG" # PLEASANTLY
#s2 = "MPAQCGGVEVHYGPGDMLWQLGKMLFHFCRYSQSKKPMFGYCSYSLETMKPRICQKMLAWKYHKGHWKFTWYRMFIPTVSGLHNWMPERYLMKTTRSKTETPTENHIPITCGMQCYDHPVHVFNINSVDKMAPLIQVNGESVFATYTSKVPDWFSKRMNHVFCYADVDEYARYLDQFTQPERHVAIYLPNKQKDTNAESSMSDKYLPAIEIFTCSQLAEAMSIYFVRGGYFPKVHSGSWQAVATLMNWFIQMDWVQIGICYTQAAIRKIMGMWYCRHDLEKMSLETSRIVQDVLAEECDFFKSVIDAIMEGAYGTQYAGMDPHKWVKMCHPYRFLHQLEPWYHMKSQEYCTRMLAAILQLDSGEKGVLTIMWMVDYYDRWNMDFQRMSPCYHHFISNQWGVDHGTSCIKLPGYAMIIHYPSIFETQTTQQNMNGEKRNEKVSDRSWHSFNMVFPHHFISCPIWHEGMFPLRHFCKIWMHLHDYKCIMGREWQAACWEDNVVDVLVIMYNLVVIYERMPHPKCVRDGGHFSSGLWYFEIKTYRQSVSQACTRSFNWYMPGVDHSPECNDVNSIDCTAECSTVAYPYKHWHYCDHHDDGQVGKYKAYQIIMDYPIKDLSCGDDTMWEPLERYWMGQPYHWKICEINCTGAHNICQLFPGCKQNEPSPIDVNCNPNQAWVWSDAKKWMVISQGRERGGSAHLEMTTEPYMVSNISGFWWPWPPDMSHIVPCRRHHEFHAFMCPTISIKPTSSCPIWFPNHHIWPCDKWSVLLGLVCMIHLCAQHQDDCQLLWFIRTWG" # -MEA--N-LY

# s1 = "ASGEEDN" # AS----GEEDN
# s2 = "GPPPWLSEEQN" # GPPPWLSEEQN

#b = backtrack(s1, s2)

#output = global_alignment(b, s1, s2)


#print(''.join(output[0]))
#print(''.join(output[1]))


