N = int(input())

S = str(N)

SL = len(S)


result = 0
for i in range(SL):
    result += int(S[i]) ** SL
    
print(result)
