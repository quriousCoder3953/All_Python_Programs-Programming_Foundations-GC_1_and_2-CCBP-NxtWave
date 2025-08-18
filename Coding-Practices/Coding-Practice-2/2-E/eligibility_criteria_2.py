M = int(input())
P = int(input())
C = int(input())

X = (M + P) or (P + C) or (M + C) >= 100
Y = M + P + C >= 180

print(X and Y)
