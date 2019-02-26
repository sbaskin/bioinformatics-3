


def mtlp(n, m, down_matrix, right_matrix):
    s = [[0]]
    for i in range(1, n+1):
        value = s[i-1][0] + down_matrix[i-1][0]
        s.append([value])
    for i in range(1, m+1):
        value = s[0][i-1] + right_matrix[0][i-1]
        s[0].append(value)
    for i in range(1,n+1):
        for j in range(1,m+1):
            down = s[i-1][j] + down_matrix[i-1][j]
            right = s[i][j-1] + right_matrix[i][j-1]
            value = max(down, right)
            s[i].append(value)
    
    for row in s:
        print(row)

    return s[n][m]


n = 9
m = 6


down = [
    [0, 4, 2, 1, 0, 4, 2],
    [3, 2, 0 ,3 ,0, 2, 2],
    [0 ,4 ,4, 1, 3, 4, 1],
    [2 ,3 ,3, 0, 3, 1, 1],
    [3, 0, 4 ,4, 0, 3 ,2],
    [0 ,0, 0, 3, 4, 4, 1],
    [1, 1, 3 ,1, 3 ,3 ,4],
    [0, 2, 1, 4, 1 ,2, 1],
    [0, 1, 1 ,0, 0, 1, 2]
]

right = [
    [1, 3, 1 ,3, 3, 1],
    [2 ,1, 0, 0, 2, 2],
    [4, 3, 4, 0, 3 ,4],
    [2, 2 ,0 ,3 ,1 ,2],
    [1, 3, 2 ,0, 2, 2],
    [2, 0, 0, 2, 1, 4],
    [3, 2, 3 ,2 ,0, 4],
    [4, 3, 4 ,0, 1, 3],
    [4, 2 ,1 ,0, 0, 2],
    [4, 2, 4, 4, 2, 3]
]

longestpath = mtlp(n, m, down, right)
print(longestpath)
