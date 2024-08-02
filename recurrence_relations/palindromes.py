with open('input.txt', 'r') as file:
    word = file.read()

n = len(word)

lps_table = [[0] * n for _ in range(n)]

for i in range(n):
    lps_table[i][i] = 1

for i in range(1, n):
    if word[i] == word[i - 1]:
        lps_table[i - 1][i] = 2
    else:
        lps_table[i - 1][i] = 1

for j in range(2, n):
    for i in range(0, n - j):
        if word[i] == word[i + j]:
            lps_table[i][i + j] = lps_table[i + 1][i + j - 1] + 2
        else:
            lps_table[i][i + j] = max(lps_table[i][j + i - 1], lps_table[i + 1][i + j])

path = []
start_index, end_index = 0, n - 1
path.append([start_index, end_index])

while end_index - start_index + 1 > lps_table[start_index][end_index]:
    if lps_table[start_index][end_index] == lps_table[start_index][end_index - 1]:
        start_index, end_index = start_index, end_index - 1
    elif lps_table[start_index][end_index] == lps_table[start_index + 1][end_index]:
        start_index, end_index = start_index + 1, end_index
    else:
        start_index, end_index = start_index + 1, end_index - 1
    path.append([start_index, end_index])

palindrom = word[start_index:end_index + 1]

for i in range(len(path) - 2, -1, -1):
    if path[i][0] < path[i + 1][0] and path[i][1] > path[i + 1][1]:
        palindrom = word[path[i][0]] + palindrom + word[path[i][1]]

with open("output.txt", 'w') as file:
    file.write(str(lps_table[0][n - 1]) + '\n' + palindrom)