import bisect

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))

lis_array = [float('inf')] * n
lis_array[0] = numbers[0]
lis_length = 1

for i in range(1, n):
    pos = bisect.bisect_left(lis_array, numbers[i], hi=lis_length)
    if pos == n:
        lis_array[-1] = numbers[i]
        lis_length = n
    else:
        lis_array[pos] = numbers[i]
        if lis_length < pos + 1:
            lis_length = pos + 1

with open('output.txt', 'w') as file:
    file.write(str(lis_length))