A = int(input())
B = int(input())
C = int(input())

X = A + B > C
Y = A + C > B
Z = B + C > A

if X and Y and Z:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
