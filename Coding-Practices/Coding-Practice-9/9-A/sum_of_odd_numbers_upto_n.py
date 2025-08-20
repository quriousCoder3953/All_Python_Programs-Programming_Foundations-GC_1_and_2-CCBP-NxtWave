N = int(input())
z = 0

for i in range(1, N + 1):
    if i % 2 != 0:
        z = i + z
print(z)
