A = int(input())
B = int(input())
C = int(input())
triangle_ABC = A + B + C == 180
if triangle_ABC:
    for i in range(3):
        print("*" * (i+1))
else:
    print("Not a Valid Triangle")
