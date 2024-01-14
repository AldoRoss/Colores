import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image
from matplotlib.widgets import Button
from matplotlib import gridspec

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleccione un umbral")

        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.fig.suptitle('Humbral', fontsize=22, color='navy')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.umbral_var = tk.DoubleVar()
        self.umbral_slider = ttk.Scale(self.root, from_=0, to=150, orient="horizontal", variable=self.umbral_var)
        self.umbral_slider.pack(side=tk.TOP, fill=tk.X)

        self.refresh_button = tk.Button(self.root, text="Refrescar", command=self.refresh_image, font=('Arial', 14))
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.send_button = tk.Button(self.root, text="Enviar", command=self.send_data, font=('Arial', 14))
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.image_path = None
        self.color_original = None
        self.load_image()

    def load_image(self):
        self.image_path = filedialog.askopenfilename(title="Seleccione una imagen", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.save("Muestra.jpg")
            img = Image.open("Muestra.jpg")
            img.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(img)
            self.ax.imshow(img)
            self.ax.axis('off')
            self.canvas.draw()

            # Obtiene el color original al cargar la imagen
            self.color_original = np.array(self.impixel(img)[0])

    def impixel(self, imagen):
        rgb = []
        plt.imshow(imagen)
        plt.axis('on') 
        def onclick(event):
            if event.xdata is not None and event.ydata is not None:
                x = int(event.xdata)
                y = int(event.ydata)
                valor_pixel = imagen.getpixel((x, y))
                rgb.append(valor_pixel)

        cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)
        plt.show()
        plt.gcf().canvas.mpl_disconnect(cid)
        matriz_rgb = np.array(rgb)
        return matriz_rgb

    def refresh_image(self):
        if self.image_path and self.color_original is not None:
            umbral_value = self.umbral_var.get()
            img_original = Image.open(self.image_path)
            img_original.thumbnail((400, 400))
            self.photo_original = ImageTk.PhotoImage(img_original)

            # Obtiene las dimensiones originales y posición
            original_width, original_height = img_original.size
            original_position = self.ax.get_position()

            self.ax.clear()
            self.ax.imshow(img_original)
            self.ax.axis('off')

            # Restaura la posición y límites originales
            self.ax.set_position(original_position)
            self.ax.set_xlim([0, original_width])
            self.ax.set_ylim([original_height, 0])

            self.canvas.draw()

            # Aplica los cambios solo en la imagen copiada
            img_copia = Image.open(self.image_path)
            humbral = umbral_value
            Color = [253, 226, 0]
            titulo = "Muestra"
            print(self.Cambiar_color(img_copia, Color, humbral, titulo))
            img_copia.close()

    def Cambiar_color(self, imagen, color, umbral, titulo):
        nuevo_color = np.array(color)
        umbral = umbral

        ImgCambioColor = imagen.copy()
        np_img = np.array(ImgCambioColor)

        # Calcular la diferencia de color para todos los píxeles de una vez
        diferencia_color = np.abs(np_img - self.color_original)

        # Encontrar los píxeles que cumplen con el umbral
        pixels_a_cambiar = np.all(diferencia_color < umbral, axis=-1)

        for i in range(3):
            # Aplicar la transformación por componente solo a los píxeles seleccionados
            np_img[pixels_a_cambiar, i] = nuevo_color[i] - (10 * (nuevo_color[i]) / (np_img[pixels_a_cambiar, i] + 1))

        ImgCambioColor = Image.fromarray(np_img)
        titulo = titulo + ".jpg"
        ImgCambioColor.save(titulo)

        # Muestra la imagen modificada
        img = ImgCambioColor.copy()
        img.thumbnail((400, 400))
        self.photo_modified = ImageTk.PhotoImage(img)
        self.ax.clear()
        self.ax.imshow(img)
        self.ax.axis('off')
        self.canvas.draw()

        ImgCambioColor.close()
        return "Terminé"

    def send_data(self):
        if self.image_path:
            print(f"Umbral seleccionado: {self.umbral_var.get()}")
            print(f"Color original: {self.color_original}")
            print("Datos enviados")
            self.AplicarColores()

    def AplicarColores(self):
        def Cambiar_color(imagen, color, umbral, titulo,color_original):
            nuevo_color = np.array(color)
            umbral = umbral

            ImgCambioColor = imagen.copy()
            np_img = np.array(ImgCambioColor)

            # Calcular la diferencia de color para todos los píxeles de una vez
            diferencia_color = np.abs(np_img - color_original)

            # Encontrar los píxeles que cumplen con el umbral
            pixels_a_cambiar = np.all(diferencia_color < umbral, axis=-1)

            for i in range(3):
                # Aplicar la transformación por componente solo a los píxeles seleccionados
                np_img[pixels_a_cambiar, i] = nuevo_color[i] - (10 * (nuevo_color[i]) / (np_img[pixels_a_cambiar, i] + 1))

            ImgCambioColor = Image.fromarray(np_img)
            titulo = titulo + ".jpg"
            ImgCambioColor.save(titulo)

            ImgCambioColor.close()
            return "Terminé"
        Colores2 = [[251, 253, 253, 255],
                    [4, 4, 4, 255],
                    [251, 2, 140, 255],
                    [221, 200, 179, 255],
                    [103, 61, 41, 255],
                    [255, 116, 2, 255]] 

        Num = len(Colores2)
        Foto = Image.open(self.image_path)
        color_original = self.color_original
        humbral = self.umbral_var.get()
        for i in range(Num):
            Color = Colores2[i]
            titulo = str(i)
            print(Cambiar_color(Foto, Color, humbral, titulo, color_original))
        Foto.close()
        self.mostrar_imagenes_2()

    def mostrar_imagenes_2(self):
        # Obtén la ruta del directorio actual
        directorio_actual = os.getcwd()

        # Lista todos los archivos en el directorio actual
        archivos = os.listdir(directorio_actual)

        # Filtra solo los archivos con extensiones de imagen (puedes añadir más extensiones si es necesario)
        imagenes = [archivo for archivo in archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        # Limita la lista a las primeras 6 imágenes
        imagenes = imagenes[:6]

        # Configura la cuadrícula de subgráficos
        filas = 2
        columnas = 3
        gs = gridspec.GridSpec(filas, columnas, width_ratios=[1]*columnas)

        # Crea la figura y los subgráficos
        fig = plt.figure(figsize=(10, 7))
        fig.suptitle('Colorimetría', fontsize=22, color='navy')  # Título de la figura
        subplots = [plt.subplot(gs[i]) for i in range(filas * columnas)]

        # Muestra las imágenes en los subgráficos
        for i, imagen in enumerate(imagenes):
            ruta_imagen = os.path.join(directorio_actual, imagen)
            img = Image.open(ruta_imagen)
            
            # Agrega un marco azul marino a la imagen
            img_marco = self.agregar_marco_azul(img)
            
            subplots[i].imshow(img_marco)
            subplots[i].axis('off')  # Desactiva los ejes

        # Añade la capacidad de seleccionar/deseleccionar imágenes mediante clics
        def onclick(event):
            indice_imagen = subplots.index(event.inaxes)
            imagen_seleccionada = imagenes[indice_imagen]

            if imagen_seleccionada in self.imagenes_seleccionadas:
                # Si la imagen ya está seleccionada, se deselecciona
                self.imagenes_seleccionadas.remove(imagen_seleccionada)
                print(f'Se deseleccionó: {imagen_seleccionada}')
            else:
                # Si la imagen no está seleccionada, se selecciona
                self.imagenes_seleccionadas.append(imagen_seleccionada)
                print(f'Se seleccionó: {imagen_seleccionada}')
                
            # Actualiza el estilo de la imagen seleccionada/deseleccionada
            self.actualizar_estilo_imagenes()

        def actualizar_estilo_imagenes():
            for i, imagen in enumerate(imagenes):
                ruta_imagen = os.path.join(directorio_actual, imagen)
                img = Image.open(ruta_imagen)

                if imagen in self.imagenes_seleccionadas:
                    # Agrega un marco azul marino a la imagen seleccionada
                    img_marco = self.agregar_marco_azul(img)
                    subplots[i].imshow(img_marco)
                else:
                    subplots[i].imshow(img)

                subplots[i].axis('off')  # Desactiva los ejes

        self.imagenes_seleccionadas = []
        fig.canvas.mpl_connect('button_press_event', onclick)

        # Añade un botón para enviar a otra ventana
        def on_button_click(event):
            plt.close(fig)
            # Aquí puedes agregar el código para abrir otra ventana o realizar la acción que desees
            print('Imágenes seleccionadas:', self.imagenes_seleccionadas)

        button_ax = fig.add_axes([0.5, 0.01, 0.1, 0.05])  # Ajusta las coordenadas y el tamaño del botón
        button = Button(button_ax, 'Enviar')
        button.on_clicked(on_button_click)

        plt.tight_layout(rect=[0, 0, 1, 0.96])  
        plt.show()

    def agregar_marco_azul(self, imagen):
        img_array = np.array(imagen)
        alto, ancho, _ = img_array.shape

        # Tamaño del marco
        grosor_marco = 10

        # Crea una nueva imagen con el marco azul marino
        img_marco = Image.new('RGB', (ancho + 2 * grosor_marco, alto + 2 * grosor_marco), color='navy')
        img_marco.paste(imagen, (grosor_marco, grosor_marco))

        return img_marco


if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazGrafica(root)

    # Configura el tamaño de la ventana para que ocupe toda la pantalla
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    root.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

    # Llama al método mainloop para mostrar la interfaz
    root.mainloop()
