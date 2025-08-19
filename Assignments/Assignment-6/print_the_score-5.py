D = int(input())
if D <= 50:
    Score = D * 3
elif 50 < D <= 100:
    Score = 50 * 3 + ((D - 50) * 5)
elif 100 < D <= 200:
    Score = 50 * 3 + 50 * 5 + ((D - 100) * 6)
else:
    Score = 50 * 3 + 50 * 5 + 100 * 6 + ((D - 200) * 10)
Score += 100
print(Score)
