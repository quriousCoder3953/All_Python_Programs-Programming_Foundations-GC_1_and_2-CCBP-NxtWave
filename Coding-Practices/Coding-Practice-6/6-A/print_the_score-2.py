D = int(input())
if D <= 50:
    Score = D * 3
else:
    Score = 50 * 3 + ((D - 50) * 5)
print(Score)
