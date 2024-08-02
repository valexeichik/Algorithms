numbers = input().split()
n = int(numbers[0])
k = int(numbers[1])

binom_table = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(k + 1):
        if j == 0 or j == i:
            binom_table[i][j] = 1
        else:
            binom_table[i][j] = binom_table[i - 1][j] + binom_table[i - 1][j - 1]

print(binom_table[n][k] % (10 ** 9 + 7))