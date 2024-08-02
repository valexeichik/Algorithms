import mmap

def prefix_function(string, n):
    prefix = [0] * n
    prefix[0] = -1
    k = 0
    for i in range(1, n):
        while k > 0 and string[k] != string[i]:
            k = prefix[k - 1]
        if string[i] == string[k]:
            k += 1
        prefix[i] = k
    return prefix

def kmp(text, string, n):
    prefix = prefix_function(string, n)
    k = 0
    for i in range(2 * n):
        while k > 0 and string[k] != text[i]:
            k = prefix[k - 1]
        if string[k] == text[i]:
            k += 1
        if k == n:
            return i - n + 1
    return -1

def main():
    with open('input.txt', 'r') as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mfile:
            n = int(mfile.readline())
            string1 = mfile.readline().strip()
            string2 = mfile.readline().strip()

    result = kmp(string1 + string1, string2, n)
    
    with open('output.txt', 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    main()