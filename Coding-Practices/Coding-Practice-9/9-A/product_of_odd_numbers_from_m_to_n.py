M = int(input())

N = int(input())

odd_prod = 1

for i in range(M, N+1):
    if i%2==1:
        odd_prod *= i

print(odd_prod)
