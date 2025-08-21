N = int(input())
a = int(input())
smallest_number = a

for i in range(N-1):
    b = int(input())
    if b < smallest_number:
        smallest_number = b
        
print(smallest_number)
