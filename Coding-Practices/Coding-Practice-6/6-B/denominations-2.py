Amount = int(input())

A = Amount // 100
B = (Amount % 100) //  50
C = ((Amount % 100) %  50 ) // 10
D = ((Amount % 100) %  50 ) % 10

print("100:" + str(A))
print("50:" + str(B))
print("10:" + str(C))
print("1:"+ str(D))
