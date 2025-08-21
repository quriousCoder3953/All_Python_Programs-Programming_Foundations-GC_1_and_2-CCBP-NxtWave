N = int(input())

for i in range(N,0,-1):
    S = str(i)
    Line = S*i
    print(" " * (N-i) +  Line)
