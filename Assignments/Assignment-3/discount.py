A = input()
B = input()
X = A[:3]
Y = B[:3]
U = X == "DIS"
V = Y == "DIS"
if U or V:
    print("Discount")
else:
    print("No Discount")
