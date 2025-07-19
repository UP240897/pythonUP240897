#DiA 7 Nvl 1...


# Conjuntos

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Encuentra la longitud del conjunto it_companies
print(len(it_companies))

#2. Añade 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insertar varias empresas de TI a la vez en el conjunto it_companies
Empresas = {'IBM','Softtek','Accenture'}
it_companies.update(Empresas)
print(it_companies)

#4. Eliminar una de las empresas del conjunto it_companies
it_companies.remove('Accenture')
print(it_companies)

#5. ¿Cuál es la diferencia entre eliminar y descartar?
#REMOVE: Elimina un elemento del conjunto. Si el elemento no está, lanza un error KeyError.
#DISCARD: Elimina un elemento del conjunto. Si el elemento no está, no lanza error, simplemente no hace nada.

#EJERCICIOS NIVEL 2:
#1. Unir A y B
print(A.union(B))

#2. Encuentra la intersección de A y B
print(A.intersection(B))

#3. Es un subconjunto de B
print(A.issubset(B))  

#4. ¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))

#5. Unir A con B y B con A
print(A.union(B))
print(B.union(A))

#6. ¿Cuál es la diferencia simétrica entre A y B?
print(A.symmetric_difference(B))

#7. Eliminar los conjuntos por completo
print(A)
print(B)
del A
del B

#EJERCICIOS NIVEL 3:
#1. Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
edad = set(age)
print(len(edad))
print(len(age))

#2. Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.
#cadena: str= Secuencia de caracteres (texto) no mutable
#lista: list= Colección de elementos (números, texto, etc.)
#tupla: tuple= Como una lista, pero inmutable (no se puede modificar)
#conjunto: set= Colección desordenada de elementos únicos

#3. Soy profesor y me encanta inspirar y enseñar. ¿Cuántas palabras únicas se han usado en la oración? Usa los métodos de división y configuración para obtener las palabras únicas.
oracion = "Soy profesor y me encanta inspirar y enseñar"
palabras = oracion.split()
palabras_unicas = set(palabras)
print(len(palabras_unicas))