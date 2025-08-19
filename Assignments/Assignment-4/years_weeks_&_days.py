N = int(input())
Y = N//365
sub = N - Y * 365
W = sub // 7
D = sub - W * 7
print(Y)
print(W)
print(D)
