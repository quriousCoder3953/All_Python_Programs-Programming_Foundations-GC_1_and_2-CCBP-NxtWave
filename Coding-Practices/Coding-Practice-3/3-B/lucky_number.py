A = int(input())
B = int(input())

X = A == 6 or B == 6
Y = (A + B) == 6 or (A - B) == 6 or (B - A) == 6
if X:
    print("Lucky")
elif Y:
    print("Lucky")
else:
    print("Not Lucky")
