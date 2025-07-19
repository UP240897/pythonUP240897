#DIA 8 NVL 1 ...

#Diccionario vacío []
perro = {}

# Añadir elementos al diccionario
perro['nombre'] = 'Fido'
perro['color'] = 'marrón'
perro['raza'] = 'labrador'
perro['patas'] = 4
perro['edad'] = 5
print(perro)

#3. Cree un diccionario de estudiantes y agregue nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario.
estudiantes = {
    'Nombre': 'Ana',
    'Apellido': 'Garcia',
    'Genero': 'Femenino',
    'Edad': '13',
    'Estado civil': 'Soltera',
    'Habilidades': ['Trabajo en equipo', 'Excel'],
    'Pais': 'México',
    'Ciudad': 'Guadalajara',
    'Dirección': 'Av. Revolución 123, Col. Centro'
}
print(estudiantes)

#4. Obtenga la longitud del diccionario del estudiante
print(len(estudiantes))

#5. Obtenga el valor de las habilidades y verifique el tipo de dato, debe ser una lista
habilidades = estudiantes['Habilidades']
print('Habilidades: ', habilidades)
print(type(habilidades))

#6. Modifique los valores de las habilidades agregando una o dos habilidades
estudiantes['Habilidades'] = 'Trabajo en equipo','Excel','Patinar'
print(estudiantes)

#7. Obtenga las claves del diccionario como una lista
claves = estudiantes.keys()
print(claves)

#8 .Obtener los valores del diccionario como una lista
valores = estudiantes.values()
print(valores)

#9. Cambie el diccionario a una lista de tuplas usando el método items()
print(estudiantes.items())

#10. Eliminar uno de los elementos del diccionario
estudiantes.pop('Dirección')
print(estudiantes)

#11. Eliminar uno de los diccionarios
print(perro)
del perro