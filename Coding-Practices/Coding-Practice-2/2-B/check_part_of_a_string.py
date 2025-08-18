A = input()
B = input()
N = int(input())
res = True
for i in range(len(B)):
    if A[i + N] != B[i]:
        res = False
        break
print(res)
