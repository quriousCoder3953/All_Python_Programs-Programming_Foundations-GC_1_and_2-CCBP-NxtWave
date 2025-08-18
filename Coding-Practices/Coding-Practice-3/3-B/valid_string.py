S = input()
X = S[0] != "a"
Y = 2 < len(S) < 7
if X or Y:
    print("Valid String")
else:
    print("Not a Valid String")
