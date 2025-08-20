M = int(input())
N = int(input())

num_prod = 1

for i in range(M, N+1):
    num_prod *= i

print(num_prod)
