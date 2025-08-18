N = input()
A = int(N[0]) > 4
B = int(N[1]) > 4
C = int(N[2]) > 4
X = int(N[0]) == 6
Y = A and B and C
print(X or Y)
