N = int(input())
z = 0

for i in range(1, N):
    if N % i == 0:
        z += i
if z == N:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
