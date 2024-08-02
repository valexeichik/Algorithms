with open('input.txt', 'r') as file:
    n = int(file.read())

pow = 0 
result = []
while n:
    if n % 2 == 1:
        result.append(pow)
    pow += 1
    n //= 2

with open('output.txt', 'w') as file:
    file.write('\n'.join(list(map(str, result))))