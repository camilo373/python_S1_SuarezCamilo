##comparacion de numeros
print("los numeros que satisfacen la siguiente exprecion p**3 + q**4 -2 p**2 < 680 son:")
for p in range (0,200):
    for q in range(0,200):
        expecionMatematica= p**3 + q**4 -2 + q**2
        if (expecionMatematica<680):
            print("p",p)
            print("q",q)
            print("resultado",expecionMatematica)
            