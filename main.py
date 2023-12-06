import re
import random
from random import randint

def play():
    while True:
        try: 
            svar = int(input("""Vill du spela?  
1. Ja
2. Nej                       
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
1. Nej, klart att jag vågar!. Hejdå!
2. Ja... jag vågar kanske inte.
Svar: """))
                match svar2:
                       case 1:
                        quit()
                       case 2:
                        svar = 1
            case _:
                print("Svara med '1' eller '2'. Tack")               #ser till att man svarar bara Ja eller Nej
play()
                                                                    
class Player:
    def __init__(self, name, strength, hp, lvl):                             #innehåler spelarens stats
       self.name = name 
       self.strength = strength
       self.hp = hp
       self.lvl = lvl

class Door:
    def __init__(self,number):
        self.number = number

def stats():
    """
    Visar spelarens statistik
    """
    print(f"""Ditt namn är:{player1.name}
              Din hälsa är {player1.hp} 
              Din lvl är {player1.lvl} 
              Din styrka är {player1.strength}""")#visar s

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

player1 = Player(Namn(),5,10,1)                                                #Gör så att man får dessa stats från början

class Item():
    def __init__(self): #bestämmer namnet på vapnet
        self.name = random.choice(["Sword of Extermination","Muramasa","Mjolnir","Excalibur","Baxcalibur", "Zangetsu", "Kiribachi","Umbra","En fryst lax"] )
        self.strength = random.randint(1,10)
    
    def get_rarity_item(self):
        if 0 < self.strength <= 5:
            return "Common"
        elif 5 < self.strength <= 7:
            return "Uncommon"
        elif 7 < self.strength <= 9:
            return "Epic"
        elif 9 < self.strength <= 10:
            return "LEGENDARY"
        else:
            return "Vad vet jag?!?!"


# Basera item rarity på dess strength
class Inventory():
    def __init__(self):
        self.items = []
    def view_inventory(self):
        print("Inventory")
        for item_number, (item) in enumerate(self.items, 1):
            print(f"{item_number}, {item.name}")
    
    def add_inventory(self, added_item):
        if len(self.items) < 5:
            self.items.append(added_item)
        else:
            deleteitem = int(input("""Ditt inventory är fullt, villl du byta ut något?
1. Ja
2. Nej, jag slänger bort det
Svar: """)) 
            if deleteitem == 1:
                self.view_inventory()
                chosenitem = input("""vilket item vill du ta bort?
                                   Svara i nummer på listan!""")
                self.items.remove(chosenitem-1)
            elif deleteitem == 2: 
                print("Du slängde bort ditt item och gick vidare")
            else:
                print("Ogiltigt svar, du slänger bort ditt item och går vidare")       

                        
    
player_inventory = Inventory()
Weapon_Item = Item()
player_inventory.view_inventory()

   
        

def chest_event():
    print("chest")
    global player1     
    global Weapon_Item      
    global player_inventory       
    print(Weapon_Item.get_rarity_item())
    print(Weapon_Item.name, str(Weapon_Item.strength) +  " STRENGTH")
    player_inventory.add_inventory(Weapon_Item)

      
    
    

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
    if monster.str > player1.strength + 3:
        print("den verkar vara stark...")
    elif player1.strength > monster.str + 3:
        print("...men, den ser ganska svag ut!")
    
    if monster.str > player1.strength:
        print("monstret var starkare än vad du trodde och du blir skadad! du springer snabbt till nästa dörr...")
        player1.hp -= 1
        print(f"du har {player1.hp} hp kvar")
    elif monster.str <= player1.strength:
        print("Du dödar monstret och går vidare till nästa rum")
        player1.lvl += 1


def trap_event(): #En fälla som kan göra så at
    print("(______)")
    print("Oj, en fälla! du ramlar ner i ett hål fyllt med små taggar! Du förlorar 1 HP")
    global player1
    player1.hp = player1.hp-1
    print(f"du har {player1.hp} hp kvar") 
    
def door():    
    while True:
        doorchoise= int(input("""vilken dörr vill du gå in i?
              1. Röd dörr 2. Blå dörr 3. Svart dörr
                              ditt svar: """))
        match doorchoise:
            case 1:
                print("Du gick in i den röda dörren")
                break
            case 2:
                print("Du gick in i den blåa dörren")
                break
            case 3: 
                print("Du gick in i den svarta dörren")
                break
            case _:
                print("Välj mellan 1,2 eller 3.")
                continue
    while True:
        random_number = randint(0,2)
        door = Door(random_number)
        break

    if door.number == 0:
        chest_event()
    elif door.number == 1:
        monster_event()
    elif door.number == 2:
        print("Trap")
        trap_event()

def choise():
    global player_inventory
    while True:
            choose = int(input("""Välj vad vill du göra:
1. Gå vidare och välja dörr                 
2. Kolla ditt inventiry
3. Kolla dina stats
4. Avsluta spel
Svar: """)) #Man väljer vad ska göras
            match choose:
                case 1:
                    door()  #Om man väljer 1 så körs funktion door
                case 2:
                    player_inventory.view_inventory()
                case 3:
                    stats()
                case 4:
                    print("Game Over")
                    quit()
                case _:
                    print("Svara med 1,2,3 eller 4. Tack")                       #skickar felmeddelande om spellaren värljer ett ogiltigt svar. 

choise()

if player1.hp == 0:
    print("Oj, du dog! Game Over!")
    play()
elif player1.lvl == 10:
    print("Gratulerar, du vann spelet!")
    play()