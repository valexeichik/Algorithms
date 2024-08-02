with open('input.txt', 'r') as file:
    n = int(file.readline())
    nodes = [-1] + list(map(int, file.read().split()))

i = 1
result = True
while 2 * i <= n:
    if 2 * i + 1 <= n:
        if not (nodes[2 * i + 1] >= nodes[i] and nodes[2 * i] >= nodes[i]):
            result = False
            break
    else:
        if not nodes[2 * i] >= nodes[i]:
            result = False
            break
    i += 1

with open('output.txt', 'w') as file:
    if result:
        file.write('Yes')
    else:
        file.write('No')