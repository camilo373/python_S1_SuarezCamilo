## Mayor y menor
grande=0
pequeño=0
for i in range (1,11):
    N=int(input("ingrese numero:"))
    if i==1:
        grande=N
        pequeño=N
    elif N> grande:
        grande=N
    elif N<pequeño:
        pequeño=N

        print("el mayor es:",grande)
        print("el manor es:",pequeño)
        ## Desarollado por Camilo Suarez Fuentes TI 1097784213
