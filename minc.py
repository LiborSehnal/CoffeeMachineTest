class Mincomat:
    # zásobník s počtem mincí / zásobník počtu jednotlivých vložených mincí při konkrétním nákupu(po úspěšném zaplacení se vklad_ maže)
    def __init__(self):
        self.zasobnik_koruna = 20
        self.zasobnik_petikoruna = 10
        self.zasobnik_desetikoruna = 10
        self.zasobnik_dvacetikoruna = 10
        self.vklad_koruna = 0
        self.vklad_petikoruna = 0
        self.vklad_desetikoruna = 0
        self.vklad_dvacetikoruna = 0

    # přijímá mince, ukladá do dočasné vklad_, kontroluje jestli vklad >= ceně, pokud platba OK, přičte mince do zásobníku
    def pocitadlo(self, vybrano):
        self.vybrano = vybrano
        print(f"Cena vašeho nápoje: {self.vybrano}Kč")
        print("Prosím vložte mince hodnoty: 1, 5, 10, 20")
        vlozeno = False
        mezisoucet = 0
        while not vlozeno:
            koruna = int(input("Vložte 1Kč mince: "))
            self.vklad_koruna += koruna
            petikoruna = int(input("Vložte 5Kč mince: ")) * 5
            self.vklad_petikoruna += (petikoruna / 5)
            desetikoruna = int(input("Vložte 10Kč mince: ")) * 10
            self.vklad_desetikoruna += (desetikoruna / 10)
            dvacetikoruna = int(input("Vložte 20Kč mince: ")) * 20
            self.vklad_dvacetikoruna += (dvacetikoruna / 20)
            self.soucet_minci = koruna + petikoruna + desetikoruna + dvacetikoruna
            mezisoucet += self.soucet_minci
            print(f"Vložil jste: {self.soucet_minci} Kč")
            if mezisoucet < self.vybrano:
                malo_penez = input(f"Vložil jste příliš nízkou částku. Aktuálně máte vloženo {mezisoucet}Kč. Přejete si doplnit mince? ano/ne: ")
                if malo_penez == "ne":
                    print(f"Děkujeme za použití. Vracím vloženou částku {self.soucet_minci} Kč")
                    break  #doplnit vymazání dočasných vklad_ / vymyslet jak při NE vrátit program na start
            else:
                vlozeno = True
        # vyprázdnění "cache" vklad_ hodnot poté, co je vložená částka ověřená + přičtení počtu mincí do zásobníku
        self.zasobnik_koruna += self.vklad_koruna
        self.vklad_koruna = 0
        self.zasobnik_petikoruna += self.vklad_petikoruna
        self.vklad_petikoruna = 0
        self.zasobnik_desetikoruna += self.vklad_desetikoruna
        self.vklad_desetikoruna = 0
        self.zasobnik_dvacetikoruna += self.vklad_dvacetikoruna
        self.vklad_dvacetikoruna = 0
        print("Platba přijata")
        return self.soucet_minci

    # funkce na vrácení přeplatku. Snaha o vrácení v co největších dostupných mincích.
    def vraceni(self):
        self.dvacky = 0
        self.desitky = 0
        self.petky = 0
        self.koruny = 0
        """Vymyslet jak následující proiterovat a neopakovat kód. Pokud vklad > cena nápoje tak zjistí rozdíl a rozloží vrácení na nejvyšší možné mince
        vymyslet podmínku pro nedostatek konkrétního druhu mincí v zásobníku. Jak přehodit vrácení na další nižší hodnotu? 20 -> 2x10 atp"""
        if self.soucet_minci > self.vybrano:
            vratit_hodnota = self.soucet_minci - self.vybrano
            dvacky_pocet = int(vratit_hodnota / 20)
            self.dvacky += dvacky_pocet
            vratit_hodnota = (self.soucet_minci - (self.dvacky * 20) - self.vybrano)
            desitky_pocet = int(vratit_hodnota / 10)
            self.desitky += desitky_pocet
            vratit_hodnota = (self.soucet_minci - (self.dvacky * 20) - (self.desitky * 10) - self.vybrano)
            petky_pocet = int(vratit_hodnota / 5)
            self.petky += petky_pocet
            vratit_hodnota = (self.soucet_minci - (self.dvacky * 20) - (self.desitky * 10) - (self.petky * 5) - self.vybrano)
            koruny_pocet = int(vratit_hodnota / 1)
            self.koruny += koruny_pocet
            vratit_hodnota = (self.soucet_minci - (self.dvacky * 20) - (self.desitky * 10) - (self.petky * 5) - self.koruny - self.vybrano)
            print(f"Vracím: {self.soucet_minci - self.vybrano}Kč")
            # print(self.zasobnik_dvacetikoruna, self.zasobnik_desetikoruna, self.zasobnik_petikoruna, self.zasobnik_koruna)    #kód pro kontrolu - hodn. před vrácením
        # odečtení vrácených mincí ze zásobníku mincí
        self.zasobnik_dvacetikoruna -= self.dvacky
        self.zasobnik_desetikoruna -= self.desitky
        self.zasobnik_petikoruna -= self.petky
        self.zasobnik_koruna -= self.koruny
        # print(self.zasobnik_dvacetikoruna, self.zasobnik_desetikoruna, self.zasobnik_petikoruna, self.zasobnik_koruna)    #kód pro kontrolu - hodn. po vrácení

    # funkce pro servsní reset počtu mincí
    def servis(self):
        self.zasobnik_koruna = 20
        self.zasobnik_petikoruna = 10
        self.zasobnik_desetikoruna = 10
        self.zasobnik_dvacetikoruna = 10










