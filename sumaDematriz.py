#Suma de matrices
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
def sumar_matrices(matriz,matriz1):
    if len(matriz)==len(matriz1) and len(matriz[0]) ==len(matriz1[0]):
        m3=[]
        for i in range (len(matriz)):
            m3.append([])
            for j in range(len(matriz[0])):
                m3[i].append(matriz[i][j]+matriz1[i][j])
        return m3
    else:
        return None

c=sumar_matrices(matriz,matriz1)       
if c==None:
    print("No se pueden sumar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento,end=" ")
        print("]")

print("ga")