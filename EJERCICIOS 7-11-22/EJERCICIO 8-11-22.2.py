n1 = int(input("Dame el numero 1: "))
n2 = int(input("Dame el numero 2: "))
n3 = int(input("Dame el numero 3: "))

if n1 != n2 and n1 != n3 and n2 != n3 and n2 != n1:
    if n1 > n2:
        if n1 > n3:
            print("El numero mayor es: ",n1)
        else:
            print("El numero mayor es: ",n3)
    else:
        if n2 > n3:
            print("El numero mayor es: ",n2)
        else:
            print("El numero mayor es:",n3)
