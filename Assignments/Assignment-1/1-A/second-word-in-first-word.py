W_1 = input()
W_2 = input()
index = -1
for i in range(len(W_2)):
    if W_1[i] == W_2[i]:
        index += 1
    else:
        break
print(index)
