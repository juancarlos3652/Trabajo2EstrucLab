tamArreglo=int(input("Ingrese el tamaño del array: "))
tamMultiplos=int(input("Ingrese un número:  "))
array=[]
for i in range(0,tamArreglo):
    array.append((i+1)*tamMultiplos)
print(array)