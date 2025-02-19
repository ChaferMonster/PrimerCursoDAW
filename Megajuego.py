import tkinter

class personaje():
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion):
        self.nombre = nombre
        self.vida = vida
        self.estamina = estamina
        self.vivo = vivo
        self.ataque = ataque
        self.defensa = defensa
        self.suerte = suerte
        self.descripcion = descripcion
        pass

    def muerto(self): #Define que el personaje muere
        if self.vida <= 0:
            self.vivo == False

    def aparecer(self): #Define si el personaje aparece como muerto o como vivo en el menú de selección
        if self.vivo == True:
            return True
        else:
            return False



class tanque(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, tipo, suerte, descripción, megadefensa):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, tipo, suerte, descripción)
        self.megadefensa = megadefensa

    def ataque_1(self): #Ataque de personaje
        nombre_ataque = "Escudo antidarius"
        potencia = 50 + (self.suerte)

    def ataque_2(self): #Ataque de personaje
        nombre_ataque = "Pisotón antidario"
        potencia = 40 + (self.suerte)

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Quebrantadarios"
        potencia = 60 + (self.suerte)


class asesino(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, evasion, critico):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.evasion = evasion
        self.critico = critico

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Ruleta de la suerte asesina"
        potencia = 20 + (self.suerte)

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "DagametidapordetrasaDario"
        potencia = 10 + (self.suerte + self.suerte)

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Lluvia de las millones de dagas"
        potencia = 40 + (self.suerte)


class heroe(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, critico, golpe_valor):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.critico = critico
        self.golpe_valor = golpe_valor

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Espada penetradora. Pobre Dario"
        potencia = 60 + (self.suerte)

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "Puño del valor"
        potencia = 30 + (self.suerte)

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Doble espada penetradora"
        potencia = 10 + (self.suerte + self.suerte)


class mago(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, poder_magico):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.poder_magico = poder_magico

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "Bola de permatrago"
        potencia = 30 + (self.suerte)

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "Rayo congelabolas"
        potencia = 30 + (self.suerte)

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "MAEB"
        potencia = 150


class dario(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, desgaste):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.desgaste = desgaste

    def ataque_1(self):#Ataque de personaje
        nombre_ataque = "FIIIIIU"
        potencia = 50 + (self.suerte)

    def ataque_2(self):#Ataque de personaje
        nombre_ataque = "Aplausos"
        potencia = 30 + (self.suerte)

    def ataque_3(self):#Ataque de personaje
        nombre_ataque = "Quejas, quejas y más quejas"
        potencia = 10 + (self.suerte + self.suerte)

    def ataque_4(self):#Ataque de personaje
        nombre_ataque = "ME F*LLO A TU MADRE"
        potencia = 80 + (self.suerte)



class objeto():
    def __init__():
        pass
