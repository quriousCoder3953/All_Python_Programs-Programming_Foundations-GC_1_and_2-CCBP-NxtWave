N = input()
X = int(N[:2]) == 19
Y = 30 < int(N[2:]) < 60
print(X and Y)
