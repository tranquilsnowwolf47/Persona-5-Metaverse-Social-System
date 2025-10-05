# Filename: ListOfPersonas.py
# Date: Updated 10/5/25
# Author: tranquilsnowwolf
# Process:
# Make lists for each Arcana and index with for loops to display the name of each Persona based on the user's input of the Arcana. 
# A while loop will allow the user to continue if they choose to do so, letting the user see as many Personas of each Arcana they choose
# If the user doesn't enter y, the loop breaks and the program ends.


# ! Self note:
# This program shows all Personas regardless of if they've been unlocked or rnot


class Personas:
    # Clear
    def foolArcanaPersonasList():
        fool_persona_list = ["Arsene","Obariyon","Orpheus F","Orpheus F Picaro","High Pixie",
        "Izanagi","Izanagi Picaro","Orpheus","Orpheus Picaro","Legion","Ose",
        "Bugs","Crystal Skull", "Black Frost","Raoul","Vishnu","Satanael"]
        return fool_persona_list

    def display_fool_personas(persona_list_index):
        fool = Personas.foolArcanaPersonasList()
        print("\nList of Fool Arcana Personas:")
        for persona in fool:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona} ")

    # Clear
    def magicianArcanaPersonasList():
        magician_persona_List = ["Jack-o'-Lantern","Cait Sith","Jack Frost","Nekomata","Sandman",
        "Choronzon","Queen Mab","Rangda","Forneus","Surt","Futsunushi"]
        return magician_persona_List

    def display_magician_personas(persona_list_index):
        magician = Personas.magicianArcanaPersonasList()
        print("\nList of Magician Arcana Personas:")
        for persona in magician:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def priestessArcanaPersonasList():
        priestess_persona_list = ["Silky","Apsaras","Koh-i-Noor","Isis","Kikuri-Hime",
        "Sarasvati","Skadi","Scathach","Cybele"]
        return priestess_persona_list

    def display_priestess_personas(persona_list_index):
        priestess = Personas.priestessArcanaPersonasList()
        print("\nList of Priestess Arcana Personas:")
        for persona in priestess:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def empressArcanaPersonasList():
        empress_persona_list = ["Queen's Necklace","Yaksini","Lamia","Hariti","Dakini",
        "Titania","Kali","Alilat","Mother Harlot"]
        return empress_persona_list

    def display_empress_personas(persona_list_index):
        empress = Personas.empressArcanaPersonasList()
        print("\nList of Empress Arcana Personas:")
        for persona in empress:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def emperorArcanaPersonasList():
        emperor_persona_list = ["Regent","Eligor","Setanta","Thoth",
        "Barong","King Frost","Oberon","Baal","Odin"]
        return emperor_persona_list

    def display_emperor_personas(persona_list_index):
        emperor = Personas.emperorArcanaPersonasList()
        print("\nList of Emperor Arcana Personas:")
        for persona in emperor:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def hierophantArcanaPersonasList():
        hierophant_persona_list = ["Berith","Orobas","Anzu","Daisoujou","Mishaguji","Bishamonten","Kohryu"]
        return hierophant_persona_list

    def display_hierophant_personas(persona_list_index):
        hierophant = Personas.hierophantArcanaPersonasList()
        print("\nList of Hierophant Arcana Personas:")
        for persona in hierophant:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def loversArcanaPersonasList():
        lovers_persona_list = ["Pixie","Saki Mitama","Ame-no-Uzume","Leanan Sidhe","Kushinada","Narcissus",
        "Parvati","Raphael","Ishtar"]
        return lovers_persona_list

    def display_lovers_personas(persona_list_index):
        lovers = Personas.loversArcanaPersonasList()
        print("\nList of Lovers Arcana Personas:")
        for persona in lovers:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def chariotArcanaPersonasList():
        chariot_persona_list = ["Agathion","Slime","Shiki-Ouji","Kin-Ki","Ara Mitama","White Rider","Athena",
        "Athena Picaro","Cerberus","Thor","Chi You"]
        return chariot_persona_list

    def display_chariot_personas(persona_list_index):
        chariot = Personas.chariotArcanaPersonasList()
        print("\nList of Chariot Arcana Personas:")
        for persona in chariot:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def justiceArcanaPersonasList():
        justice_persona_list = ["Angel","Archangel","Principality","Power","Melchizedek","Throne",
        "Uriel","Metatron"]
        return justice_persona_list

    def display_justice_persona(persona_list_index):
        justice = Personas.justiceArcanaPersonasList()
        print("\nList of Justice Arcana Personas:")
        for persona in justice:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def hermitArcanaPersonasList():
        hermit_persona_list = ["Bicorn","Koropokkuru","Ippon-Datara","Sudama","Naga","Kurama Tengu","Arahabaki",
        "Kumbhanda","Koumokuten","Loa","Fafnir","Ongyo-Ki"]
        return hermit_persona_list
            
    def display_hermit_personas(persona_list_index):
        hermit = Personas.hermitArcanaPersonasList()
        print("\nList of Hermit Arcana Personas:")
        for persona in hermit:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def fortuneArcanaPersonaList():
        fortune_persona_list = ["Stone of Scone","Clotho","Ariadne","Lachesis","Atropos","Ariadne Picaro","Fortuna","Norn",
        "Asterius","Asterius Picaro","Lakshmi"]
        return fortune_persona_list

    def display_fortune_personas(persona_list_index):
        fortune = Personas.fortuneArcanaPersonaList()
        print("\nList of Fortune Arcana Personas:")
        for persona in fortune:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def strengthArcanaPersonaList():
        strength_persona_list = ["Kelpie","Shiisaa","Oni","Rakshasa","Orlov","Zouchouten","Valkyrie","Hanuman","Chimera","Zaou-Gongen"]
        return strength_persona_list

    def display_strength_personas(persona_list_index):
        strength = Personas.strengthArcanaPersonaList()
        print("\nList of Strength Arcana Personas:")
        for persona in strength:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def hangedManArcanaPersonaList():
        hanged_man_persona_list = ["Hua Po","Inugami","Orthrus","Take-Minakata","Emperor's Amulet","Hecatoncheires","Jatayu",
        "Moloch","Macabre","Attis"]
        return hanged_man_persona_list

    def display_hanged_man_personas(persona_list_index):
        hanged_man = Personas.hangedManArcanaPersonaList()
        print("\nList of Hanged Man Arcana Personas: ")
        for persona in hanged_man:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def deathArcanaPersonaList():
        death_persona_list = ["Mandrake","Mokoi","Matador","Nue","Pisaca","Hell Biker","Hope Diamond","Pale Rider","Chernobog",
        "Thanatos","Thanatos Picaro","Mot","Alice"]
        return death_persona_list

    def display_death_personas(persona_list_index):
        death = Personas.deathArcanaPersonaList()
        print("\nList of Death Arcana Personas:")
        for persona in death:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # Clear
    def temperanceArcanaPersonasList():
        temperance_persona_list = ["Genbu","Koppa Tengu","Makami","Jikokuten","Mithra","Byakko","Raja Naga","Gabriel",
        "Ardha"]
        return temperance_persona_list

    def display_temperance_personas(persona_list_index):
        temperance = Personas.temperanceArcanaPersonasList()
        print("\nList of Temperance Arcana Personas:")
        for persona in temperance:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    #
    def devilArcanaPersonasList():
        devil_persona_list = ["Incubus","Flauros","Andras","Lilim","Pazuzu","Baphomet","Nebiros","Belial","Beelzebub"]
        return devil_persona_list

    def display_devil_personas(persona_list_index):
        devil = Personas.devilArcanaPersonasList()
        print("\nList of Devil Arcana Personas:")
        for persona in devil:
            persona_list_index += 1
            print(f"{persona_list_index}.{persona}")

    #
    def towerArcanaPersonasList():
        tower_persona_list = ["Belphegor","Red Rider","Magatsu-Izanagi","Magatsu-Izanagi Picaro","Seth","Black Rider",
        "Mara","Yoshitsune","Mada"]
        return tower_persona_list

    def display_tower_personas(persona_list_index):
        tower = Personas.towerArcanaPersonasList()
        print("\nList of Tower Arcana Personas:")
        for persona in tower:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # 
    def starArcanaPersonasList():
        star_persona_list = ["Kodama","Fuu-Ki","Neko Shogun","Kaiwan","Garuda","Vasuki","Sraosha","Hastur","Lucifer"]
        return star_persona_list

    def display_star_personas(persona_list_index):
        star = Personas.starArcanaPersonasList()
        print("\nList of Star Arcana Personas:")
        for persona in star:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # 
    def moonArcanaPersonasList():
        moon_persona_list = ["Succubus","Onmoraki","Kaguya","Black Ooze","Sui-Ki","Kaguya Picaro","Mothman",
        "Girimehkala","Tsukiyomi","Tsukiyomi Picaro","Lilith","Byakhee","Sandalphon"]
        return moon_persona_list

    def display_moon_personas(persona_list_index):
        moon = Personas.moonArcanaPersonasList()
        print("\nList of Moon Arcana Personas:")
        for person in moon:
            persona_list_index += 1
            print(f"{persona_list_index}.{person}")

    # 
    def sunArcanaPersonasList():
        sun_persona_list = ["Suzaku","Thunderbird","Mithras","Yurlungur","Horus","Ganesha","Quetzalcoatl","Asura"]
        return sun_persona_list

    def display_sun_personas(persona_list_index):
        sun = Personas.sunArcanaPersonasList()
        print("\nList of Sun Arcana Personas:")
        for persona in sun:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # 
    def judgementArcanaPersonasList():
        judgement_persona_list = ["Anubis","Trumpeter","Yamata-no-Orochi","Abaddon","Messiah",
        "Shiva","Michael","Messiah Picaro","Satan"]
        return judgement_persona_list

    def display_judgement_personas(persona_list_index):
        judgement = Personas.judgementArcanaPersonasList()
        print("\nList of Judgement Arcana Personas:")
        for persona in judgement:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # 
    def faithArcanaPersonasList():
        faith_persona_list = ["Phoenix","Tam Lin","Unicorn","Okuninushi","Orichalcum","Atavaka","Cu Chulainn",
        "Siegfried","Maria"]
        return faith_persona_list

    def display_faith_personas(persona_list_index):
        faith = Personas.faithArcanaPersonasList()
        print("\nList of Faith Arcana Personas:")
        for persona in faith: 
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    # 
    def councillorArcanaPersonasList():
        councillor_persona_list = ["Kushi Mitama","Nigi Mitama","Decarabia","Ananta","Yatagarasu","Seiryu",
        "Dionysus","Vohu Manah"]
        return councillor_persona_list

    def display_councillor_personas(persona_list_index):
        councillor = Personas.councillorArcanaPersonasList()
        print("\nList of Counillor Arcana Personas:")
        for persona in councillor:
            persona_list_index += 1
            print(f"{persona_list_index}. {persona}")

    def space_lines():
        print()
        print("--------------------------------------------------------")


# 23 arcanas in total


class Menu:
    def display_intro():
        print("Welcome to the Persona Compendium List! ")
        print("Below are a list of Personas of various Arcanas. Please choose the Arcana you would like to see Personas for.")
        print()

    def display_option_choices():
        valid_arcanas = ["Fool","Magician","Priestess","Empress","Emperor","Hierophant",
                         "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                         "Hanged Man","Death","Temperance","Devil","Tower","Star",
                         "Moon","Sun","Judgement","Faith","Councillor"]
        print("Available Arcanas:")
        for arcana in valid_arcanas:
            print(arcana)
        print()
        return valid_arcanas


    def get_arcana():
        print("Please enter an arcana:")
        arcana_choice = str(input()).title()
        return arcana_choice
    
    def display_arcana_details():
        valid_arcanas = Menu.display_option_choices()
        valid_arcana_choice = False
        arcana_choice = Menu.get_arcana()
        if arcana_choice in valid_arcanas:
            valid_arcana_choice = True
            if valid_arcana_choice:
                if arcana_choice == valid_arcanas[0]:
                    Personas.display_fool_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[1]:
                    Personas.display_magician_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[2]:
                    Personas.display_priestess_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[3]:
                    Personas.display_empress_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[4]:
                    Personas.display_emperor_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[5]:
                    Personas.display_hierophant_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[6]:
                    Personas.display_lovers_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[7]:
                    Personas.display_chariot_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[8]:
                    Personas.display_justice_persona(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[9]:
                    Personas.display_hermit_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[10]:
                    Personas.display_fortune_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[11]:
                    Personas.display_strength_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[12]:
                    Personas.display_hanged_man_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[13]:
                    Personas.display_death_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[14]:
                    Personas.display_temperance_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[15]:
                    Personas.display_devil_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[16]:
                    Personas.display_tower_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[17]:
                    Personas.display_star_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[18]:
                    Personas.display_moon_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[19]:
                    Personas.display_sun_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[20]:
                    Personas.display_judgement_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[21]:
                    Personas.display_faith_personas(0)
                    Personas.space_lines()
                elif arcana_choice == valid_arcanas[22]:
                    Personas.display_councillor_personas(0)
                    Personas.space_lines()

                while valid_arcana_choice != False:
                    print("Would you like to see another Arcana? Please Enter y to do so.")
                    loop_prompt = input()
                    if loop_prompt == "y":
                        print()
                        Menu.display_arcana_details()
                    else:
                        print("\nTake care Trickster.")
                        valid_arcana_choice = False



Menu.display_intro()
Menu.display_option_choices()
Menu.display_arcana_details()