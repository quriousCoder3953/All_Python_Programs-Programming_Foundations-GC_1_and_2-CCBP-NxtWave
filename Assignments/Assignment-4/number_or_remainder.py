N = int(input())
A = N % 5
B = N % 7
X = A == 0 and B == 0
Y = N < 7

if X or Y:
    print(N)
else:
    print(A)
    print(B)
