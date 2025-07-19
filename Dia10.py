# Dia 10 Nvl 1...


#1. Itere del 0 al 10 usando el bucle for y while
number = 0
while number <11:
    print(number)
    number = number + 1

for num in range(10):
    print(num)

#2. Itere de 10 a 0 usando el bucle for y while
for n in range(10, -1, -1):
    print(n)

i = 10
while i >= 0:
    print(i)
    i -= 1
#3. Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:

h = "#"
o = 0
while o < 7:
    print(h)
    h += "#"
    o += 1

#4. Utilice bucles anidados 
for fila in range(8):  
    for fila in range(8):
        print("#", end=" ")    
    print()               

#5. Tabla
n1= 0
for tabla in range(11):
    for fila in range(1):
        print(n1 ,"x" , n1 ,"=" , n1*n1)
        n1 += 1

#6. Lista
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lis in lista:
    print(lis)

#7. Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares
for n1 in range(0, 100):
    if n1 % 2 == 0:
        print(n1)
#8. Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares
for n2 in range(0, 100):
    if n2 % 2 != 0:
        print(n2)

#EJERCICIOS NIVEL 2:
#1, Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.
suma = 0
for n3 in range(0, 101):
    suma += n3
print(suma)

#2. Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todos los impares.
par = 0
impar = 0
for n5 in range(0,100):
    if n5 % 2 == 0:
        par += n5
    elif n5 % 2 != 0:
        impar += n5
print(par, impar)