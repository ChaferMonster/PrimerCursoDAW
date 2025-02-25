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
        super().__init__(nombre="Marilu", vida=4000, suerte=int(random.randint(5,12)), ataque=60, defensa=40, descripcion="Marilu la gigante.")
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
        super().__init__(nombre="Turpin", vida=3500, suerte=random.randint(8,15), ataque=80, defensa=10, descripcion="El héroe de una historia mal contada.")
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
        super().__init__(nombre="J.P.", vida=3200, suerte=14, ataque=90, defensa=5, descripcion="Mago olvidadizo.")
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
        super().__init__(nombre="Albertin", vida=3000, suerte=int(random.randint(5,25)), ataque=100, defensa=0, descripcion="Un asesino letal.")
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

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.geometry("650x400")

# Cargar imágenes
try:
    imagen_fondo_original = Image.open("fondo.png")
    imagen_titulo_original = Image.open("titulo_juego.png")
    imagen_info_original = Image.open("texto_info.png")
    imagen_boton_original = Image.open("boton.png")

    # Redimensionar imágenes
    ancho_boton = 150
    alto_boton = 75
    imagen_boton = ImageTk.PhotoImage(redimensionar_imagen(imagen_boton_original, ancho_boton, alto_boton))

    # Convertir imágenes a formato Tkinter
    imagen_titulo = ImageTk.PhotoImage(imagen_titulo_original)
    imagen_info = ImageTk.PhotoImage(imagen_info_original)

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

# Función cuando el usuario presiona "Comenzar juego"
def comenzar_juego():
    # Esconde la pantalla principal y muestra la pantalla de selección de personajes
    etiqueta_titulo.pack_forget()
    boton_comenzar.pack_forget()
    boton_emergente.pack_forget()

    # Crear botones para seleccionar personaje
    seleccionar_personaje_label = tk.Label(ventana_principal, text="Elige un personaje", font=("Arial", 16))
    seleccionar_personaje_label.pack(pady=20)

    # Botones para elegir personaje
    boton_tanque = tk.Button(ventana_principal, text="Marilu - Tanque", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=seleccionar_tanque, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_tanque.pack(pady=10)

    boton_heroe = tk.Button(ventana_principal, text="Turpin - Héroe", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=seleccionar_heroe, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_heroe.pack(pady=10)

    boton_mago = tk.Button(ventana_principal, text="J.P. - Mago", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=seleccionar_mago, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_mago.pack(pady=10)

    boton_asesino = tk.Button(ventana_principal, text="Albertin - Asesino", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=seleccionar_asesino, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
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
    # Limpiar la pantalla principal
    for widget in ventana_principal.winfo_children():
        widget.destroy()

    # Mostrar imagen de texto_info
    etiqueta_info = tk.Label(ventana_principal, image=imagen_info)
    etiqueta_info.pack(pady=20)

    # Botón para regresar a la pantalla principal
    boton_regreso = tk.Button(ventana_principal, text="Volver", image=imagen_boton, compound="center", font=("System", 14, "bold"), command=volver_inicio, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
    boton_regreso.pack()

# Función para volver a la pantalla principal
def volver_inicio():
    # Limpiar la pantalla actual
    for widget in ventana_principal.winfo_children():
        widget.destroy()

    # Mostrar la pantalla principal
    etiqueta_titulo.pack()
    boton_comenzar.pack(pady=20)
    boton_emergente.pack()

# Botón "Comenzar juego"
boton_comenzar = tk.Button(ventana_principal, text="Comenzar", image=imagen_boton, compound="center", font=("System", 14, "bold"), fg="black", activeforeground="white", command=comenzar_juego, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
boton_comenzar.pack(pady=20)

# Botón "Mostrar imagen"
boton_emergente = tk.Button(ventana_principal, text="Mostrar", image=imagen_boton, compound="center", font=("System", 14, "bold"), fg="black", activeforeground="white", command=mostrar_info, relief=tk.FLAT, bd=0, width=ancho_boton, height=alto_boton)
boton_emergente.pack()

# Ejecutar la ventana
ventana_principal.mainloop()
