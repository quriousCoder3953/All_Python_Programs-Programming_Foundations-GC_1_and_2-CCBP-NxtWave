N = int(input())
z = 0

for i in range(1, N + 1):
    if N % i == 0:
        z = i + z
print(z)
