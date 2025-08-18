N = input()
S = 0
contains_1 = False
for i in N:
    S += int(i)
for i in N:
    if int(i) == 1:
        contains_1 = True
        break
    
if contains_1 and S < 12 and int(N[-1]) == 5:
    print(True)
else:
    print(False)
