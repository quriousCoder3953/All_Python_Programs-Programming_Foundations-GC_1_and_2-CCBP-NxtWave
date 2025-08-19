A = input()
N = int(input())
letter = input()
B = A[:N] + letter + A[N+1:]
print(B)
