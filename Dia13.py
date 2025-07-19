# Dia 13 Nvl 1 ...


# 1. Negativos

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if n <= 0]
print(filtered)
print()

# 2. Aplanar lista

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(flattened)
print()

# 3. Tuplas con compresión

tuples = [(x, 1, x**1, x**2, x**3, x**4, x**5) for x in range(11)]
print(tuples)
print()

# 4. Aplanar lostas de paises

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.upper()] for item in countries for (country, city) in item]
print(output)
print()

# 5. Lista a dicionario

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_output = [{'country': country.upper(), 'city': city.upper()} for item in countries for (country, city) in item]
print(dict_output)
print()

#6. Lista a Lista de cadenas

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for item in names for (first, last) in item]
print(full_names)
print()

# 7.Función lambda

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1 if x2 != x1 else None
print(slope(1, 2, 3, 4))      
print(intercept(1, 2, 3, 4))  