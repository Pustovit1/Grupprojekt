import re
import random
from random import randint

def play():
    while True:
            svar = input("Vill du spela? ").capitalize() # Frågar om man vill spela eller inte
            if svar == "Nej": #Om man skriver Nej så avslutas kod
                print("Vad? Vågar du kanske inte?")
                quit() 
            elif svar == "Ja":  #om man skriver Ja så börjas spel
             print("Då kör vi!")
             return #Avslutar funktion
            print("Svara med 'Ja' eller 'Nej'. Tack") #ser till att man svarar bara Ja eller Nej
play()

def choise():
    while True:
            choose = int(input("""Välj vad vill du göra:
                    1. Gå vidare och välja dörr                 
                    2. Kolla ditt inventiry
                    3. Kolla dina stats
                    4. Avsluta spel
                    Ditt val -> """)) #Man väljer vad ska göras
            if choose == 1:            #Om man väljer 1 så körs funktion door
                door()
            elif choose == 2:          #om man väljer 2 så kollar man sin inventory
                print("inventory")
            elif choose == 3:           #Om man väljer 3 så koollar man sin stats
                stats()
            elif choose == 4:           #om man väljer 4 så avslutas spel
                print("Game Over")
                quit()
            else:
                print("Svara med 1,2,3 eller 4. Tack")#skickar felmeddelande om spellaren värljer ett ogiltigt svar. 
class Player:
    def __init__(self, name, strength, hp, lvl): #innehåler spelarens stats
       self.name = name 
       self.strength = strength
       self.hp = hp
       self.lvl = lvl

class Door:
    def __init__(self,number):
        self.number = number

def stats():
    print(f"""Ditt namn är:{player1.name}
              Din hälsa är {player1.hp} 
              Din lvl är {player1.lvl} 
              Din styrka är {player1.strength}""")#visar s

def Namn(): #låter spelaren knappa in ett namn, och ger ett felmeddelande om det finns någon annat än bokstäver i namn
    namn = ""
    while True:
        namn = input("Skriv ditt namn: ")
        if re.match('^[A-Za-z]+$',namn):
            break
        else:  
            print("Du kan endast ha bokstäver i ditt namn!")
    return namn
player1 = Player(Namn(),5,10,1) #Gör så att man får dessa stats från början

class Item():
    def __init__(self): #bestämmer namnet på vapnet
        self.name = random.choice(["Sword of Extermination","Muramasa","Mjolnir","Excalibur","Baxcalibur", "Zangetsu"] )
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


# Basera item rarity på dess strength
class Inventory():
    def __init__(self):
        self.items = []
    def view_invetory(self):
        print("Inventory")
        for item, (item,) in enumerate
        
            

   
        

def chest_event():
    print("chest")
#     global player1
#     Weapon_item = Item()
#     player_input = input("Du hittade en kista, vill du öpnna den?\n Ja/Nej").capitalize
#     if player_input == "Ja":
#         Weapon_item = Item()
#         print(Weapon_item.get_rarity_item())
#         print(Weapon_item.name, str(Weapon_item.strength) +  " STRENGTH")
#         player_input = input("Vill du plocka upp item?\n Ja/Nej").capitalize
#         if player_input == "Ja":
#             inventory.append(Weapon_item)
            
            
            
    
    

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
choise()

if player1.hp == 0:
    print("Du dog")
    quit()
elif player1.lvl == 10:
    print("gratulerar du vann spelet!")
    quit()