N = int(input())
a = int(input())
greatest_number = a
for i in range(N - 1):
    b = int(input())
    if b > greatest_number:
        greatest_number = b
        
print(greatest_number)
