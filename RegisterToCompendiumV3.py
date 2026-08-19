# Filename: RegisterToCompendiumV3.py
# Date: 7/7/26
# Author: Aoi | shadowsnowwolf

# should take user input
# should use arrays

# Bug: 
# Fix the line spacing to be even and consistent


# It should go:
# Please enter an Persona arcana to register Personas for  | clear
# Then it should use a for loop to display a list of Personas of that arcana | clear
# Then it should ask which persona to register data for | clear
# when you choose, it will then ask for the details of that Persona
# once you get the user input, store that data into variables, format it into string format
# And then write it 

class Compendium:
    def __init__(self, name, arcana, level,
                     st, ma, en, ag, lu,
                     skill1, skill2, 
                     skill3, skill4,
                     skill5, skill6,
                     skill7, skill8):
            # Basic info attribtues
            self.name = name
            self.arcana = arcana
            self.level = level
    
            # Combat stat attributes
            self.st =  st
            self.ma = ma
            self.en = en
            self.ag = ag
            self.lu = lu
    
            # Skill attributes
            self.skill1 = skill1
            self.skill2 = skill2
            self.skill3 = skill3
            self.skill4 = skill4
            self.skill5 = skill5
            self.skill6 = skill6
            self.skill7 = skill7
            self.skill8 = skill8


    # Gets input from the user on the Persona they want to register
    def get_persona_info(self):
        print("Persona to Register:")
        print("--------------------------------")
        print(f"{self.name} ({self.arcana})")
        print("--------------------------------\n\n")
    
        try:
            level = int(input(f"Enter {self.name}'s level: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            st = int(input(f"Enter {self.name}'s St stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            ma = int(input(f"Enter {self.name}'s Ma stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            en = int(input(f"Enter {self.name}'s En stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            ag = int(input(f"Enter {self.name}'s Ag stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            lu = int(input(f"Enter {self.name}'s Lu stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        
        print(f"\nPlease enter {self.name} skills in the following format: ")
        print("(Skill Name) (Damage Grade Element) | Ex: Data Hex (Heavy Curse)")
        
        try:
            skill1 = input("\nEnter skill 1: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill2 = input("Enter skill 2: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill3 = input("Enter skill 3: W")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill4 = input("Enter skill 4: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill5 = input("Enter skill 5: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill6 = input("Enter skill 6: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill7 = input("Enter skill 7: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill8 = input("Enter skill 8: ")
        except ValueError:
            print("Please enter a valid string.")
        
        return level, st, ma, en, ag, lu, skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8



    def format_persona_log_entry(self):
        return f"""\n\nPersona Registered: \n------------------------
Name: {self.name}
Arcana: {self.arcana}
Level: {self.level}\n
Stats: \n------------------------
St: {self.st}
Ma: {self.ma}
En: {self.en}
Ag: {self.ag}
Lu: {self.lu}

Skills: \n------------------------
1. {self.skill1}
2. {self.skill2}
3. {self.skill3}
4. {self.skill4}
5. {self.skill5}
6. {self.skill6}
7. {self.skill7}
8. {self.skill8}\n"""



class Persona(Compendium):
    persona_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant","Lovers","Chariot","Justice","Hermit",
                   "Fortune","Strength","Hanged Man", "Death","Temperance","Devil","Tower","Star","Moon","Sun","Judgement","Faith","Councillor")

    fool_personas_list = ("Arsene","Obariyon","Orpheus F","Orpheus F Picaro","High Pixie",
        "Izanagi","Izanagi Picaro","Orpheus","Orpheus Picaro","Legion","Ose",
        "Bugs","Crystal Skull", "Black Frost","Raoul","Vishnu","Satanael")
    
    def display_fool_personas(ending_range=0):
        print("\nList of Fool Personas:")
        for persona_index, persona in enumerate(Persona.fool_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range
    
    magician_personas_list = ("Jack-o'-Lantern","Cait Sith","Jack Frost","Nekomata","Sandman",
        "Choronzon","Queen Mab","Rangda","Forneus","Surt","Futsunushi")
    
    def display_magician_personas(ending_range=0):
        print("\nList of Magician Personas:")
        for persona_index, persona in enumerate(Persona.magician_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range
    
    priestess_personas_list = ("Silky","Apsaras","Koh-i-Noor","Isis","Kikuri-Hime",
        "Sarasvati","Skadi","Scathach","Cybele")
    
    def display_priestess_personas(ending_range=0):
        print("\nList of Priestess Personas:")
        for persona_index, persona in enumerate(Persona.priestess_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range
    
    empress_personas_list = ("Queen's Necklace","Yaksini","Lamia","Hariti","Dakini",
        "Titania","Kali","Alilat","Mother Harlot")
    
    def display_empress_personas(ending_range=0):
        print("\nList of Empress Personas:")
        for persona_index, persona in enumerate(Persona.empress_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range
    
    emperor_personas_list = ("Regent","Eligor","Setanta","Thoth",
        "Barong","King Frost","Oberon","Baal","Odin")
    
    def display_emperor_personas(ending_range=0):
        print("\nList of Emperor Personas:")
        for persona_index, personas in enumerate(Persona.emperor_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {personas}")
        print("------------------------------------------------------------------------")
        return ending_range
    
    hierophant_personas_list = ("Berith","Orobas","Anzu","Daisoujou","Mishaguji","Bishamonten","Kohryu")
    def display_hierophant_personas(ending_range=0):
        print("\nList of Hierophant Personas:")
        for persona_index, persona in enumerate(Persona.hierophant_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    lovers_personas_list = ("Pixie","Saki Mitama","Ame-no-Uzume","Leanan Sidhe","Kushinada","Narcissus",
            "Parvati","Raphael","Ishtar")
    
    def display_lovers_personas(ending_range=0):
        print("\nList of Lovers Personas:")
        for persona_index, persona in enumerate(Persona.lovers_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    chariot_personas_list = ("Agathion","Slime","Shiki-Ouji","Kin-Ki","Ara Mitama","White Rider","Athena",
            "Athena Picaro","Cerberus","Thor","Chi You")
    
    def display_chariot_personas(ending_range=0):
        print("\nList of Chariot Personas:")
        for persona_index, persona in enumerate(Persona.chariot_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    justice_personas_list = ("Angel","Archangel","Principality","Power","Melchizedek","Throne",
            "Uriel","Metatron")
    
    def display_justice_personas(ending_range=0):
        print("\nList of Justice Personas:")
        for persona_index, persona in enumerate(Persona.justice_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    hermit_personas_list = ("Bicorn","Koropokkuru","Ippon-Datara","Sudama","Naga","Kurama Tengu","Arahabaki",
            "Kumbhanda","Koumokuten","Loa","Fafnir","Ongyo-Ki")
    
    def display_hermit_personas(ending_range=0):
        print("\nList of Hermit Personas:")
        for persona_index, persona in enumerate(Persona.hermit_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    fortune_personas_list = ("Stone of Scone","Clotho","Ariadne","Lachesis","Atropos","Ariadne Picaro","Fortuna","Norn",
            "Asterius","Asterius Picaro","Lakshmi")
    
    def display_fortune_personas(ending_range=0):
        print("\nList of Fortune Personas:")
        for persona_index, persona in enumerate(Persona.fortune_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    strength_personas_list = ("Kelpie","Shiisaa","Oni","Rakshasa","Orlov","Zouchouten","Valkyrie","Hanuman","Chimera","Zaou-Gongen")

    def display_strength_personas(ending_range=0):
        print("\nList of Strength Personas:")
        for persona_index, persona in enumerate(Persona.strength_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    hanged_man_personas_list = ("Hua Po","Inugami","Orthrus","Take-Minakata","Emperor's Amulet","Hecatoncheires","Jatayu",
            "Moloch","Macabre","Attis")
    
    def display_hanged_man_personas(ending_range=0):
        print("\nList of Hanged Man Personas:")
        for persona_index, persona in enumerate(Persona.hanged_man_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    death_personas_list = ("Mandrake","Mokoi","Matador","Nue","Pisaca","Hell Biker","Hope Diamond","Pale Rider","Chernobog",
            "Thanatos","Thanatos Picaro","Mot","Alice")
    
    def display_death_personas(ending_range=0):
        print("\nList of Death Personas:")
        for persona_index, persona in enumerate(Persona.death_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    temperance_personas_list = ("Genbu","Koppa Tengu","Makami","Jikokuten","Mithra","Byakko","Raja Naga","Gabriel",
            "Ardha")
    
    def display_temperance_personas(ending_range=0):
        print("\nList of Temperance Personas:") 
        for persona_index, persona in enumerate(Persona.temperance_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    devil_personas_list = ("Incubus","Flauros","Andras","Lilim","Pazuzu","Baphomet","Nebiros","Belial","Beelzebub")

    def display_devil_personas(ending_range=0):
        print("\nList of Devil Personas: ")
        for persona_index, persona in enumerate(Persona.devil_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    tower_personas_list = ("Belphegor","Red Rider","Magatsu-Izanagi","Magatsu-Izanagi Picaro","Seth","Black Rider",
        "Mara","Yoshitsune","Mada")

    def display_tower_personas(ending_range=0):
            print("\nList of Tower Personas:")
            for persona_index, persona in enumerate(Persona.tower_personas_list, start=1):
                ending_range += 1
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")
            return ending_range


    star_personas_list = ("Kodama","Fuu-Ki","Neko Shogun","Kaiwan","Garuda","Vasuki","Sraosha","Hastur","Lucifer")

    def display_star_personas(ending_range=0):
        print("\nList of Star Personas:")
        for persona_index, persona in enumerate(Persona.star_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    moon_personas_list = ("Succubus","Onmoraki","Kaguya","Black Ooze","Sui-Ki","Kaguya Picaro","Mothman",
            "Girimehkala","Tsukiyomi","Tsukiyomi Picaro","Lilith","Byakhee","Sandalphon")

    def display_moon_personas(ending_range=0):
        print("\nList of Moon Personas:")
        for persona_index, persona in enumerate(Persona.moon_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {persona}")
        print("------------------------------------------------------------------------")
        return ending_range

    sun_personas_list = ("Suzaku","Thunderbird","Mithras","Yurlungur","Horus","Ganesha","Quetzalcoatl","Asura")

    def display_sun_personas(ending_range=0):
        print("\nList of Sun Personas:")
        for persona_index, personas in enumerate(Persona.sun_personas_list, start=1):
            ending_range += 1
            print(f"{persona_index}. {personas}")
        print("------------------------------------------------------------------------")
        return ending_range

    judgement_personas_list = ("Anubis","Trumpeter","Yamata-no-Orochi","Abaddon","Messiah",
            "Shiva","Michael","Messiah Picaro","Satan")

    def display_judgement_personas(ending_range=0):
            print("\nList of Judgement Personas:")
            for persona_index, persona in enumerate(Persona.judgement_personas_list, start=1):
                ending_range += 1
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")
            return ending_range

    faith_personas_list = ("Phoenix","Tam Lin","Unicorn","Okuninushi","Orichalcum","Atavaka","Cu Chulainn",
            "Siegfried","Maria")

    def display_faith_personas(ending_range=0):
            print("\nList of Faith Personas:")
            for persona_index, persona in enumerate(Persona.faith_personas_list, start=1):
                ending_range += 1
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")
            return ending_range

    councillor_personas_list = ("Kushi Mitama","Nigi Mitama","Decarabia","Ananta","Yatagarasu","Seiryu",
                "Dionysus","Vohu Manah")

    def display_councillor_personas(ending_range=0):
            print("\nList of Councillor Personas:")
            for persona_index, persona in enumerate(Persona.councillor_personas_list, start=1):
                ending_range += 1
                print(f"{persona_index}. {persona}")
            print("------------------------------------------------------------------------")
            return ending_range

class FoolPersonas(Persona):
    pass

class MagicianPersonas(Persona):
    pass

class PriestessPersonas(Persona):
    pass

class EmpressPersonas(Persona):
    pass

class EmperorPersonas(Persona):
    pass

class HierophantPersonas(Persona):
    pass

class LoversPersonas(Persona):
    pass

class ChariotPersonas(Persona):
    pass

class JusticePersonas(Persona):
    pass

class HermitPersonas(Persona):
    pass

class FortunePersonas(Persona):
    pass

class StrengthPersonas(Persona):
    pass

class HangedManPersonas(Persona):
    pass

class DeathPersonas(Persona):
    pass

class TemperancePersonas(Persona):
    pass

class DevilPersonas(Persona):
    pass

class TowerPersonas(Persona):
    pass

class StarPersonas(Persona):
    pass

class MoonPersonas(Persona):
    pass

class SunPersonas(Persona):
    pass

class JudgementPersonas(Persona):
    pass

class FaithPersonas(Persona):
    pass

class CouncillorPersonas(Persona):
    pass

#----------------------------------------------------------

# Objects
# Fool Personas:
# ------------------------------------------------------------------------------------
arsene = FoolPersonas("Arsene", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

obariyon = FoolPersonas("Obariyon", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

orpheus_f = FoolPersonas("Orpheus F", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

orpheus_f_picaro = FoolPersonas("Orpheus F Picaro", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

high_pixie = FoolPersonas("High Pixie", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

izanagi = FoolPersonas("Izanagi", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

izanagi_picaro = FoolPersonas("Izanagi Picaro", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")
                              
orpheus = FoolPersonas("Orpheus", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

orpheus_picaro = FoolPersonas("Orpheus Picaro", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

legion = FoolPersonas("Legion", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

ose = FoolPersonas("Ose", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

bugs = FoolPersonas("Bugs", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

crystal_skull = FoolPersonas("Crystal Skull", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

black_frost =  FoolPersonas("Black Frost", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

raoul = FoolPersonas("Raoul", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

vishnu = FoolPersonas("Vishnu", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

satanael = FoolPersonas("Satanael", f"{Persona.persona_arcanas[0]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

fool_personas = (arsene, obariyon, orpheus_f, orpheus_f_picaro, high_pixie, izanagi, izanagi_picaro,
                 orpheus, orpheus_picaro, legion, ose, bugs, crystal_skull, black_frost, raoul, vishnu,
                 satanael)

# Magician Personas:
# ------------------------------------------------------------------------------------
jack_o_lantern = MagicianPersonas("Jack-o'-Lantern", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

cait_sith = MagicianPersonas("Cait Sith", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

jack_frost = MagicianPersonas("Jack Frost", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

nekomata = MagicianPersonas("Nekomata", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

sandman = MagicianPersonas("Sandman", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

choronzon = MagicianPersonas("Chronzon", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

queen_mab = MagicianPersonas("Queen Mab", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

rangda = MagicianPersonas("Rangda", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

forneus = MagicianPersonas("Forneus", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

surt = MagicianPersonas("Surt", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

futsunushi = MagicianPersonas("Futsunushi", f"{Persona.persona_arcanas[1]}",1,
                    1,1,1,1,1,
                    "","","","",
                    "","","","")

magician_personas = (jack_o_lantern, cait_sith, jack_frost, nekomata, sandman,
                     choronzon, queen_mab, rangda, forneus, surt, futsunushi)


# Priestess Personas:
# ------------------------------------------------------------------------------------
silky = PriestessPersonas("Silky", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

apsaras = PriestessPersonas("Apsaras", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kohi_i_noor = PriestessPersonas("Kohi-i-Noor", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

isis = PriestessPersonas("Isis", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kikuri_hime = PriestessPersonas("Kikuri-Hime", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

sarasvati = PriestessPersonas("Sarasvati", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

skadi = PriestessPersonas("Skadi", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

scathach = PriestessPersonas("Scathach", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

cybele = PriestessPersonas("Cybele", f"{Persona.persona_arcanas[2]}",1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")


priestess_personas = (silky, apsaras, kohi_i_noor, isis, kikuri_hime, sarasvati,
                      skadi, scathach, cybele)

# Empress Personas:
# ------------------------------------------------------------------------------------
queens_necklace = EmpressPersonas("Queen's Necklace", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")
yaksini = EmpressPersonas("Yaksini", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")
lamia = EmpressPersonas("Lamia", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")
hariti = EmpressPersonas("Hariti", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

dakini = EmpressPersonas("Dakini", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

titania =  EmpressPersonas("Titania", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kali =  EmpressPersonas("Kali", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

alilat =  EmpressPersonas("Alilat", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

mother_harlot = EmpressPersonas("Mother Harlot", f"{Persona.persona_arcanas[3]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

empress_personas = (queens_necklace, yaksini, lamia, hariti, dakini, titania, kali, alilat, mother_harlot)

# Emperor Personas:
# ------------------------------------------------------------------------------------
regent = EmperorPersonas("Regent", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

eligor = EmperorPersonas("Eligor", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

setanta = EmperorPersonas("Setanta", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

thoth = EmperorPersonas("Thoth", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

barong = EmperorPersonas("Barong", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

king_frost = EmperorPersonas("King Frost", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

oberon = EmperorPersonas("Oberon", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

baal = EmperorPersonas("Baal", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

odin = EmperorPersonas("Odin", f"{Persona.persona_arcanas[4]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

emperor_personas = (eligor, regent, setanta, thoth, barong, king_frost, oberon, baal, odin)

# Hierophant Personas:
# ------------------------------------------------------------------------------------
berith = HierophantPersonas("Berith", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

orobas = HierophantPersonas("Orobas", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

anzu = HierophantPersonas("Anzu", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

daisoujou = HierophantPersonas("Daisoujou", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

mishaguji = HierophantPersonas("Mishaguji", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

bishamonten = HierophantPersonas("Bishamonten", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kohryu = HierophantPersonas("Kohryu", f"{Persona.persona_arcanas[5]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

hierophant_personas = (berith, orobas, anzu, daisoujou, mishaguji, bishamonten, 
                       kohryu)

# Lovers Personas:
# ------------------------------------------------------------------------------------
pixie = LoversPersonas("Pixie", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

saki_mitama = LoversPersonas("Saki Mitama", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

ame_no_uzume = LoversPersonas("Ame-no-Uzume", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

leanan_sidhe = LoversPersonas("Leanan Sidhe", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kushinada = LoversPersonas("Kushinada", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

narcissus = LoversPersonas("Narcissus", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

parvati = LoversPersonas("Parvati", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

ralphael = LoversPersonas("Ralphael", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

ishtar = LoversPersonas("Ishtar", f"{Persona.persona_arcanas[6]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")


lovers_personas = (pixie, saki_mitama, ame_no_uzume, leanan_sidhe, kushinada,
                   narcissus, parvati, ralphael, ishtar)


# Chariot Personas:
# ------------------------------------------------------------------------------------
agation = ChariotPersonas("Agathion", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

slime = ChariotPersonas("Slime", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

shiki_ouji = ChariotPersonas("Shiki-Ouji", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kin_ki = ChariotPersonas("Kin-Ki", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

ara_mitama = ChariotPersonas("Ara Mitama", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

white_rider = ChariotPersonas("White Rider", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

athena = ChariotPersonas("Athena", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

athena_picaro = ChariotPersonas("Athena Picaro", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

cerberus = ChariotPersonas("Cerberus", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

thor = ChariotPersonas("Thor", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

chi_you = ChariotPersonas("Chi You", f"{Persona.persona_arcanas[7]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

chariot_personas = (agation, slime, shiki_ouji, kin_ki, ara_mitama, white_rider, athena, 
                   cerberus, thor, chi_you)

# Justice Personas:
# ------------------------------------------------------------------------------------
angel = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

archangel = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

principality = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

power = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

melchizedek = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

throne = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

uriel = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

metatron = JusticePersonas("", f"{Persona.persona_arcanas[8]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

justice_personas = (angel, archangel, principality, power, melchizedek, 
                    throne, uriel, metatron)

# Hermit Personas:
# ------------------------------------------------------------------------------------
bicorn = HermitPersonas("", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

koropokkuru = HermitPersonas("Koropokkuru", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")
                    
ippon_datara = HermitPersonas("Ippon-Datara", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

sudama = HermitPersonas("Sudama", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

naga = HermitPersonas("Naga", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kurama_tengu = HermitPersonas("Kurama Tengu", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

arahabaki = HermitPersonas("Arahabaki", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

kumbhanda = HermitPersonas("Kumbhanda", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

koumokuten = HermitPersonas("Koumokuten", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

loa = HermitPersonas("Loa", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

fafnir = HermitPersonas("Fafnir", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

ongyo_ki = HermitPersonas("Ongyo-Ki", f"{Persona.persona_arcanas[9]}", 1,
                        1,1,1,1,1,
                        "","","","",
                        "","","","")

hermit_personas = (bicorn, koropokkuru, ippon_datara, sudama, naga, kurama_tengu, arahabaki,
                   kumbhanda, koumokuten, loa, fafnir, ongyo_ki)

# Fortune Personas:
# ------------------------------------------------------------------------------------
stone_of_scone = FortunePersonas("Stone of Scone", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

clotho = FortunePersonas("Clotho", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")
                         
ariadne  = FortunePersonas("Ariadne", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")
                           
lachesis = FortunePersonas("Lachesis", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")
                           
atropos = FortunePersonas("Atropos", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

ariadne_picaro = FortunePersonas("Ariadne Picaro", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

fortuna = FortunePersonas("Fortuna", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

norn = FortunePersonas("Norn", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

asterius = FortunePersonas("Asterius", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

asterius_picaro = FortunePersonas("Asterius Picaro", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

lakshmi = FortunePersonas("Lakshmi", f"{Persona.persona_arcanas[10]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

fortune_personas = (stone_of_scone, clotho, ariadne, lachesis, atropos, ariadne_picaro, fortuna,
                    norn, asterius, asterius_picaro, lakshmi)

# Strength Personas:
# ------------------------------------------------------------------------------------
kelpie = StrengthPersonas("Kelpie", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

shiisa = StrengthPersonas("Shiisaa", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

oni = StrengthPersonas("Oni", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

rakshasa = StrengthPersonas("Rakshasa", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

orlov = StrengthPersonas("Orlov", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

zouchouten = StrengthPersonas("Zouchouten", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

valkyrie = StrengthPersonas("", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

hanuman = StrengthPersonas("", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

chimera = StrengthPersonas("", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

zaou_gongen = StrengthPersonas("", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")


strength_personas = (kelpie, shiisa, oni, rakshasa, orlov, zouchouten, valkyrie,
                     hanuman, chimera, zaou_gongen)

# Hanged Man Personas:
# ------------------------------------------------------------------------------------
hua_po = HangedManPersonas("Hua Po", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

inugami = HangedManPersonas("Inugami", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

orthrus = HangedManPersonas("Orthrus", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

take_minakata = HangedManPersonas("Take-Minakata", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

emperors_amulet = HangedManPersonas("Emperor's Amulet", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

hecatoncheires = HangedManPersonas("Hecatoncheires", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","") 

jatayu = HangedManPersonas("Jatayu", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")      

moloch = HangedManPersonas("Moloch", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")      

macabre = HangedManPersonas("", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")      

attis = HangedManPersonas("", f"{Persona.persona_arcanas[12]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")                                

hanged_man_personas = (hua_po, inugami, orthrus, take_minakata, emperors_amulet, 
                       hecatoncheires, jatayu, moloch, macabre, attis)

# Death Personas:
# ------------------------------------------------------------------------------------
mandrake = DeathPersonas("Mandrake", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mokoi = DeathPersonas("Mokoi", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

matador = DeathPersonas("Matador", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")
 
nue = DeathPersonas("Nue", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

pisaca = DeathPersonas("Pisaca", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

hell_biker = DeathPersonas("Hell Biker", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

hope_diamond = DeathPersonas("Hope Diamond", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

pale_rider = DeathPersonas("Pale Rider", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

chernobog = DeathPersonas("Chernobog", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

thanatos = DeathPersonas("Thanatos", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

thanatos_picaro = DeathPersonas("Thanatos Picaro", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mot = DeathPersonas("Mot", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

alice = DeathPersonas("Alice", f"{Persona.persona_arcanas[13]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

death_personas = (mandrake, mokoi, matador, nue, pisaca, hell_biker, hope_diamond, pale_rider,
                  chernobog, thanatos, thanatos_picaro, mot, alice)

# Temperance Personas:
# ------------------------------------------------------------------------------------
genbu = TemperancePersonas("Genbu", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

koppa_tengu = TemperancePersonas("Koppa Tengu", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

makami = TemperancePersonas("Makami", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

jikokuten = TemperancePersonas("Jikokuten", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mithra = TemperancePersonas("Mithra", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

byakko = TemperancePersonas("Byakko", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

raja_naga = TemperancePersonas("Raja Naga", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

gabriel = TemperancePersonas("Gabriel", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

ardha = TemperancePersonas("Ardha", f"{Persona.persona_arcanas[14]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")


temperance_personas = (genbu, koppa_tengu, makami, jikokuten, mithra, byakko, raja_naga,
                       gabriel, ardha)

# Devil Personas:
# ------------------------------------------------------------------------------------
incubus = DevilPersonas("Incubus", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

flauros = DevilPersonas("Flauros", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

andras = DevilPersonas("Andras", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

lilim = DevilPersonas("Lilim", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

pazuzu = DevilPersonas("Pazuzu", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

baphomet = DevilPersonas("Baphomet", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

nebiros = DevilPersonas("Nebiros", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

belial = DevilPersonas("Belial", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

beelzebub = DevilPersonas("Beelzebub", f"{Persona.persona_arcanas[15]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")


devil_personas = (incubus, flauros, andras, lilim, pazuzu, baphomet, nebiros,
                  belial, beelzebub)

# Tower Personas:
# ------------------------------------------------------------------------------------
belphegor = TowerPersonas("Belphegor", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

red_rider = TowerPersonas("Red Rider", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

magatsu_izanagi = TowerPersonas("Magatsu Izanagi", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

magatsu_izanagi_picaro = TowerPersonas("Magatsu Izanagi Picaro", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

seth = TowerPersonas("Seth", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

black_rider = TowerPersonas("Black Rider", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mara = TowerPersonas("Mara", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

yoshitsune = TowerPersonas("Yoshitsune", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mada = TowerPersonas("Mada", f"{Persona.persona_arcanas[16]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

tower_personas = (belphegor, red_rider, magatsu_izanagi, magatsu_izanagi_picaro, seth, black_rider,
                  mara, yoshitsune, mada)

# Star Personas:
# ------------------------------------------------------------------------------------
kodama = StarPersonas("Kodama", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

fuuki = StarPersonas("Fuuki", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

neko_shogun = StarPersonas("Neko Shogun", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

kaiwan = StarPersonas("Kaiwan", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

gardua = StarPersonas("Gardua", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

vasuki = StarPersonas("Vasuki", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

sraosha = StarPersonas("Sraosha", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

hastur = StarPersonas("Hastur", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

lucifer = StarPersonas("Lucifer", f"{Persona.persona_arcanas[17]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

star_personas = (kodama, fuuki, neko_shogun, kaiwan, gardua, vasuki, sraosha,
                 hastur, lucifer)

# Moon Personas: 
# ------------------------------------------------------------------------------------
succbus = MoonPersonas("Succubus", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

onmoraki = MoonPersonas("Onmoraki", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

kaguya = MoonPersonas("Kaguya", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

black_ooze = MoonPersonas("Black Ooze", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

sui_ki = MoonPersonas("Sui-Ki", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

kaguya_picaro = MoonPersonas("Kaguya Picaro", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mothman = MoonPersonas("Mothman", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

girimehkala = MoonPersonas("Girimehkala", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

tsukiyomi = MoonPersonas("Tsukiyomi", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

tsukiyomi_picaro = MoonPersonas("Tsukiyomi Picaro", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

lilith = MoonPersonas("Lilith", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

byakhee = MoonPersonas("Byakhee", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

sandalphon = MoonPersonas("Sandalphon", f"{Persona.persona_arcanas[18]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

moon_personas = (succbus, onmoraki, kaguya, black_ooze, sui_ki, kaguya_picaro, mothman,
                 girmehkala, tsukiyomi, tsukiyomi_picaro, lilith, sandalphon)

# Sun Personas:
# ------------------------------------------------------------------------------------
suzaku = SunPersonas("Suzaku", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

thunderbird = SunPersonas("Thunderbird", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

mitrhas = SunPersonas("Mithras", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

yurlungur = SunPersonas("Yurlungur", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

horus = SunPersonas("Horus", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

ganesha = SunPersonas("Ganesha", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

quetzalcoatl = SunPersonas("Quetzalcoatl", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

asura = SunPersonas("Asura", f"{Persona.persona_arcanas[19]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

sun_personas = (suzaku, thunderbird, mitrhas, yurlungur, horus, ganesha,
                quetzalcoatl, asura)

# Judgement Personas:
# ------------------------------------------------------------------------------------
anubis = JudgementPersonas("Anubis", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

trumpeter = JudgementPersonas("Trumpeter", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

yamata_no_orochi = JudgementPersonas("Yamata-no-Orochi", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

abaddon = JudgementPersonas("Abaddon", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

messiah = JudgementPersonas("Messiah", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

shiva = JudgementPersonas("Shiva", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

michael = JudgementPersonas("Michael", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

messiah_picaro = JudgementPersonas("Messiah Picaro", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

satan = JudgementPersonas("Satan", f"{Persona.persona_arcanas[20]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

judgement_personas = (anubis, trumpeter, yamata_no_orochi, abaddon, messiah, shiva,
                      michael, messiah_picaro, satan)

# Faith Personas:
# ---------------------------------------------------------------------------
phoenix = FaithPersonas("Phoenix", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

tam_lin = FaithPersonas("Tam Lin", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

unicorn = FaithPersonas("Unicorn", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

okuninushi = FaithPersonas("Okuninushi", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

orichalcum = FaithPersonas("Orichalcum", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

atavaka = FaithPersonas("Atavaka", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

cu_chulainn = FaithPersonas("Cu Chulainn", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

siegfried = FaithPersonas("Siegfried", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

maria = FaithPersonas("Maria", f"{Persona.persona_arcanas[21]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

faith_personas = (phoenix, tam_lin, unicorn, okuninushi, orichalcum, atavaka,
                  cu_chulainn, siegfried, maria)

# Councillor Personas:
# ---------------------------------------------------------------------------
kushi_mitama = CouncillorPersonas("Kushi Mitama", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

nigi_mitama = CouncillorPersonas("Nigi Mitama", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

decarabia = CouncillorPersonas("Decarabia", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

ananta = CouncillorPersonas("Ananta", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

yatagarasu = CouncillorPersonas("Yatagarasu", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

seiryu  = CouncillorPersonas("Seiryu", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

dionysus = CouncillorPersonas("Dionysus", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

vohu_manah = CouncillorPersonas("Vohu Manah", f"{Persona.persona_arcanas[22]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")


councillor_personas = (kushi_mitama, nigi_mitama, decarabia, ananta, yatagarasu,
                       seiryu, dionysus, vohu_manah)

# ------------------------------------------------------------------------------
# Operations
def get_persona_arcana():
    print("Persona Arcanas:")
    print("------------------------------------------------")
    for arcana_index, arcana in enumerate(Persona.persona_arcanas,start=1):
        print(f"{arcana_index}. {arcana}")
    arcana_choice = int(input("\nPlease enter the Arcana of the Persona you'd like to register (1-23): "))
    return arcana_choice



selected_personas_arcana = ""


# Call function
arcana_choice = get_persona_arcana()


# I need to get the final index after the loop has looped through all of them

# Fool Personas Options
# Registration option for Arsene
if arcana_choice == 1:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[0]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_fool_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    # Registration option for Arsene 
    if persona_choice == 1:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = arsene.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        arsene.level = level_input
        arsene.st = st_input
        arsene.ma = ma_input
        arsene.en = en_input
        arsene.ag = ag_input
        arsene.lu = lu_input
        arsene.skill1 = skill1_input
        arsene.skill2 = skill2_input
        arsene.skill3 = skill3_input
        arsene.skill4 = skill4_input
        arsene.skill5 = skill5_input
        arsene.skill6 = skill6_input
        arsene.skill7 = skill7_input
        arsene.skill8 = skill8_input

    # Registration option for Obariyon
    elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = obariyon.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        obariyon.level = level_input
        obariyon.st = st_input
        obariyon.ma = ma_input
        obariyon.en = en_input
        obariyon.ag = ag_input
        obariyon.lu = lu_input
        obariyon.skill1 = skill1_input
        obariyon.skill2 = skill2_input
        obariyon.skill3 = skill3_input
        obariyon.skill4 = skill4_input
        obariyon.skill5 = skill5_input
        obariyon.skill6 = skill6_input
        obariyon.skill7 = skill7_input
        obariyon.skill8 = skill8_input

        # Registration option for Orpheus F 
        elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = orpheus_f.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]

        # Now set the default values to the values of the user input
        orpheus_f.level = level_input
        orpheus_f.st = st_input
        orpheus_f.ma = ma_input
        orpheus_f.en = en_input
        orpheus_f.ag = ag_input
        orpheus_f.lu = lu_input
        orpheus_f.skill1 = skill1_input
        orpheus_f.skill2 = skill2_input
        orpheus_f.skill3 = skill3_input
        orpheus_f.skill4 = skill4_input
        orpheus_f.skill5 = skill5_input
        orpheus_f.skill6 = skill6_input
        orpheus_f.skill7 = skill7_input
        orpheus_f.skill8 = skill8_input

        # Registration option for Orpheus F Picaro
        elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = orpehus_f_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]

        # Now set the default values to the values of the user input
        orpheus_f_picaro.level = level_input
        orpheus_f_picaro.st = st_input
        orpheus_f_picaro.ma = ma_input
        orpheus_f_picaro.en = en_input
        orpheus_f_picaro.ag = ag_input
        orpheus_f_picaro.lu = lu_input
        orpheus_f_picaro.skill1 = skill1_input
        orpheus_f_picaro.skill2 = skill2_input
        orpheus_f_picaro.skill3 = skill3_input
        orpheus_f_picaro.skill4 = skill4_input
        orpheus_f_picaro.skill5 = skill5_input
        orpheus_f_picaro.skill6 = skill6_input
        orpheus_f_picaro.skill7 = skill7_input
        orpheus_f_picaro.skill8 = skill8_input

        # Registration option for High Pixie 
        elif persona_choice == 5:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = high_pixie.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                high_pixie.level = level_input
                high_pixie.st = st_input
                high_pixie.ma = ma_input
                high_pixie.en = en_input
                high_pixie.ag = ag_input
                high_pixie.lu = lu_input
                high_pixie.skill1 = skill1_input
                high_pixie.skill2 = skill2_input
                high_pixie.skill3 = skill3_input
                high_pixie.skill4 = skill4_input
                high_pixie.skill5 = skill5_input
                high_pixie.skill6 = skill6_input
                high_pixie.skill7 = skill7_input
                high_pixie.skill8 = skill8_input

        # Registration option for Izanagi
        elif persona_choice == 6:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = izanagi.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                izanagi.level = level_input
                izanagi.st = st_input
                izanagi.ma = ma_input
                izanagi.en = en_input
                izanagi.ag = ag_input
                izanagi.lu = lu_input
                izanagi.skill1 = skill1_input
                izanagi.skill2 = skill2_input
                izanagi.skill3 = skill3_input
                izanagi.skill4 = skill4_input
                izanagi.skill5 = skill5_input
                izanagi.skill6 = skill6_input
                izanagi.skill7 = skill7_input
                izanagi.skill8 = skill8_input

        # Registration option for Izanagi Picaro
        elif persona_choice == 7:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = izanagi_picaro.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                izanagi_picaro.level = level_input
                izanagi_picaro.st = st_input
                izanagi_picaro.ma = ma_input
                izanagi_picaro.en = en_input
                izanagi_picaro.ag = ag_input
                izanagi_picaro.lu = lu_input
                izanagi_picaro.skill1 = skill1_input
                izanagi_picaro.skill2 = skill2_input
                izanagi_picaro.skill3 = skill3_input
                izanagi_picaro.skill4 = skill4_input
                izanagi_picaro.skill5 = skill5_input
                izanagi_picaro.skill6 = skill6_input
                izanagi_picaro.skill7 = skill7_input
                izanagi_picaro.skill8 = skill8_input

        # Registration option for Orpheus
        elif persona_choice == 8:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = orpheus.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                orpheus.level = level_input
                orpheus.st = st_input
                orpheus.ma = ma_input
                orpheus.en = en_input
                orpheus.ag = ag_input
                orpheus.lu = lu_input
                orpheus.skill1 = skill1_input
                orpheus.skill2 = skill2_input
                orpheus.skill3 = skill3_input
                orpheus.skill4 = skill4_input
                orpheus.skill5 = skill5_input
                orpheus.skill6 = skill6_input
                orpheus.skill7 = skill7_input
                orpheus.skill8 = skill8_input

        # Registration option for Orpheus Picaro
        elif persona_choice == 9:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = orpheus_picaro.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                orpheus_picaro.level = level_input
                orpheus_picaro.st = st_input
                orpheus_picaro.ma = ma_input
                orpheus_picaro.en = en_input
                orpheus_picaro.ag = ag_input
                orpheus_picaro.lu = lu_input
                orpheus_picaro.skill1 = skill1_input
                orpheus_picaro.skill2 = skill2_input
                orpheus_picaro.skill3 = skill3_input
                orpheus_picaro.skill4 = skill4_input
                orpheus_picaro.skill5 = skill5_input
                orpheus_picaro.skill6 = skill6_input
                orpheus_picaro.skill7 = skill7_input
                orpheus_picaro.skill8 = skill8_input

        # Registration option for Legion
        elif persona_choice == 10:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = legion.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                legion.level = level_input
                legion.st = st_input
                legion.ma = ma_input
                legion.en = en_input
                legion.ag = ag_input
                legion.lu = lu_input
                legion.skill1 = skill1_input
                legion.skill2 = skill2_input
                legion.skill3 = skill3_input
                legion.skill4 = skill4_input
                legion.skill5 = skill5_input
                legion.skill6 = skill6_input
                legion.skill7 = skill7_input
                legion.skill8 = skill8_input

        # Registration option for Ose
        elif persona_choice == 11:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = ose.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                ose.level = level_input
                ose.st = st_input
                ose.ma = ma_input
                ose.en = en_input
                ose.ag = ag_input
                ose.lu = lu_input
                ose.skill1 = skill1_input
                ose.skill2 = skill2_input
                ose.skill3 = skill3_input
                ose.skill4 = skill4_input
                ose.skill5 = skill5_input
                ose.skill6 = skill6_input
                ose.skill7 = skill7_input
                ose.skill8 = skill8_input

        # Registration option for Bugs
        elif persona_choice == 12:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = bugs.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                bugs.level = level_input
                bugs.st = st_input
                bugs.ma = ma_input
                bugs.en = en_input
                bugs.ag = ag_input
                bugs.lu = lu_input
                bugs.skill1 = skill1_input
                bugs.skill2 = skill2_input
                bugs.skill3 = skill3_input
                bugs.skill4 = skill4_input
                bugs.skill5 = skill5_input
                bugs.skill6 = skill6_input
                bugs.skill7 = skill7_input
                bugs.skill8 = skill8_input

        # Registration option for Crystal Skull
        elif persona_choice == 13:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = crystal_skull.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                crystal_skull.level = level_input
                crystal_skull.st = st_input
                crystal_skull.ma = ma_input
                crystal_skull.en = en_input
                crystal_skull.ag = ag_input
                crystal_skull.lu = lu_input
                crystal_skull.skill1 = skill1_input
                crystal_skull.skill2 = skill2_input
                crystal_skull.skill3 = skill3_input
                crystal_skull.skill4 = skill4_input
                crystal_skull.skill5 = skill5_input
                crystal_skull.skill6 = skill6_input
                crystal_skull.skill7 = skill7_input
                crystal_skull.skill8 = skill8_input

        # Registration option for Black Frost
        elif persona_choice == 14:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = black_frost.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                black_frost.level = level_input
                black_frost.st = st_input
                black_frost.ma = ma_input
                black_frost.en = en_input
                black_frost.ag = ag_input
                black_frost.lu = lu_input
                black_frost.skill1 = skill1_input
                black_frost.skill2 = skill2_input
                black_frost.skill3 = skill3_input
                black_frost.skill4 = skill4_input
                black_frost.skill5 = skill5_input
                black_frost.skill6 = skill6_input
                black_frost.skill7 = skill7_input
                black_frost.skill8 = skill8_input

        # Registration option for Raoul
        elif persona_choice == 15:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = raoul.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                raoul.level = level_input
                raoul.st = st_input
                raoul.ma = ma_input
                raoul.en = en_input
                raoul.ag = ag_input
                raoul.lu = lu_input
                raoul.skill1 = skill1_input
                raoul.skill2 = skill2_input
                raoul.skill3 = skill3_input
                raoul.skill4 = skill4_input
                raoul.skill5 = skill5_input
                raoul.skill6 = skill6_input
                raoul.skill7 = skill7_input
                raoul.skill8 = skill8_input

        # Registration option for Vishnu
        elif persona_choice == 16:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = vishnu.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                vishnu.level = level_input
                vishnu.st = st_input
                vishnu.ma = ma_input
                vishnu.en = en_input
                vishnu.ag = ag_input
                vishnu.lu = lu_input
                vishnu.skill1 = skill1_input
                vishnu.skill2 = skill2_input
                vishnu.skill3 = skill3_input
                vishnu.skill4 = skill4_input
                vishnu.skill5 = skill5_input
                vishnu.skill6 = skill6_input
                vishnu.skill7 = skill7_input
                vishnu.skill8 = skill8_input

        # Registration option for Satanael
        elif persona_choice == 17:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = satanael.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                satanael.level = level_input
                satanael.st = st_input
                satanael.ma = ma_input
                satanael.en = en_input
                satanael.ag = ag_input
                satanael.lu = lu_input
                satanael.skill1 = skill1_input
                satanael.skill2 = skill2_input
                satanael.skill3 = skill3_input
                satanael.skill4 = skill4_input
                satanael.skill5 = skill5_input
                satanael.skill6 = skill6_input
                satanael.skill7 = skill7_input
                satanael.skill8 = skill8_input
        


# Magician Personas Options
elif arcana_choice == 2:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[1]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_magician_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    # Registration option for Jack-o'-Lantern
    if persona_choice == 1:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = jack_o_lantern.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        jack_o_lantern.level = level_input
        jack_o_lantern.st = st_input
        jack_o_lantern.ma = ma_input
        jack_o_lantern.en = en_input
        jack_o_lantern.ag = ag_input
        jack_o_lantern.lu = lu_input
        jack_o_lantern.skill1 = skill1_input
        jack_o_lantern .skill2 = skill2_input
        jack_o_lantern .skill3 = skill3_input
        jack_o_lantern.skill4 = skill4_input
        jack_o_lantern.skill5 = skill5_input
        jack_o_lantern.skill6 = skill6_input
        jack_o_lantern.skill7 = skill7_input
        jack_o_lantern.skill8 = skill8_input

        # Registration option for Cait Sith 
        elif persona_choice == 2:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = caith_sith.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                cait_sith.level = level_input
                cait_sith.st = st_input
                cait_sith.ma = ma_input
                cait_sith.en = en_input
                cait_sith.ag = ag_input
                cait_sith.lu = lu_input
                cait_sith.skill1 = skill1_input
                cait_sith.skill2 = skill2_input
                cait_sith.skill3 = skill3_input
                cait_sith.skill4 = skill4_input
                cait_sith.skill5 = skill5_input
                cait_sith.skill6 = skill6_input
                cait_sith.skill7 = skill7_input
                cait_sith.skill8 = skill8_input

        # Registration option for Jack Frost
        elif persona_choice == 3:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = jack_frost.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                jack_frost.level = level_input
                jack_frost.st = st_input
                jack_frost.ma = ma_input
                jack_frost.en = en_input
                jack_frost.ag = ag_input
                jack_frost.lu = lu_input
                jack_frost.skill1 = skill1_input
                jack_frost.skill2 = skill2_input
                jack_frost.skill3 = skill3_input
                jack_frost.skill4 = skill4_input
                jack_frost.skill5 = skill5_input
                jack_frost.skill6 = skill6_input
                jack_frost.skill7 = skill7_input
                jack_frost.skill8 = skill8_input

        # Registration option for Nekomata
        elif persona_choice == 4:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = nekomata.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                nekomata.level = level_input
                nekomata.st = st_input
                nekomata.ma = ma_input
                nekomata.en = en_input
                nekomata.ag = ag_input
                nekomata.lu = lu_input
                nekomata.skill1 = skill1_input
                nekomata.skill2 = skill2_input
                nekomata.skill3 = skill3_input
                nekomata.skill4 = skill4_input
                nekomata.skill5 = skill5_input
                nekomata.skill6 = skill6_input
                nekomata.skill7 = skill7_input
                nekomata.skill8 = skill8_input

        # Registration option for Sandman
        elif persona_choice == 5:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = sandman.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                sandman.level = level_input
                sandman.st = st_input
                sandman.ma = ma_input
                sandman.en = en_input
                sandman.ag = ag_input
                sandman.lu = lu_input
                sandman.skill1 = skill1_input
                sandman.skill2 = skill2_input
                sandman.skill3 = skill3_input
                sandman.skill4 = skill4_input
                sandman.skill5 = skill5_input
                sandman.skill6 = skill6_input
                sandman.skill7 = skill7_input
                sandman.skill8 = skill8_input

        # Registration option for Choronzon
        elif persona_choice == 6:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = choronzon.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                choronzon.level = level_input
                choronzon.st = st_input
                choronzon.ma = ma_input
                choronzon.en = en_input
                choronzon.ag = ag_input
                choronzon.lu = lu_input
                choronzon.skill1 = skill1_input
                choronzon.skill2 = skill2_input
                choronzon.skill3 = skill3_input
                choronzon.skill4 = skill4_input
                choronzon.skill5 = skill5_input
                choronzon.skill6 = skill6_input
                choronzon.skill7 = skill7_input
                choronzon.skill8 = skill8_input

        # Registration option for Queen Mab
        elif persona_choice == 7:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = queen_mab.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                queen_mab.level = level_input
                queen_mab.st = st_input
                queen_mab.ma = ma_input
                queen_mab.en = en_input
                queen_mab.ag = ag_input
                queen_mab.lu = lu_input
                queen_mab.skill1 = skill1_input
                queen_mab.skill2 = skill2_input
                queen_mab.skill3 = skill3_input
                queen_mab.skill4 = skill4_input
                queen_mab.skill5 = skill5_input
                queen_mab.skill6 = skill6_input
                queen_mab.skill7 = skill7_input
                queen_mab.skill8 = skill8_input

        # Registration option for Rangda
        elif persona_choice == 8:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = rangda.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                rangda.level = level_input
                rangda.st = st_input
                rangda.ma = ma_input
                rangda.en = en_input
                rangda.ag = ag_input
                rangda.lu = lu_input
                rangda.skill1 = skill1_input
                rangda.skill2 = skill2_input
                rangda.skill3 = skill3_input
                rangda.skill4 = skill4_input
                rangda.skill5 = skill5_input
                rangda.skill6 = skill6_input
                rangda.skill7 = skill7_input
                rangda.skill8 = skill8_input

        # Registration option for Forneus
        elif persona_choice == 9:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = forneus.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                forneus.level = level_input
                forneus.st = st_input
                forneus.ma = ma_input
                forneus.en = en_input
                forneus.ag = ag_input
                forneus.lu = lu_input
                forneus.skill1 = skill1_input
                forneus.skill2 = skill2_input
                forneus.skill3 = skill3_input
                forneus.skill4 = skill4_input
                forneus.skill5 = skill5_input
                forneus.skill6 = skill6_input
                forneus.skill7 = skill7_input
                forneus.skill8 = skill8_input

        # Registration option for Surt
        elif persona_choice == 10:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = surt.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                surt.level = level_input
                surt.st = st_input
                surt.ma = ma_input
                surt.en = en_input
                surt.ag = ag_input
                surt.lu = lu_input
                surt.skill1 = skill1_input
                surt.skill2 = skill2_input
                surt.skill3 = skill3_input
                surt.skill4 = skill4_input
                surt.skill5 = skill5_input
                surt.skill6 = skill6_input
                surt.skill7 = skill7_input
                surt.skill8 = skill8_input

        # Registration option for Futsunushi
        elif persona_choice == 11:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = futsunushi.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                futsunushi.level = level_input
                futsunushi.st = st_input
                futsunushi.ma = ma_input
                futsunushi.en = en_input
                futsunushi.ag = ag_input
                futsunushi.lu = lu_input
                futsunushi.skill1 = skill1_input
                futsunushi.skill2 = skill2_input
                futsunushi.skill3 = skill3_input
                futsunushi.skill4 = skill4_input
                futsunushi.skill5 = skill5_input
                futsunushi.skill6 = skill6_input
                futsunushi.skill7 = skill7_input
                futsunushi.skill8 = skill8_input


# Personas Options    
# Registration option for Silky
elif arcana_choice == 3:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[2]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_priestess_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = silky.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        silky.level = level_input
        silky.st = st_input
        silky.ma = ma_input
        silky.en = en_input
        silky.ag = ag_input
        silky.lu = lu_input
        silky.skill1 = skill1_input
        silky.skill2 = skill2_input
        silky.skill3 = skill3_input
        silky.skill4 = skill4_input
        silky.skill5 = skill5_input
        silky.skill6 = skill6_input
        silky.skill7 = skill7_input
        silky.skill8 = skill8_input

        # Registration option for Apsaras
        elif persona_choice == 2:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = apsaras.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                apsaras.level = level_input
                apsaras.st = st_input
                apsaras.ma = ma_input
                apsaras.en = en_input
                apsaras.ag = ag_input
                apsaras.lu = lu_input
                apsaras.skill1 = skill1_input
                apsaras.skill2 = skill2_input
                apsaras.skill3 = skill3_input
                apsaras.skill4 = skill4_input
                apsaras.skill5 = skill5_input
                apsaras.skill6 = skill6_input
                apsaras.skill7 = skill7_input
                apsaras.skill8 = skill8_input

        # Registration option for Kohi-i-Noor
        elif persona_choice == 3:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = kohi_i_noor.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                kohi_i_noor.level = level_input
                kohi_i_noor.st = st_input
                kohi_i_noor.ma = ma_input
                kohi_i_noor.en = en_input
                kohi_i_noor.ag = ag_input
                kohi_i_noor.lu = lu_input
                kohi_i_noor.skill1 = skill1_input
                kohi_i_noor.skill2 = skill2_input
                kohi_i_noor.skill3 = skill3_input
                kohi_i_noor.skill4 = skill4_input
                kohi_i_noor.skill5 = skill5_input
                kohi_i_noor.skill6 = skill6_input
                kohi_i_noor.skill7 = skill7_input
                kohi_i_noor.skill8 = skill8_input

        
        # Registration option for Isis 
        elif persona_choice == 4:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = isis.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                isis.level = level_input
                isis.st = st_input
                isis.ma = ma_input
                isis.en = en_input
                isis.ag = ag_input
                isis.lu = lu_input
                isis.skill1 = skill1_input
                isis.skill2 = skill2_input
                isis.skill3 = skill3_input
                isis.skill4 = skill4_input
                isis.skill5 = skill5_input
                isis.skill6 = skill6_input
                isis.skill7 = skill7_input
                isis.skill8 = skill8_input

        # Registration option for Kikuri-Hime
        elif persona_choice == 5:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = kikuri_hime.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                kikuri_hime.level = level_input
                kikuri_hime.st = st_input
                kikuri_hime.ma = ma_input
                kikuri_hime.en = en_input
                kikuri_hime.ag = ag_input
                kikuri_hime.lu = lu_input
                kikuri_hime.skill1 = skill1_input
                kikuri_hime.skill2 = skill2_input
                kikuri_hime.skill3 = skill3_input
                kikuri_hime.skill4 = skill4_input
                kikuri_hime.skill5 = skill5_input
                kikuri_hime.skill6 = skill6_input
                kikuri_hime.skill7 = skill7_input
                kikuri_hime.skill8 = skill8_input

        # Registration option for Sarasvati
        elif persona_choice == 6:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = sarasvati.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                sarasvati.level = level_input
                sarasvati.st = st_input
                sarasvati.ma = ma_input
                sarasvati.en = en_input
                sarasvati.ag = ag_input
                sarasvati.lu = lu_input
                sarasvati.skill1 = skill1_input
                sarasvati.skill2 = skill2_input
                sarasvati.skill3 = skill3_input
                sarasvati.skill4 = skill4_input
                sarasvati.skill5 = skill5_input
                sarasvati.skill6 = skill6_input
                sarasvati.skill7 = skill7_input
                sarasvati.skill8 = skill8_input

        # Registration option for Skadi
        elif persona_choice == 7:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = skadi.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                skadi.level = level_input
                skadi.st = st_input
                skadi.ma = ma_input
                skadi.en = en_input
                skadi.ag = ag_input
                skadi.lu = lu_input
                skadi.skill1 = skill1_input
                skadi.skill2 = skill2_input
                skadi.skill3 = skill3_input
                skadi.skill4 = skill4_input
                skadi.skill5 = skill5_input
                skadi.skill6 = skill6_input
                skadi.skill7 = skill7_input
                skadi.skill8 = skill8_input

        # Registration option for Scathach
        elif persona_choice == 8:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = scathach.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                scathach.level = level_input
                scathach.st = st_input
                scathach.ma = ma_input
                scathach.en = en_input
                scathach.ag = ag_input
                scathach.lu = lu_input
                scathach.skill1 = skill1_input
                scathach.skill2 = skill2_input
                scathach.skill3 = skill3_input
                scathach.skill4 = skill4_input
                scathach.skill5 = skill5_input
                scathach.skill6 = skill6_input
                scathach.skill7 = skill7_input
                scathach.skill8 = skill8_input

        # Registration option for Cybele
        elif persona_choice == 9:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = cybele.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                cybele.level = level_input
                cybele.st = st_input
                cybele.ma = ma_input
                cybele.en = en_input
                cybele.ag = ag_input
                cybele.lu = lu_input
                cybele.skill1 = skill1_input
                cybele.skill2 = skill2_input
                cybele.skill3 = skill3_input
                cybele.skill4 = skill4_input
                cybele.skill5 = skill5_input
                cybele.skill6 = skill6_input
                cybele.skill7 = skill7_input
                cybeleskill8 = skill8_input


# Personas Options    
elif arcana_choice == 4:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[3]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_empress_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

        # Registration option for Queen's Necklace 
        if persona_choice == 1:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = queens_necklace.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                queens_necklace.level = level_input
                queens_necklace.st = st_input
                queens_necklace.ma = ma_input
                queens_necklace.en = en_input
                queens_necklace.ag = ag_input
                queens_necklace.lu = lu_input
                queens_necklace.skill1 = skill1_input
                queens_necklace.skill2 = skill2_input
                queens_necklace.skill3 = skill3_input
                queens_necklace.skill4 = skill4_input
                queens_necklace.skill5 = skill5_input
                queens_necklace.skill6 = skill6_input
                queens_necklace.skill7 = skill7_input
                queens_necklace.skill8 = skill8_input

        # Registration option for Yaksnini
        elif persona_choice == 2:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = yaksini.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                yaksini.level = level_input
                yaksini.st = st_input
                yaksini.ma = ma_input
                yaksini.en = en_input
                yaksini.ag = ag_input
                yaksini.lu = lu_input
                yaksini.skill1 = skill1_input
                yaksini.skill2 = skill2_input
                yaksini.skill3 = skill3_input
                yaksini.skill4 = skill4_input
                yaksini.skill5 = skill5_input
                yaksini.skill6 = skill6_input
                yaksini.skill7 = skill7_input
                yaksini.skill8 = skill8_input

        # Registration option for Lamia 
        elif persona_choice == 3:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = lamia.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                lamia.level = level_input
                lamia.st = st_input
                lamia.ma = ma_input
                lamia.en = en_input
                lamia.ag = ag_input
                lamia.lu = lu_input
                lamia.skill1 = skill1_input
                lamia.skill2 = skill2_input
                lamia.skill3 = skill3_input
                lamia.skill4 = skill4_input
                lamia.skill5 = skill5_input
                lamia.skill6 = skill6_input
                lamia.skill7 = skill7_input
                lamia.skill8 = skill8_input

        # Registration option for Hariti
        elif persona_choice == 4:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = hariti.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                hariti.level = level_input
                hariti.st = st_input
                hariti.ma = ma_input
                hariti.en = en_input
                hariti.ag = ag_input
                hariti.lu = lu_input
                hariti.skill1 = skill1_input
                hariti.skill2 = skill2_input
                hariti.skill3 = skill3_input
                hariti.skill4 = skill4_input
                hariti.skill5 = skill5_input
                hariti.skill6 = skill6_input
                hariti.skill7 = skill7_input
                hariti.skill8 = skill8_input

        # Registration option for Dakini
        elif persona_choice == 5:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = dakini.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                dakini.level = level_input
                dakini.st = st_input
                dakini.ma = ma_input
                dakini.en = en_input
                dakini.ag = ag_input
                dakini.lu = lu_input
                dakini.skill1 = skill1_input
                dakini.skill2 = skill2_input
                dakini.skill3 = skill3_input
                dakini.skill4 = skill4_input
                dakini.skill5 = skill5_input
                dakini.skill6 = skill6_input
                dakini.skill7 = skill7_input
                dakini.skill8 = skill8_input

        # Registration option for Titania
        elif persona_choice == 6:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = titania.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                titania.level = level_input
                titania.st = st_input
                titania.ma = ma_input
                titania.en = en_input
                titania.ag = ag_input
                titania.lu = lu_input
                titania.skill1 = skill1_input
                titania.skill2 = skill2_input
                titania.skill3 = skill3_input
                titania.skill4 = skill4_input
                titania.skill5 = skill5_input
                titania.skill6 = skill6_input
                titania.skill7 = skill7_input
                titania.skill8 = skill8_input

        # Registration option for Kali
        elif persona_choice == 7:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = kali.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                kali.level = level_input
                kali.st = st_input
                kali.ma = ma_input
                kali.en = en_input
                kali.ag = ag_input
                kali.lu = lu_input
                kali.skill1 = skill1_input
                kali.skill2 = skill2_input
                kali.skill3 = skill3_input
                kali.skill4 = skill4_input
                kali.skill5 = skill5_input
                kali.skill6 = skill6_input
                kali.skill7 = skill7_input
                kali.skill8 = skill8_input

        # Registration option for Alilat
        elif persona_choice == 8:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = alilat.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                alilat.level = level_input
                alilat.st = st_input
                alilat.ma = ma_input
                alilat.en = en_input
                alilat.ag = ag_input
                alilat.lu = lu_input
                alilat.skill1 = skill1_input
                alilat.skill2 = skill2_input
                alilat.skill3 = skill3_input
                alilat.skill4 = skill4_input
                alilat.skill5 = skill5_input
                alilat.skill6 = skill6_input
                alilat.skill7 = skill7_input
                alilat.skill8 = skill8_input

        # Registration option for Mother Harlot
        elif persona_choice == 9:
                print()
                # Call the function to get the stats from the user 
                stats_to_register = mother_harlot.get_persona_info()
                # Unpack them into values
                level_input = stats_to_register[0]
                st_input = stats_to_register[1]
                ma_input = stats_to_register[2]
                en_input = stats_to_register[3]
                ag_input = stats_to_register[4]
                lu_input = stats_to_register[5]
                skill1_input = stats_to_register[6]
                skill2_input = stats_to_register[7]
                skill3_input = stats_to_register[8]
                skill4_input = stats_to_register[9]
                skill5_input = stats_to_register[10]
                skill6_input = stats_to_register[11]
                skill7_input = stats_to_register[12]
                skill8_input = stats_to_register[13]
                
                # Now set the default values to the values of the user input
                mother_harlot.level = level_input
                mother_harlot.st = st_input
                mother_harlot.ma = ma_input
                mother_harlot.en = en_input
                mother_harlot.ag = ag_input
                mother_harlot.lu = lu_input
                mother_harlot.skill1 = skill1_input
                mother_harlot.skill2 = skill2_input
                mother_harlot.skill3 = skill3_input
                mother_harlot.skill4 = skill4_input
                mother_harlot.skill5 = skill5_input
                mother_harlot.skill6 = skill6_input
                mother_harlot.skill7 = skill7_input
                mother_harlot.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 5:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[4]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_emperor_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

# Registration option for
elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Registration option for
elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 6:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[5]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hierophant_personas()
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 7:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[6]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_lovers_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 8:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[7]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_chariot_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 9:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[8]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_justice_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input
elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 10:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[9]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hermit_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 11:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[10]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_fortune_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 12:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[11]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_strength_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 13:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[12]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hanged_man_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input


# Personas Options    
elif arcana_choice == 14:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[13]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_death_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input
    

# Personas Options    
elif arcana_choice == 15:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[14]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_temperance_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 16:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[15]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_devil_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 17:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[16]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_tower_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 18:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[17]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_star_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 19:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[18]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_moon_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 20:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[19]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_sun_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

            elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 21:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[20]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_judgement_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

            elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 22:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[21]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_faith_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

            elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

# Personas Options    
elif arcana_choice == 23:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[22]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_councillor_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = .get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            .level = level_input
            .st = st_input
            .ma = ma_input
            .en = en_input
            .ag = ag_input
            .lu = lu_input
            .skill1 = skill1_input
            .skill2 = skill2_input
            .skill3 = skill3_input
            .skill4 = skill4_input
            .skill5 = skill5_input
            .skill6 = skill6_input
            .skill7 = skill7_input
            .skill8 = skill8_input

            elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input

elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        .level = level_input
        .st = st_input
        .ma = ma_input
        .en = en_input
        .ag = ag_input
        .lu = lu_input
        .skill1 = skill1_input
        .skill2 = skill2_input
        .skill3 = skill3_input
        .skill4 = skill4_input
        .skill5 = skill5_input
        .skill6 = skill6_input
        .skill7 = skill7_input
        .skill8 = skill8_input
    

# Containers for formatted log data for all Persona arcanas 
fool_personas_log_data = []
magician_personas_log_data = []
priestess_personas_log_data = []
empress_personas_log_data = []
emperor_personas_log_data = []
hierophant_personas_log_data = []
lovers_personas_log_data = []
chariot_personas_log_data = []
justice_personas_log_data = []
hermit_personas_log_data = []
fortune_personas_log_data = []
strength_personas_log_data = []
hanged_man_personas_log_data = []
death_personas_log_data = []
temperance_personas_log_data = []
devil_personas_log_data = []
tower_personas_log_data = []
star_personas_log_data = []
moon_personas_log_data = []
sun_personas_log_data = []
judgement_personas_log_data = []
faith_personas_log_data = []
councillor_personas_log_data = []

# Uses a for loop to format all Fool Personas' info a string 
for fool_persona in fool_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = fool_persona.format_persona_log_entry()
    # Append the data into the list 
    fool_personas_log_data.append(formatted_data)

for magician_persona in magician_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = magician_persona.format_persona_log_entry()
    # Append the data into the list 
    magician_personas_log_data.append(formatted_data)

for priestess_persona in priestess_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = priestess_persona.format_persona_log_entry()
    # Append the data into the list 
    priestess_personas_log_data.append(formatted_data)

for empress_persona in empress_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = empress_persona.format_persona_log_entry()
    # Append the data into the list 
    empress_personas_log_data.append(formatted_data)

for emperor_persona in emperor_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = emperor_persona.format_persona_log_entry()
    # Append the data into the list 
    emperor_personas_log_data.append(formatted_data)

for hierophant_persona in hierophant_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = hierophant_persona.format_persona_log_entry()
    # Append the data into the list 
    hierophant_personas_log_data.append(formatted_data)

for lovers_persona in lovers_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = lovers_persona.format_persona_log_entry()
    # Append the data into the list 
    lovers_personas_log_data.append(formatted_data)
    
for chariot_persona in chariot_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = chariot_persona.format_persona_log_entry()
    # Append the data into the list 
    chariot_personas_log_data.append(formatted_data)

for justice_persona in justice_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = justice_persona.format_persona_log_entry()
    # Append the data into the list 
    justice_personas_log_data.append(formatted_data)

for hermit_persona in hermit_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = hermit_persona.format_persona_log_entry()
    # Append the data into the list 
    hermit_personas_log_data.append(formatted_data)

for fortune_persona in fortune_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = fortune_persona.format_persona_log_entry()
    # Append the data into the list 
    fortune_personas_log_data.append(formatted_data)

for strength_persona in strength_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = strength_persona.format_persona_log_entry()
    # Append the data into the list 
    strength_personas_log_data.append(formatted_data)

for hanged_man_persona in hanged_man_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = hanged_man_persona.format_persona_log_entry()
    # Append the data into the list 
    hanged_man_personas_log_data.append(formatted_data)

for death_persona in death_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = death_persona.format_persona_log_entry()
    # Append the data into the list 
    death_personas_log_data.append(formatted_data)

for temperance_persona in temperance_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = temperance_persona.format_persona_log_entry()
    # Append the data into the list 
    temperance_personas_log_data.append(formatted_data)

for devil_persona in devil_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = devil_persona.format_persona_log_entry()
    # Append the data into the list 
    devil_personas_log_data.append(formatted_data)

for tower_persona in tower_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = tower_persona.format_persona_log_entry()
    # Append the data into the list 
    tower_personas_log_data.append(formatted_data)

for star_persona in star_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = star_persona.format_persona_log_entry()
    # Append the data into the list 
    star_personas_log_data.append(formatted_data)

for moon_persona in moon_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = moon_persona.format_persona_log_entry()
    # Append the data into the list 
    moon_personas_log_data.append(formatted_data)

for sun_persona in sun_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = sun_persona.format_persona_log_entry()
    # Append the data into the list 
    sun_personas_log_data.append(formatted_data)

for judgement_persona in judgement_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = judgement_persona.format_persona_log_entry()
    # Append the data into the list 
    sun_personas_log_data.append(formatted_data)

for faith_persona in faith_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = faith_persona.format_persona_log_entry()
    # Append the data into the list 
    faith_personas_log_data.append(formatted_data)

for councillor_persona in councillor_personas:
    # Call the function that formats the data and put the result in a variable
    formatted_data = councillor_persona.format_persona_log_entry()
    # Append the data into the list 
    faith_personas_log_data.append(formatted_data)


# Writes the formatted info to the file 
with open("Persona_compendium_logbookV3.txt","w") as compendium_log:
    # Write Fool Personas to the compendium
    for fool_persona_log in fool_personas_log_data:
        compendium_log.write(fool_persona_log)

    # Magician Personas to the compendium
    for magician_persona_log in magician_personas_log_data:
        compendium_log.write(magician_persona_log)
        
    # Priestess Personas to the compendium
    for priestess_persona_log in priestess_personas_log_data:
            compendium_log.write(priestess_persona_log)

    # Empress Personas to the compendium
    for empress_persona_log in empress_personas_log_data:
        compendium_log.write(empress_persona_log)

    # Emperor Personas
    for emperor_persona_log in emperor_personas_log_data:
        compendium_log.write(emperor_persona_log)

    # Hierophant Personas
    for hierophant_persona_log in hierophant_personas_log_data:
        compendium_log.write(hierophant_persona_log)

    # Lovers Personas
    for lovers_persona_log in lovers_personas_log_data:
        compendium_log.write(lovers_persona_log)

    # Chariot Personas
    for chariot_persona_log in chariot_personas_log_data:
        compendium_log.write(chariot_persona_log)

    # Justice Personas
    for justice_persona_log in justice_personas_log_data:
        compendium_log.write(justice_persona_log)

    # Hermit Personas
    for hermit_persona_log in hermit_personas_log_data:
        compendium_log.write(hermit_persona_log)

    # Fortune Personas
    for fortune_persona_log in fortune_personas_log_data:
        compendium_log.write(fortune_persona_log)

    # Strength Personas
    for strength_persona_log in strength_personas_log_data:
        compendium_log.write(strength_persona_log)

    # Hanged Man Personas
    for hanged_man_persona_log in hanged_man_personas_log_data:
        compendium_log.write(hanged_man_persona_log)

    # Death Personas
    for death_persona_log in death_personas_log_data:
        compendium_log.write(death_persona_log)

    # Temperance Personas
    for temperance_persona_log in temperance_personas_log_data:
        compendium_log.write(temperance_persona_log)

    # Devil Personas
    for devil_persona_log in devil_personas_log_data:
        compendium_log.write(devil_persona_log)

    # Tower Personas
    for tower_persona_log in tower_personas_log_data:
        compendium_log.write(tower_persona_log)

    # Star Personas
    for star_persona_log in star_personas_log_data:
        compendium_log.write(star_persona_log)

    # Moon Personas 
    for moon_persona_log in moon_personas_log_data:
        compendium_log.write(moon_persona_log)

    # Sun Personas
    for sun_persona_log in sun_personas_log_data:
        compendium_log.write(sun_persona_log)

    # Judgement Personas
    for judgement_persona_log in judgement_personas_log_data:
        compendium_log.write(judgement_persona_log)

    # Faith Personas
    for faith_persona_log in faith_personas_log_data:
        compendium_log.write(faith_persona_log)
    
    # Let the user know that the Personas have been registered
    print("Current Personas registered to compendium.")
    print("Previous Personas have been overwritten.")
