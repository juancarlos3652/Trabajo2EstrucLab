matriz=[]
matriz1=[]
print("Ingrese el orden de la matriz")
fila=int(input("Ingrese la cantidad de la fila: "))
columna=int(input("Ingrese la cantidad de columna: "))
for i in range(fila):
    matriz.append([])
    matriz1.append([])
    for j in range(columna):
        print("Para la primera matriz")
        filaMatriz=int(input("Fila {}, columna {} ".format(i+1,j+1)))
        print("Para la segunda matriz")
        filamatriz1=int(input("Fila {}, columna {} ".format(i+1,j+1)))
        matriz[i].append(filaMatriz)
        matriz1[i].append(filamatriz1)
def multipliMatrices(matriz, matriz1):
    if len(matriz[0])==len(matriz1):
        matriz2=[]
        for i in range(len(matriz)):
            matriz2.append([])
            for j in range(len(matriz1[0])):
                matriz2[i].append(0)

        for i in range(len(matriz)):
            for j in range(len(matriz1[0])):
                for k in range(len(matriz[0])):
                    matriz2[i][j] +=matriz[i][k] * matriz1[k][j]
        return matriz2
a=multipliMatrices(matriz,matriz1)
for fila in a:
    print("[", end=" ")
    for elemento in fila:
        print(elemento,end=" ")
    print("]")

