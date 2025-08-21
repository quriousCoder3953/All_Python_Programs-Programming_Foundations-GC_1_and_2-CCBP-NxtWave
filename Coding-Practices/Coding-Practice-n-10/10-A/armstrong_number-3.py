N = input()

L = len(N)

z = 0

for i in range(L):
    A = int(N[i]) ** L
    z = A + z
    
if z == int(N):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
