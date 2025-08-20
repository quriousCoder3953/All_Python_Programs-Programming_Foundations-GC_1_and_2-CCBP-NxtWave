X = int(input())
N = int(input())

product = 1

for i in range(N):
    X += 1
    product *= X
print(product)
