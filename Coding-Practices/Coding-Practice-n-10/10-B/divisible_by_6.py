M = int(input())
N = int(input())
numbers_divisible_by_6 = ""

for i in range(M, N+1):
    if i%6==0:
        number= str(i) + " "
        numbers_divisible_by_6+=number
        
if numbers_divisible_by_6 == "":
    print("No Numbers Found")
else:
    print(numbers_divisible_by_6)
