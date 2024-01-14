import random
import matplotlib.pyplot as plt
semilla = random.randint(1,1000)
random.seed(semilla) 
print(semilla)
""""
def generar_paleta_de_colores(n):
    paleta = []
    for _ in range(n):
        r = random.uniform(0.4, 0.8)
        g = random.uniform(0.4, 0.8)
        b = random.uniform(0.4, 0.8)
        color = (r, g, b)
        paleta.append(color)
    return paleta
"""
def imshow(image_path, ventana_nombre="Imagen"):
    import cv2
    imagen = cv2.imread(image_path)
    cv2.imshow(ventana_nombre, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Ruido Blanco
def generar_paleta_aleatoria(n):
    paleta = []
    for _ in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = (r, g, b)
        paleta.append(color)
    return paleta

#Paletas monocormaticas
def generar_paleta_Monocromaticas(n):
    variacion = .4
    paleta = []
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    paleta.append(color)
    for _ in range(n - 1):
        var = random.uniform(1-variacion, 1+variacion)
        r = r * var
        r = max(0, min(r, 255))
        g = g * var
        g = max(0, min(g, 255))
        b = b * var
        b = max(0, min(b, 255))

        color = (r, g, b)
        paleta.append(color)
    return paleta

#Ruido Browniano
def generar_paleta_Analogos(n):
    variacion = 130
    paleta = []
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    paleta.append(color)

    for _ in range(n - 1):
        var_r = random.randint(0, variacion)
        r = random.randint(r - var_r, r + var_r)
        r = max(0, min(r, 255))
        var_g = random.randint(0, variacion)
        g = random.randint(g - var_g, g + var_g)
        g = max(0, min(g, 255))
        var_b = random.randint(0, variacion)
        b = random.randint(b - var_b, b + var_b)
        b = max(0, min(b, 255))
        color = (r, g, b)
        paleta.append(color)
    return paleta

#Ruido 
def generar_paleta_Complementario(n):
    variacion = 130
    paleta = []
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    regla = [1,2]
    paleta.append(color)

    for _ in range(n-1):
        sel = random.choice(regla)
        if sel == 1:    
            comp = [r, g, b]
            r = random.choice(comp)
            comp.remove(r)
            g = random.choice(comp)
            comp.remove(g)
            b = random.choice(comp)
            color = (r, g, b)
            paleta.append(color)
        elif sel == 2:
            r = 255 - r
            g = 255 - g
            b = 255 - b
            color = (r, g, b)
            paleta.append(color)
        var_r = random.randint(0, variacion)
        r = random.randint(r - var_r, r + var_r)
        r = max(0, min(r, 255))
        var_g = random.randint(0, variacion)
        g = random.randint(g - var_g, g + var_g)
        g = max(0, min(g, 255))
        var_b = random.randint(0, variacion)
        b = random.randint(b - var_b, b + var_b)
        b = max(0, min(b, 255))
    return paleta


def mostrar_paleta(paleta):
    fig, ax = plt.subplots(1, 1, figsize=(8, 1))
    for i, color in enumerate(paleta):
        ax.bar(i, 1, color=color)
    ax.set_xticks([]) 
    ax.set_yticks([])  
    plt.show()

print("PROGRAMA PARA GENERAR PALETAS DE COLORES")
print("¿Que regla desea para generar paletas?")
print("0. Aleatorio")
print("1. Monocromatico")
print("2. Analogico")
print("3. Complementario")

tipo = input("Ingrese la opcion que desea observar:")
n = input("Ingrese el numero de colores [1-9]:")
tipo = int(tipo)
n = int(n)
if tipo == 0:
    paleta = generar_paleta_aleatoria(n)
elif tipo == 1:
    paleta = generar_paleta_Monocromaticas(n)
elif tipo == 2:
    paleta = generar_paleta_Analogos(n)
elif tipo == 3:
    paleta = generar_paleta_Complementario(n)
paleta = [(componente[0] * (1/255), componente[1] * (1/255), componente[2] * (1/255)) for componente in paleta]
mostrar_paleta(paleta)

