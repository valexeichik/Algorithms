import math
import sys

def build_blocks(sequence, block_size):
    blocks = [0] * block_size

    for i, item in enumerate(sequence):
        blocks[i // block_size] += item

    return blocks

def modification(blocks, sequence, block_size, index, value):
    blocks[index // block_size] += value
    sequence[index] += value

def find_sum(blocks, sequence, block_size, l, r):
    sum = 0
    left = l // block_size
    right = (r - 1) // block_size

    for i in range(left, right + 1):
        if i == left and i == right:
            for j in range(l, r):
                sum += sequence[j]
        elif i == left:
            for j in range(l, (i + 1) * block_size):
                sum += sequence[j]
        elif i == right:
            for j in range(i * block_size, r):
                sum += sequence[j]
        else:
            sum += blocks[i]

    return sum

def main():
    n = int(sys.stdin.readline())
    sequence = list(map(int, sys.stdin.readline().split()))

    block_size = math.ceil(math.sqrt(n))
    blocks = build_blocks(sequence, block_size)

    q = int(sys.stdin.readline())
    for _ in range(q):
        operation, op1, op2 = sys.stdin.readline().split()
        op1, op2 = int(op1), int(op2)
        
        if operation == 'FindSum':
            sys.stdout.write(str(find_sum(blocks, sequence, block_size, op1, op2)) + '\n')
        else:
            modification(blocks, sequence, block_size, op1, op2)

if __name__ == "__main__":
    main()