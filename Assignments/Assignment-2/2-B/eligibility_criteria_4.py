M = int(input())
P = int(input())
C = int(input())

x = M >= 60 and P >= 50 and C >=45
y = M + P + C >= 180
X = x and y
Y = (M + P) >= 120 or (C + P) >=110
print(X or Y)
