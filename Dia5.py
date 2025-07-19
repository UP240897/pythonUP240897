#DIA 5 - Nvl. 1



# 1: Declarar una lista vacía


lista_vacia = []

# 2:Lista con más de 5 elementos
frutas = ["manzana", "naranja", "plátano", "fresa", "sandía", "kiwi"]

# 3: Encuentra la longitud de tu lista
print(len(frutas))

# 4: Obtener el primer, el del medio y el último elemento
print(frutas[0])                       
print(frutas[len(frutas) // 2])        
print(frutas[-1])                      

# 5: Declarar lista mixed_data_types con información personal
mixed_data_types = ["José", 18, 1.72, "Soltero", "Ags"]

# 6: Declarar it_companies con empresas de tecnología
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7: Imprimir la lista
print(it_companies)

# 8: Imprimir el número de empresas en la lista
print(len(it_companies))

# 9: Imprimir la primera, segunda y última empresa
print(it_companies[0])    
print(it_companies[1])    
print(it_companies[-1])   

# 10: Modificar una de las empresas (por ejemplo cambiar 'Google' por 'Alphabet')
it_companies[1] = "Alphabet"
print(it_companies)

# 11: Agregar una empresa de TI
it_companies.append("Spotify")
print(it_companies)

# 12: Insertar una empresa en el medio (por ejemplo 'Tesla')
mitad = len(it_companies) // 2
it_companies.insert(mitad, "Tesla")
print(it_companies)

# 13: Cambiar una empresa (excepto IBM) a mayúsculas (por ejemplo 'Facebook')
upper_all = list(map(str.upper, it_companies))
index_ibm = it_companies.index("IBM")
it_companies_final = upper_all[:index_ibm] + ["IBM"] + upper_all[index_ibm+1:]
print(it_companies_final)

# 14: Unir it_companies con '#; '
unir = '#; '.join(it_companies)
print(unir)

# 15: Comprobar si existe una empresa (por ejemplo 'GOOGLE')
print("GOOGLE" in it_companies)

# 16: Ordenar la lista
it_companies.sort()
print(it_companies)

# 17: Invertir la lista
it_companies.reverse()
print(it_companies)

# 18: Separar las primeras 3 empresas
tres = it_companies[:3]
print(tres)

# 19: Eliminar las últimas 3 empresas
del it_companies[-3:]
print(it_companies)

# 20: Eliminar empresas intermedias
lon = len(it_companies)
if lon % 2 == 1:
    del it_companies[lon // 2 - 1: lon // 2 + 1]
print(it_companies)

# 21: Eliminar la primera empresa
del it_companies[0]
print(it_companies)

# 22: Eliminar nuevamente empresas intermedias
longitud = len(it_companies)
if longitud % 2 == 1:
    del it_companies[longitud // 2]
else:
    del it_companies[longitud // 2 - 1: longitud // 2 + 1]
print(it_companies)

# 23: Eliminar la última empresa
it_companies.pop()
print(it_companies)

# 24: Eliminar todas las empresas
it_companies.clear()
print(it_companies)

# 25: Destruir la lista
del it_companies
# print(it_companies)  # Esto generaría un error porque ya fue destruida

# 26: Join de listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#EJERCICIOS: NIVEL 2
# 27: Lista de edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista
ages.sort()
print("Lista ordenada:", ages)

# Edad mínima y máxima
edad_minima = min(ages)
edad_maxima = max(ages)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

#Agregar nuevamente la edad mínima y máxima a la lista
ages.extend([edad_minima, edad_maxima])
print("Lista con mín y máx agregados:", ages)

# Volver a ordenar por si las nuevas edades cambian el orden
ages.sort()

#Encontrar la edad media (valor central)
n = len(ages)
if n % 2 == 0:
    edad_media = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    edad_media = ages[n // 2]
print("Edad media:", edad_media)

#Encontrar la edad promedio
promedio = sum(ages) / len(ages)
print("Edad promedio:", promedio)

#Rango de edades
rango = edad_maxima - edad_minima
print("Rango de edades:", rango)

#Comparar |mín - promedio| y |máx - promedio|
diferencia_min = abs(edad_minima - promedio)
diferencia_max = abs(edad_maxima - promedio)
print("abs(mín - promedio):", diferencia_min)
print("abs(máx - promedio):", diferencia_max)

#Encontrar país del medio
paises = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
n = len(paises)
pais_medio = paises[n // 2]  # índice 3
print("País del medio:", pais_medio)

#Dividir la lista de países en dos partes iguales
if n % 2 == 0:
    mitad1 = paises[:n // 2]
    mitad2 = paises[n // 2:]
else:
    mitad1 = paises[:n // 2 + 1]
    mitad2 = paises[n // 2 + 1:]
print("Primera mitad:", mitad1)
print("Segunda mitad:", mitad2)

#Desglosar los primeros tres países
primeros_tres = paises[:3]
escandinavos = paises[3:]
print("Primeros tres países:", primeros_tres)
print("Países escandinavos:", escandinavos)