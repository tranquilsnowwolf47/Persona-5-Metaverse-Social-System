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
    
    magician_personas_list = ("Jack-o'-Lantern","Cait Sith","Jack Frost","Nekomata","Sandman",
        "Choronzon","Queen Mab","Rangda","Forneus","Surt","Futsunushi")
    
    priestess_personas_list = ("Silky","Apsaras","Koh-i-Noor","Isis","Kikuri-Hime",
        "Sarasvati","Skadi","Scathach","Cybele")
    
    empress_personas_list = ("Queen's Necklace","Yaksini","Lamia","Hariti","Dakini",
        "Titania","Kali","Alilat","Mother Harlot")
    
    emperor_personas_list = ("Regent","Eligor","Setanta","Thoth",
        "Barong","King Frost","Oberon","Baal","Odin")
    
    hierophant_personas_list = ("Berith","Orobas","Anzu","Daisoujou","Mishaguji","Bishamonten","Kohryu")

    lovers_personas_list = ("Pixie","Saki Mitama","Ame-no-Uzume","Leanan Sidhe","Kushinada","Narcissus",
            "Parvati","Raphael","Ishtar")

    chariot_personas_list = ("Agathion","Slime","Shiki-Ouji","Kin-Ki","Ara Mitama","White Rider","Athena",
            "Athena Picaro","Cerberus","Thor","Chi You")

    justice_personas_list = ("Angel","Archangel","Principality","Power","Melchizedek","Throne",
            "Uriel","Metatron")

    hermit_personas_list = ("Bicorn","Koropokkuru","Ippon-Datara","Sudama","Naga","Kurama Tengu","Arahabaki",
            "Kumbhanda","Koumokuten","Loa","Fafnir","Ongyo-Ki")

    fortune_personas_list = ("Stone of Scone","Clotho","Ariadne","Lachesis","Atropos","Ariadne Picaro","Fortuna","Norn",
            "Asterius","Asterius Picaro","Lakshmi")

    strength_personas_list = ("Kelpie","Shiisaa","Oni","Rakshasa","Orlov","Zouchouten","Valkyrie","Hanuman","Chimera","Zaou-Gongen")

    hanged_man_personas_list = ("Hua Po","Inugami","Orthrus","Take-Minakata","Emperor's Amulet","Hecatoncheires","Jatayu",
            "Moloch","Macabre","Attis")

    death_personas_list = ("Mandrake","Mokoi","Matador","Nue","Pisaca","Hell Biker","Hope Diamond","Pale Rider","Chernobog",
            "Thanatos","Thanatos Picaro","Mot","Alice")

    temperance_personas_list = ("Genbu","Koppa Tengu","Makami","Jikokuten","Mithra","Byakko","Raja Naga","Gabriel",
            "Ardha")
    devil_personas_list = ("Incubus","Flauros","Andras","Lilim","Pazuzu","Baphomet","Nebiros","Belial","Beelzebub")

    tower_personas_list = ("Belphegor","Red Rider","Magatsu-Izanagi","Magatsu-Izanagi Picaro","Seth","Black Rider",
        "Mara","Yoshitsune","Mada")

    star_personas_list = ("Kodama","Fuu-Ki","Neko Shogun","Kaiwan","Garuda","Vasuki","Sraosha","Hastur","Lucifer")

    moon_personas_list = ("Succubus","Onmoraki","Kaguya","Black Ooze","Sui-Ki","Kaguya Picaro","Mothman",
            "Girimehkala","Tsukiyomi","Tsukiyomi Picaro","Lilith","Byakhee","Sandalphon")

    sun_personas_list = ("Suzaku","Thunderbird","Mithras","Yurlungur","Horus","Ganesha","Quetzalcoatl","Asura")

    judgement_personas_list = ("Anubis","Trumpeter","Yamata-no-Orochi","Abaddon","Messiah",
            "Shiva","Michael","Messiah Picaro","Satan")

    faith_personas_list = ("Phoenix","Tam Lin","Unicorn","Okuninushi","Orichalcum","Atavaka","Cu Chulainn",
            "Siegfried","Maria")

    councillor_personas_list = ("Kushi Mitama","Nigi Mitama","Decarabia","Ananta","Yatagarasu","Seiryu",
            "Dionysus","Vohu Manah")
    
def get_persona_arcana():
    print("Persona Arcanas:")
    print("------------------------------------------------")
    for arcana_index, arcana in enumerate(Persona.persona_arcanas,start=1):
        print(f"{arcana_index}. {arcana}")

    arcana_choice = int(input("\nPlease enter the Arcana of the Persona you'd like to register (1-23): "))
    if arcana_choice == 1:
        pass
    elif arcana_choice == 2:
        pass
    elif arcana_choice == 3:
        pass
    elif arcana_choice == 4:
        pass
    elif arcana_choice == 5:
        pass
    elif arcana_choice == 6:
        pass 
    


get_persona_arcana()
