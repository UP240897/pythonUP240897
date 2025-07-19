#Dia 6 Nvl. 1 ...



#1.Tupla vacía

tpl = ()

#2.Tupla que contenga los nombres de tus hermanos
hermanas = ("Esme", "Fer")
hermanos = ("Alejandro", "Emiliano")

#3.Unir tuplas de hermanos y hermanas y asignarlas a hermanos
hermanos_tt = hermanas +  hermanos

#4. ¿Cuántos hermanos tienes?
print(len(hermanos_tt))

#5. Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members
#No se pueden modificar las tuplas por lo cual agregare otra variable
padres = ("Armando", "Alondra")
family_members = hermanos_tt + padres
print(len(family_members))

#EJERCICIOS NIVEL 2:
#1. Desempaquetar a hermanos y padres de los miembros de la familia
*hermanos, padre, madre = family_members

print("Hermanos:", hermanos)
print("Padre:", padre)
print("Madre:", madre)


#2. Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
frutas = ("manzana", "pera",)
verduras = ("zanahoria", "brocoli")
productos = ("Gel", "escoba")
food_staff_tp = frutas + verduras + productos

#3. Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_staff_lt = list(food_staff_tp)

#4. Extraiga el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
Lon = (len(food_staff_lt))
mitad = Lon//2
elementos_medio = food_staff_lt[mitad - 1 : mitad + 1]
print(elementos_medio)

#5. SepARAR LOS tres elementos y los últimos tres elementos de la lista food_staff_lt
tres_primeros_elemenots = food_staff_lt[:3]
tres_ultimos_elementos = food_staff_lt[-3:]
print(tres_primeros_elemenots)
print(tres_ultimos_elementos)

#6. Eliminar la tupla food_staff_tp por completo
print(food_staff_tp)
del food_staff_tp

#7. Si un elemento existe en una tupla:
#7. Si un elemento existe en la lista (ya que la tupla fue eliminada)
print("pera" in food_staff_lt)
print("chocolate" in food_staff_lt)

#8.Si 'Estonia' es un país nórdico
países_nórdicos = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')
print('Estonia' in países_nórdicos)

#9. Si 'Islandia' es un país nórdico
print('Islandia' in países_nórdicos)