class Zasobnik:
    # vstupní parametry zásobníku
    def __init__(self):
        self.kava = 500
        self.voda = 2000
        self.mleko = 1000

    # hlídání, jestli je zásoba surovin > objednanému nápoji
    def suroviny_check(self, vybrano):
        if vybrano == 1:
            if self.kava < 8 or self.voda < 40:
                return False
            else:
                return True
        elif vybrano == 2:
            if self.kava < 8 or self.voda < 40 or self.mleko < 100:
                return False
            else:
                return True
        elif vybrano == 3:
            if self.kava < 8 or self.voda < 50 or self.mleko < 150:
                return False
            else:
                return True

    # odpočet surovin při výdeji
    def vydej(self, vybrano):
        if vybrano == 1:
            self.kava = self.kava - 8
            self.voda = self.voda - 40
        elif vybrano == 2:
            self.kava = self.kava - 8
            self.voda = self.voda - 40
            self.mleko = self.mleko - 100
        elif vybrano == 3:
            self.kava = self.kava - 8
            self.voda = self.voda - 50
            self.mleko = self.mleko - 150
        print("Zde je váš nápoj")
        print(f"pomocné (vymazat) káva: {self.kava}, voda: {self.voda}, mléko: {self.mleko}")   #pomocný kód pro kontrolu odpočtu surovin

    # funkce pro servsní reset hodnot surovin
    def servis(self):
        self.kava = 500
        self.voda = 2000
        self.mleko = 1000