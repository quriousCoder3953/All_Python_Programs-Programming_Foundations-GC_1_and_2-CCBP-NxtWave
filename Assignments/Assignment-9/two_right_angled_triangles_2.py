N = int(input())

for i in range (1, 2*N+1):
    if i >= N+1:
        i = 2*N-i+1
    print("* " * i)
