Variables, funciones y clases => nombre_palabradescriptiva
comentar todo lo que vamos haciendo para que los demás sepan que hace cada parte del código

Juego: Apocalipsis Dario

Definición del juego: Juego donde hay una serie de personajes que van a derrotar al jefe final (Dario). 

Cada jugador (personaje) tiene unas habilidades. Dario también es un personaje con más habilidades.
Hay objetos para usar (Pociones de diferentes tipos)

Comienzo: 
    - Creación de las clases y subclases (personajes y objetos)
    - Creación de métodos (ataques, orden de usar ubjeto, que tipo de objetos)
    - Creación de menú
    - Creación de la pantalla de pelea

Cosas a tener en cuenta:
    - Cuando un personaje muere debe aparecer como muerto.
    - Un personaje muerto puede revivir si se usa una poción de revivir.
    - Cuando un personaje muere, Dario debe aparecer contra el siguiente personaje que se escoja con la misma vida con la que se ha quedado. anteriormente.
    - Las pociones aumentan atributos como: vida, suerte, fuerza...

Atributos:
    - Nombre
    - Vida
    - vivo
    - ataque
    - defensa
    - tipo
    - suerte
    - descripción
    - atributos especiales de cada personaje

Métodos:
    - Atacar (Selección de ataques de cada personaje)
    - Usar objeto (Al usarlo, que haga el efecto de cada objeto)
    - Morir 
    - Aumentar estadísticas (Al usar objeto)
    - recibir daño (Cuando el personaje sea atacado)

Menú:
    - Título
    - Imágen 1
    - Botón de comenzar juego (Pasa a pantalla "Historia")

Pantalla "Historia":
    - Breve historia del juego
    - Imágen 2
    - Botón de Continuar (pasa a pantalla "Escoger personaje")

Pantalla "Escoger personaje":
    - Mensaje de "Escoge a tu luchador:"
    - contenedor con:
        - Foto del luchador
        - Nombre 
        - Descripción 
        - Botón de "Más información" (Abre ventana de "Información del luchador")
            - Atributos
            - Ataques
            - Objetos
            - Habilidad especial
        - Botón de "Seleccionar" (Pasa a pantalla de "Comienza el juego")

Pantalla "Comienza el juego":
    - Dario con su vida 
    - Personaje escogido con su vida
    - menú:
        - Botón de ataque 1
        - Botón de ataque 2
        - Botón de ataque 3
        - Boton de menú de objetos:
            - Objeto 1
            - objeto 2
            - objeto 3
Cosas que sucede al atacar
    - Al usar ataque o objeto cambia vida de Dario o de personaje
    - Cuando ataque nuestro personaje, ataca dario.
    




    
