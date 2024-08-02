def to_syllable(i):
    if i == 0:
        return 'chu'
    elif i == 1:
        return 'ka'
    else:
        return 'pi'
    
def get_indeces(i):
    if i == 0 or i == 3 or i == 6:
        return [0, 1, 2]
    elif i == 1:
        return [3, 4]
    elif i == 2 or i == 5:
        return [6, 7, 8]
    elif i == 4:
        return [3, 5]
    elif i == 7:
        return [3, 4, 5]
    elif i == 8:
        return [6, 7]

def find_city_name(n, k):
    if n == 1:
        return to_syllable(k - 1)
    else:
        words = [[0 for _ in range(n - 1)] for _ in range(9)]

        for j in range(9):
            words[j][0] = 1

        for i in range(1, n - 1):
            words[0][i] = words[3][i] = words[6][i] = words[0][i - 1] + words[1][i - 1] + words[2][i - 1]
            words[1][i] = words[3][i - 1] + words[4][i - 1]
            words[2][i] = words[5][i] = words[6][i - 1] + words[7][i - 1] + words[8][i - 1]
            words[4][i] = words[3][i - 1] + words[5][i - 1]
            words[7][i] = words[3][i - 1] + words[4][i - 1] + words[5][i - 1]
            words[8][i] = words[6][i - 1] + words[7][i - 1]

        name = []
        sum = 0
        index = 0
        for i in range(9):
            sum += words[i][n - 2]
            if k <= sum:
                index = i
                k -= (sum - words[i][n - 2])
                name.append(to_syllable(index // 3))
                break
        
        for i in range(n - 3, -1, -1):
            sum = 0
            for j in get_indeces(index):
                sum += words[j][i]
                if k <= sum:
                    index = j
                    k -= (sum - words[j][i])
                    name.append(to_syllable(index // 3))
                    break
        name.append(to_syllable(index % 3))
        return ''.join(name)

def main():
    n, k = map(int, input().split())
    name = find_city_name(n, k)
    print(name)

if __name__ == "__main__":
    main()