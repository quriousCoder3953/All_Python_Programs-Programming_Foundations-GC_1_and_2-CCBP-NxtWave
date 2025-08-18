A = input()

X = (int(A[0]) + int(A[1])) == 7
Y = (int(A[0]) == 7) or (int(A[1]) == 7)

A = int(A)

Z = A % 7 == 0

if X or Y or Z:
    print("Special Number")
else:
    print("Normal Number")
