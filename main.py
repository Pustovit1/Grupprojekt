import re
import random
from os import system

def clear():
    input("""
          


--------------------------Tryck enter för att gå vidare--------------------------
          

          
""")
    system('cls')

def play():
    while True:
        try:
            svar = int(input("""Vill du spela?  
1. Ja
2. Nej 
3. Kolla credits                                                  
Svar: """))   # Frågar om man vill spela eller inte
        except ValueError:
            print("Svara med '1' eller '2'. Tack")      
            continue              
        match svar:
            case 1:
                print("Då kör vi! Ditt mål är att nå level 10")
               
                return            
            case 2:
                svar2 = int(input("""Vad? Vågar du kanske inte?
1. Ja, jag vågar!. Hejdå!
2. Nej, jag vågar inte.
Ditt svar: """))
                
                match svar2:
                       case 1:
                        """

╔╦══╦════════════════╗
║║╔═╬═╦══╦═╗╔═╦╦╦═╦═╗║
║║╚╝╠╝║║║║╩╣║║║║║╩╣╠╝║
║╚══╩═╩╩╩╩═╝╚═╩═╩═╩╝ ║
╚════════════════════╝      
             
              """
                        quit()
                       case 2:
                        svar = 1
            case 3:
                print("""
Programmers: Taras, Kasumi, Ray
Team name: Ghosts'n goblins                               
                                """)
                clear()
            case _:
                print("Svara med '1', '2' eller '3'. Tack")               #ser till att man svarar bara Ja eller Nej
play()


class Inventory():
    def __init__(self):
        self.items: list[Item] = []


    def view_inventory(self):
        print("Inventory\n")
        for item in range(0, len(self.items)):
            print(f"{item + 1}, {self.items[item].rarity}, {self.items[item].name}, +{self.items[item].strength} Strength\n")
   
    def add_inventory(self, added_item):
        while True:
            if len(self.items) < 5:
                self.items.append(added_item)
                return
            else:
                try: deleteitem = int(input("""Ditt inventory är fullt, villl du byta ut något?
1. Ja
2. Nej, jag slänger bort det
Ditt svar: """))
                except ValueError:
                    print("Svara med '1' eller '2'. Tack")
                    continue
            if deleteitem == 1:
                self.view_inventory()
                chosenitem = int(input("""Vilket item vill du ta bort? Svara med nummer på listan!"""))
                self.items.remove(self.items[chosenitem-1])
                #player1.strength = self.items.strength[chosenitem-1]
                print("Du byter ut ditt item och går vidare")
                clear()
            elif deleteitem == 2:
                print("Du slängde bort ditt item och går vidare")
                clear()
            else:
                print("Ogiltigt svar, du slänger bort ditt item och går vidare")
                clear
                                         


class Player:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.inventory = Inventory()
        self.strength = 5





class Door:
    def __init__(self,number):
        self.number = number


def stats():
    """
    Visar spelarens statistik
    """
    global player1
    print(f"""
Ditt namn är: {player1.name}
Din hälsa är: {player1.hp}
Din lvl är: {player1.lvl}
Din styrka är: {player1.strength}""")
    clear() # visar s




def Namn():
    """
    låter spelaren knappa in ett namn, och ger ett felmeddelande om det finns någon annat än bokstäver i namn
    """
    namn = ""  
    while True:
        namn = input("Skriv ditt namn: ")
        if re.match('^[A-Za-z]+$',namn):
            break
        else:  
            print("Du kan endast ha bokstäver i ditt namn!")
    return namn


player1 = Player(Namn(), 10, 1)                                                #Gör så att man får dessa stats från början


class Item():
    def __init__(self): #bestämmer namnet på vapnet
        self.name = random.choice(["Sword of Extermination","Muramasa","Mjolnir","Excalibur","Baxcalibur", "Zangetsu", "Kiribachi","Umbra","En fryst lax"] )
        self.strength = random.randint(1,10)
        self.rarity = ""
        if self.strength <= 5:
            self.rarity = "Common"
        elif self.strength <= 7:
            self.rarity = "Uncommon"
        elif self.strength <= 9:
            self.rarity = "Epic"
        elif self.strength == 10:
            self.rarity = "LEGENDARY"
        else:
            self.rarity = "Unknown"




                       
   
player_inventory = Inventory()
Weapon_Item = Item()
player_inventory.view_inventory()




def chest_event():
    print("chest")
    global player1      
    global player_inventory
    Weapon_Item = Item()

    print(Weapon_Item.rarity)
    print(Weapon_Item.name, str(Weapon_Item.strength) +  " STRENGTH")
    player_inventory.add_inventory(Weapon_Item)
    player1.strength = player1.strength + (Weapon_Item.strength) 
    clear()




class Monster:
    def __init__(self, str):
            self.str = str
def monster_strengt():
    while True:
        strengt = random.randint(player1.strength - 5, player1.strength + 5)
        monster = Monster(strengt)
        return monster
   


def monster_event():
    global player1


    monster = monster_strengt()
    print("₍Ꙭ̂₎")
    print("Oj, ett monster!")
    clear()
    if monster.str > player1.strength + 3:
        print("Den verkar vara stark...")
        clear()
    elif player1.strength > monster.str + 3:
        print("...men, den ser ganska svag ut!")
        clear()
    if monster.str > player1.strength:
        print("""Monstret var starkare än vad du trodde och du blir skadad! du springer snabbt till nästa dörr...""")
        clear()
        player1.hp -= 1
        if player1.hp<=0:
            print("""Oj, du dog!
                  
╔╦══╦════════════════╗
║║╔═╬═╦══╦═╗╔═╦╦╦═╦═╗║
║║╚╝╠╝║║║║╩╣║║║║║╩╣╠╝║
║╚══╩═╩╩╩╩═╝╚═╩═╩═╩╝ ║
╚════════════════════╝
                  
                  """)
            clear()
            play()
        else:
            print(f"""Du har {player1.hp} hp kvar.
                  
                  """)
            clear()
    elif monster.str <= player1.strength:
        player1.lvl = player1.lvl+1
        print(f"""
            Du dödar monstret och går vidare till nästa rum.
            Ditt lvl är {player1.lvl} """)
        clear()
        if player1.lvl >=10:
            print("""Grattis, du nådde level 10 och har därför vunnit spelet!
                  
                  """)
            clear()
            play()




def trap_event(): #En fälla som kan göra så at
    print("(______)")
    print("Oj, en fälla! Du ramlar ner i ett hål fyllt med små taggar! Du förlorar 1 HP")
    clear()
    global player1
    player1.hp = player1.hp-1
    if player1.hp<=0:
        print("""Oj, du dog! 

╔╦══╦════════════════╗
║║╔═╬═╦══╦═╗╔═╦╦╦═╦═╗║
║║╚╝╠╝║║║║╩╣║║║║║╩╣╠╝║
║╚══╩═╩╩╩╩═╝╚═╩═╩═╩╝ ║
╚════════════════════╝      
             
              """)
        play()
    else:
        print(f"""Du har {player1.hp} hp kvar
              
              """)
   
def door():    
    while True:
        try :
            doorchoise= int(input("""Vilken dörr vill du gå in i?
1. Röd dörr 
2. Blå dörr
3. Svart dörr
Ditt svar: """))
            
        except ValueError:
            print("Svara med '1', '2' eller '3'. Tack")
            continue
        match doorchoise:
            case 1:
                print("Du gick in i den röda dörren")
                clear()
                break
            case 2:
                print("Du gick in i den blåa dörren")
                clear()
                break
            case 3:
                print("Du gick in i den svarta dörren")
                clear()
                break
            case _:
                print("Välj mellan 1,2 eller 3.")
                continue
    while True:
        random_number = random.randint(0,2)
        door = Door(random_number)
        break


    if door.number == 0:
        chest_event()
    elif door.number == 1:
        monster_event()
    elif door.number == 2:
        trap_event()


def choise():
    global player_inventory
    global player1
    while True:
        try: choose = int(input(f"""spelare:{player1.name}
HP kvar: {player1.hp}                           
Välj vad vill du göra:
1. Gå vidare och välja dörr                
2. Kolla ditt inventiry
3. Kolla dina stats
4. Avsluta spel
Svar: """))  # Man väljer vad ska göras
        except ValueError:
            print("Svara med '1', '2', '3' eller '4'. Tack")
            continue
        clear()
        match choose:
            case 1:
                door()  # Om man väljer 1 så körs funktion door
                clear()
            case 2:
                player_inventory.view_inventory()
                clear()
            case 3:
                stats()
                clear()
            case 4:
                print(""" 

╔╦══╦════════════════╗
║║╔═╬═╦══╦═╗╔═╦╦╦═╦═╗║
║║╚╝╠╝║║║║╩╣║║║║║╩╣╠╝║
║╚══╩═╩╩╩╩═╝╚═╩═╩═╩╝ ║
╚════════════════════╝      
             
              """)
                quit()
            case _:
                print("Svara med '1', '2', '3' eller '4'. Tack")  # skickar felmeddelande om spellaren värljer ett ogiltigt svar.
choise()


