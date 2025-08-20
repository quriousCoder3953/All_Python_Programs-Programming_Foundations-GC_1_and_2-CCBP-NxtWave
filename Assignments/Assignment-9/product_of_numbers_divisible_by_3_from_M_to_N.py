M = int(input())
N = int(input())
prod = 1

for i in range(M, N+1):
    if i % 3 == 0:
        prod *= i
        
print(prod)
