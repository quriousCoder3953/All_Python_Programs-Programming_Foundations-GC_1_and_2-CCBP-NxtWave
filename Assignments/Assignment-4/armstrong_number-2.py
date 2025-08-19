N = input()

A = int(N[0]) ** 4
B = int(N[1]) ** 4
C = int(N[2]) ** 4
D = int(N[3]) ** 4

N = int(N)

X = A + B + C + D

if X == N:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
