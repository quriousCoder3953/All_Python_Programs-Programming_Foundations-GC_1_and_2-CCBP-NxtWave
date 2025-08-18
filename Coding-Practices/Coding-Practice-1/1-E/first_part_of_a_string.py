W = input()
z = ""
for i in W:
    if i.isdigit():
        z += i
    else:
        break
print(z)
