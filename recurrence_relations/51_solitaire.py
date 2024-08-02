cards = [0]
with open('input.txt', 'r') as file:
    n = int(file.readline())
    cards += list(map(int, file.readline().split()))

positions = [0] * (n + 1)
solitaire_table = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    solitaire_table[i][i] = 0
    positions[cards[i]] = i

for stack_length in range(2, n + 1):
    for i in range(n - stack_length + 1, 0, -1):
        j = i + stack_length - 1
        for k in range(i, j):
            penalty = solitaire_table[i][k] + solitaire_table[k + 1][j] + abs(positions[j] - positions[k])
            if penalty < solitaire_table[i][j]:
                solitaire_table[i][j] = penalty
        
with open('output.txt', 'w') as file:
    file.write(str(solitaire_table[1][n]))