N = int(input())

numbersSum = 0

for i in range(1, N+1):
    numbersSum += i
    
numbersAVG = numbersSum / N

print(numbersAVG)
