#DIA 4

# 1: Concatenar
space = " "
Tre = "Treinta"
Di = "Dias"
De = "De"      #variables
Py = "Python"
Cadena = Tre + space + Di + space + De + space + Py
print(Cadena) 

# 2: Concatenar "Codificación Para Todos"
Cod = "Codificación"
pa = "Para"     #variables
to = "Todos"
Cadena2 = Cod + space + pa + space + to
print(Cadena2)

# 3:Variable llamada empresa y asignarle un valor inicial
empresa = "Codificación para todos"

# 4: Imprimir la variable
print(empresa)

# 5: Imprimir la longitud 
print(len(empresa))

# 6: Convertir a mayúsculas
print(empresa.upper())

# 7: Convertir a minúsculas
print(empresa.lower())

# 8: Crear una nueva cadena para los siguientes métodos
cadena = "Coding For All"

# Aplicar capitalize()
print(cadena.capitalize())

# Aplicar title()
print(cadena.title())

# Aplicar swapcase()
print(cadena.swapcase())

# 9: Cortar (rebanar) la primera palabra de la cadena "Codificación para todos"
print(empresa[13:])  # Asumiendo que "Codificación" tiene 13 caracteres incluyendo el espacio

# 10: Comprobar si contiene la palabra "Codificación"
print("Codificación" in empresa)         # Usando 'in'
print(empresa.find("Codificación") != -1)  # Usando find()
print(empresa.index("Codificación") >= 0)  # Usando index()

# 11: Reemplazar "Codificación" con "Python"
empresa = "Codificación para todos"
print(empresa.replace("Codificación", "Python"))

# 12: Cambiar "Python para todos" a sí mismo usando replace
frase = "Python para todos"
print(frase.replace("Python", "Python"))

# 13: Dividir 'Coding For All' usando el espacio
cadena = "Coding For All"
print(cadena.split())

# 14: Dividir usando coma
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(", "))

# 15: Carácter en el índice 0
print(empresa[0])

# 16: Último índice de la cadena
print(len(empresa) - 1)

# 17: Carácter en el índice 10
print(empresa[10])

# 18: Acrónimo de 'Python para todos'
palabras1 = "Python para todos".split()
acronimo1 = ''.join([p[0].upper() for p in palabras1])
print(acronimo1)

# 19: Acrónimo de 'Coding For All'
palabras2 = "Coding For All".split()
acronimo2 = ''.join([p[0].upper() for p in palabras2])
print(acronimo2)

# 20: Índice de la primera aparición de 'C'
print(empresa.index("C"))

# 21: Índice de la primera aparición de 'F'
print("Codificación para todos".find("F"))  # Devuelve -1 si no se encuentra

# 22: rfind para la última aparición de 'l'
print("Coding For All People".rfind("l"))

# 23: Buscar la palabra 'because'
oracion = "No puedes terminar una oración con 'because' porque 'because' es una conjunción."
print(oracion.find("because"))

# 24: rindex de la última aparición de 'porque'
oracion2 = "No puedes terminar una oración con porque porque porque es una conjunción"
print(oracion2.rindex("porque"))

# 25: Eliminar "porque porque porque"
inicio = oracion2.find("porque porque porque")
fin = inicio + len("porque porque porque")
nueva_oracion = oracion2[:inicio].strip() + " " + oracion2[fin:].strip()
print(nueva_oracion)

# 26: Posición de la primera aparición de 'porque'
print(oracion2.find("porque"))

# 27: Otra forma de eliminar la frase repetida
print(oracion2.replace("porque porque porque", "").strip())

# 28: ¿'Coding For All' comienza con 'Coding'?
print("Coding For All".startswith("Coding"))

# 29: ¿'Coding For All' termina con 'coding'?
print("Coding For All".endswith("coding"))

# 30: Eliminar espacios a los lados
print("Codificación para todos  ".strip())

# 31: Comprobar si las cadenas son identificadores válidos
print("30 días de Python".isidentifier())       # False
print("treinta_días_de_python".isidentifier())  # True

# 32: Unir lista de bibliotecas con hash y espacio
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerias))

# 33: Separar oraciones con salto de línea
print("\nI am enjoying this challenge.\nI just wonder what is next..")

# 34: Usar secuencia de escape de tabulación para alinear columnas
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# 35: Usar formato de cadena para mostrar el área de un círculo
radio = 10
area = 3.14 * radio ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radio, area))

# 36: Operaciones usando formato de cadena
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))