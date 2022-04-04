from cenik import Cenik
from minc import Mincomat
from zasobnik import Zasobnik



cenik = Cenik(0)
vklad = Mincomat()
zasobnik = Zasobnik()
zapnuto = True
while zapnuto:  # smyčka while pro stálý běh kávomatu
    print("Dobrý den. Prosím vyberte si Váš nápoj: ")
    print(cenik)
    user_choice = int(input("volba: "))
    if user_choice == 9999:    #kód pro servis - manuální reset surovin a vhozených mincí na původní hodnoty. Bylo by možné ošetřit např. zadáním následného č. kódu
        vklad.servis()
        zasobnik.servis()
        print("provedeno doplnění surovin / výběr hotovosti. Počítadla nastavena na výchozí hodnoty.")
    if zasobnik.suroviny_check(user_choice):
        cenik = Cenik(user_choice)
        vklad.pocitadlo(cenik.vyber_napoj())
        vklad.vraceni()
        zasobnik.vydej(user_choice)
    else:
        print("Nedostatek surovin")
