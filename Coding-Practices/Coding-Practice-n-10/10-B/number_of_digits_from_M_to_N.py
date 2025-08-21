M = int(input())
N = int(input())
no_of_digits = 0

for i in range(M, N+1):
    SL = len(str(i))
    no_of_digits+=SL

print(no_of_digits)
