N = int(input())
i = 1
SUM = 0

while i < N+1:
    square_of_number = i ** 2
    SUM += square_of_number
    i+=1
    
print(SUM)
