N = input()

A = len(N)

if A == 1:
    print(N)
elif A == 2:
    U = int(N[0])
    W = int(N[1])
    print(U + W)
elif A == 3:
    U = int(N[0])
    W = int(N[1])
    X = int(N[2])
    print(U + W + X)
else:
    U = int(N[0])
    W = int(N[1])
    X = int(N[2])
    Y = int(N[3])
    print(U + W + X + Y)
