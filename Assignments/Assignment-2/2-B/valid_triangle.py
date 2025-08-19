A = int(input())
B = int(input())
C = int(input())
X = (A + B) > C
Y = (B + C) > A
Z = (A + C) > B
print(X and Y and Z)
