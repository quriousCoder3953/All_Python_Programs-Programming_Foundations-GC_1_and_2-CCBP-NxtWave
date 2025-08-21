M = int(input())
N = int(input())

numbers_divisible = ""
for i in range(M, N+1):
    if i%9==0:
        div_num = str(i) + " "
        numbers_divisible+=div_num

if numbers_divisible != "":
    print(numbers_divisible)
else:
    print("No Numbers found")
