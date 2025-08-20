N = int(input())
T = int(input())

num_count = 0

for i in range(1, N+1):
    if i % T == 0:
        num_count += 1

print(num_count)
