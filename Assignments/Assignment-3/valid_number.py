N = input()

X = int(N[0]) != 5 or int(N[1]) != 5 or int(N[2]) != 5
N = int(N)
Y = 300 < N < 700

if X and Y:
    print("Valid Number")
else:
    print("Not a Valid Number")
