A = int(input())
B = int(input())
X = A > 300 or B > 300
Y = (A + B) < 500

if X and Y:
    print("Can team up")
else:
    print("Cannot team up")
