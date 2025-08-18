A = int(input())
B = int(input())
C = int(input())

X = (A - B) < 25
Y = (B - C) < 25
Z = (C - A) < 25

if X and Y and Z:
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")
