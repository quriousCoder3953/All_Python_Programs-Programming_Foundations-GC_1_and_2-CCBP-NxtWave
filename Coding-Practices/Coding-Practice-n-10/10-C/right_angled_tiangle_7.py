N =int(input())

for i in range(1, N+1):
    if i<N:
        print((" "*(N-i)) + ("*"*i))
    else:
        print("#" * N)
