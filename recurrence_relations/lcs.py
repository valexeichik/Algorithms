n = int(input())
sequence_a = input().split()
sequence_b = input().split()

lcs_table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for a_index, a_number in enumerate(sequence_a):
    for b_index, b_number in enumerate(sequence_b):
        if a_number == b_number:
            lcs_table[a_index + 1][b_index + 1] = lcs_table[a_index][b_index] + 1
        else:
            lcs_table[a_index + 1][b_index + 1] = max(
                lcs_table[a_index + 1][b_index],
                lcs_table[a_index][b_index + 1]
            )

a_index = b_index = n
match_indices_a = []
match_indices_b = []
while a_index > 0 and b_index > 0:
    if sequence_a[a_index - 1] == sequence_b[b_index - 1]:
        match_indices_a.append(a_index - 1)
        match_indices_b.append(b_index - 1)
        a_index -= 1
        b_index -= 1
    elif lcs_table[a_index - 1][b_index] > lcs_table[a_index][b_index - 1]:
        a_index -= 1
    else:
        b_index -= 1

match_indices_a_str = ' '.join(map(str, reversed(match_indices_a)))
match_indices_b_str = ' '.join(map(str, reversed(match_indices_b)))
print(lcs_table[-1][-1])
print(match_indices_a_str)
print(match_indices_b_str)