import math

BLOSUM = {
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

OPEN_PENALTY = 11
EXTEND_PENALTY = 1


def align_with_affine_gap(s1, s2):
  height = len(s1)
  width = len(s2)

  lower, lower_bt = get_new_lower_grid(width, height)
  middle, middle_bt = get_new_middle_grid(width, height)
  upper, upper_bt = get_new_upper_grid(width, height)
  #view_matrices(lower, middle, upper)

  max_d = min(width + 1, height + 1)
  for d in range(1, max_d):

    # Populate (d,d) for lower, upper and middle
    calc_lower(d, d, lower, lower_bt, middle)
    calc_upper(d, d, upper, upper_bt, middle)

    score = BLOSUM[s1[d - 1]][s2[d - 1]]
    calc_middle(d, d, middle, middle_bt, lower, upper, score)

    # Populate (d+1...N, d) for the lower and middle
    for i in range(d + 1, max_d):
      calc_lower(i, d, lower, lower_bt, middle)

      score = BLOSUM[s1[d - 1]][s2[i - 1]]
      calc_middle(i, d, middle, middle_bt, lower, upper, score)

    # Populate (d,d+1...N) for the lower matrix
    for j in range(d+1, max_d):
      calc_lower(d, j, lower, lower_bt, middle)

    # Populate (d, d+1...N) for the upper and middle
    for j in range(d + 1, max_d):
      calc_upper(d, j, upper, upper_bt, middle)

      score = BLOSUM[s1[d - 1]][s2[j - 1]]
      calc_middle(d, j, middle, middle_bt, lower, upper, score)

    # Populate (d+1...N, d) for the upper matrix
    for i in range(d+1, max_d):
      calc_upper(i, d, upper, upper_bt, middle)

  # Populate remaining columns
  for i in range(1, max_d):
    for j in range(max_d, width + 1):
      calc_upper(i, j, upper, upper_bt, middle)

      score = BLOSUM[s1[i - 1]][s2[j - 1]]
      calc_middle(i, j, middle, middle_bt, lower, upper, score)

  for i in range(1, max_d):
    for j in range(max_d, width + 1):
      calc_lower(i, j, lower, lower_bt, middle)

      score = BLOSUM[s1[i - 1]][s2[j - 1]]
      calc_middle(i, j, middle, middle_bt, lower, upper, score)

  # Populate remaining rows
  for i in range(max_d, height + 1):
    for j in range(1, max_d):
      calc_upper(i, j, upper, upper_bt, middle)

      score = BLOSUM[s1[i - 1]][s2[j - 1]]
      calc_middle(i, j, middle, middle_bt, lower, upper, score)

  for i in range(max_d, height + 1):
    for j in range(1, max_d):
      calc_lower(i, j, lower, lower_bt, middle)

      score = BLOSUM[s1[i - 1]][s2[j - 1]]
      calc_middle(i, j, middle, middle_bt, lower, upper, score)

  #view_matrices(lower, middle, upper)
  print(middle[height][width])
  return backtrack(s1, s2, lower_bt, middle_bt, upper_bt)


def view_matrices(lower, middle, upper):
  print("\nLOWER")
  for row in lower:
    print([format(n, '03') for n in row])
  print("\nMIDDLE")
  for row in middle:
    print([format(n, '03') for n in row])
  print("\nUPPER")
  for row in upper:
    print([format(n, '03') for n in row])
  print()

def view_bt_matrices(lower, middle, upper):
  print("\nLOWER")
  for row in lower:
    print(row)
  print("\nMIDDLE")
  for row in middle:
    print(row)
  print("\nUPPER")
  for row in upper:
    print(row)
  print()


def backtrack(s1, s2, lower_bt, middle_bt, upper_bt):
  s1p = []
  s2p = []
  i = len(middle_bt) - 1
  j = len(middle_bt[0]) - 1

  #view_bt_matrices(lower_bt, middle_bt, upper_bt)

  while i>=0 and j>=0 and middle_bt[i][j] != '':
        if middle_bt[i][j] == "\\":
            s1p.append(s1[i-1])
            s2p.append(s2[j-1])
            i -= 1
            j -= 1
        elif middle_bt[i][j] == "|":
            s1p.append(s1[i-1])
            s2p.append('-')
            i -= 1
        elif middle_bt[i][j] == '-':
            s1p.append('-')
            s2p.append(s2[j-1])
            j -= 1
  s1p.reverse()
  s2p.reverse()

  return (s1p, s2p)


def calc_lower(i, j, lower, lower_bt, middle):
  next_lower = lower[i - 1][j] - EXTEND_PENALTY
  next_middle = middle[i - 1][j] - OPEN_PENALTY

  max_v = max(next_lower, next_middle)
  lower[i][j] = max_v

  if max_v == next_lower:
    lower_bt[i][j] = "|"
  else:
    lower_bt[i][j] = "\\"


def calc_upper(i, j, upper, upper_bt, middle):
  next_upper = upper[i][j - 1] - EXTEND_PENALTY
  next_middle = middle[i][j - 1] - OPEN_PENALTY

  max_v = max(next_upper, next_middle)
  upper[i][j] = max_v

  if max_v == next_upper:
    upper_bt[i][j] = "-"
  else:
    upper_bt[i][j] = "\\"


def calc_middle(i, j, middle, middle_bt, lower, upper, score):
  next_lower = lower[i][j]
  next_middle = middle[i - 1][j - 1] + score
  next_upper = upper[i][j]

  max_v = max(next_lower, next_middle, next_upper)
  middle[i][j] = max_v

  if max_v == next_upper:
    middle_bt[i][j] = "-"
  elif max_v == next_lower:
    middle_bt[i][j] = "|"
  else:
    middle_bt[i][j] = "\\"


def get_new_upper_grid(width, height):
  upper = [[0]]
  upper_bt = [[""]]

  # Set left edge to OPEN_PENALTY + index * EXTEND_PENALTY
  for i in range(height):
    #value = -OPEN_PENALTY - i * EXTEND_PENALTY
    value = -OPEN_PENALTY
    upper.append([value])
    upper_bt.append(["|"])

  # Set all other columns to negative infinity
  for i in range(height + 1):
    for j in range(width):
      upper[i].append(-math.inf)
      upper_bt[i].append("")

  return (upper, upper_bt)


def get_new_lower_grid(width, height):
  lower = [[0]]
  lower_bt = [[""]]

  # Set top edge to OPEN_PENALTY + index * EXTEND_PENALTY
  for i in range(width):
    #value = -OPEN_PENALTY - i * EXTEND_PENALTY
    value = -OPEN_PENALTY
    lower[0].append(value)
    lower_bt[0].append("-")


  # Set all other rows to negative infinity
  for i in range(1, height + 1):
    lower.append([-math.inf])
    lower_bt.append([""])
    for j in range(width):
      lower[i].append(-math.inf)
      lower_bt[i].append("")

  return (lower, lower_bt)


def get_new_middle_grid(width, height):
  middle = [[0]]
  middle_bt = [[""]]

  # Set top edge to OPEN_PENALTY + index * EXTEND_PENALTY
  for i in range(width):
    #value = -OPEN_PENALTY - i * EXTEND_PENALTY
    value = -OPEN_PENALTY
    middle[0].append(value)
    middle_bt[0].append("-")


  # Set left edge to OPEN_PENALTY + index * EXTEND_PENALTY
  for i in range(height):
    #value = -OPEN_PENALTY - i * EXTEND_PENALTY
    value = -OPEN_PENALTY
    middle.append([value])
    middle_bt.append(["|"])

  # Set all other rows and columns to negative infinity
  for i in range(1, height + 1):
    for j in range(width):
      middle[i].append(-math.inf)
      middle_bt[i].append("")

  return (middle, middle_bt)


#s1 = 'PRTEINS'
#s2 = 'PRTWPSEIN'

#s1 = 'AHRMPQ' #AHRMPQ
#s2 = 'AHED' #AHE--D

s1 = 'EFLYGWNCKSNSPRGAIERLHHQHDWCTEPYETPRDDTQAEKYYYPDDSWDPWVGHHSSKYFAAFCYYLSALPHLA'
s2 = 'MPMISNSWCTEPTEHDRTQGEKYYKPDDSHSNKYVTHHLSMVTFCYTLSASVKEEEHLA'

s1p, s2p = align_with_affine_gap(s1, s2)
print(''.join(s1p))
print(''.join(s2p))
