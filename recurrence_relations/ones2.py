numbers = input().split()
n = int(numbers[0])
k = int(numbers[1])

if k > n - k:
    k = n - k

mod = 10 ** 9 + 7
numerator = denominator = 1
for i in range(1, k + 1):
    numerator = (numerator * (n + 1 - i)) % mod
    denominator = (denominator * i) % mod 

binom_n_k = (numerator * pow(denominator, mod - 2, mod)) % mod
print(binom_n_k)