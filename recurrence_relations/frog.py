n = int(input())
mosquitoes = [int(mosq) for mosq in input().split()]

frog_array = [-1] * n
frog_array[0] = mosquitoes[0]
for i in range(2, n):
    frog_array[i] = max(frog_array[i - 2], frog_array[i - 3]) + mosquitoes[i]

print(frog_array[n - 1])

if frog_array[n - 1] != -1:
    jumps = [n]
    index = n - 1
    while (index > 3):
        if frog_array[index - 2] > frog_array[index - 3]:
            jumps.append(index - 1)
            index -= 2
        else:
            jumps.append(index - 2)
            index -= 3
    if n > 1:
        jumps.append(1)

    print(' '.join(map(str, reversed(jumps))))