T = int(input())
M = int(input())
N = int(input())

z = 0

for i in range(M, N + 1):
    if i % T == 0:
        z = i + z
print(z)
