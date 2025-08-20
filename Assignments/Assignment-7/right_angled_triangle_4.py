N = int(input())
i = 0
while i < 2:
    j = 1
    while j < N+1:
        triangled_string = ("*" + " ") * j
        print(triangled_string)
        j += 1
    i+=1
