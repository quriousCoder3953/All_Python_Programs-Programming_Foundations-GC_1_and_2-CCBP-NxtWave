U = int(input())
if U <= 50:
    B = U * 2
elif U <= 150:
    B = 50 * 2 + (U - 50) * 3
elif U <= 250:
    B = 50 * 2 + 100 * 3 + (U - 150) * 5
else:
    B = 50 * 2 + 100 * 3 + 100 * 5 + (U - 250) * 8
S = B * 20 / 100
TB = B + S
print(TB)
