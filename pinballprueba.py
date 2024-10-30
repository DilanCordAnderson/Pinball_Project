import tkinter as tk
from PIL import Image, ImageTk
import pygame

# Variables globales para almacenar la configuración
nombre_jugador = ""
jugadores = [
    {"nombre": "Jugador: Dilan", "foto": "brownie.jpg"},
    {"nombre": "Jugador: Job", "foto": "job.jpg"}
]
modo_juego = "un_jugador"  # Por defecto a un jugador

# Clase de la ventana de configuración inicial
class ConfiguracionInicial(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Configuración Inicial")
        self.geometry("400x400")

        # Opciones de modo de juego
        self.modo_label = tk.Label(self, text="Selecciona el modo de juego")
        self.modo_label.pack(pady=10)

        self.modo_var = tk.StringVar(value="un_jugador")
        self.radio_un_jugador = tk.Radiobutton(self, text="Un Jugador", variable=self.modo_var, value="un_jugador")
        self.radio_un_jugador.pack()
        self.radio_dos_jugadores = tk.Radiobutton(self, text="Dos Jugadores", variable=self.modo_var, value="dos_jugadores")
        self.radio_dos_jugadores.pack()

        # Selección del jugador inicial
        self.jugador_label = tk.Label(self, text="Selecciona el Jugador Inicial")
        self.jugador_label.pack(pady=10)

        self.jugador_var = tk.IntVar()
        self.jugador_slider = tk.Scale(self, from_=0, to=len(jugadores) - 1, orient="horizontal", variable=self.jugador_var, command=self.actualizar_jugador)
        self.jugador_slider.pack()

        # Mostrar información del jugador seleccionado
        self.jugador_imagen = tk.Label(self)
        self.jugador_imagen.pack(pady=5)
        self.jugador_nombre = tk.Label(self, text="")
        self.jugador_nombre.pack(pady=5)

        # Actualizar visualización del jugador inicial
        self.actualizar_jugador(0)

        # Botón para confirmar y avanzar al menú principal
        self.boton_avanzar = tk.Button(self, text="Avanzar", command=self.confirmar_configuracion)
        self.boton_avanzar.pack(pady=20)

    def actualizar_jugador(self, event):
        idx = self.jugador_var.get()
        jugador = jugadores[idx]
        self.jugador_nombre.config(text=jugador["nombre"])

        imagen = Image.open(jugador["foto"])
        imagen.thumbnail((100, 100))
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.jugador_imagen.config(image=imagen_tk)
        self.jugador_imagen.image = imagen_tk

    def confirmar_configuracion(self):
        global nombre_jugador, modo_juego
        nombre_jugador = jugadores[self.jugador_var.get()]["nombre"]
        modo_juego = self.modo_var.get()
        self.destroy()  # Cierra la ventana de configuración
        ventana_principal()  # Abre la ventana principal

# Función para abrir la ventana de configuración inicial
def abrir_configuracion_inicial():
    ConfiguracionInicial(window)

# Ventana Principal
def ventana_principal():
    global window, imagen_fondo_tk

    # Inicializar pygame y cargar la música
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Elderite.mp3")  # Ruta de tu archivo MP3
    pygame.mixer.music.play(-1)  # Reproducir en bucle infinito

    # Configuración de la ventana principal
    window.geometry("800x600")
    imagen_fondo = Image.open("fondo.jpg")
    imagen_fondo = imagen_fondo.resize((800, 600))
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    # Canvas para la imagen de fondo
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=imagen_fondo_tk, anchor="nw")

    # Botones en el menú principal
    boton_configuraciones = tk.Button(window, text="Configuraciones", bg="black", fg="white", border=8, borderwidth=4, font=("Helvetica", 12), command=abrir_configuracion_inicial)
    canvas.create_window(660, 200, window=boton_configuraciones)

    boton_salir = tk.Button(window, text="Salir", font=("Helvetica", 12), bg='red', border=10, fg='white', command=salir_juego)
    canvas.create_window(110, 420, window=boton_salir)
    
    boton_puntajes = tk.Button(window, text="About Us", bg="light green", border=8, font=("Helvetica", 12), command=about)
    canvas.create_window(660, 430, window=boton_puntajes) 



def about():
    
    about_window = tk.Toplevel(window)
    about_window.title("Acerca de Nosotros")
    about_window.geometry("400x400")
    
    # Mostrar el nombre y la foto de Dilan
    nombre_dilan = tk.Label(about_window, text="Dilan Cordero Anderson", font=("Helvetica", 12))
    nombre_dilan.pack(pady=10)
    
    foto_dilan = Image.open("brownie.jpg")
    foto_dilan = foto_dilan.resize((100, 100))
    foto_dilan_tk = ImageTk.PhotoImage(foto_dilan)
    foto_dilan_label = tk.Label(about_window, image=foto_dilan_tk)
    foto_dilan_label.image = foto_dilan_tk
    foto_dilan_label.pack()

    # Mostrar el nombre y la foto del compañero
    nombre_job = tk.Label(about_window, text="Job Esteban Jiménez Sandí", font=("Helvetica", 12))
    nombre_job.pack(pady=10)
    
    foto_job = Image.open("job.jpg")
    foto_job = foto_job.resize((100, 100))
    foto_job_tk = ImageTk.PhotoImage(foto_job)
    foto_job_label = tk.Label(about_window, image=foto_job_tk)
    foto_job_label.image = foto_job_tk
    foto_job_label.pack()

    # Botón para regresar al menú principal
    boton_regresar = tk.Button(about_window, text="Regresar al Menú Principal", command=about_window.destroy)
    boton_regresar.pack(pady=20)
    
# Función para salir del juego
def salir_juego():
    window.quit()

# Configuración inicial antes de la ventana principal
window = tk.Tk()
abrir_configuracion_inicial()
window.mainloop()
