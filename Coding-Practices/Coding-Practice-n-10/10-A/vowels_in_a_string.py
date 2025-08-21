S = input()

vowels = "aeiou"

VS = ""

for i in S:
    for j in vowels:
        if i == j:
            VS+=i
            
print(VS)
