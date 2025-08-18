A = int(input())
B = int(input())
X = A + B
Y = A * B
U = len(str(X)) < 3
V = len(str(Y)) < 3
print(U and V)
