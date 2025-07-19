# Dia 11 Nvl 1...


#1. Declare la función add_two_numbers .
def add_two_numbers(n1, n2):
    suma = n1 + n2
    return(suma)
print(add_two_numbers(2,4))

#2.Función que calcule área_del_círculo.
def área_del_circulo(r):
    return 3.14*r*r
print(área_del_circulo(2))

#3. Numero arbitrario
def add_all_numbers(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Error: Todos los elementos deben ser numericos"
    return sum(args)
print(add_all_numbers(1,'a',2))

#4. Temperatura
def convert_celsius_to_fahrenheit(C):
    return (C*(9/5)) + 32
print(convert_celsius_to_fahrenheit(90))
    
#5. Temporada
def check_season(mes):
    mes = mes.lower()
    if mes in ['marzo', 'abril', 'mayo']:
        return "Primavera"
    elif mes in ['junio', 'julio', 'agosto']:
        return "Verano"
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return "Otoño"
    elif mes in ['diciembre', 'enero', 'febrero']:
        return "Invierno"
    else:
        return "Este mes no existe"
print(check_season('junio'))

#6. pendiente
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Pendiente indefinida"
    else:
        return (y2-y1)/(x2-x1)
print(calculate_slope(1,2,3,6))

#7. Cuadratica
import math

def solve_quadratic_eqn(a,b,c):
    dis = b**2 - 4*a*c
    if dis < 0:
        return "No hay soluciones reales"
    elif dis == 0:
        x= -b / (2*a)
        return f"Una solución real: {x}"
    elif dis > 0:
        j = (-b + math.sqrt(dis))/(2*a)
        j1 = (-b - math.sqrt(dis))/(2*a)
        return f"Dos soluciones reales: {j} y {j1}"
print(solve_quadratic_eqn(1,2,3))

#8.  lista 
def print_list(lista):
    for elemento in lista:
        print(elemento)

frutas = ['manzana', 'banana', 'pera']
print_list(frutas)

#9. array
def reverse_list(list):
    inver_list = []
    for i in range(len(list) -1, -1, -1):
        inver_list.append(list[i])
    return inver_list
numeros = [1,2,3,4,5]
res = reverse_list(numeros)
print(res)

#10. Captalize item
def capitalize_list_items(lista):
    lista_mayusculas = []
    for item in lista:
        lista_mayusculas.append(item.upper())
    return lista_mayusculas

palabras = ['manzana', 'banana', 'pera']
resultado = capitalize_list_items(palabras)
print(resultado)  


#11. add item
def add_item(Lista, ele):
    New_list = []
    for it in Lista:
        if it == ele:
            New_list.append(it)
    return New_list

fruits = ['manzana', 'banana', 'pera',]
resultado1 = add_item(fruits, 'banana')
print(resultado1)  

#12. Remover item
def remove_item(lista, elemento):
    nueva_lista = []
    eliminado = False
    for item in lista:
        if item == elemento and not eliminado:
            eliminado = True  
            continue
        nueva_lista.append(item)
    return nueva_lista

frutas = ['manzana', 'banana', 'pera', 'banana']
resultado = remove_item(frutas, 'banana')
print(resultado)  



#13. Suma de numeros
def suma_de_numeros(n1):
    suma = 0
    for i in range(1, n1 + 1):
        suma += i
    return suma

print(suma_de_numeros(5))    

#14. Suma de impares
def suma_de_impares(n2):
    suma = 0
    for i in range(1, n2 + 1):
        if i % 2 != 0:
            suma += i
    return suma

print(suma_de_impares(5))    
print(suma_de_impares(10))   

#15. Suma de pares
def suma_de_numeros_pares(n3):
    suma = 0
    for i in range(1, n3 + 1):
        if i % 2 == 0:
            suma += i
    return suma

print(suma_de_numeros_pares(5))    

#EJERCICIOS NIVEL 2:
#1. evens_and_odds
def evens_and_odds(n4):
    evens = 0
    odds = 0
    for i in range(1, n4 + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))

#2. Factorial 
def factorial(n5):
    if n5 < 0:
        return "El factorial no está definido para números negativos."
    result = 1
    for i in range(1, n5 + 1):
        result *= i
    return result
print(factorial(5))  

#3. def is_empty(param):
def is_empty(param):
    if not param:
        return True
    else:
        return False
print(is_empty([]))       
print(is_empty([1, 2]))  
print(is_empty(""))       
print(is_empty("Hola"))  

#4. Estadistica
import statistics
def calcular_media(lista):
    return statistics.mean(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_moda(lista):
    try:
        return statistics.mode(lista)
    except statistics.StatisticsError:
        return "No hay moda única"

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    return statistics.variance(lista)

def calcular_desviacion_estandar(lista):
    return statistics.stdev(lista)

numeros = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print("Media:", calcular_media(numeros))
print("Mediana:", calcular_mediana(numeros))
print("Moda:", calcular_moda(numeros))
print("Rango:", calcular_rango(numeros))
print("Varianza:", calcular_varianza(numeros))
print("Desviación estándar:", calcular_desviacion_estandar(numeros))

#EJERCICIOS NIVEL 3:
#1: Verificar numero primo
def is_prime(n7):
    if n7 <= 1:
        return False
    for i in range(2, int(n7**0.5) + 1):
        if n7 % i == 0:
            return False
    return True

print(is_prime(7))  
print(is_prime(10)) 

#2. Unicos en la lista
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3]))  
print(all_unique([1,2,2]))  

#3. Tipos de datos
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(x) == first_type for x in lst)

print(all_same_type([1,2,3]))        
print(all_same_type([1, 'dos', 3]))  

#4. Variable python
def is_valid_variable(name):
    import keyword
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    return True

print(is_valid_variable('variable1'))  
print(is_valid_variable('1variable'))  
print(is_valid_variable('for'))        