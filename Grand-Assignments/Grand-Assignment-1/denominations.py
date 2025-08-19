N = int(input())
A = N // 1000
B = (N - (A * 1000)) // 500
C = (N - (A * 1000 + B * 500)) // 100
D = (N - (A * 1000 + B * 500 + C * 100)) // 50
E = (N - (A * 1000 + B * 500 + C *100 + D * 50)) // 20
F = (N - (A * 1000 + B * 500 + C *100 + D * 50 + E * 20)) // 5
G = (N - (A * 1000 + B * 500 + C *100 + D * 50 + E * 20 + F * 5)) // 1
print("1000:" + str(A))
print("500:" + str(B))
print("100:" + str(C))
print("50:" + str(D))
print("20:" + str(E))
print("5:" + str(F))
print("1:" + str(G))
