array=[20, 15,12,11,8,4,1]
for i in range(len(array)-1):
    for j in range(len(array)-1):
        if array[j]>array[j+1]:
            temporal = array[j]
            array[j]=array[j+1]
            array[j+1]=temporal
print(array)
array.pop(0)
suma_de_notas=0
for notas in array:
    suma_de_notas+=notas
print("El promedio de notas es", (suma_de_notas)/len(array))







