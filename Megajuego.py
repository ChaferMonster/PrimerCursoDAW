import tkinter as tk

ventana_principal = tk.Tk()
ventana_principal.geometry("650x400")

try:
    imagen_titulo = tk.PhotoImage(file="titulo_juego.png")
except FileNotFoundError:
    print("Error: No se encontró la imagen del título.")
    exit()

etiqueta_titulo = tk.Label(ventana_principal, image=imagen_titulo)
etiqueta_titulo.pack()

def comenzar_juego():
    # Aquí va la lógica para iniciar el juego
    print("¡Juego comenzado!")

def mostrar_texto():
    # Oculta el botón "Abrir ventana emergente" y el botón "Comenzar juego"
    boton_emergente.pack_forget()
    boton_comenzar.pack_forget()
    etiqueta_titulo.pack_forget()  # Oculta la imagen del título

    # Muestra el texto en la ventana principal
    texto = "Esta es la primera línea.\nEsta es la segunda línea.\nEsta es la tercera línea."
    etiqueta_texto = tk.Label(ventana_principal, text=texto, justify=tk.LEFT)
    etiqueta_texto.pack(padx=20, pady=20)

# Botón "Comenzar juego" con mejoras para el relieve
boton_comenzar = tk.Button(ventana_principal, text="Comenzar juego", command=comenzar_juego, font=("Times New Roman", 14), padx=20, pady=10, relief=tk.RAISED, bd=3)  # Añadido relieve y borde
boton_comenzar.pack(pady=20)  # Espacio vertical alrededor del botón

# Nuevo botón para abrir la ventana emergente
boton_emergente = tk.Button(ventana_principal, text="Mostrar texto", command=mostrar_texto, font=("Times New Roman", 14), padx=20, pady=10, relief=tk.RAISED, bd=3)
boton_emergente.pack()

ventana_principal.mainloop()
