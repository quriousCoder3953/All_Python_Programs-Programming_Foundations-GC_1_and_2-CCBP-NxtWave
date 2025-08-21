N = int(input())
is_divisibe = False
for i in range(2, 10):
    if N%i==0:
        is_divisibe=True
        break
    
if (is_divisibe):
    print("Divisible Number")
else:
    print("Indivisible Number")
