S = input()
vowels = "aeiou"
vowels_count = 0

for i in S:
    for j in vowels:
        if i==j:
            vowels_count+=1


if vowels_count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
