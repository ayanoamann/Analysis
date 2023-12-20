import numpy as np

def align_sequences(x, y, Array2):
    n = len(x)
    m = len(y)
    Array = np.zeros((n+1, m+1))

    for i in range(1, n+1):
        for j in range(1, m+1):
            match_score = Array[i-1, j-1] + Array2[x[i-1]][y[j-1]]
            delete_score = Array[i-1, j] + Array2[x[i-1]]['-']
            insert_score = Array[i, j-1] + Array2['-'][y[j-1]]
            Array[i, j] = max(match_score, delete_score, insert_score)

   
    Al_x = []
    Al_y = []
    i, j = n, m
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and Array[i, j] == Array[i-1, j-1] + Array2[x[i-1]][y[j-1]]:
            Al_x.append(x[i-1])
            Al_y.append(y[j-1])
            i -= 1
            j -= 1
        elif i > 0 and Array[i, j] == Array[i-1, j] + Array2[x[i-1]]['-']:
            Al_x.append(x[i-1])
            Al_y.append('-')
            i -= 1
        else:
            Al_x.append('-')
            Al_y.append(y[j-1])
            j -= 1

    Al_x.reverse()
    Al_y.reverse()

    return ''.join(Al_x), ''.join(Al_y)

# matrix
Array2 = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': None}
}

# the example
x = "ATGCC"
y = "TACGCA"


Al_x, Al_y = align_sequences(x, y, Array2)

print("Sequence x:", Al_x)
print("Sequence y:", Al_y)
