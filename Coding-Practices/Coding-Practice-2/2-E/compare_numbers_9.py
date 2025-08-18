N = input()
greater_than_7 = True
for i in N:
    if int(i) <= 7:
        greater_than_7 = False
X = (int(N[0]) * int(N[1])) <= 30
Y = (int(N[1]) * int(N[2])) <= 30
Z = (int(N[0]) * int(N[2])) <= 30
W = X and Y and Z

print(greater_than_7 or W)
