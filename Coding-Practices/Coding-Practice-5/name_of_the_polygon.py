N = int(input())
if N < 3:
    print("Not Polygon")
elif N == 3:
    print("Triangle")
elif N == 4:
    print("Quadrilateral")
elif N == 5:
    print("Pentagon")
else:
    print("Big Polygon")
