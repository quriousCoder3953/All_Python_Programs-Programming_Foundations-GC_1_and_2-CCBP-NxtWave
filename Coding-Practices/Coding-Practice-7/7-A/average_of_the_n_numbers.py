N = int(input())
sum_of_natural_numbers = 0
i = 1

while i < N+1:
    sum_of_natural_numbers += i
    i+=1
    
average = float(sum_of_natural_numbers / N)
print(average)
