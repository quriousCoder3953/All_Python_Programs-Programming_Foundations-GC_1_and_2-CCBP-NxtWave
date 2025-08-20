N = int(input())
K = int(input())

z = 0

for i in range(1, N + 1):
    z = i ** K + z
print(z)
