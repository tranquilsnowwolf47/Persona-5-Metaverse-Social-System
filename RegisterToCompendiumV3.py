# Filename: RegisterToCompendiumV3.py
# Date: 7/7/26
# Author: Aoi | shadowsnowwolf

# should take user input
# should use arrays


# It should go:
# Please enter an Persona arcana to register Personas for 
# Then it should use a for loop to display a list of Personas of that arcana
# Then it should ask which persona to register data for 
# when you choose, it will then ask for the details of that Persona
# once you get the user input, store that data into variables, format it into string format
# And then write it 


class Persona:
    persona_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant","Lovers","Chariot","Justice","Hermit",
                   "Fortune","Strength","Hanged Man", "Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","Faith","Councillor")

    fool_personas_list = ("Arsene","Obariyon","Orpheus F","Orpheus F Picaro","High Pixie",
        "Izanagi","Izanagi Picaro","Orpheus","Orpheus Picaro","Legion","Ose",
        "Bugs","Crystal Skull", "Black Frost","Raoul","Vishnu","Satanael")
    
    def display_fool_personas():
        print("\nList of Fool Personas:")
        for persona_index, persona in enumerate(Persona.fool_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
    
    magician_personas_list = ("Jack-o'-Lantern","Cait Sith","Jack Frost","Nekomata","Sandman",
        "Choronzon","Queen Mab","Rangda","Forneus","Surt","Futsunushi")
    
    def display_magician_personas():
        print("\nList of Magician Personas:")
        for persona_index, persona in enumerate(Persona.magician_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
    
    priestess_personas_list = ("Silky","Apsaras","Koh-i-Noor","Isis","Kikuri-Hime",
        "Sarasvati","Skadi","Scathach","Cybele")
    
    def display_priestess_personas():
        print("\nList of Priestess Personas:")
        for persona_index, persona in enumerate(Persona.priestess_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
    
    empress_personas_list = ("Queen's Necklace","Yaksini","Lamia","Hariti","Dakini",
        "Titania","Kali","Alilat","Mother Harlot")
    
    def display_empress_personas():
        print("\nList of Empress Personas:")
        for persona_index, persona in enumerate(Persona.empress_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
    
    emperor_personas_list = ("Regent","Eligor","Setanta","Thoth",
        "Barong","King Frost","Oberon","Baal","Odin")
    
    def display_emperor_personas():
        print("\nList of Emperor Personas:")
        for persona_index, personas in enumerate(Persona.emperor_personas_list, start=1):
            print(f"{persona_index}. {personas}")
        print("------------------------------------------------------------------------")
    
    hierophant_personas_list = ("Berith","Orobas","Anzu","Daisoujou","Mishaguji","Bishamonten","Kohryu")
    def display_hierophant_personas():
        print("\nList of Hierophant Personas:")
        for persona_index, persona in enumerate(Persona.hierophant_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    lovers_personas_list = ("Pixie","Saki Mitama","Ame-no-Uzume","Leanan Sidhe","Kushinada","Narcissus",
            "Parvati","Raphael","Ishtar")
    
    def display_lovers_personas():
        print("\nList of Lovers Personas:")
        for persona_index, persona in enumerate(Persona.lovers_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    chariot_personas_list = ("Agathion","Slime","Shiki-Ouji","Kin-Ki","Ara Mitama","White Rider","Athena",
            "Athena Picaro","Cerberus","Thor","Chi You")
    
    def display_chariot_personas():
        print("\nList of Chariot Personas:")
        for persona_index, persona in enumerate(Persona.chariot_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    justice_personas_list = ("Angel","Archangel","Principality","Power","Melchizedek","Throne",
            "Uriel","Metatron")
    
    def display_justice_personas():
        print("\nList of Justice Personas:")
        for persona_index, persona in enumerate(Persona.justice_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    hermit_personas_list = ("Bicorn","Koropokkuru","Ippon-Datara","Sudama","Naga","Kurama Tengu","Arahabaki",
            "Kumbhanda","Koumokuten","Loa","Fafnir","Ongyo-Ki")
    
    def display_hermit_personas():
        print("\nList of Hermit Personas:")
        for persona_index, persona in enumerate(Persona.hermit_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    fortune_personas_list = ("Stone of Scone","Clotho","Ariadne","Lachesis","Atropos","Ariadne Picaro","Fortuna","Norn",
            "Asterius","Asterius Picaro","Lakshmi")
    
    def display_fortune_personas():
        print("\nList of Fortune Personas:")
        for persona_index, persona in enumerate(Persona.fortune_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    strength_personas_list = ("Kelpie","Shiisaa","Oni","Rakshasa","Orlov","Zouchouten","Valkyrie","Hanuman","Chimera","Zaou-Gongen")

    def display_strength_personas():
        print("\nList of Strength Personas:")
        for persona_index, persona in enumerate(Persona.strength_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    hanged_man_personas_list = ("Hua Po","Inugami","Orthrus","Take-Minakata","Emperor's Amulet","Hecatoncheires","Jatayu",
            "Moloch","Macabre","Attis")
    
    def display_hanged_man_personas():
        print("\nList of Hanged Man Personas:")
        for persona_index, persona in enumerate(Persona.hanged_man_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    death_personas_list = ("Mandrake","Mokoi","Matador","Nue","Pisaca","Hell Biker","Hope Diamond","Pale Rider","Chernobog",
            "Thanatos","Thanatos Picaro","Mot","Alice")
    
    def display_death_personas():
        print("\nList of Death Personas:")
        for persona_index, persona in enumerate(Persona.death_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    temperance_personas_list = ("Genbu","Koppa Tengu","Makami","Jikokuten","Mithra","Byakko","Raja Naga","Gabriel",
            "Ardha")
    
    def display_temperance_personas():
        print("\nList of Temperance Personas:") 
        for persona_index, persona in enumerate(Persona.temperance_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    devil_personas_list = ("Incubus","Flauros","Andras","Lilim","Pazuzu","Baphomet","Nebiros","Belial","Beelzebub")

    def display_devil_personas():
        print("\nList of Devil Personas: ")
        for persona_index, persona in enumerate(Persona.devil_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    tower_personas_list = ("Belphegor","Red Rider","Magatsu-Izanagi","Magatsu-Izanagi Picaro","Seth","Black Rider",
        "Mara","Yoshitsune","Mada")

    def display_tower_personas():
            print("\nList of Tower Personas:")
            for persona_index, persona in enumerate(Persona.tower_personas_list, start=1):
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")


    star_personas_list = ("Kodama","Fuu-Ki","Neko Shogun","Kaiwan","Garuda","Vasuki","Sraosha","Hastur","Lucifer")

    def display_star_personas():
        print("\nList of Star Personas:")
        for persona_index, persona in enumerate(Persona.star_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    moon_personas_list = ("Succubus","Onmoraki","Kaguya","Black Ooze","Sui-Ki","Kaguya Picaro","Mothman",
            "Girimehkala","Tsukiyomi","Tsukiyomi Picaro","Lilith","Byakhee","Sandalphon")

    def display_moon_personas():
        print("\nList of Moon Personas:")
        for persona_index, persona in enumerate(Persona.moon_personas_list, start=1):
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")

    sun_personas_list = ("Suzaku","Thunderbird","Mithras","Yurlungur","Horus","Ganesha","Quetzalcoatl","Asura")

    def display_sun_personas():
        print("\nList of Sun Personas:")
        for persona_index, personas in enumerate(Persona.sun_personas_list, start=1):
            print(f"{persona_index}. {personas}")
        print("------------------------------------------------------------------------")

    judgement_personas_list = ("Anubis","Trumpeter","Yamata-no-Orochi","Abaddon","Messiah",
            "Shiva","Michael","Messiah Picaro","Satan")

    def display_judgement_personas():
            print("\nList of Judgement Personas:")
            for persona_index, persona in enumerate(Persona.judgement_personas_list, start=1):
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")

    faith_personas_list = ("Phoenix","Tam Lin","Unicorn","Okuninushi","Orichalcum","Atavaka","Cu Chulainn",
            "Siegfried","Maria")

    def display_faith_personas():
            print("\nList of Faith Personas:")
            for persona_index, persona in enumerate(Persona.faith_personas_list, start=1):
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")

    councillor_personas_list = ("Kushi Mitama","Nigi Mitama","Decarabia","Ananta","Yatagarasu","Seiryu",
                "Dionysus","Vohu Manah")

    def display_councillor_personas():
            print("\nList of Councillor Personas:")
            for persona_index, persona in enumerate(Persona.councillor_personas_list, start=1):
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")
    
def get_persona_arcana():
    print("Persona Arcanas:")
    print("------------------------------------------------")
    for arcana_index, arcana in enumerate(Persona.persona_arcanas,start=1):
        print(f"{arcana_index}. {arcana}")
    arcana_choice = int(input("\nPlease enter the Arcana of the Persona you'd like to register (1-23): "))
    return arcana_choice

selected_personas_arcana = ""


arcana_choice = get_persona_arcana()
#arcana_index = get_persona_arcana[1]

def get_persona_choice():
    persona_choice = int(input(f"Please enter a Persona (1-x): "))

if arcana_choice == 1:
    selected_persona_arcana = f"{persona.arcanas[]}"
    Persona.display_fool_personas()
    x = int(input("Enter a Persona to register (1-y)":
elif arcana_choice == 2:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_magician_personas()
elif arcana_choice == 3:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_priestess_personas()
elif arcana_choice == 4:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_empress_personas()
elif arcana_choice == 5:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_emperor_personas()
elif arcana_choice == 6:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_hierophant_personas()
elif arcana_choice == 7:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_lovers_personas()
elif arcana_choice == 8:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_chariot_personas()
elif arcana_choice == 9:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Personas.display_justice_personas()
elif arcana_choice == 10:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_hermit_personas()
elif arcana_choice == 11:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_fortune_personas()
elif arcana_choice == 12:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_strength_personas()
elif arcana_choice == 13:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_hanged_man_personas()
elif arcana_choice == 14:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_death_personas()
elif arcana_choice == 15:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_temperance_personas()
elif arcana_choice == 16:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_devil_personas()
elif arcana_choice == 17:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_tower_personas()
elif arcana_choice == 18:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_star_personas()
elif arcana_choice == 19:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_moon_personas()
elif arcana_choice == 20:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_sun_personas()
elif arcana_choice == 21:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_judgement_personas()
elif arcana_choice == 22:
        selected_persona_arcana = f"{persona.arcanas[]}"

    Persona.display_faith_personas()
elif arcana_choice == 23:
      selected_persona_arcana = f"{persona.arcanas[]}"
    Persona.display_councillor_personas()
    
