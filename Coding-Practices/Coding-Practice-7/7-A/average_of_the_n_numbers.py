N = int(input())
sum_of_natural_numbers = 0

for i in range(1, N+1):
    sum_of_natural_numbers += i
    
average = float(sum_of_natural_numbers / N)
print(average)
