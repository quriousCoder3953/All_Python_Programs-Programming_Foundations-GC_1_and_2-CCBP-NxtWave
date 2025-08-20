M = int(input())
N = int(input())

squaresSum = 0

for i in range(M, N+1):
    squaresSum += (i**2)
    
print(squaresSum)
