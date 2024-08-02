def manacher_odd(string, n):
    d = [1] * n
    l, r = 0, -1
    for i in range(n):
        if i <= r:
            d[i] = min(r - i + 1, d[l + r - i])
        while i - d[i] >= 0 and i + d[i] < n and string[i - d[i]] == string[i + d[i]]:
            d[i] += 1
        if i + d[i] - 1 > r:
            l, r = i - d[i] + 1, i + d[i] - 1
    return d

def manacher_even(string, n):
    d = [0] * n
    l, r = 0, -1
    for i in range(n):
        if i <= r:
            d[i] = min(r - i + 1, d[l + r - i + 1])
        while i - d[i] - 1 >= 0 and i + d[i] < n and string[i - d[i] - 1] == string[i + d[i]]:
            d[i] += 1
        if i + d[i] - 1 > r:
            l, r = i - d[i], i + d[i] - 1
    return d

def solve(string, n, man_0, man_1):
    positions = [[1] * 26 for _ in range(n)]
    references = [True] * n

    right = 1
    for i in range(1, n - 1):
        radius = man_1[i]
        if i < right:
            references[i] = False
        right = max(right, i + radius)
        if right == n:
            references[n - 1] = False
        if i + radius < n and i - radius >= 0:
            positions[i + radius][ord(string[i - radius]) - 97] = 0

    right = 1
    for i in range(1, n):    
        radius = man_0[i]
        right = max(right, i + radius)
        if i < right:
            references[i] = False
        if i + radius < n and i - radius - 1 >= 0:
            positions[i + radius][ord(string[i - radius - 1]) - 97] = 0

    return positions, references

def main():
    string = input()
    n = len(string)

    man_0 = manacher_even(string, n)
    man_1 = manacher_odd(string, n)

    positions, references = solve(string, n, man_0, man_1)
    
    result = 1
    mod = 10 ** 9 + 7
    for i in range(n):
        if references[i]:
            result = (result * sum(positions[i])) % mod

    print(result)

if __name__ == "__main__":
    main()