A = input()
B = input()
L = len(B)
z = ""
for i in A:
    z = i + z
last_part = z[:L]
last_part_of_string = ""
for i in last_part:
    last_part_of_string = i + last_part_of_string
print(last_part_of_string == B)
