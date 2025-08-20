N = input()
L = len(N)
z = 0

for i in range(L):
    z = int(N[i]) + z
print(z)
