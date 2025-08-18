A = int(input())
B = int(input())

X = A % 3 == 0 and B % 3 == 0
Y = A % 12 == 0 or B % 12 == 0

if X and Y:
    print("Pair")
else:
    print("Not a Pair")
