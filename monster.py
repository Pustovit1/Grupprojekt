import random
player_strength = 10
player_hp=3
monster_str = random.randint(player_strength-5,player_strength+5)

def monster_event():
    print("(#'Д')")
    print("Oj, ett monster!")
    print("Oj, ett monster!")
    
    if monster_str>player_strength+3:
        print("den verkar vara stark...")
    elif player_strength>monster_str+3:
        print("...men, den ser ganska svag ut!")
    
    if monster_str > player_strength:
        print("monstret var starkare än vad du trodde och du blir skadad! du springer snabbt till nästa dörr...")
        player_hp=player_hp-1
    elif monster_str > player_strength:
        print("Du dödar monstret och går vidare till nästa rum")

monster_event()
