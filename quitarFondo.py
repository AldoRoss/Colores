import cv2
import numpy as np

def obtenerRuta():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()

    ruta = filedialog.askopenfilename()
    if ruta:
        return ruta
    else:
        print("No has seleccionado ningún archivo")

def imshow(image_path, ventana_nombre="Imagen"):
    imagen = cv2.imread(image_path)
    cv2.imshow(ventana_nombre, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def quitarFondo(rutaOrigen, output_path, umbral_binario=128):
    Img = cv2.imread(rutaOrigen, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    _, binario = cv2.threshold(gray, umbral_binario, 255, cv2.THRESH_BINARY)
    binario_invertido = cv2.bitwise_not(binario)
    resultado = cv2.bitwise_and(Img, Img, mask=binario_invertido)
    cv2.imwrite(output_path, resultado)
    print("Termine")

def imbinarize(image_path, umbral=128):
    import cv2
    imagen = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, imagen_binaria = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)

    return imagen_binaria

def color_mas_repetido(image_path):
    import cv2
    import numpy as np
    image = cv2.imread(image_path)
    pixels = image.reshape((-1, 3))
    pixels = pixels.tolist()
    frecuencia_colores = {}
    for pixel in pixels:
        color = tuple(pixel)
        if color != (0, 0, 0):
            frecuencia_colores[color] = frecuencia_colores.get(color, 0) + 1
            
    if frecuencia_colores:
        color_mas_repetido = max(frecuencia_colores, key=frecuencia_colores.get)
        return color_mas_repetido
    else:
        return None

def mostrar_color(color, ventana_nombre="Color"):
    imagen_color = np.zeros((100, 100, 3), dtype=np.uint8)
    imagen_color[:, :] = color
    cv2.imshow(ventana_nombre, imagen_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    ruta = obtenerRuta()

    if ruta:
        nombre_archivo = ruta.split("/")[-1]
        output_rutaOrigen = ruta.replace(nombre_archivo, "Imgn_sin_fondo.jpg")
        quitarFondo(ruta, output_rutaOrigen)
        imshow(output_rutaOrigen)
        color = color_mas_repetido(output_rutaOrigen)
        mostrar_color(color, "a")
        print(f"El color más repetido en la imagen es: {color}")
    else:
        print("No has seleccionado ningún archivo")
