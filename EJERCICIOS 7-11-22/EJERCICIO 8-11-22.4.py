precio = int(input("Deme el precio a pagar de la compra: "))

if precio > 1499 and precio < 2801:
    Descuento = (precio / 100) * 13
    Total = precio - Descuento
    Total = str(Total)
    Descuento = str(Descuento)
    print("Recibio un descuento del 13% por lo tanto, su total a pagar es de: " + Total)

if precio > 2801 and precio < 3501:
    Descuento = (precio / 100) * 18
    Total = precio - Descuento
    Descuento = str(Descuento)
    Total = str(Total)
    print("Recibio un descuento del 18% por lo tanto, su total a pagar es de: " + Total)

if precio > 3500:
    Descuento = (precio / 100) * 20
    Total = precio - Descuento
    Total = str(Total)
    Descuento = str(Descuento)
    print("Recibio un descuento del 20% por lo tanto, su total a pagar es de: " + Total)
