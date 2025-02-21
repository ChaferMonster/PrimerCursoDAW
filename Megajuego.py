import tkinter

class personaje():
    def __init__(self, nombre, vida, vivo, ataque, defensa, suerte, descripcion):
        self.nombre = nombre #nombre del personaje
        self.vida = vida #vida del personaje
        self.vivo = vivo #Indica si el personaje esta vivo
        self.ataque = ataque #potencia de ataque del personaje
        self.defensa = defensa #potencia que resiste el personaje en cada golpe
        self.suerte = suerte #número que se suma a la potencia en cada movimiento para añadirle fuerza al ataque
        self.descripcion = descripcion #descripción del personaje
        pass

    def muerto(self): #Define que el personaje muere
        if self.vida <= 0:
            self.vivo == False

    def aparecer(self): #Define si el personaje aparece como muerto o como vivo en el menú de selección
        if self.vivo == True:
            return True
        else:
            return False
        
    def recibir_danio(self, danio):
        danio_real = max(0, danio - self.defensa)  # El daño se reduce por la defensa, pero nunca es negativo
        self.vida -= danio_real  # Se resta el daño a la vida
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False  # Marca al personaje como muerto si su vida llega a 0
        return danio_real  # Retorna el daño que realmente recibió


class tanque(personaje):
    def __init__(self, nombre, vida, vivo, ataque, defensa, tipo, suerte, descripción, megadefensa):
        super().__init__(nombre, vida, vivo, ataque, defensa, tipo, suerte, descripción)
        self.megadefensa = megadefensa

    def ataque_1(self): #Ataque de personaje
        nombre_ataque = "Escudo antidarius"
        potencia = (50 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_2(self): #Ataque de personaje
        nombre_ataque = "Pisotón antidario"
        potencia = (40 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Quebrantadarios"
        potencia = (60 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque


class asesino(personaje):
    def __init__(self, nombre, vida, vivo, ataque, defensa, suerte, descripcion, evasion, critico):
        super().__init__(nombre, vida, vivo, ataque, defensa, suerte, descripcion)
        self.evasion = evasion
        self.critico = critico

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Ruleta de la suerte asesina"
        potencia = (20 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "DagametidapordetrasaDario"
        potencia = (10 + (self.suerte + self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Lluvia de las millones de dagas"
        potencia = (40 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque


class heroe(personaje):
    def __init__(self, nombre, vida, vivo, ataque, defensa, suerte, descripcion, critico, golpe_valor):
        super().__init__(nombre, vida, vivo, ataque, defensa, suerte, descripcion)
        self.critico = critico
        self.golpe_valor = golpe_valor

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Espada penetradora. Pobre Dario"
        potencia = (60 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque 

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "Puño del valor"
        potencia = (30 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Doble espada penetradora"
        potencia = (10 + (self.suerte + self.suerte)) * self.ataque
        return potencia, nombre_ataque


class mago(personaje):
    def __init__(self, nombre, vida, vivo, ataque, defensa, suerte, descripcion, poder_magico):
        super().__init__(nombre, vida, vivo, ataque, defensa, suerte, descripcion)
        self.poder_magico = poder_magico

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Bola de permatrago"
        potencia = (30 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "Rayo congelabolas"
        potencia = (30 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "MAEB"
        potencia = 150 * self.ataque
        return potencia, nombre_ataque


class dario(personaje):
    def __init__(self, nombre, vida, vivo, ataque, defensa, suerte, descripcion, desgaste):
        super().__init__(nombre, vida, vivo, ataque, defensa, suerte, descripcion)
        self.desgaste = desgaste

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Silbido: FIIIIIU"
        potencia = (50 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "Aplausos"
        potencia = (30 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Quejas, quejas y más quejas"
        potencia = (10 + (self.suerte + self.suerte)) * self.ataque
        return potencia, nombre_ataque

    def ataque_4(self):#Ataque de personaje
        nombre_ataque = "ME F*LLO A TU MADRE"
        potencia = (80 + (self.suerte)) * self.ataque
        return potencia, nombre_ataque



class objeto():
    def __init__(self, cant_usos):
        self.cant_usos = cant_usos

class pocion(objeto):
    def __init__(self, cant_usos, cant_cura):
        super().__init__(cant_usos)
        self.cant_cura = cant_cura

class superpocion(pocion):
    def __init__(self, cant_usos, cant_cura):
        super().__init__(cant_usos, cant_cura)

class mas_ataque(objeto):
    def __init__(self, cant_usos, suma_fuerza):
        super().__init__(cant_usos)
        self.suma_fuerza = suma_fuerza


heroe1 = heroe("Leon", 200, True, 10, 5, 3, "Un valiente guerrero", 2, 1)
asesino1 = asesino("Shadow", 150, True, 12, 3, 5, "Un asesino sigiloso", 8, 4)

# Heroe ataca con su ataque_1
potencia, nombre_ataque = heroe1.ataque_1()
print(f"{heroe1.nombre} usa {nombre_ataque} con una potencia de {potencia}!")

# Asesino recibe el daño
danio_recibido = asesino1.recibir_danio(potencia)
print(f"{asesino1.nombre} recibe {danio_recibido} de daño. Vida restante: {asesino1.vida}")

# Verificar si sigue vivo
if not asesino1.vivo:
    print(f"{asesino1.nombre} ha sido derrotado.")

class objeto():
    def __init__():
        pass
