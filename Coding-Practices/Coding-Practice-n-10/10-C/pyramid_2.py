N = int(input())

for i in range(1, N+1):
    j = str(i) + " "
    S = j * (2*i-1)
    spaces = " " * (2*(N-i))
    L = spaces + S
    print(L)
