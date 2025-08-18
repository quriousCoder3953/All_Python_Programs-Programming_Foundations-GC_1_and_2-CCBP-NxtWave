A = int(input())
B = int(input())
C = int(input())
X = A > 100
Y = B > 100
Z = C > 100
N = X and Y and Z
if N:
    print("All are greater than 100")
else:
    print("Not all are greater than 100")
