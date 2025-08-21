S = input()

vowels_list = ['a', 'e', 'i', 'o', 'u']

VS = ""

for i in S:
    for j in vowels_list:
        if i == j:
            VS+=i
            
print(VS)       
