from PIL import Image, ImageTk
import tkinter as tk
import pygame

# Variables globales para almacenar la configuración
nombre_jugador = ""
jugador_inicial = None
modo_juego = "manual"  # Por defecto a modo manual

# Datos de los jugadores
jugadores = [
    {"nombre": "Jugador: Dilan", "foto": "brownie.jpg"},
    {"nombre": "Jugador: Job", "foto": "job.jpg"}
]

# Clase de la ventana de configuración inicial
class ConfiguracionInicial(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Configuración Inicial")
        self.geometry("400x400")

        # Ocultar la ventana principal
        master.withdraw()

        # Opciones de modo de juego
        self.modo_label = tk.Label(self, text="Selecciona el modo de juego")
        self.modo_label.pack(pady=10)

        self.modo_var = tk.StringVar(value="manual")
        self.radio_manual = tk.Radiobutton(self, text="Manual", variable=self.modo_var, value="manual")
        self.radio_manual.pack()
        self.radio_automatico = tk.Radiobutton(self, text="Automático", variable=self.modo_var, value="automatico")
        self.radio_automatico.pack()

        # Selección del jugador inicial (solo relevante en modo Manual)
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
        global nombre_jugador, modo_juego, jugador_inicial
        modo_juego = self.modo_var.get()

        # Asignar jugador inicial en función del modo de juego
        if modo_juego == "automatico":
            jugador_inicial = jugadores[0]["nombre"]  # Jugador 1 se selecciona automáticamente
        else:
            jugador_inicial = jugadores[self.jugador_var.get()]["nombre"]  # El jugador elegido por el usuario

        # Guardar el nombre del jugador inicial
        nombre_jugador = jugador_inicial
        self.destroy()  # Cierra la ventana de configuración
        self.master.deiconify()  # Mostrar de nuevo la ventana principal
        ventana_principal()  # Abre la ventana principal

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
    
    boton_puntajes = tk.Button(window, text="Estadísticas", bg="light blue", border=8, font=("Helvetica", 12), command=ver_puntajes)
    canvas.create_window(400, 520, window=boton_puntajes) 


# Función para abrir la ventana de configuración inicial
def abrir_configuracion_inicial():
    ConfiguracionInicial(window)

# Función para mostrar "About Us"
def about():
    about_window = tk.Toplevel(window)
    about_window.title("Acerca de Nosotros")
    about_window.geometry("500x600")  # Ampliar tamaño para acomodar información

    # Información institucional
    info_label = tk.Label(about_window, text="Tecnológico de Costa Rica\nGrupo 1\nCarrera: Ingeniería en Computadores\nCurso: Fundamentos Computacionales\nLugar: Cartago, Costa Rica\nversión 1.0\n", 
                          font=("Helvetica", 10), justify="center")
    info_label.pack(pady=10)

    # Información del jugador Dilan
    nombre_dilan = tk.Label(about_window, text="Dilan Cordero Anderson", font=("Helvetica", 12, "bold"))
    nombre_dilan.pack(pady=5)
    
    cedula_dilan = tk.Label(about_window, text="Cédula:119660110 ", font=("Helvetica", 10))
    cedula_dilan.pack()

    foto_dilan = Image.open("brownie.jpg")
    foto_dilan = foto_dilan.resize((100, 100))
    foto_dilan_tk = ImageTk.PhotoImage(foto_dilan)
    foto_dilan_label = tk.Label(about_window, image=foto_dilan_tk)
    foto_dilan_label.image = foto_dilan_tk
    foto_dilan_label.pack()

    # Espacio entre los jugadores
    spacer = tk.Label(about_window, text="")
    spacer.pack(pady=5)

    # Información del jugador Job
    nombre_job = tk.Label(about_window, text="Job Esteban Jiménez Sandí", font=("Helvetica", 12, "bold"))
    nombre_job.pack(pady=5)
    
    cedula_job = tk.Label(about_window, text="Cédula: 1-18680252 ", font=("Helvetica", 10))
    cedula_job.pack()

    foto_job = Image.open("job.jpg")
    foto_job = foto_job.resize((100, 100))
    foto_job_tk = ImageTk.PhotoImage(foto_job)
    foto_job_label = tk.Label(about_window, image=foto_job_tk)
    foto_job_label.image = foto_job_tk
    foto_job_label.pack()

    # Espacio para futuras indicaciones
    instrucciones_label = tk.Label(about_window, text="\n\n\n", font=("Helvetica", 10), fg="grey")
    instrucciones_label.pack(fill="x", pady=10)

    # Botón para regresar al menú principal
    boton_regresar = tk.Button(about_window, text="Regresar al Menú Principal", command=about_window.destroy)
    boton_regresar.pack(pady=20)

# Función para salir del juego
def salir_juego():
    window.quit()
    
def ver_puntajes():
    """
    Muestra las estadísticas en una nueva ventana sin cerrar la ventana principal
    """
    # Crear una nueva ventana para mostrar los puntajes
    puntajes_window = tk.Toplevel(window)
    puntajes_window.title("Top Jugadores")
    puntajes_window.geometry("800x600")

    # Crear un canvas para la nueva ventana de puntajes
    canvas = tk.Canvas(puntajes_window, width=800, height=600)
    canvas.pack()

    # Cargar una imagen de fondo para la pantalla de puntajes y asegurar que se mantenga en memoria
    fondo_img = Image.open("top_jugadores.png").resize((800, 600))
    fondo_img_tk = ImageTk.PhotoImage(fondo_img)
    canvas.create_image(0, 0, image=fondo_img_tk, anchor="nw")
    canvas.image = fondo_img_tk  # Guardar referencia para evitar que se borre de la memoria

    # Texto de puntajes de ejemplo
    texto_puntajes = "Estadísticas:\nJugador1: ________ pts\nJugador2: ________ pts"
    
    # Mostrar el texto en el canvas
    canvas.create_text(400, 200, text=texto_puntajes, font=("Helvetica", 20), fill="white")

    # Botón para cerrar la ventana de puntajes
    boton_regresar = tk.Button(puntajes_window, text="Cerrar", command=puntajes_window.destroy)
    canvas.create_window(400, 500, window=boton_regresar)


def regresar():
    global window
    window.destroy()
    ventana_principal()
    
# Configuración inicial antes de la ventana principal
window = tk.Tk()
abrir_configuracion_inicial()  # Llamar a la ventana de configuración inicial una sola vez
window.mainloop()
