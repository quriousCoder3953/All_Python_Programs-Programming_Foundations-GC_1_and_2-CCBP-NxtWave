X = int(input())
N = int(input())

product = 1
i = 0

while i<N:
    X += 1
    product *= X
    i+=1
    
print(product)
