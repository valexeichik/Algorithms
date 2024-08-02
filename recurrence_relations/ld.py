with open('in.txt', 'r') as file:
    d_penalty = int(file.readline())
    i_penalty = int(file.readline())
    r_penalty = int(file.readline())
    A_string = file.readline()
    B_string = file.readline()

a_length = len(A_string)
b_length = len(B_string)

ld_table = [[0 for _ in range(b_length + 1)] for _ in range(a_length + 1)]

for a_i in range(a_length + 1):
    ld_table[a_i][0] = a_i * d_penalty
for b_i in range(b_length + 1):
    ld_table[0][b_i] = b_i * i_penalty

for a_i in range(1, a_length + 1):
    for b_i in range(1, b_length + 1):
        ld_table[a_i][b_i] = min(ld_table[a_i - 1][b_i] + d_penalty,
                                 ld_table[a_i][b_i - 1] + i_penalty,
                                 ld_table[a_i - 1][b_i - 1] 
                                 + (0 if A_string[a_i - 1] == B_string[b_i - 1] else 1) * r_penalty)

with open('out.txt', 'w') as file:
    file.write(str(ld_table[-1][-1]))