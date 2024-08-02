import heapq
import mmap

def encode(frequencies):
    total = 0
    while len(frequencies) > 1:
        freq1 = heapq.heappop(frequencies)
        freq2 = heapq.heappop(frequencies)
        new_freq = freq1 + freq2
        heapq.heappush(frequencies, new_freq)

        total += new_freq

    return total

def main():
    with open('huffman.in', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline())
            frequencies = [int(freq) for freq in mfile.read().split()]

    sum = encode(frequencies)

    with open('huffman.out', 'w') as file:
        file.write(str(sum))

if __name__ == "__main__":
    main()