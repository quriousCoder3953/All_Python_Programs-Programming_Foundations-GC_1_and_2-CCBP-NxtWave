A = int(input())

X = A % 11 == 0
Y = A % 11 == 1

if X or Y:
    print("Special Eleven")
    
else:
    print("Normal Number")
