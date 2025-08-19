N = int(input())
Remainder = N % 6
if Remainder == 0:
    print("Group 6")
else:
    print("Group " + str(Remainder))
