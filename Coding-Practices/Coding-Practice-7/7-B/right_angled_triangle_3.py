N = int(input())
i = 1

while i < N+1:
    if i == N:
        triangled_string = ("+" + " ") * i
    else:
        triangled_string = ("*" + " ") * i
    print(triangled_string)
    i += 1
