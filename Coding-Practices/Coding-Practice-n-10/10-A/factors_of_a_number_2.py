N = int(input())

factors = ""

for i in range(1, N+1):
    if N%i==0:
        fct_str = str(i) + " "
        factors+=fct_str
        
print(factors)
