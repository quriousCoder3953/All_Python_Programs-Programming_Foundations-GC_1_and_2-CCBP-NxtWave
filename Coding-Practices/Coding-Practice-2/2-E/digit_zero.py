A = input()
contains_zero = False
for i in A:
    if int(i) == 0:
        contains_zero = True
        break
print(contains_zero)
