with open('input.txt', 'r') as file:
    m, c, n = (int(item) for item in file.readline().split())
    keys = list(map(int, file.readlines()))

table = [-1] * m 
for key in keys:
    i = 0
    index = key % m
    while table[index] != -1:
        index = ((key % m) + c * i) % m
        i += 1
        if table[index] == key:
            break
    table[index] = key

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, table)))