M = int(input())
P = int(input())
C = int(input())

X = M >= 70 and P >= 60 and C >=60
Y = M + P + C >= 180

print(X or Y)
