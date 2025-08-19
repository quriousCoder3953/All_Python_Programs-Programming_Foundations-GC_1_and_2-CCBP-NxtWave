Y = input()

A = int(Y[-2])
B = int(Y[-1])

Y = int(Y)

if A == 0 and B == 0:
    if Y % 400 == 0:
        print("True")
    else:
        print("False")
elif Y % 4 == 0:
    print("True")
else:
    print("False")
