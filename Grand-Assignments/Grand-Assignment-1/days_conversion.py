N = int(input())
Y = N//365
sub = N % 365
W = sub // 7
D = sub % 7
print(Y, "years", W, "weeks", D, "days")
