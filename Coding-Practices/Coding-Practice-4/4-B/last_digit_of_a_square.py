N = int(input())
M = N ** 2
A = str(N)
B = str(M)
C = A[-1] == B[-1]
if C:
    print("Equal")
else:
    print("Not Equal")
