S = input()
Multiplicative_number = S[-1]
Integer_Value = int(S[:-1])
if Multiplicative_number == 'T':
    Final_Output = Integer_Value * 10
elif Multiplicative_number == 'H':
    Final_Output = Integer_Value * 100
else:
    Final_Output = Integer_Value * 1000
print(Final_Output)
