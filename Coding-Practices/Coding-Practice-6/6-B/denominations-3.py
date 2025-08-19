Amount = int(input())

A = Amount // 500
B = (Amount - (500 * A)) //  50
C = (Amount - (500 *A + 50 * B)) // 10
D = (Amount - (500*A + 50 * B + 10 * C)) // 1

print(("500:" + " " +  str(A)) + " " + ("50:" + " " + str(B)) + " " + ("10:" + " " + str(C)) + " " + ("1:" + " " + str(D)))
