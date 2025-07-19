# Dia 12 Nvl 1...


# 1. ID Ramdom


import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choices(characters, k=6))
print(random_user_id())
print()

# 2. User_id con input

def user_id_gen_by_user():
    import random
    import string

    num_chars = int(input("Número de caracteres: "))
    num_ids = int(input("Número de Ids a generar: "))
    characters = string.ascii_letters + string.digits  
    ids = [''.join(random.choices(characters, k=num_chars)) for _ in range(num_ids)]
    return '\n'.join(ids)
print(user_id_gen_by_user())
print()

# 3. Color RGB
def rgb_color_gen():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen()) 
print()

#EJERCICIOS NIVEL 2:
# 1. Colores hexadecimales
import random

def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hex_colors.append(color)
    return hex_colors
print(list_of_hexa_colors(5))
print()

# 2. Colores RGB 2
import random

def list_of_rgb_colors(n):
    return [f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})" for _ in range(n)]
print(list_of_rgb_colors(5))
print()

# 3. Cantidad de colores
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]
    elif color_type == 'rgb':
        return [f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})" for _ in range(n)]
    else:
        return ['Invalid color type. Use "hexa" or "rgb".']
print(generate_colors('hexa', 5))
print()

#EJERICICIOS NIVEL 3:
# 1. Lista aleatoria
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1, 2, 3, 4, 5]))
print()

# 2. Array aleatorio

def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())