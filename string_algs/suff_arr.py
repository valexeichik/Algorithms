def build_suffix_array(string, n):
    suffixes = [(i, string[i:]) for i in range(n)]
    suffixes.sort(key=lambda pair: pair[1])

    indices = [suffix[0] for suffix in suffixes]

    ranks = [0] * n
    ranks[indices[0]] = 0
    rank = 1
    for i in range(1, n):
        if suffixes[i][1] != suffixes[i - 1][1]:
            rank += 1
        ranks[indices[i]] = rank

    k = 1
    new_ranks = [0] * n
    while k < n:
        suffixes.sort(key=lambda pair: (ranks[pair[0]], ranks[( pair[0] + k) % n]))
        for i in range(n):
            new_ranks[i] = 0

        new_ranks[suffixes[0][0]] = 0
        rank = 1
        for i in range(1, n):
            if (ranks[suffixes[i][0]], ranks[(suffixes[i][0] + k) % n]) != (ranks[suffixes[i - 1][0]], ranks[(suffixes[i - 1][0] + k) % n]):
                rank += 1
        ranks = new_ranks
        k *= 2

    return [suffix[0] + 1 for suffix in suffixes]

def main():
    string = input() 
    n = len(string)
    print(n)
    print(' '.join([str(item) for item in build_suffix_array(string, n)]))

if __name__ == "__main__":
    main()