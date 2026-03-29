A = 0
B = 0
C = 1

numero = int(input("Dame la posicion hasta donde quieras que pare: "))
print(B)
print(C)

for x in range(numero):
    A = B + C
    B = C
    C = A
    print(A)
