A = input()
X = int(A[0])
Y = int(A[1])

A = int(A)

if (X == 9 or Y == 9) or (A % 9 == 0):
    print("Lucky Number")
else:
    print("Unlucky Number")
