from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def Cambiar_color(imagen, color, umbral, titulo, color_original):
    nuevo_color = np.array(color)
    umbral = umbral

    ImgCambioColor = imagen.copy()
    np_img = np.array(ImgCambioColor)

    diferencia_color = np.abs(np_img - color_original)
    pixels_a_cambiar = np.all(diferencia_color < umbral, axis=-1)

    for i in range(3):
        np_img[pixels_a_cambiar, i] = nuevo_color[i] * (np_img[pixels_a_cambiar, i]/255)

    ImgCambioColor = Image.fromarray(np_img)
    titulo = titulo + ".jpg"
    ImgCambioColor.save(titulo)

    return ImgCambioColor


import random
import matplotlib.pyplot as plt

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
    plt.subplots()

print("PROGRAMA PARA GENERAR PALETAS DE COLORES")
print("¿Que regla desea para generar paletas?")
print("0. Aleatorio")
print("1. Monocromatico")
print("2. Analogico")
print("3. Complementario")

tipo = input("Ingrese la opcion que desea observar:")
n = 5
tipo = int(tipo)
n = int(n)
if tipo == 0:
    paletaRGB = generar_paleta_aleatoria(n)
elif tipo == 1:
    paletaRGB = generar_paleta_Monocromaticas(n)
elif tipo == 2:
    paletaRGB = generar_paleta_Analogos(n)
elif tipo == 3:
    paletaRGB = generar_paleta_Complementario(n)
paleta = [(componente[0] * (1/255), componente[1] * (1/255), componente[2] * (1/255)) for componente in paletaRGB]
mostrar_paleta(paleta)


ruta = r"D:\Documentos\Escuela\tareas\ESCOM\5to semestre\Lenguaje Natura\Protipos\OutfitInspo\Screenshot_20231102_123414_H&M.jpg"
imagen = Image.open(ruta)

ColorChamarra = [92, 86, 62]
Humbral1 = 51.12201963534362
Titulo = "chamarra"
F1 = Cambiar_color(imagen, paletaRGB[0], Humbral1, Titulo, ColorChamarra)

ruta = r"D:\Documentos\Escuela\tareas\ESCOM\5to semestre\Lenguaje Natura\Protipos\OutfitInspo\Screenshot_20231214_120038_H&M.jpg"
imagen = Image.open(ruta)

ColorPantalon = [48, 42, 42]
Humbral2 = 39.130434782608695
Titulo2 = "Pantalon"
F4 = Cambiar_color(imagen, paletaRGB[3], Humbral2, Titulo2, ColorPantalon)

ruta = r"D:\Documentos\Escuela\tareas\ESCOM\5to semestre\Lenguaje Natura\Protipos\OutfitInspo\Screenshot_20231128_123009_H&M.jpg"
imagen = Image.open(ruta)

ColorSudadera = [157, 180, 136]
Humbral3 = 90
Titulo3 = "Sudadera"
F2 = Cambiar_color(imagen, paletaRGB[1], Humbral3, Titulo3, ColorSudadera)

ruta = r"D:\Documentos\Escuela\tareas\ESCOM\5to semestre\Lenguaje Natura\Protipos\OutfitInspo\Screenshot_20231102_122728_H&M.jpg"
imagen = Image.open(ruta)

ColorPlayera = [71, 44, 125]
Humbral4 = 83.2047685834502
Titulo4 = "Playera"
F3 = Cambiar_color(imagen, paletaRGB[2], Humbral4, Titulo4, ColorPlayera)

ruta = r"D:\Documentos\Escuela\tareas\ESCOM\5to semestre\Lenguaje Natura\Protipos\OutfitInspo\Screenshot_20231102_123558_H&M.jpg"
imagen = Image.open(ruta)

ColorTenis = [205, 188, 204]
Humbral5 = 33.97615708274895
Titulo5 = "tenis"
F5 = Cambiar_color(imagen, paletaRGB[4], Humbral5, Titulo5, ColorTenis)

fig, axs = plt.subplots(1, 5, figsize=(15, 5))

axs[0].imshow(np.array(F1))
axs[0].set_title('F1')

axs[1].imshow(np.array(F2))
axs[1].set_title('F2')

axs[2].imshow(np.array(F3))
axs[2].set_title('F3')

axs[3].imshow(np.array(F4))
axs[3].set_title('F4')

axs[4].imshow(np.array(F5))
axs[4].set_title('F5')

plt.tight_layout()
plt.show()
F1.close()
F2.close()
F3.close()
F4.close()
F5.close()
