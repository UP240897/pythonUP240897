#Day 2: Level 2 Exercises

# 1. Verifica los tipos de variables
print(type('Pedro'))  
print(type('Guerrero Carranco'))  
print(type('Pedro Guerrero Carranco'))  
print(type('México'))  
print(type('Aguascalientes'))  
print(type(18))  
print(type(2006))  
print(type(False))  
print(type(True))
print(type(True))  
print(type(5))  
print(type(10))  
print(type(15))  

# 2. Longitud del primer nombre
first_name = 'Pedro Guerrero Carranco'
print(len(first_name))

# 3. Comparar longitud del primer nombre y apellido
last_name = 'Guerrero Carranco'
print(len(first_name) > len(last_name))

# 4-11. Operaciones aritméticas
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Diferencia:", diff)
print("Producto:", product)
print("División:", division)
print("Resto:", remainder)
print("Exponencial:", exp)
print("División entera:", floor_division)

# 12. Cálculos con círculo
pi = 3.14159
radius = 30

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# 12.3. Radio desde input
user_radius = float(input("Ingresa el radio del círculo: "))
user_area = pi * user_radius ** 2
print("Área del círculo con radio del usuario:", user_area)

# 13. Obtener datos del usuario
first_name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
country = input("Ingresa tu país: ")
age = int(input("Ingresa tu edad: "))

print("Nombre completo:", first_name + " " + last_name)
print("País:", country)
print("Edad:", age)