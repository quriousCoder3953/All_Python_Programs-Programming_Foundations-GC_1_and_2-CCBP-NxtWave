D = int(input())
if D <= 20:
    Score = D * 2
elif 20 < D <= 60:
    Score = 20 * 2 + ((D - 20) * 4)
else:
    Score = 20 * 2 + 40 * 4 + ((D - 60) * 6)
Score += 30
print(Score)
