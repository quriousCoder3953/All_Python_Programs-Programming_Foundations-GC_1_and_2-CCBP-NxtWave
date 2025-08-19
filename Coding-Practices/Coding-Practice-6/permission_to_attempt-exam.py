A = input()
B = input()
X = len(A)-1
A = int(A[:X])

if A >= 75 :
    print("Allowed to write exam")
elif A < 75 and B == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
