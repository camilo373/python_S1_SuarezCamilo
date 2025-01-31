## numeros enteros positivos

def suma_divisores_propios(n):
    suma = 0
    for i in range(1,n // 2 + 1 ):
        if n % i == 0: 
            suma += i
            return suma
        n1 = int(input("ingrese el primer numero (n1):"))
        n2 = int(input)("ingrese el segundo numero (n2):")
if suma_divisores_propios(n1)== n2 and suma_divisores_propios(n2)== n1:
    print(f"los numeros {n1} y {n2}son amigos")
else:
    print(f"los numeros {n1} y {n2} no son amigos")

    ##Desarrollado Camilo Suarez Fuentes TI 1097784213