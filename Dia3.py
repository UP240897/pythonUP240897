#EXERCICES : LEVEL 1  (1-4)=============== -
Age = 18                  #Numero entero
Height = 1.72             #Numero flotante
NC = 2 + 4j               #Numero complejo
b = int(input("Ingresa la base del triangulo: "))  #Base de triangulo
h = int(input("Ingresa la altura del triangulo: "))#altura de triangulo
Area = (b*h)/2               #Área del triangulo
print("El Área del triangulo es de: ", Area) 

#LEVEL 2  (5)====================
print("\n")
print("|Ingresa los lados del triangulo|")
l1 = int(input("Ingresa el lado a: ")) #Lado 1
l2 = int(input("Ingresa el lado b: ")) #Lado 2
l3= int(input("Ingresa el lado c: "))  #Lado 3
perimetro = l1 + l2 + l3
print("EL perimetro del traingulo es: ", perimetro) #Calcular perimetro

#Level 3 (6-21)===
#Rectangulo
print("\n")
print("|Área y perimetro de un rectangulo|")
length = int(input("Ingresa la longitud del rectangulo: "))
width = int(input("Ingresa el ancho del rectangulo: "))
a = length * width
perimeter = 2 * (length + width)
print("El área del rectangulo es: ", a , " y el perimetro es: ", perimeter)

#Circulo
print("\n")
print("|Área y Perimetro de un circulo|")
r = int(input("Ingresa el radio del circulo: "))
pi = 3.14
Ac = pi * r ** 2
circumference = 2 * pi * r
print ("El área del circulo es :", Ac) 
print("El perimetro es: ", circumference)

print("\n")
print("|pendiente|")

import math
# Ecuación: y = 2x - 2
print("\n")
m1 = 2
b1 = -2
x_int = (0 - b1) / m1
y_int = b1

print("Pendiente:", m1)
print("Intersección con eje x: (", x_int, ", 0 )")
print("Intersección con eje y: ( 0 ,", y_int, ")")

#Puntos (2,2) y (6,10)
print("\n")
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("\n=== Entre puntos (2,2) y (6,10) ===")
print("Pendiente entre puntos:", m2)
print("Distancia Euclidiana:", distance)

#Comparación
print("\n")
print("¿Las pendientes son iguales?", m1 == m2) 

#Value
print("\n")
print("|Value|")
for x in range(-10, 5):
    y = x**2 + 6*x + 9
    print(f"{x}\t|\t{y}")

# Verificación de cuándo y es 0
print("\n")
print("Cuando y = 0, el valor de x que satisface la ecuación es:")
x_zero = -3
y_zero = x_zero**2 + 6*x_zero + 9
print(f"x = {x_zero}, y = {y_zero}")


# Longitudes y comparación falsa
print("\n")
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))  # Falsy si son iguales

print("'on' en ambos")
print('on' in 'python' and 'on' in 'dragon')

print("Verificar si 'jargon' está en la frase")
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

print("Afirmación falsa: 'on' no está en ambos")
print('on' not in 'python' and 'on' not in 'dragon')

print("Convertir longitud a float y luego a string")
le = len("python")
print(float(le))
print(str(le))


print("\n")
print("Verificar si un número es par")
num = int(input("Ingresa un número: "))
print(num % 2 == 0)

print("División de piso")
print(7 // 3 == int(2.7))

print("Comparar tipos")
print(type('10') == type(10))

print("Comparar conversión de '9.8'")
print(int(float('9.8')) == 10)

# Calcular pago por horas
print("\n")
horas = int(input("Horas trabajadas: "))
tarifa = int(input("Tarifa por hora: "))
print("Pago total:", horas * tarifa)

#LEVEL 4 (22) =====================================
#Solicitar años vividos
print("\n")
year = int(input("Ingresa tus años vividos: "))
d = year * 365
h = d * 24
m = h * 60
s = m * 60
print("Has vivido ", s , " segundos.")

#LEVEL 5 (23) 
print("\n")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

