X = int(input())
N = int(input())

sum_of_terms = 0

for i in range(1, N+1):
    j = 2*i
    term = X ** j
    if i%2==0:
        term*=(-1)
    sum_of_terms+=term
    
print(sum_of_terms)
