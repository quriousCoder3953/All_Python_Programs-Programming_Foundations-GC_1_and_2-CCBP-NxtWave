X = input()
N = int(input())
final_sum = 0

for i in range(1, N+1):
    digit = int(X*i)
    final_sum+=digit
    
print(final_sum)
