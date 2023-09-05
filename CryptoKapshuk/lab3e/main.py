import random


def isPrime(n):
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


primes = [i for i in range(2 ** 7, 2 ** 8) if isPrime(i)]
p = 199
primes.remove(p)
q = 163

n = p * q
F = (p - 1) * (q - 1)

e = 3931
s = isPrime(140)
get_d = lambda x: ((F * x) + 1) / e

i = 1
d = get_d(i)

while d % 1 != 0:
    i += 1
    d = get_d(i)

d = int(d)

print(f"p = {p}\n"
      f"q = {q}\n"
      f"n = {n}\n"
      f"F = {F}\n"
      f"e = {e}\n"
      f"d = {d}")

message = "Face detection is the first step in automated face recognition."

chars = list(map(lambda x: ord(x), message))

encrypted = list(map(lambda x: x ** e % n, chars))

dec_chars = list(map(lambda x: x ** d % n, encrypted))

decrypted = list(map(lambda x: chr(x), dec_chars))

print(f"message = {message}\n"
      f"chars = {chars}\n"
      f"encrypted = {encrypted}\n"
      f"decrypted chars = {dec_chars}\n"
      f"decrypted = {''.join(decrypted)}")
