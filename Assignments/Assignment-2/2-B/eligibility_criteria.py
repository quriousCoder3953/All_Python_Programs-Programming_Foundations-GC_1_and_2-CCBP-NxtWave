M = int(input())
P = int(input())
C = int(input())

X = M>=35 and P >=35 and C>=35
Y = (M + P) >= 90  or (P + C) >= 90 or (M + C) >=90
print(X and Y)
