N =int(input())

for i in range(1, N+1):
    if i<N:
        print((" "*(2*(N-i))) + ("* "*i))
    else:
        print("* " * N)
