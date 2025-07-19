# Dia 9 Nvl 1...


#1. Verificar si es mayor de edad 

edad = int(input("ingrese su edad = "))
if edad >= 18:
    print("Tiene edad suficiente para conducir")
else:
    print("espere los años que faltan: ", 18-edad)

#2. Comparar edades
my_age = int(input("Ingresa tu edad(mia): "))
your_age = int(input("Ingresa tu edad(tuya): "))

if my_age == your_age:
    print("Tenemos la misma edad")
elif my_age > your_age:
    if my_age - your_age > 1:
        print("Soy mayor que tu por ",my_age - your_age, " años")
    else:
        print("Soy mayor que tu por 1 año")
else:
    if your_age - my_age > 1:
        print("Eres mayor que yo por ",your_age - my_age, " años")
    else:
        print("Eres mayor que  yo por 1 año")

#3. Obtener dos números del usuario mediante la solicitud de entrada.
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))
if a > b:
    print(a, "es mayor que", b)
else:
    print(a, "es menor que", b)

#EJERCICIOS NIVEL 2:
#1. Escriba un código que califique a los estudiantes según sus puntuaciones:
puntuación = float(input("Ingresa tu puntuación: "))
if puntuación >= 80:
    print("Tu calificación es 'A'" )
elif puntuación >= 70:
    print("Tu calificación es 'B'" )
elif puntuación >= 60:
    print("Tu calificación es 'c'" )
elif puntuación >= 50:
    print("Tu calificación es 'D'" )
else:
    print("Tu calificación es 'F'")

#2. Comprueba la temporada
mes = input("Ingresa en que mes estas: ").lower()

if mes in ["septiembre", "octubre", "diciembre"]:
    print("La temporada es otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("La temporada es invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("La temporada es primavera")
elif mes in ["julio", "junio", "agosto"]:
    print("la temporada es verano")
else:
    print("Mes invalido")

#3. Frutas
fruits = ['platano', 'naranja', 'mango', 'limon']
nueva_fruta = input("Ingresa una fruta: ").lower()

if nueva_fruta in fruits:
    print("Esa fruta ya existe en esta lista")
else:
    fruits.append(nueva_fruta)
    print("Fruta agregada, lista actualizada: ", fruits)

#EJERCICIOS NIVEL 3:
#1. Diccionario de personas
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = person['skills']
    if len(skills) > 0:
        mitad = len(skills) // 2
        print("Habilidad intermedia: ", skills[mitad])
    
    print('python' in skills)

    if set(skills) == {'JavaScript', 'React'}:
        print('Es un desarrollador front-end')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('Es un desarrollador back-end')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('Es un desarrollador fullstack')
    else:
        print('Título desconocido')

    if person.get('is_marred') and person.get('country') == 'Finland':
        nombre_completo= person['first_name']+' '+person['last_name'] 
        print(f"{nombre_completo} esta casado(a) y vive en {person['country']}")