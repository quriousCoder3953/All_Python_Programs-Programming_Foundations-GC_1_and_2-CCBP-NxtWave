N = int(input())

for i in range(N,0,-1):
    S = str(i) + " "
    spaces = " " * (2*(N-i))
    L = spaces + S*i
    print(L)
