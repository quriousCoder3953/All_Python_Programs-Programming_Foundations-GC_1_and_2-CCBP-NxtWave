D = int(input())
if D <= 40:
    Score = D * 2
elif 40 < D <= 60:
    Score = 40 * 2 + ((D - 40) * 4)
elif 60 < D <= 120:
    Score = 40 * 2 + 20 * 4 + ((D - 60) * 6)
else:
    Score = 40 * 2 + 20 * 4 + 60 * 6 + ((D - 120) * 8)
Score += 50
print(Score)
