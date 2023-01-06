#Estructura compuestas MATRICES 
def cantidadCaninos(matriz,matriz1):
    print("Ingrese el orden de la matriz")
    fila=int(input("Ingrese la cantidad de la fila: "))
    columna=int(input("Ingrese la cantidad de columna: "))
    for i in range(fila):
        matriz.append([])
        matriz1.append([])
        for j in range(columna):
            filaMatriz=input("Fila {}, columna {} ".format(i+1,j+1))
            matriz[i].append(filaMatriz)
            matriz1[i].append(len(filaMatriz))
    return matriz, matriz1
matriz1=[]
matriz2=[]
print(cantidadCaninos(matriz1,matriz2))
print()
print()
print("Lista de nombres")
for fila in matriz1:
    print("[", end=" ")
    for elemento in fila:
        print(elemento,end=" ")
    print("]")
print()
print("Tamaño de la fila y columna de la primera matriz")
for fila in matriz2:
    print("[", end=" ")
    for elemento in fila:
        print(elemento,end=" ")
    print("]")
