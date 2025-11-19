# Filename: ListOfPersonasV2.py
# Date: Updated 11/13/25
# Author: shadowsnowwolf
# Process:
# Make tuples for each Arcana and index with for loops to display the name of each Persona based on the user's input of the Arcana. 
# A while loop will allow the user to continue if they choose to do so, letting the user see as many Personas of each Arcana they choose
# If the user doesn't enter y, the loop breaks and the program ends.

# Can practice enumerate when I do the display functions
# Maybe have an option where you can search for a Persona and if the Persona exists, you get the details of it

# Important note: 
# Needs to debug to be approved for use 
# Bugs: Has a logic error with both loops 



class Personas:
    # Done
    def foolArcanaPersonasList():
        fool_personas_list = ("Arsene","Obariyon","Orpheus F","Orpheus F Picaro","High Pixie",
        "Izanagi","Izanagi Picaro","Orpheus","Orpheus Picaro","Legion","Ose",
        "Bugs","Crystal Skull", "Black Frost","Raoul","Vishnu","Satanael")
        return fool_personas_list

    # Done
    def display_fool_personas():
        fool_personas_list = Personas.foolArcanaPersonasList()
        print("\nList of Fool Personas:")
        for persona_index, persona in enumerate(fool_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def magicianArcanaPersonasList():
        magician_personas_list = ("Jack-o'-Lantern","Cait Sith","Jack Frost","Nekomata","Sandman",
        "Choronzon","Queen Mab","Rangda","Forneus","Surt","Futsunushi")
        return magician_personas_list

    # Done
    def display_magician_personas():
        magician_personas_list = Personas.magicianArcanaPersonasList()
        print("\nList of Magician Personas:")
        for persona_index, persona in enumerate(magician_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        
    # Done
    def priestessArcanaPersonasList():
        priestess_personas_list = ("Silky","Apsaras","Koh-i-Noor","Isis","Kikuri-Hime",
        "Sarasvati","Skadi","Scathach","Cybele")
        return priestess_personas_list
    
    # Done
    def display_priestess_personas():
        priestess_personas_list = Personas.priestessArcanaPersonasList()
        print("\nList of Priestess Personas:")
        for persona_index, persona in enumerate(priestess_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def empressArcanaPersonasList():
        empress_personas_list = ("Queen's Necklace","Yaksini","Lamia","Hariti","Dakini",
        "Titania","Kali","Alilat","Mother Harlot")
        return empress_personas_list

    # Done
    def display_empress_personas():
        empress_personas_list = Personas.empressArcanaPersonasList()
        print("\nList of Empress Personas:")
        for persona_index, persona in enumerate(empress_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done 
    def emperorArcanaPersonasList():
        emperor_personas_list = ("Regent","Eligor","Setanta","Thoth",
        "Barong","King Frost","Oberon","Baal","Odin")
        return emperor_personas_list
    
    # Done
    def display_emperor_personas():
        emperor_personas_list = Personas.emperorArcanaPersonasList()
        print("\nList of Emperor Personas:")
        for persona_index, personas in enumerate(emperor_personas_list, start=1):
            print(f"{persona_index}. {personas}")
        print("------------------------------------------------------------------------")

    # Done
    def hierophantArcanaPersonaList():
        hierophant_personas_list = ("Berith","Orobas","Anzu","Daisoujou","Mishaguji","Bishamonten","Kohryu")
        return hierophant_personas_list
    
    # Done
    def display_hierophant_personas():
        hierophant_personas_list = Personas.hierophantArcanaPersonaList()
        print("\nList of Hierophant Personas:")
        for persona_index, persona in enumerate(hierophant_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def loversArcanaPersonasList():
        lovers_personas_list = ("Pixie","Saki Mitama","Ame-no-Uzume","Leanan Sidhe","Kushinada","Narcissus",
        "Parvati","Raphael","Ishtar")
        return lovers_personas_list

    # Done
    def display_lovers_personas():
        lovers_personas_list = Personas.loversArcanaPersonasList()
        print("\nList of Lovers Personas:")
        for persona_index, persona in enumerate(lovers_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def chariotArcanaPersonasList():
        chariot_personas_list = ("Agathion","Slime","Shiki-Ouji","Kin-Ki","Ara Mitama","White Rider","Athena",
        "Athena Picaro","Cerberus","Thor","Chi You")
        return chariot_personas_list

    # Done
    def display_chariot_personas():
        chariot_personas_list = Personas.chariotArcanaPersonasList()
        print("\nList of Chariot Personas:")
        for persona_index, persona in enumerate(chariot_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def justiceArcanaPersonasList():
        justice_personas_list = ("Angel","Archangel","Principality","Power","Melchizedek","Throne",
        "Uriel","Metatron")
        return justice_personas_list
    
    # Done
    def display_justice_personas():
        justice_personas_list = Personas.justiceArcanaPersonasList()
        print("\nList of Justice Personas:")
        for persona_index, persona in enumerate(justice_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def hermitArcanaPersonasList():
        hermit_personas_list = ("Bicorn","Koropokkuru","Ippon-Datara","Sudama","Naga","Kurama Tengu","Arahabaki",
        "Kumbhanda","Koumokuten","Loa","Fafnir","Ongyo-Ki")
        return hermit_personas_list
    
    # Done
    def display_hermit_personas():
        hermit_personas_list = Personas.hermitArcanaPersonasList()
        print("\nList of Hermit Personas:")
        for persona_index, persona in enumerate(hermit_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def fortuneArcanaPersonasList():
        fortune_personas_list = ("Stone of Scone","Clotho","Ariadne","Lachesis","Atropos","Ariadne Picaro","Fortuna","Norn",
        "Asterius","Asterius Picaro","Lakshmi")
        return fortune_personas_list
    
    # Done
    def display_fortune_personas():
        fortune_personas_list = Personas.fortuneArcanaPersonasList()
        print("\nList of Fortune Personas:")
        for persona_index, persona in enumerate(fortune_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def strengthArcanaPersonasList():
        strength_personas_list = ("Kelpie","Shiisaa","Oni","Rakshasa","Orlov","Zouchouten","Valkyrie","Hanuman","Chimera","Zaou-Gongen")
        return strength_personas_list

    # Done
    def display_strength_personas():
        strength_personas_list = Personas.strengthArcanaPersonasList()
        print("\nList of Strength Personas:")
        for persona_index, persona in enumerate(strength_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def hangedManArcanaPersonaList():
        hanged_man_personas_list = ("Hua Po","Inugami","Orthrus","Take-Minakata","Emperor's Amulet","Hecatoncheires","Jatayu",
        "Moloch","Macabre","Attis")
        return hanged_man_personas_list

    # Done
    def display_hanged_man_personas():
        hanged_man_personas_list = Personas.hangedManArcanaPersonaList()
        print("\nList of Hanged Man Personas:")
        for persona_index, persona in enumerate(hanged_man_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def deathArcanaPersonaList():
        death_personas_list = ("Mandrake","Mokoi","Matador","Nue","Pisaca","Hell Biker","Hope Diamond","Pale Rider","Chernobog",
        "Thanatos","Thanatos Picaro","Mot","Alice")
        return death_personas_list

    # Done
    def display_death_personas():
        death_personas_list = Personas.deathArcanaPersonaList()
        print("\nList of Death Personas:")
        for persona_index, persona in enumerate(death_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def temperanceArcanaPersonaList():
        temperance_personas_list = ("Genbu","Koppa Tengu","Makami","Jikokuten","Mithra","Byakko","Raja Naga","Gabriel",
        "Ardha")
        return temperance_personas_list
    
    # Done
    def display_temperance_personas():
        temperance_personas_list = Personas.temperanceArcanaPersonaList()
        print("\nList of Temperance Personas:")
        for persona_index, persona in enumerate(temperance_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done 
    def devilArcanaPersonasList():
        devil_personas_list = ("Incubus","Flauros","Andras","Lilim","Pazuzu","Baphomet","Nebiros","Belial","Beelzebub")
        return devil_personas_list 
    
    # Done
    def display_devil_personas():
        devil_personas_list = Personas.devilArcanaPersonasList()
        print("\nList of Devil Personas: ")
        for persona_index, persona in enumerate(devil_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def towerArcanaPersonasList():
        tower_personas_list = ("Belphegor","Red Rider","Magatsu-Izanagi","Magatsu-Izanagi Picaro","Seth","Black Rider",
        "Mara","Yoshitsune","Mada")
        return tower_personas_list

    # Done
    def display_tower_personas():
        tower_personas_list = Personas.towerArcanaPersonasList()
        print("\nList of Tower Personas:")
        for persona_index, persona in enumerate(tower_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def starArcanaPersonasList():
        star_personas_list = ("Kodama","Fuu-Ki","Neko Shogun","Kaiwan","Garuda","Vasuki","Sraosha","Hastur","Lucifer")
        return star_personas_list
    
    # Done
    def display_star_personas():
        star_personas_list = Personas.starArcanaPersonasList()
        print("\nList of Star Personas:")
        for persona_index, persona in enumerate(star_personas_list, start=1):
            print(f"{persona}. {persona_index}")
        print("------------------------------------------------------------------------")

    # Done
    def moonArcanaPersonasList():
        moon_personas_list = ("Succubus","Onmoraki","Kaguya","Black Ooze","Sui-Ki","Kaguya Picaro","Mothman",
        "Girimehkala","Tsukiyomi","Tsukiyomi Picaro","Lilith","Byakhee","Sandalphon")
        return moon_personas_list

    # Done
    def display_moon_personas():
        moon_personas_list = Personas.moonArcanaPersonasList()
        print("\nList of Moon Personas:")
        for persona_index, persona in enumerate(moon_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def sunArcanaPersonasList():
        sun_personas_list = ("Suzaku","Thunderbird","Mithras","Yurlungur","Horus","Ganesha","Quetzalcoatl","Asura")
        return sun_personas_list

    # Done
    def display_sun_personas():
        sun_personas_list = Personas.sunArcanaPersonasList()
        print("\nList of Sun Personas:")
        for persona_index, personas in enumerate(sun_personas_list, start=1):
            print(f"{persona_index}. {personas}")
        print("------------------------------------------------------------------------")

    # Done
    def judgementArcanaPersonaList():
        judgement_personas_list = ("Anubis","Trumpeter","Yamata-no-Orochi","Abaddon","Messiah",
        "Shiva","Michael","Messiah Picaro","Satan")
        return judgement_personas_list

    # Done
    def display_judgement_personas():
        judgement_personas_list = Personas.judgementArcanaPersonaList()
        print("\nList of Judgement Personas:")
        for persona_index, persona in enumerate(judgement_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def faithArcanaPersonaList():
        faith_personas_list = ("Phoenix","Tam Lin","Unicorn","Okuninushi","Orichalcum","Atavaka","Cu Chulainn",
        "Siegfried","Maria")
        return faith_personas_list

    # Done
    def display_faith_personas():
        faith_personas_list = Personas.faithArcanaPersonaList()
        print("\nList of Faith Personas:")
        for persona_index, persona in enumerate(faith_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    # Done
    def councillorArcanaPersonaList():
        councillor_personas_list = ("Kushi Mitama","Nigi Mitama","Decarabia","Ananta","Yatagarasu","Seiryu",
        "Dionysus","Vohu Manah")
        return councillor_personas_list
    
    # Done
    def display_councillor_personas():
        councillor_personas_list = Personas.councillorArcanaPersonaList()
        print("\nList of Councillor Personas:")
        for persona_index, persona in enumerate(councillor_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    def display_arcana_list():
        print("\nList of Arcanas:")
        for arcana_index, arcana in enumerate(persona_arcanas, start=1):
            print(f"{arcana_index}. {arcana}")

# Now I want to ask the user for an Arcana type and use a loop that ends when they enter finish

valid_arcana_choice = False
persona_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant","Lovers","Chariot","Justice","Hermit",
                   "Fortune","Strength","Hanged Man", "Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","Faith","Councillor")


# I need a loop to do this 

arcana_list_choice = ""
while arcana_list_choice != "y": # Loop 1: Handles if they want to see the list of Personas
    arcana_list_choice = input("Would you like to see a list of available Personas? (Enter y for yes, anything else for no): ")
    if arcana_list_choice == "y":   # If they choose yes, call the function
        Personas.display_arcana_list()
    else:
        print("Cool") # Debugging 

    arcana_choice = "" 
    while arcana_choice != "Finish": # Loop 2: Asks the Arcana they want to see Personas for 
        # Give them the option to view the list of Arcanas if they don't already know what they want to see
    
        arcana_choice = input("Please enter an Arcana to display Personas for (enter Finish to end): ").title()
        if arcana_choice in persona_arcanas:
            valid_arcana_choice = True
            if valid_arcana_choice:
                if arcana_choice == persona_arcanas[0]: # Fool
                    Personas.display_fool_personas()
                elif arcana_choice == persona_arcanas[1]: # Magician
                    Personas.display_magician_personas()
                elif arcana_choice == persona_arcanas[2]: # Priestess
                    Personas.display_priestess_personas()
                elif arcana_choice == persona_arcanas[3]: # Empress
                    Personas.display_empress_personas()
                elif arcana_choice == persona_arcanas[4]: # Emperor 
                    Personas.display_emperor_personas()
                elif arcana_choice == persona_arcanas[5]: # Hierophant
                    Personas.display_hierophant_personas()
                elif arcana_choice == persona_arcanas[6]: # Lovers
                    Personas.display_lovers_personas()
                elif arcana_choice == persona_arcanas[7]: # Chariot
                    Personas.display_chariot_personas()
                elif arcana_choice == persona_arcanas[8]: # Justice
                    Personas.display_justice_personas()
                elif arcana_choice == persona_arcanas[9]: # Hermit
                    Personas.display_hermit_personas()
                elif arcana_choice == persona_arcanas[10]: # Fortune
                    Personas.display_fortune_personas()
                elif arcana_choice == persona_arcanas[11]: # Strength
                    Personas.display_strength_personas()
                elif arcana_choice == persona_arcanas[12]: # Hanged Man
                    Personas.display_hanged_man_personas()
                elif arcana_choice == persona_arcanas[13]: # Death
                    Personas.display_death_personas()
                elif arcana_choice == persona_arcanas[14]: # Temperance 
                    Personas.display_temperance_personas()
                elif arcana_choice == persona_arcanas[15]: # Devil
                    Personas.display_devil_personas()
                elif arcana_choice == persona_arcanas[16]: # Tower
                    Personas.display_tower_personas()
                elif arcana_choice == persona_arcanas[17]: # Star
                    Personas.display_star_personas()
                elif arcana_choice == persona_arcanas[18]: # Moon
                    Personas.display_moon_personas()
                elif arcana_choice == persona_arcanas[19]: # Sun
                    Personas.display_sun_personas()
                elif arcana_choice == persona_arcanas[20]: # Judgement
                    Personas.display_judgement_personas()
                elif arcana_choice == persona_arcanas[21]: # Faith
                    Personas.display_faith_personas()
                elif arcana_choice == persona_arcanas[22]: # Councillor
                    Personas.display_councillor_personas()
            else:
                valid_arcana_choice = False
                print("Invalid Arcana choice.")