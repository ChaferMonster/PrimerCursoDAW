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


class tanque(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, tipo, suerte, descripción, megadefensa):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, tipo, suerte, descripción)
        self.megadefensa = megadefensa


class asesino(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, evasion, critico):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.evasion = evasion
        self.critico = critico


class heroe(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, critico, golpe_valor):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.critico = critico
        self.golpe_valor = golpe_valor


class mago(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, poder_magico):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.poder_magico = poder_magico


class demonio(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, desgaste):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)
        self.desgaste = desgaste

        

class cerbero(personaje):
    def __init__(self, nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion, ):
        super().__init__(nombre, vida, estamina, vivo, ataque, defensa, suerte, descripcion)

Print("Hugo es inutil")
