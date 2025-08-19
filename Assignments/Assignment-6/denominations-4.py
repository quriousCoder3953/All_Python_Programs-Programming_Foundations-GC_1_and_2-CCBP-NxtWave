Amount = int(input())

A = Amount // 100
B = (Amount - (100 * A)) //  50
C = (Amount - (100 *A + 50 * B)) // 20
D = (Amount - (100*A + 50 * B + 20 * C)) // 10

print("100 Notes:", A)
print("50 Notes:", B)
print("20 Notes:", C)
print("10 Notes:", D)
