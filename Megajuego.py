import tkinter as tk
from PIL import Image, ImageTk
import random

# CLASES DE PERSONAJES CON ATRIBUTOS ESPECIALES
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, suerte, descripcion):
        self.nombre = nombre
        self.vida = vida
        self.vivo = True
        self.ataque = ataque
        self.defensa = defensa
        self.suerte = suerte
        self.descripcion = descripcion

    def recibir_danio(self, danio):
        danio_real = max(0, danio - self.defensa)
        self.vida -= danio_real
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
        return danio_real

    def esta_vivo(self):
        return self.vivo


class Tanque(Personaje):
    def __init__(self):
        super().__init__(nombre="Marilu", vida=4000, suerte=int(random.randint(5,12)), ataque=60, defensa=40, descripcion="Marilu la gigante. La única guerrera en aguantar más de 2 minutos hablando con La temida Rosa")
        self.megadefensa = 20
        self.defensa += self.suerte

    def recibir_danio(self, danio):
        danio_reducido = max(0, danio - (self.defensa + self.megadefensa))
        self.vida -= danio_reducido
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
        return danio_reducido

    def ataque_1(self):
        return (50 + self.suerte) * self.ataque, "Escudo antidarius"

    def ataque_2(self):
        return (40 + self.suerte) * self.ataque, "Pisotón antidario"

    def ataque_3(self):
        return (60 + self.suerte) * self.ataque, "Quebrantadarios"


class Heroe(Personaje):
    def __init__(self):
        super().__init__(nombre="Turpin", vida=3500, suerte=random.randint(8,15), ataque=80, defensa=10, descripcion="El héroe de una historia mal contada. Siempre dispuesto a inseminarte.")
        self.defensa += self.suerte
        self.golpe_valor = 1.5

    def ataque_heroico(self):
        if self.vida < 1000:
            return (self.ataque * self.golpe_valor, "Golpe del destino")
        return self.ataque, "Ataque normal"

    def ataque_1(self):
        return (60 + self.suerte) * self.ataque, "Espada penetradora"

    def ataque_2(self):
        return (30 + self.suerte) * self.ataque, "Puño del valor"

    def ataque_3(self):
        return (10 + (2 * self.suerte)) * self.ataque, "Doble espada penetradora"


class Mago(Personaje):
    def __init__(self):
        super().__init__(nombre="J.P.", vida=3200, suerte=14, ataque=90, defensa=5, descripcion="Mago olvidadizo, su varita tiene más ideas que él.")
        self.poder_magico = 1.3
        self.defensa += self.suerte

    def ataque_magico(self):
        return self.poder_magico * self.ataque, "Varita venosa"

    def ataque_1(self):
        return (30 + self.suerte) * self.ataque, "Bola de permatrago"

    def ataque_2(self):
        return (30 + self.suerte) * self.ataque, "Rayo congelabolas"

    def ataque_3(self):
        return 150 * self.ataque, "MAEB"


class Asesino(Personaje):
    def __init__(self):
        super().__init__(nombre="Albertin", vida=3000, suerte=int(random.randint(5,25)), ataque=100, defensa=0, descripcion="Un asesino letal, ágil y pillín. Aprendió sus habilidades de su maestro el Oso Berni.")
        self.evasion = 30
        self.defensa += self.suerte

    def esquivar_ataque(self):
        from random import randint
        return randint(1, 100) <= self.evasion

    def ataque_1(self):
        return (20 + self.suerte) * self.ataque, "Ruleta de la suerte asesina"

    def ataque_2(self):
        return (10 + (2 * self.suerte)) * self.ataque, "DagametidapordetrasaDario"

    def ataque_3(self):
        return (40 + self.suerte) * self.ataque, "Lluvia de las millones de dagas"


# Función para redimensionar imágenes
def redimensionar_imagen(imagen_original, ancho, alto):
    return imagen_original.resize((ancho, alto), Image.LANCZOS)

# Función para manejar imágenes con transparencia (PNG)
def cargar_imagen_con_transparencia(ruta_imagen):
    # Abrir la imagen en modo RGBA (esto asegura que la imagen tiene canal alfa)
    imagen = Image.open(ruta_imagen).convert("RGBA")
    
    # Si la imagen tiene fondo blanco, hacerlo transparente
    datos = imagen.getdata()

    nueva_imagen = []
    for item in datos:
        # Cambiar el fondo blanco (255, 255, 255) a transparente (255, 255, 255, 0)
        if item[:3] == (255, 255, 255):
            nueva_imagen.append((255, 255, 255, 0))  # Hacer transparente
        else:
            nueva_imagen.append(item)

    # Actualizar la imagen con los datos modificados
    imagen.putdata(nueva_imagen)

    return ImageTk.PhotoImage(imagen)

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.geometry("650x400")

# Cargar imágenes
try:
    imagen_fondo_original = Image.open("fondo.png")
    imagen_titulo_original = Image.open("hola.png")
    imagen_info_original = Image.open("texto_info.png")
    imagen_boton_original = Image.open("boton.png")

    # Redimensionar imágenes
    ancho_boton = 180
    alto_boton = 90
    imagen_boton = ImageTk.PhotoImage(redimensionar_imagen(imagen_boton_original, ancho_boton, alto_boton))

    # Convertir imágenes a formato Tkinter
    imagen_titulo = ImageTk.PhotoImage(imagen_titulo_original)
    imagen_info = cargar_imagen_con_transparencia("texto_info.png")

except FileNotFoundError as e:
    print("Error: No se encontró una de las imágenes.", e)
    exit()

# Crear un label para el fondo
label_fondo = tk.Label(ventana_principal)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Función para ajustar la imagen de fondo al tamaño de la ventana
def ajustar_fondo(event=None):
    ancho = ventana_principal.winfo_width()
    alto = ventana_principal.winfo_height()
    nueva_imagen = redimensionar_imagen(imagen_fondo_original, ancho, alto)
    nueva_imagen = ImageTk.PhotoImage(nueva_imagen)

    label_fondo.config(image=nueva_imagen)
    label_fondo.image = nueva_imagen  # Mantener referencia

# Llamar a la función al iniciar para cargar el fondo
ajustar_fondo()

# Vincular la función al evento de cambio de tamaño
ventana_principal.bind("<Configure>", ajustar_fondo)

# Imagen del título
etiqueta_titulo = tk.Label(ventana_principal, image=imagen_titulo)
etiqueta_titulo.pack()

# Función para mostrar la pantalla del mago
def mostrar_mago():
    global etiqueta_mago, etiqueta_desc_mago, boton_regreso

    for widget in ventana_principal.winfo_children():
        widget.pack_forget()

    try:
        imagen_mago_original = Image.open("mago.png")
        imagen_mago = ImageTk.PhotoImage(redimensionar_imagen(imagen_mago_original, 300, 300))
    except FileNotFoundError:
        print("Error: No se encontró la imagen 'mago.png'.")
        return

    etiqueta_mago = tk.Label(ventana_principal, image=imagen_mago)
    etiqueta_mago.image = imagen_mago
    etiqueta_mago.pack(pady=20)

    etiqueta_desc_mago = tk.Label(ventana_principal, text="J.P.\n Mago olvidadizo, su varita tiene más ideas que él.", font=("System", 14))
    etiqueta_desc_mago.pack()

    boton_batalla = tk.Button(ventana_principal, text="Comenzar Batalla", font=("System", 14, "bold"), command=pantalla_batalla)
    boton_batalla.pack(pady=10)

    boton_regreso = tk.Button(ventana_principal, text="Volver", font=("System", 14, "bold"), command=comenzar_juego)
    boton_regreso.pack(pady=20)

# Función para mostrar la pantalla del asesino
def mostrar_asesino():
    global etiqueta_asesino, etiqueta_desc_asesino, boton_regreso

    for widget in ventana_principal.winfo_children():
        widget.pack_forget()

    try:
        imagen_asesino_original = Image.open("asesino.png")
        imagen_asesino = ImageTk.PhotoImage(redimensionar_imagen(imagen_asesino_original, 300, 300))
    except FileNotFoundError:
        print("Error: No se encontró la imagen 'asesino.png'.")
        return

    etiqueta_asesino = tk.Label(ventana_principal, image=imagen_asesino)
    etiqueta_asesino.image = imagen_asesino
    etiqueta_asesino.pack(pady=20)

    etiqueta_desc_asesino = tk.Label(ventana_principal, text="Albertin\nUn asesino letal, ágil y pillín. Aprendió sus habilidades de su maestro el Oso Berni.", font=("System", 14))
    etiqueta_desc_asesino.pack()

    boton_batalla = tk.Button(ventana_principal, text="Comenzar Batalla", font=("System", 14, "bold"), command=pantalla_batalla)
    boton_batalla.pack(pady=10)

    boton_regreso = tk.Button(ventana_principal, text="Volver", font=("System", 14, "bold"), command=comenzar_juego)
    boton_regreso.pack(pady=20)

# Funcion para mostrar la pantalla del tanque
def mostrar_tanque():
    global etiqueta_tanque, etiqueta_desc_tanque, boton_regreso

    for widget in ventana_principal.winfo_children():
        widget.pack_forget()

    try:
        imagen_tanque_original = Image.open("tanque.png")
        imagen_tanque = ImageTk.PhotoImage(redimensionar_imagen(imagen_tanque_original, 300, 300))
    except FileNotFoundError:
        print("Error: No se encontró la imagen 'tanque.png'.")
        return

    etiqueta_tanque = tk.Label(ventana_principal, image=imagen_tanque)
    etiqueta_tanque.image = imagen_tanque
    etiqueta_tanque.pack(pady=20)

    etiqueta_desc_tanque = tk.Label(ventana_principal, text="Marilu\nMarilu la gigante. La única guerrera en aguantar más de 2 minutos hablando con La temida Rosa.", font=("System", 14))
    etiqueta_desc_tanque.pack()

    boton_batalla = tk.Button(ventana_principal, text="Comenzar Batalla", font=("System", 14, "bold"), command=pantalla_batalla)
    boton_batalla.pack(pady=10)

    boton_regreso = tk.Button(ventana_principal, text="Volver", font=("System", 14, "bold"), command=comenzar_juego)
    boton_regreso.pack(pady=20)

# Funcion para mostrar la pantalla del heroe
def mostrar_heroe():
    global etiqueta_heroe, etiqueta_desc_heroe, boton_regreso

    for widget in ventana_principal.winfo_children():
        widget.pack_forget()

    try:
        imagen_heroe_original = Image.open("turpin.png")
        imagen_heroe = ImageTk.PhotoImage(redimensionar_imagen(imagen_heroe_original, 300, 300))
    except FileNotFoundError:
        print("Error: No se encontró la imagen 'turpin.png'.")
        return

    etiqueta_heroe = tk.Label(ventana_principal, image=imagen_heroe)
    etiqueta_heroe.image = imagen_heroe
    etiqueta_heroe.pack(pady=20)

    etiqueta_desc_heroe = tk.Label(ventana_principal, text="Turpin\nEl héroe de una historia mal contada. Siempre dispuesto a inseminarte.", font=("System", 14))
    etiqueta_desc_heroe.pack()

    boton_batalla = tk.Button(ventana_principal, text="Comenzar Batalla", font=("System", 14, "bold"), command=pantalla_batalla)
    boton_batalla.pack(pady=10)

    boton_regreso = tk.Button(ventana_principal, text="Volver", font=("System", 14, "bold"), command=comenzar_juego)
    boton_regreso.pack(pady=20)

# Función para mostrar la pantalla de batalla
def pantalla_batalla():
    for widget in ventana_principal.winfo_children():
        widget.pack_forget()

    etiqueta_batalla = tk.Label(ventana_principal, text="¡La batalla comienza!", font=("System", 18, "bold"))
    etiqueta_batalla.pack(pady=20)

# Función cuando el usuario presiona "Comenzar juego"
def comenzar_juego():
    # Esconde la pantalla principal y muestra la pantalla de selección de personajes
    for widget in ventana_principal.winfo_children():
        widget.pack_forget()


    # Crear botones para seleccionar personaje
    seleccionar_personaje_label = tk.Label(ventana_principal, text="Elige un personaje", font=("System", 16))
    seleccionar_personaje_label.pack(pady=20)

    # Botones para elegir personaje
    boton_tanque = tk.Button(ventana_principal, text="Marilu - Tanque", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=mostrar_tanque, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_tanque.pack(pady=10)

    boton_heroe = tk.Button(ventana_principal, text="Turpin - Héroe", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=mostrar_heroe, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_heroe.pack(pady=10)

    boton_mago = tk.Button(ventana_principal, text="J.P. - Mago", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=mostrar_mago, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_mago.pack(pady=10)

    boton_asesino = tk.Button(ventana_principal, text="Albertin - Asesino", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=mostrar_asesino, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_asesino.pack(pady=10)

# Función para seleccionar un personaje
def seleccionar_tanque():
    print("Has elegido a Marilu - Tanque")

def seleccionar_heroe():
    print("Has elegido a Turpin - Héroe")

def seleccionar_mago():
    print("Has elegido a J.P. - Mago")

def seleccionar_asesino():
    print("Has elegido a Albertin - Asesino")

# Función para mostrar la información
def mostrar_info():
    global etiqueta_info, boton_regreso  # Definir como global para poder eliminarlos luego

    # Ocultar los widgets de la pantalla principal sin eliminar el fondo
    etiqueta_titulo.pack_forget()
    boton_comenzar.pack_forget()
    boton_emergente.pack_forget()

    # Mostrar imagen de texto_info
    etiqueta_info = tk.Label(ventana_principal, image=imagen_info)
    etiqueta_info.pack(pady=40)

    # Botón para regresar a la pantalla principal
    boton_regreso = tk.Button(ventana_principal, text="Volver", image=imagen_boton, compound="center", 
                              font=("System", 14, "bold"), command=volver_inicio, relief=tk.FLAT, bd=0, 
                              width=ancho_boton, height=alto_boton)
    boton_regreso.pack(pady=20)

# Función para volver a la pantalla principal
def volver_inicio():
    for widget in ventana_principal.winfo_children():
        widget.pack_forget()

    # Restaurar la pantalla principal
    etiqueta_titulo.pack()
    boton_comenzar.pack(pady=20)
    boton_emergente.pack()

# Botón "Comenzar juego"
boton_comenzar = tk.Button(ventana_principal, text="Comenzar", image=imagen_boton, compound="center", font=("System", 14, "bold"), fg="black", activeforeground="white", command=comenzar_juego, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
boton_comenzar.pack(pady=40)

# Botón "Información"
boton_emergente = tk.Button(ventana_principal, text="Información", image=imagen_boton, compound="center", font=("System", 14, "bold"), fg="black", activeforeground="white", command=mostrar_info, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
boton_emergente.pack(pady=40)

# Ejecutar la ventana
ventana_principal.mainloop()
