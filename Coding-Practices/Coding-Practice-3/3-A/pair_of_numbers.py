A = int(input())
B = int(input())
X = A <= 1000 and B <= 1000
Y = B > 500

if X or Y:
    print("Pair")
else:
    print("Not a Pair")
