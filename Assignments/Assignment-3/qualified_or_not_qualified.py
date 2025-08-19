M = int(input())
P = int(input())

X = M > 35 and P > 35
Y = (M + P) >= 100
if X or Y:
    print("Qualified")
else:
    print("Not Qualified")
