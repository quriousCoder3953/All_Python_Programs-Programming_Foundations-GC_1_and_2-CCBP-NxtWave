S = input()
X = S[:3] == "NXT"
Y = int(S[3:]) % 2 == 0 or int(S[3:]) % 7 == 0
if X and Y:
    print("Special String")
else:
    print("Not a Special String")
