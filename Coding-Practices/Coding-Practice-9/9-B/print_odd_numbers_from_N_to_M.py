M = int(input())
N = int(input())
odd_num_str = ""

for i in range(N, M-1, -1):
    if i%2==1:
        odd_num = str(i) + " "
        odd_num_str+=odd_num

print(odd_num_str)
