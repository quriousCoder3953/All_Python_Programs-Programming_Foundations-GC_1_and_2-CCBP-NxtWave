N = input()
A = int(N[0])
B = int(N[1])
N = int(N)

X = N % A == 0
Y = N % B == 0

if X and Y:
    print(N * 2)
else:
    print(N)
