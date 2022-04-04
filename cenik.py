class Cenik:
    # modul pro uložení cen nápojů a jejich výběr uživatlem. Input je INT, returnuje cenu nápoje
    def __init__(self, volba):
        self.cena_presso = 25
        self.cena_cappuccino = 35
        self.cena_lattee = 40
        self.volba = volba

    def vyber_napoj(self):
        if self.volba == 1:
            zvoleno = self.cena_presso
        elif self.volba == 2:
            zvoleno = self.cena_cappuccino
        elif self.volba == 3:
            zvoleno = self.cena_lattee
        return zvoleno
    # textový výstup cen nápojů pro uživatele
    def __str__(self):
        return f"1) Presso: {self.cena_presso}Kč, 2) Cappuccino: {self.cena_cappuccino}Kč, 3) Lattee: {self.cena_lattee}Kč"






