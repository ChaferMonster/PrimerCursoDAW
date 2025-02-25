import tkinter
import random
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, suerte, descripcion):
        self.nombre = nombre  # Nombre del personaje
        self.vida = vida  # Vida del personaje
        self.vivo = True  # Indica si el personaje está vivo
        self.ataque = ataque  # Potencia de ataque del personaje
        self.defensa = defensa  # Defensa del personaje
        self.suerte = suerte  # Modificador de ataque
        self.descripcion = descripcion  # Descripción del personaje

    def recibir_danio(self, danio):
        danio_real = max(0, danio - self.defensa)  # Reduce el daño con la defensa
        self.vida -= danio_real
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False  # Marca al personaje como muerto
        return danio_real  # Retorna el daño recibido

    def esta_vivo(self):
        return self.vivo


# CLASES DE PERSONAJES CON ATRIBUTOS ESPECIALES
class Tanque(Personaje):
    def __init__(self):
        super().__init__(nombre="Marilu", vida=4000,suerte=int(random.randint(5,12)), ataque=60, defensa=40, descripcion="Marilu la gigante. La única guerrera en aguantar más de 2 minutos hablando con La temida Rosa")
        self.megadefensa = 20  # Reducción de daño adicional
        self.defensa+=self.suerte

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


class Asesino(Personaje):
    def __init__(self):
        super().__init__(nombre="Albertin", vida=3000,suerte=int(random.randint(5,25)), ataque=100, defensa=0,  descripcion="Un asesino letal, ágil y pillín. Aprendió sus habilidades de su maestro el Oso Berni.")
        self.evasion = 30  # Posibilidad de evadir ataques
        self.defensa+=self.suerte

    def esquivar_ataque(self):
        from random import randint
        return randint(1, 100) <= self.evasion  # Probabilidad de esquivar

    def ataque_1(self):
        return (20 + self.suerte) * self.ataque, "Ruleta de la suerte asesina"

    def ataque_2(self):
        return (10 + (2 * self.suerte)) * self.ataque, "DagametidapordetrasaDario"

    def ataque_3(self):
        return (40 + self.suerte) * self.ataque, "Lluvia de las millones de dagas"


class Heroe(Personaje):
    def __init__(self):
        super().__init__(nombre="Turpin", vida=3500,suerte=random.randint(8,15), ataque=80, defensa=10,  descripcion="El héroe de una historia mal contada. Siempre dispuesto a inseminarte.")
        self.defensa+=self.suerte
        self.golpe_valor = 1.5  # Aumenta el daño cuando tiene poca vida

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
        super().__init__(nombre="J.P.", vida=3200,suerte=14, ataque=90, defensa=5,  descripcion="Mago olvidadizo, su varita tiene más ideas que él.")
        self.poder_magico = 1.3  # Aumenta el daño de sus ataques mágicos
        self.defensa+=self.suerte

    def ataque_magico(self):
        return self.poder_magico * self.ataque, "Varita venosa"

    def ataque_1(self):
        return (30 + self.suerte) * self.ataque, "Bola de permatrago"

    def ataque_2(self):
        return (30 + self.suerte) * self.ataque, "Rayo congelabolas"

    def ataque_3(self):
        return 150 * self.ataque, "MAEB"


class Dario(Personaje):
    def __init__(self):
        super().__init__(nombre="Dariork", vida=50000,suerte=20, ataque=70, defensa=15,  descripcion="Cejas de ques. Teleja. Y los bolsillos naranjas.")
        self.desgaste = 5  # Reduce la defensa de los enemigos en cada golpe
        self.defensa+=self.suerte

    def ataque_desgastante(self, objetivo):
        objetivo.defensa = max(0, objetivo.defensa - self.desgaste)

    def ataque_1(self):
        return (50 + self.suerte) * self.ataque, "Silbido: FIIIIIU"

    def ataque_2(self):
        return (30 + self.suerte) * self.ataque, "Aplausos"

    def ataque_3(self):
        return (10 + (2 * self.suerte)) * self.ataque, "Quejas, quejas y más quejas"

    def ataque_4(self):
        return (80 + self.suerte) * self.ataque, "ME F*LLO A TU MADRE"


# OBJETOS Y POCIONES
class Objeto:
    def __init__(self, cant_usos):
        self.cant_usos = cant_usos


class Pocion(Objeto):
    def __init__(self, cant_usos, cant_cura):
        super().__init__(cant_usos)
        self.cant_cura = cant_cura


class Superpocion(Pocion):
    def __init__(self, cant_usos):
        super().__init__(cant_usos, cant_cura=1500)


class MasAtaque(Objeto):
    def __init__(self, cant_usos):
        super().__init__(cant_usos)
        self.suma_fuerza = 0.25  # Aumenta el daño un 25% durante 3 turnos


# EJEMPLO DE BATALLA
heroe1 = Heroe()
dario1 = Dario()

# Heroe ataca con su ataque_1
potencia, nombre_ataque = heroe1.ataque_1()
print(f"{heroe1.nombre} usa {nombre_ataque} con una potencia de {potencia}!")

# Dario recibe el daño
danio_recibido = dario1.recibir_danio(potencia)
print(f"{dario1.nombre} recibe {danio_recibido} de daño. Vida restante: {dario1.vida}")

# Verificar si sigue vivo
if not dario1.esta_vivo():
    print(f"{dario1.nombre} ha sido derrotado.")
