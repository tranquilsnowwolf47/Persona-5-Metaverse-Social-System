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
agathion = ChariotPersonas("Agathion", f"{Persona.persona_arcanas[7]}", 1,
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

chariot_personas = (agathion, slime, shiki_ouji, kin_ki, ara_mitama, white_rider, athena, 
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

valkyrie = StrengthPersonas("Valkyrie", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

hanuman = StrengthPersonas("Hanuman", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

chimera = StrengthPersonas("Chimera", f"{Persona.persona_arcanas[11]}", 1,
                                1,1,1,1,1,
                                "","","","",
                                "","","","")

zaou_gongen = StrengthPersonas("Zaou-Gongen", f"{Persona.persona_arcanas[11]}", 1,
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

fuuki = StarPersonas("Fuu-Ki", f"{Persona.persona_arcanas[17]}", 1,
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
                 girimehkala, tsukiyomi, tsukiyomi_picaro, lilith, sandalphon)

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

seiryu = CouncillorPersonas("Seiryu", f"{Persona.persona_arcanas[22]}", 1,
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
    
    # Registration option for Regent
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = regent.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            regent.level = level_input
            regent.st = st_input
            regent.ma = ma_input
            regent.en = en_input
            regent.ag = ag_input
            regent.lu = lu_input
            regent.skill1 = skill1_input
            regent.skill2 = skill2_input
            regent.skill3 = skill3_input
            regent.skill4 = skill4_input
            regent.skill5 = skill5_input
            regent.skill6 = skill6_input
            regent.skill7 = skill7_input
            regent.skill8 = skill8_input

# Registration option for Eligor
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = eligor.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        eligor.level = level_input
        eligor.st = st_input
        eligor.ma = ma_input
        eligor.en = en_input
        eligor.ag = ag_input
        eligor.lu = lu_input
        eligor.skill1 = skill1_input
        eligor.skill2 = skill2_input
        eligor.skill3 = skill3_input
        eligor.skill4 = skill4_input
        eligor.skill5 = skill5_input
        eligor.skill6 = skill6_input
        eligor.skill7 = skill7_input
        eligor.skill8 = skill8_input

# Registration option for Setanta
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = setanta.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        setanta.level = level_input
        setanta.st = st_input
        setanta.ma = ma_input
        setanta.en = en_input
        setanta.ag = ag_input
        setanta.lu = lu_input
        setanta.skill1 = skill1_input
        setanta.skill2 = skill2_input
        setanta.skill3 = skill3_input
        setanta.skill4 = skill4_input
        setanta.skill5 = skill5_input
        setanta.skill6 = skill6_input
        setanta.skill7 = skill7_input
        setanta.skill8 = skill8_input

# Registration option for Thoth
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = thoth.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        thoth.level = level_input
        thoth.st = st_input
        thoth.ma = ma_input
        thoth.en = en_input
        thoth.ag = ag_input
        thoth.lu = lu_input
        thoth.skill1 = skill1_input
        thoth.skill2 = skill2_input
        thoth.skill3 = skill3_input
        thoth.skill4 = skill4_input
        thoth.skill5 = skill5_input
        thoth.skill6 = skill6_input
        thoth.skill7 = skill7_input
        thoth.skill8 = skill8_input

# Registration option for Barong
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = barong.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        barong.level = level_input
        barong.st = st_input
        barong.ma = ma_input
        barong.en = en_input
        barong.ag = ag_input
        barong.lu = lu_input
        barong.skill1 = skill1_input
        barong.skill2 = skill2_input
        barong.skill3 = skill3_input
        barong.skill4 = skill4_input
        barong.skill5 = skill5_input
        barong.skill6 = skill6_input
        barong.skill7 = skill7_input
        barong.skill8 = skill8_input

# Registration option for King Frost 
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = king_frost.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        king_frost.level = level_input
        king_frost.st = st_input
        king_frost.ma = ma_input
        king_frost.en = en_input
        king_frost.ag = ag_input
        king_frost.lu = lu_input
        king_frost.skill1 = skill1_input
        king_frost.skill2 = skill2_input
        king_frost.skill3 = skill3_input
        king_frost.skill4 = skill4_input
        king_frost.skill5 = skill5_input
        king_frost.skill6 = skill6_input
        king_frost.skill7 = skill7_input
        king_frost.skill8 = skill8_input

# Registration option for Oberon
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = oberon.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        oberon.level = level_input
        oberon.st = st_input
        oberon.ma = ma_input
        oberon.en = en_input
        oberon.ag = ag_input
        oberon.lu = lu_input
        oberon.skill1 = skill1_input
        oberon.skill2 = skill2_input
        oberon.skill3 = skill3_input
        oberon.skill4 = skill4_input
        oberon.skill5 = skill5_input
        oberon.skill6 = skill6_input
        oberon.skill7 = skill7_input
        oberon.skill8 = skill8_input

# Registration option for Baal
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = baal.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        baal.level = level_input
        baal.st = st_input
        baal.ma = ma_input
        baal.en = en_input
        baal.ag = ag_input
        baal.lu = lu_input
        baal.skill1 = skill1_input
        baal.skill2 = skill2_input
        baal.skill3 = skill3_input
        baal.skill4 = skill4_input
        baal.skill5 = skill5_input
        baal.skill6 = skill6_input
        baal.skill7 = skill7_input
        baal.skill8 = skill8_input

# Registration option for Odin
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = odin.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        odin.level = level_input
        odin.st = st_input
        odin.ma = ma_input
        odin.en = en_input
        odin.ag = ag_input
        odin.lu = lu_input
        odin.skill1 = skill1_input
        odin.skill2 = skill2_input
        odin.skill3 = skill3_input
        odin.skill4 = skill4_input
        odin.skill5 = skill5_input
        odin.skill6 = skill6_input
        odin.skill7 = skill7_input
        odin.skill8 = skill8_input



# Personas Options    
elif arcana_choice == 6:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[5]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hierophant_personas()
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Berith
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = berith.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            berith.level = level_input
            berith.st = st_input
            berith.ma = ma_input
            berith.en = en_input
            berith.ag = ag_input
            berith.lu = lu_input
            berith.skill1 = skill1_input
            berith.skill2 = skill2_input
            berith.skill3 = skill3_input
            berith.skill4 = skill4_input
            berith.skill5 = skill5_input
            berith.skill6 = skill6_input
            berith.skill7 = skill7_input
            berith.skill8 = skill8_input

# Registration option for Orobas
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = orobas.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        orobas.level = level_input
        orobas.st = st_input
        orobas.ma = ma_input
        orobas.en = en_input
        orobas.ag = ag_input
        orobas.lu = lu_input
        orobas.skill1 = skill1_input
        orobas.skill2 = skill2_input
        orobas.skill3 = skill3_input
        orobas.skill4 = skill4_input
        orobas.skill5 = skill5_input
        orobas.skill6 = skill6_input
        orobas.skill7 = skill7_input
        orobas.skill8 = skill8_input

# Registration option for Anzu
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = anzu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        anzu.level = level_input
        anzu.st = st_input
        anzu.ma = ma_input
        anzu.en = en_input
        anzu.ag = ag_input
        anzu.lu = lu_input
        anzu.skill1 = skill1_input
        anzu.skill2 = skill2_input
        anzu.skill3 = skill3_input
        anzu.skill4 = skill4_input
        anzu.skill5 = skill5_input
        anzu.skill6 = skill6_input
        anzu.skill7 = skill7_input
        anzu.skill8 = skill8_input

# Registration option for Daisoujou
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = daisoujou.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        daisoujou.level = level_input
        daisoujou.st = st_input
        daisoujou.ma = ma_input
        daisoujou.en = en_input
        daisoujou.ag = ag_input
        daisoujou.lu = lu_input
        daisoujou.skill1 = skill1_input
        daisoujou.skill2 = skill2_input
        daisoujou.skill3 = skill3_input
        daisoujou.skill4 = skill4_input
        daisoujou.skill5 = skill5_input
        daisoujou.skill6 = skill6_input
        daisoujou.skill7 = skill7_input
        daisoujou.skill8 = skill8_input

# Registration option for Mishaguji
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mishaguji.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mishaguji.level = level_input
        mishaguji.st = st_input
        mishaguji.ma = ma_input
        mishaguji.en = en_input
        mishaguji.ag = ag_input
        mishaguji.lu = lu_input
        mishaguji.skill1 = skill1_input
        mishaguji.skill2 = skill2_input
        mishaguji.skill3 = skill3_input
        mishaguji.skill4 = skill4_input
        mishaguji.skill5 = skill5_input
        mishaguji.skill6 = skill6_input
        mishaguji.skill7 = skill7_input
        mishaguji.skill8 = skill8_input

# Registration option for Bishamonten
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = bishamonten.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        bishamonten.level = level_input
        bishamonten.st = st_input
        bishamonten.ma = ma_input
        bishamonten.en = en_input
        bishamonten.ag = ag_input
        bishamonten.lu = lu_input
        bishamonten.skill1 = skill1_input
        bishamonten.skill2 = skill2_input
        bishamonten.skill3 = skill3_input
        bishamonten.skill4 = skill4_input
        bishamonten.skill5 = skill5_input
        bishamonten.skill6 = skill6_input
        bishamonten.skill7 = skill7_input
        bishamonten.skill8 = skill8_input

# Registration option for Kohryu
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kohryu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kohryu.level = level_input
        kohryu.st = st_input
        kohryu.ma = ma_input
        kohryu.en = en_input
        kohryu.ag = ag_input
        kohryu.lu = lu_input
        kohryu.skill1 = skill1_input
        kohryu.skill2 = skill2_input
        kohryu.skill3 = skill3_input
        kohryu.skill4 = skill4_input
        kohryu.skill5 = skill5_input
        kohryu.skill6 = skill6_input
        kohryu.skill7 = skill7_input
        kohryu.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 7:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[6]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_lovers_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

    # Registration option for Pixie
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = pixie.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            pixie.level = level_input
            pixie.st = st_input
            pixie.ma = ma_input
            pixie.en = en_input
            pixie.ag = ag_input
            pixie.lu = lu_input
            pixie.skill1 = skill1_input
            pixie.skill2 = skill2_input
            pixie.skill3 = skill3_input
            pixie.skill4 = skill4_input
            pixie.skill5 = skill5_input
            pixie.skill6 = skill6_input
            pixie.skill7 = skill7_input
            pixie.skill8 = skill8_input

# Registration option for
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = saki_mitama.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        saki_mitama.level = level_input
        saki_mitama.st = st_input
        saki_mitama.ma = ma_input
        saki_mitama.en = en_input
        saki_mitama.ag = ag_input
        saki_mitama.lu = lu_input
        saki_mitama.skill1 = skill1_input
        saki_mitama.skill2 = skill2_input
        saki_mitama.skill3 = skill3_input
        saki_mitama.skill4 = skill4_input
        saki_mitama.skill5 = skill5_input
        saki_mitama.skill6 = skill6_input
        saki_mitama.skill7 = skill7_input
        saki_mitama.skill8 = skill8_input

# Registration option for Ame-no-Uzume
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ame_no_uzume.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ame_no_uzume.level = level_input
        ame_no_uzume.st = st_input
        ame_no_uzume.ma = ma_input
        ame_no_uzume.en = en_input
        ame_no_uzume.ag = ag_input
        ame_no_uzume.lu = lu_input
        ame_no_uzume.skill1 = skill1_input
        ame_no_uzume.skill2 = skill2_input
        ame_no_uzume.skill3 = skill3_input
        ame_no_uzume.skill4 = skill4_input
        ame_no_uzume.skill5 = skill5_input
        ame_no_uzume.skill6 = skill6_input
        ame_no_uzume.skill7 = skill7_input
        ame_no_uzume.skill8 = skill8_input

# Registration option for Leanan Sidhe
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = leanan_sidhe.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        leanan_sidhe.level = level_input
        leanan_sidhe.st = st_input
        leanan_sidhe.ma = ma_input
        leanan_sidhe.en = en_input
        leanan_sidhe.ag = ag_input
        leanan_sidhe.lu = lu_input
        leanan_sidhe.skill1 = skill1_input
        leanan_sidhe.skill2 = skill2_input
        leanan_sidhe.skill3 = skill3_input
        leanan_sidhe.skill4 = skill4_input
        leanan_sidhe.skill5 = skill5_input
        leanan_sidhe.skill6 = skill6_input
        leanan_sidhe.skill7 = skill7_input
        leanan_sidhe.skill8 = skill8_input

# Registration option for
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kushinada.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kushinada.level = level_input
        kushinada.st = st_input
        kushinada.ma = ma_input
        kushinada.en = en_input
        kushinada.ag = ag_input
        kushinada.lu = lu_input
        kushinada.skill1 = skill1_input
        kushinada.skill2 = skill2_input
        kushinada.skill3 = skill3_input
        kushinada.skill4 = skill4_input
        kushinada.skill5 = skill5_input
        kushinada.skill6 = skill6_input
        kushinada.skill7 = skill7_input
        kushinada.skill8 = skill8_input

# Registration option for Narcissus
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = narcissus.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        narcissus.level = level_input
        narcissus.st = st_input
        narcissus.ma = ma_input
        narcissus.en = en_input
        narcissus.ag = ag_input
        narcissus.lu = lu_input
        narcissus.skill1 = skill1_input
        narcissus.skill2 = skill2_input
        narcissus.skill3 = skill3_input
        narcissus.skill4 = skill4_input
        narcissus.skill5 = skill5_input
        narcissus.skill6 = skill6_input
        narcissus.skill7 = skill7_input
        narcissus.skill8 = skill8_input

# Registration option for Parvati
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = parvati.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        parvati.level = level_input
        parvati.st = st_input
        parvati.ma = ma_input
        parvati.en = en_input
        parvati.ag = ag_input
        parvati.lu = lu_input
        parvati.skill1 = skill1_input
        parvati.skill2 = skill2_input
        parvati.skill3 = skill3_input
        parvati.skill4 = skill4_input
        parvati.skill5 = skill5_input
        parvati.skill6 = skill6_input
        parvati.skill7 = skill7_input
        parvati.skill8 = skill8_input

# Registration option for Ralphael
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ralphael.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ralphael.level = level_input
        ralphael.st = st_input
        ralphael.ma = ma_input
        ralphael.en = en_input
        ralphael.ag = ag_input
        ralphael.lu = lu_input
        ralphael.skill1 = skill1_input
        ralphael.skill2 = skill2_input
        ralphael.skill3 = skill3_input
        ralphael.skill4 = skill4_input
        ralphael.skill5 = skill5_input
        ralphael.skill6 = skill6_input
        ralphael.skill7 = skill7_input
        ralphael.skill8 = skill8_input

# Registration option for Ishtar
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ishtar.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ishtar.level = level_input
        ishtar.st = st_input
        ishtar.ma = ma_input
        ishtar.en = en_input
        ishtar.ag = ag_input
        ishtar.lu = lu_input
        ishtar.skill1 = skill1_input
        ishtar.skill2 = skill2_input
        ishtar.skill3 = skill3_input
        ishtar.skill4 = skill4_input
        ishtar.skill5 = skill5_input
        ishtar.skill6 = skill6_input
        ishtar.skill7 = skill7_input
        ishtar.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 8:
    # Sets the selected Arcana to the Chariot Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[7]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_chariot_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
# Registration option for Agathion
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = agathion.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            agathion.level = level_input
            agathion.st = st_input
            agathion.ma = ma_input
            agathion.en = en_input
            agathion.ag = ag_input
            agathion.lu = lu_input
            agathion.skill1 = skill1_input
            agathion.skill2 = skill2_input
            agathion.skill3 = skill3_input
            agathion.skill4 = skill4_input
            agathion.skill5 = skill5_input
            agathion.skill6 = skill6_input
            agathion.skill7 = skill7_input
            agathion.skill8 = skill8_input

# Registration option for Slime
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = slime.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        slime.level = level_input
        slime.st = st_input
        slime.ma = ma_input
        slime.en = en_input
        slime.ag = ag_input
        slime.lu = lu_input
        slime.skill1 = skill1_input
        slime.skill2 = skill2_input
        slime.skill3 = skill3_input
        slime.skill4 = skill4_input
        slime.skill5 = skill5_input
        slime.skill6 = skill6_input
        slime.skill7 = skill7_input
        slime.skill8 = skill8_input

# Registration option for Shiki-Ouji
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = shiki_ouji.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        shiki_ouji.level = level_input
        shiki_ouji.st = st_input
        shiki_ouji.ma = ma_input
        shiki_ouji.en = en_input
        shiki_ouji.ag = ag_input
        shiki_ouji.lu = lu_input
        shiki_ouji.skill1 = skill1_input
        shiki_ouji.skill2 = skill2_input
        shiki_ouji.skill3 = skill3_input
        shiki_ouji.skill4 = skill4_input
        shiki_ouji.skill5 = skill5_input
        shiki_ouji.skill6 = skill6_input
        shiki_ouji.skill7 = skill7_input
        shiki_ouji.skill8 = skill8_input

# Registration option for Kin_ki
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kin_ki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kin_ki.level = level_input
        kin_ki.st = st_input
        kin_ki.ma = ma_input
        kin_ki.en = en_input
        kin_ki.ag = ag_input
        kin_ki.lu = lu_input
        kin_ki.skill1 = skill1_input
        kin_ki.skill2 = skill2_input
        kin_ki.skill3 = skill3_input
        kin_ki.skill4 = skill4_input
        kin_ki.skill5 = skill5_input
        kin_ki.skill6 = skill6_input
        kin_ki.skill7 = skill7_input
        kin_ki.skill8 = skill8_input

# Registration option for Ara Mitama
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ara_mitama.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ara_mitama.level = level_input
        ara_mitama.st = st_input
        ara_mitama.ma = ma_input
        ara_mitama3.en = en_input
        ara_mitama.ag = ag_input
        ara_mitama.lu = lu_input
        ara_mitama.skill1 = skill1_input
        ara_mitama.skill2 = skill2_input
        ara_mitama.skill3 = skill3_input
        ara_mitama.skill4 = skill4_input
        ara_mitama.skill5 = skill5_input
        ara_mitama.skill6 = skill6_input
        ara_mitama.skill7 = skill7_input
        ara_mitama.skill8 = skill8_input

# Registration option for White Rider
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = white_rider.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        white_rider.level = level_input
        white_rider.st = st_input
        white_rider.ma = ma_input
        white_rider.en = en_input
        white_rider.ag = ag_input
        white_rider.lu = lu_input
        white_rider.skill1 = skill1_input
        white_rider.skill2 = skill2_input
        white_rider.skill3 = skill3_input
        white_rider.skill4 = skill4_input
        white_rider.skill5 = skill5_input
        white_rider.skill6 = skill6_input
        white_rider.skill7 = skill7_input
        white_rider.skill8 = skill8_input

# Registration option for Athena
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = athena.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        athena.level = level_input
        athena.st = st_input
        athena.ma = ma_input
        athena.en = en_input
        athena.ag = ag_input
        athena.lu = lu_input
        athena.skill1 = skill1_input
        athena.skill2 = skill2_input
        athena.skill3 = skill3_input
        athena.skill4 = skill4_input
        athena.skill5 = skill5_input
        athena.skill6 = skill6_input
        athena.skill7 = skill7_input
        athena.skill8 = skill8_input

# Registration option for Athena Picaro
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = athena_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        athena_picaro.level = level_input
        athena_picaro.st = st_input
        athena_picaro.ma = ma_input
        athena_picaro.en = en_input
        athena_picaro.ag = ag_input
        athena_picaro.lu = lu_input
        athena_picaro.skill1 = skill1_input
        athena_picaro.skill2 = skill2_input
        athena_picaro.skill3 = skill3_input
        athena_picaro.skill4 = skill4_input
        athena_picaro.skill5 = skill5_input
        athena_picaro.skill6 = skill6_input
        athena_picaro.skill7 = skill7_input
        athena_picaro.skill8 = skill8_input

# Registration option for Cerberus
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = cerberus.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        cerberus.level = level_input
        cerberus.st = st_input
        cerberus.ma = ma_input
        cerberus.en = en_input
        cerberus.ag = ag_input
        cerberus.lu = lu_input
        cerberus.skill1 = skill1_input
        cerberus.skill2 = skill2_input
        cerberus.skill3 = skill3_input
        cerberus.skill4 = skill4_input
        cerberus.skill5 = skill5_input
        cerberus.skill6 = skill6_input
        cerberus.skill7 = skill7_input
        cerberus.skill8 = skill8_input

# Registration option for Thor
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = thor.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        thor.level = level_input
        thor.st = st_input
        thor.ma = ma_input
        thor.en = en_input
        thor.ag = ag_input
        thor.lu = lu_input
        thor.skill1 = skill1_input
        thor.skill2 = skill2_input
        thor.skill3 = skill3_input
        thor.skill4 = skill4_input
        thor.skill5 = skill5_input
        thor.skill6 = skill6_input
        thor.skill7 = skill7_input
        thor.skill8 = skill8_input

# Registration option for Chi You
elif persona_choice == 11:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = chi_you.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        chi_you.level = level_input
        chi_you.st = st_input
        chi_you.ma = ma_input
        chi_you.en = en_input
        chi_you.ag = ag_input
        chi_you.lu = lu_input
        chi_you.skill1 = skill1_input
        chi_you.skill2 = skill2_input
        chi_you.skill3 = skill3_input
        chi_you.skill4 = skill4_input
        chi_you.skill5 = skill5_input
        chi_you.skill6 = skill6_input
        chi_you.skill7 = skill7_input
        chi_you.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 9:
    # Sets the selected Arcana to the Justice Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[8]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_justice_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Angel
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = angel.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            angel.level = level_input
            angel.st = st_input
            angel.ma = ma_input
            angel.en = en_input
            angel.ag = ag_input
            angel.lu = lu_input
            angel.skill1 = skill1_input
            angel.skill2 = skill2_input
            angel.skill3 = skill3_input
            angel.skill4 = skill4_input
            angel.skill5 = skill5_input
            angel.skill6 = skill6_input
            angel.skill7 = skill7_input
            angel.skill8 = skill8_input

# Registration option for Archangel
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = archangel.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        archangel.level = level_input
        archangel.st = st_input
        archangel.ma = ma_input
        archangel.en = en_input
        archangel.ag = ag_input
        archangel.lu = lu_input
        archangel.skill1 = skill1_input
        archangel.skill2 = skill2_input
        archangel.skill3 = skill3_input
        archangel.skill4 = skill4_input
        archangel.skill5 = skill5_input
        archangel.skill6 = skill6_input
        archangel.skill7 = skill7_input
        archangel.skill8 = skill8_input

# Registration option for Principality
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = principality.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        principality.level = level_input
        principality.st = st_input
        principality.ma = ma_input
        principality.en = en_input
        principality.ag = ag_input
        principality.lu = lu_input
        principality.skill1 = skill1_input
        principality.skill2 = skill2_input
        principality.skill3 = skill3_input
        principality.skill4 = skill4_input
        principality.skill5 = skill5_input
        principality.skill6 = skill6_input
        principality.skill7 = skill7_input
        principality.skill8 = skill8_input

# Registration option for Power
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = power.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        power.level = level_input
        power.st = st_input
        power.ma = ma_input
        power.en = en_input
        power.ag = ag_input
        power.lu = lu_input
        power.skill1 = skill1_input
        power.skill2 = skill2_input
        power.skill3 = skill3_input
        power.skill4 = skill4_input
        power.skill5 = skill5_input
        power.skill6 = skill6_input
        power.skill7 = skill7_input
        power.skill8 = skill8_input

# Registration option for Melchizedek
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = melchizedek.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        melchizedek.level = level_input
        melchizedek.st = st_input
        melchizedek.ma = ma_input
        melchizedek.en = en_input
        melchizedek.ag = ag_input
        melchizedek.lu = lu_input
        melchizedek.skill1 = skill1_input
        melchizedek.skill2 = skill2_input
        melchizedek.skill3 = skill3_input
        melchizedek.skill4 = skill4_input
        melchizedek.skill5 = skill5_input
        melchizedek.skill6 = skill6_input
        melchizedek.skill7 = skill7_input
        melchizedek.skill8 = skill8_input

# Registration option for Throne
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = throne.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        throne.level = level_input
        throne.st = st_input
        throne.ma = ma_input
        throne.en = en_input
        throne.ag = ag_input
        throne.lu = lu_input
        throne.skill1 = skill1_input
        throne.skill2 = skill2_input
        throne.skill3 = skill3_input
        throne.skill4 = skill4_input
        throne.skill5 = skill5_input
        throne.skill6 = skill6_input
        throne.skill7 = skill7_input
        throne.skill8 = skill8_input

# Registration option for Uriel
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = uriel.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        uriel.level = level_input
        uriel.st = st_input
        uriel.ma = ma_input
        uriel.en = en_input
        uriel.ag = ag_input
        uriel.lu = lu_input
        uriel.skill1 = skill1_input
        uriel.skill2 = skill2_input
        uriel.skill3 = skill3_input
        uriel.skill4 = skill4_input
        uriel.skill5 = skill5_input
        uriel.skill6 = skill6_input
        uriel.skill7 = skill7_input
        uriel.skill8 = skill8_input

# Registration option for Metatron
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = metatron.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        metatron.level = level_input
        metatron.st = st_input
        metatron.ma = ma_input
        metatron.en = en_input
        metatron.ag = ag_input
        metatron.lu = lu_input
        metatron.skill1 = skill1_input
        metatron.skill2 = skill2_input
        metatron.skill3 = skill3_input
        metatron.skill4 = skill4_input
        metatron.skill5 = skill5_input
        metatron.skill6 = skill6_input
        metatron.skill7 = skill7_input
        metatron.skill8 = skill8_input



# Personas Options    
elif arcana_choice == 10:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[9]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hermit_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Bicorn
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = bicorn.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            bicorn.level = level_input
            bicorn.st = st_input
            bicorn.ma = ma_input
            bicorn.en = en_input
            bicorn.ag = ag_input
            bicorn.lu = lu_input
            bicorn.skill1 = skill1_input
            bicorn.skill2 = skill2_input
            bicorn.skill3 = skill3_input
            bicorn.skill4 = skill4_input
            bicorn.skill5 = skill5_input
            bicorn.skill6 = skill6_input
            bicorn.skill7 = skill7_input
            bicorn.skill8 = skill8_input

# Registration option for Koropokkuru
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = koropokkuru.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        koropokkuru.level = level_input
        koropokkuru.st = st_input
        koropokkuru.ma = ma_input
        koropokkuru.en = en_input
        koropokkuru.ag = ag_input
        koropokkuru.lu = lu_input
        koropokkuru.skill1 = skill1_input
        koropokkuru.skill2 = skill2_input
        koropokkuru.skill3 = skill3_input
        koropokkuru.skill4 = skill4_input
        koropokkuru.skill5 = skill5_input
        koropokkuru.skill6 = skill6_input
        koropokkuru.skill7 = skill7_input
        koropokkuru.skill8 = skill8_input

# Registration option for Ippon Datara
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ippon_datara.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ippon_datara.level = level_input
        ippon_datara.st = st_input
        ippon_datara.ma = ma_input
        ippon_datara.en = en_input
        ippon_datara.ag = ag_input
        ippon_datara.lu = lu_input
        ippon_datara.skill1 = skill1_input
        ippon_datara.skill2 = skill2_input
        ippon_datara.skill3 = skill3_input
        ippon_datara.skill4 = skill4_input
        ippon_datara.skill5 = skill5_input
        ippon_datara.skill6 = skill6_input
        ippon_datara.skill7 = skill7_input
        ippon_datara.skill8 = skill8_input

# Registration option for Sudama
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = sudama.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        sudama.level = level_input
        sudama.st = st_input
        sudama.ma = ma_input
        sudama.en = en_input
        sudama.ag = ag_input
        sudama.lu = lu_input
        sudama.skill1 = skill1_input
        sudama.skill2 = skill2_input
        sudama.skill3 = skill3_input
        sudama.skill4 = skill4_input
        sudama.skill5 = skill5_input
        sudama.skill6 = skill6_input
        sudama.skill7 = skill7_input
        sudama.skill8 = skill8_input

# Registration option for Naga
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = naga.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        naga.level = level_input
        naga.st = st_input
        naga.ma = ma_input
        naga.en = en_input
        naga.ag = ag_input
        naga.lu = lu_input
        naga.skill1 = skill1_input
        naga.skill2 = skill2_input
        naga.skill3 = skill3_input
        naga.skill4 = skill4_input
        naga.skill5 = skill5_input
        naga.skill6 = skill6_input
        naga.skill7 = skill7_input
        naga.skill8 = skill8_input

# Registration option for Kurama Tengu
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kurama_tengu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kurama_tengu.level = level_input
        kurama_tengu.st = st_input
        kurama_tengu.ma = ma_input
        kurama_tengu.en = en_input
        kurama_tengu.ag = ag_input
        kurama_tengu.lu = lu_input
        kurama_tengu.skill1 = skill1_input
        kurama_tengu.skill2 = skill2_input
        kurama_tengu.skill3 = skill3_input
        kurama_tengu.skill4 = skill4_input
        kurama_tengu.skill5 = skill5_input
        kurama_tengu.skill6 = skill6_input
        kurama_tengu.skill7 = skill7_input
        kurama_tengu.skill8 = skill8_input

# Registration option for Arahabaki
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = arahabaki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        arahabaki.level = level_input
        arahabaki.st = st_input
        arahabaki.ma = ma_input
        arahabaki.en = en_input
        arahabaki.ag = ag_input
        arahabaki.lu = lu_input
        arahabaki.skill1 = skill1_input
        arahabaki.skill2 = skill2_input
        arahabaki.skill3 = skill3_input
        arahabaki.skill4 = skill4_input
        arahabaki.skill5 = skill5_input
        arahabaki.skill6 = skill6_input
        arahabaki.skill7 = skill7_input
        arahabaki.skill8 = skill8_input

# Registration option for Kumbhanda
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kumbhanda.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kumbhanda.level = level_input
        kumbhanda.st = st_input
        kumbhanda.ma = ma_input
        kumbhanda.en = en_input
        kumbhanda.ag = ag_input
        kumbhanda.lu = lu_input
        kumbhanda.skill1 = skill1_input
        kumbhanda.skill2 = skill2_input
        kumbhanda.skill3 = skill3_input
        kumbhanda.skill4 = skill4_input
        kumbhanda.skill5 = skill5_input
        kumbhanda.skill6 = skill6_input
        kumbhanda.skill7 = skill7_input
        kumbhanda.skill8 = skill8_input

# Registration option for Koumokuten
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = koumokuten.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        koumokuten.level = level_input
        koumokuten.st = st_input
        koumokuten.ma = ma_input
        koumokuten.en = en_input
        koumokuten.ag = ag_input
        koumokuten.lu = lu_input
        koumokuten.skill1 = skill1_input
        koumokuten.skill2 = skill2_input
        koumokuten.skill3 = skill3_input
        koumokuten.skill4 = skill4_input
        koumokuten.skill5 = skill5_input
        koumokuten.skill6 = skill6_input
        koumokuten.skill7 = skill7_input
        koumokuten.skill8 = skill8_input

# Registration option for Loa 
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = loa.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        loa.level = level_input
        loa.st = st_input
        loa.ma = ma_input
        loa.en = en_input
        loa.ag = ag_input
        loa.lu = lu_input
        loa.skill1 = skill1_input
        loa.skill2 = skill2_input
        loa.skill3 = skill3_input
        loa.skill4 = skill4_input
        loa.skill5 = skill5_input
        loa.skill6 = skill6_input
        loa.skill7 = skill7_input
        loa.skill8 = skill8_input

# Registration option for Fafnir
elif persona_choice == 11:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = fafnir.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        fafnir.level = level_input
        fafnir.st = st_input
        fafnir.ma = ma_input
        fafnir.en = en_input
        fafnir.ag = ag_input
        fafnir.lu = lu_input
        fafnir.skill1 = skill1_input
        fafnir.skill2 = skill2_input
        fafnir.skill3 = skill3_input
        fafnir.skill4 = skill4_input
        fafnir.skill5 = skill5_input
        fafnir.skill6 = skill6_input
        fafnir.skill7 = skill7_input
        fafnir.skill8 = skill8_input

# Registration option for Ongyo-Ki
elif persona_choice == 12:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ongyo_ki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ongyo_ki.level = level_input
        ongyo_ki.st = st_input
        ongyo_ki.ma = ma_input
        ongyo_ki.en = en_input
        ongyo_ki.ag = ag_input
        ongyo_ki.lu = lu_input
        ongyo_ki.skill1 = skill1_input
        ongyo_ki.skill2 = skill2_input
        ongyo_ki.skill3 = skill3_input
        ongyo_ki.skill4 = skill4_input
        ongyo_ki.skill5 = skill5_input
        ongyo_ki.skill6 = skill6_input
        ongyo_ki.skill7 = skill7_input
        ongyo_ki.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 11:
    # Sets the selected Arcana to the Fortune Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[10]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_fortune_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Stone of Scone
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = stone_of_scone.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            stone_of_scone.level = level_input
            stone_of_scone.st = st_input
            stone_of_scone.ma = ma_input
            stone_of_scone.en = en_input
            stone_of_scone.ag = ag_input
            stone_of_scone.lu = lu_input
            stone_of_scone.skill1 = skill1_input
            stone_of_scone.skill2 = skill2_input
            stone_of_scone.skill3 = skill3_input
            stone_of_scone.skill4 = skill4_input
            stone_of_scone.skill5 = skill5_input
            stone_of_scone.skill6 = skill6_input
            stone_of_scone.skill7 = skill7_input
            stone_of_scone.skill8 = skill8_input

# Registration option for Clotho
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = clotho.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        clotho.level = level_input
        clotho.st = st_input
        clotho.ma = ma_input
        clotho.en = en_input
        clotho.ag = ag_input
        clotho.lu = lu_input
        clotho.skill1 = skill1_input
        clotho.skill2 = skill2_input
        clotho.skill3 = skill3_input
        clotho.skill4 = skill4_input
        clotho.skill5 = skill5_input
        clotho.skill6 = skill6_input
        clotho.skill7 = skill7_input
        clotho.skill8 = skill8_input

# Registration option for Ariadne
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ariadne.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ariadne.level = level_input
        ariadne.st = st_input
        ariadne.ma = ma_input
        ariadne.en = en_input
        ariadne.ag = ag_input
        ariadne.lu = lu_input
        ariadne.skill1 = skill1_input
        ariadne.skill2 = skill2_input
        ariadne.skill3 = skill3_input
        ariadne.skill4 = skill4_input
        ariadne.skill5 = skill5_input
        ariadne.skill6 = skill6_input
        ariadne.skill7 = skill7_input
        ariadne.skill8 = skill8_input

# Registration option for Lachesis
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = lachesis.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        lachesis.level = level_input
        lachesis.st = st_input
        lachesis.ma = ma_input
        lachesis.en = en_input
        lachesis.ag = ag_input
        lachesis.lu = lu_input
        lachesis.skill1 = skill1_input
        lachesis.skill2 = skill2_input
        lachesis.skill3 = skill3_input
        lachesis.skill4 = skill4_input
        lachesis.skill5 = skill5_input
        lachesis.skill6 = skill6_input
        lachesis.skill7 = skill7_input
        lachesis.skill8 = skill8_input

# Registration option for Atropos
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = atropos.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        atropos.level = level_input
        atropos.st = st_input
        atropos.ma = ma_input
        atropos.en = en_input
        atropos.ag = ag_input
        atropos.lu = lu_input
        atropos.skill1 = skill1_input
        atropos.skill2 = skill2_input
        atropos.skill3 = skill3_input
        atropos.skill4 = skill4_input
        atropos.skill5 = skill5_input
        atropos.skill6 = skill6_input
        atropos.skill7 = skill7_input
        atropos.skill8 = skill8_input

# Registration option for Ariadne Picaro
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ariadne_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ariadne_picaro.level = level_input
        ariadne_picaro.st = st_input
        ariadne_picaro.ma = ma_input
        ariadne_picaro.en = en_input
        ariadne_picaro.ag = ag_input
        ariadne_picaro.lu = lu_input
        ariadne_picaro.skill1 = skill1_input
        ariadne_picaro.skill2 = skill2_input
        ariadne_picaro.skill3 = skill3_input
        ariadne_picaro.skill4 = skill4_input
        ariadne_picaro.skill5 = skill5_input
        ariadne_picaro.skill6 = skill6_input
        ariadne_picaro.skill7 = skill7_input
        ariadne_picaro.skill8 = skill8_input

# Registration option for Fortuna
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = fortuna.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        fortuna.level = level_input
        fortuna.st = st_input
        fortuna.ma = ma_input
        fortuna.en = en_input
        fortuna.ag = ag_input
        fortuna.lu = lu_input
        fortuna.skill1 = skill1_input
        fortuna.skill2 = skill2_input
        fortuna.skill3 = skill3_input
        fortuna.skill4 = skill4_input
        fortuna.skill5 = skill5_input
        fortuna.skill6 = skill6_input
        fortuna.skill7 = skill7_input
        fortuna.skill8 = skill8_input

# Registration option for Norn
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = norn.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        norn.level = level_input
        norn.st = st_input
        norn.ma = ma_input
        norn.en = en_input
        norn.ag = ag_input
        norn.lu = lu_input
        norn.skill1 = skill1_input
        norn.skill2 = skill2_input
        norn.skill3 = skill3_input
        norn.skill4 = skill4_input
        norn.skill5 = skill5_input
        norn.skill6 = skill6_input
        norn.skill7 = skill7_input
        norn.skill8 = skill8_input

# Registration option for Asterius
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = asterius.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        asterius.level = level_input
        asterius.st = st_input
        asterius.ma = ma_input
        asterius.en = en_input
        asterius.ag = ag_input
        asterius.lu = lu_input
        asterius.skill1 = skill1_input
        asterius.skill2 = skill2_input
        asterius.skill3 = skill3_input
        asterius.skill4 = skill4_input
        asterius.skill5 = skill5_input
        asterius.skill6 = skill6_input
        asterius.skill7 = skill7_input
        asterius.skill8 = skill8_input

# Registration option for Asterius Picaro
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = asterius_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        asterius_picaro.level = level_input
        asterius_picaro.st = st_input
        asterius_picaro.ma = ma_input
        asterius_picaro.en = en_input
        asterius_picaro.ag = ag_input
        asterius_picaro.lu = lu_input
        asterius_picaro.skill1 = skill1_input
        asterius_picaro.skill2 = skill2_input
        asterius_picaro.skill3 = skill3_input
        asterius_picaro.skill4 = skill4_input
        asterius_picaro.skill5 = skill5_input
        asterius_picaro.skill6 = skill6_input
        asterius_picaro.skill7 = skill7_input
        asterius_picaro.skill8 = skill8_input

# Registration option for Lakshmi
elif persona_choice == 11:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = lakshmi.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        lakshmi.level = level_input
        lakshmi.st = st_input
        lakshmi.ma = ma_input
        lakshmi.en = en_input
        lakshmi.ag = ag_input
        lakshmi.lu = lu_input
        lakshmi.skill1 = skill1_input
        lakshmi.skill2 = skill2_input
        lakshmi.skill3 = skill3_input
        lakshmi.skill4 = skill4_input
        lakshmi.skill5 = skill5_input
        lakshmi.skill6 = skill6_input
        lakshmi.skill7 = skill7_input
        lakshmi.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 12:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[11]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_strength_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Kelpie
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = kelpie.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            kelpie.level = level_input
            kelpie.st = st_input
            kelpie.ma = ma_input
            kelpie.en = en_input
            kelpie.ag = ag_input
            kelpie.lu = lu_input
            kelpie.skill1 = skill1_input
            kelpie.skill2 = skill2_input
            kelpie.skill3 = skill3_input
            kelpie.skill4 = skill4_input
            kelpie.skill5 = skill5_input
            kelpie.skill6 = skill6_input
            kelpie.skill7 = skill7_input
            kelpie.skill8 = skill8_input

# Registration option for Shiisa
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = shiisa.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        shiisa.level = level_input
        shiisa.st = st_input
        shiisa.ma = ma_input
        shiisa.en = en_input
        shiisa.ag = ag_input
        shiisa.lu = lu_input
        shiisa.skill1 = skill1_input
        shiisa.skill2 = skill2_input
        shiisa.skill3 = skill3_input
        shiisa.skill4 = skill4_input
        shiisa.skill5 = skill5_input
        shiisa.skill6 = skill6_input
        shiisa.skill7 = skill7_input
        shiisa.skill8 = skill8_input

# Registration option for Oni
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = oni.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        oni.level = level_input
        oni.st = st_input
        oni.ma = ma_input
        oni.en = en_input
        oni.ag = ag_input
        oni.lu = lu_input
        oni.skill1 = skill1_input
        oni.skill2 = skill2_input
        oni.skill3 = skill3_input
        oni.skill4 = skill4_input
        oni.skill5 = skill5_input
        oni.skill6 = skill6_input
        oni.skill7 = skill7_input
        oni.skill8 = skill8_input

# Registration option for Rakshasa
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = rakshasa.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        rakshasa.level = level_input
        rakshasa.st = st_input
        rakshasa.ma = ma_input
        rakshasa.en = en_input
        rakshasa.ag = ag_input
        rakshasa.lu = lu_input
        rakshasa.skill1 = skill1_input
        rakshasa.skill2 = skill2_input
        rakshasa.skill3 = skill3_input
        rakshasa.skill4 = skill4_input
        rakshasa.skill5 = skill5_input
        rakshasa.skill6 = skill6_input
        rakshasa.skill7 = skill7_input
        rakshasa.skill8 = skill8_input

# Registration option for Orlov
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = orlov.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        orlov.level = level_input
        orlov.st = st_input
        orlov.ma = ma_input
        orlov.en = en_input
        orlov.ag = ag_input
        orlov.lu = lu_input
        orlov.skill1 = skill1_input
        orlov.skill2 = skill2_input
        orlov.skill3 = skill3_input
        orlov.skill4 = skill4_input
        orlov.skill5 = skill5_input
        orlov.skill6 = skill6_input
        orlov.skill7 = skill7_input
        orlov.skill8 = skill8_input

# Registration option for Zouchouten
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = zouchouten.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        zouchouten.level = level_input
        zouchouten.st = st_input
        zouchouten.ma = ma_input
        zouchouten.en = en_input
        zouchouten.ag = ag_input
        zouchouten.lu = lu_input
        zouchouten.skill1 = skill1_input
        zouchouten.skill2 = skill2_input
        zouchouten.skill3 = skill3_input
        zouchouten.skill4 = skill4_input
        zouchouten.skill5 = skill5_input
        zouchouten.skill6 = skill6_input
        zouchouten.skill7 = skill7_input
        zouchouten.skill8 = skill8_input

# Registration option for Valkyrie
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = valkyrie.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        valkyrie.level = level_input
        valkyrie.st = st_input
        valkyrie.ma = ma_input
        valkyrie.en = en_input
        valkyrie.ag = ag_input
        valkyrie.lu = lu_input
        valkyrie.skill1 = skill1_input
        valkyrie.skill2 = skill2_input
        valkyrie.skill3 = skill3_input
        valkyrie.skill4 = skill4_input
        valkyrie.skill5 = skill5_input
        valkyrie.skill6 = skill6_input
        valkyrie.skill7 = skill7_input
        valkyrie.skill8 = skill8_input

# Registration option for Hanuman
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = hanuman.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        hanuman.level = level_input
        hanuman.st = st_input
        hanuman.ma = ma_input
        hanuman.en = en_input
        hanuman.ag = ag_input
        hanuman.lu = lu_input
        hanuman.skill1 = skill1_input
        hanuman.skill2 = skill2_input
        hanuman.skill3 = skill3_input
        hanuman.skill4 = skill4_input
        hanuman.skill5 = skill5_input
        hanuman.skill6 = skill6_input
        hanuman.skill7 = skill7_input
        hanuman.skill8 = skill8_input

# Registration option for Chimera
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = chimera.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        chimera.level = level_input
        chimera.st = st_input
        chimera.ma = ma_input
        chimera.en = en_input
        chimera.ag = ag_input
        chimera.lu = lu_input
        chimera.skill1 = skill1_input
        chimera.skill2 = skill2_input
        chimera.skill3 = skill3_input
        chimera.skill4 = skill4_input
        chimera.skill5 = skill5_input
        chimera.skill6 = skill6_input
        chimera.skill7 = skill7_input
        chimera.skill8 = skill8_input

# Registration option for Zaou-Gongen
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = zaou_gongen.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        zaou_gongen.level = level_input
        zaou_gongen.st = st_input
        zaou_gongen.ma = ma_input
        zaou_gongen.en = en_input
        zaou_gongen.ag = ag_input
        zaou_gongen.lu = lu_input
        zaou_gongen.skill1 = skill1_input
        zaou_gongen.skill2 = skill2_input
        zaou_gongen.skill3 = skill3_input
        zaou_gongen.skill4 = skill4_input
        zaou_gongen.skill5 = skill5_input
        zaou_gongen.skill6 = skill6_input
        zaou_gongen.skill7 = skill7_input
        zaou_gongen.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 13:
    # Sets the selected Arcana to the Hanged Man Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[12]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hanged_man_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

    # Registration option for Hua Po
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = hua_po.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            hua_po.level = level_input
            hua_po.st = st_input
            hua_po.ma = ma_input
            hua_po.en = en_input
            hua_po.ag = ag_input
            hua_po.lu = lu_input
            hua_po.skill1 = skill1_input
            hua_po.skill2 = skill2_input
            hua_po.skill3 = skill3_input
            hua_po.skill4 = skill4_input
            hua_po.skill5 = skill5_input
            hua_po.skill6 = skill6_input
            hua_po.skill7 = skill7_input
            hua_po.skill8 = skill8_input

# Registration option for Inugami
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = inugami.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        inugami.level = level_input
        inugami.st = st_input
        inugami.ma = ma_input
        inugami.en = en_input
        inugami.ag = ag_input
        inugami.lu = lu_input
        inugami.skill1 = skill1_input
        inugami.skill2 = skill2_input
        inugami.skill3 = skill3_input
        inugami.skill4 = skill4_input
        inugami.skill5 = skill5_input
        inugami.skill6 = skill6_input
        inugami.skill7 = skill7_input
        inugami.skill8 = skill8_input

# Registration option for Orthrus
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = orthrus.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        orthrus.level = level_input
        orthrus.st = st_input
        orthrus.ma = ma_input
        orthrus.en = en_input
        orthrus.ag = ag_input
        orthrus.lu = lu_input
        orthrus.skill1 = skill1_input
        orthrus.skill2 = skill2_input
        orthrus.skill3 = skill3_input
        orthrus.skill4 = skill4_input
        orthrus.skill5 = skill5_input
        orthrus.skill6 = skill6_input
        orthrus.skill7 = skill7_input
        orthrus.skill8 = skill8_input

# Registration option for Take-Minakata
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = take_minakata.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        take_minakata.level = level_input
        take_minakata.st = st_input
        take_minakata.ma = ma_input
        take_minakata.en = en_input
        take_minakata.ag = ag_input
        take_minakata.lu = lu_input
        take_minakata.skill1 = skill1_input
        take_minakata.skill2 = skill2_input
        take_minakata.skill3 = skill3_input
        take_minakata.skill4 = skill4_input
        take_minakata.skill5 = skill5_input
        take_minakata.skill6 = skill6_input
        take_minakata.skill7 = skill7_input
        take_minakata.skill8 = skill8_input

# Registration option for Emperor's Amulet
elif persona_choice == 5:
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
        emperors_amulet.level = level_input
        emperors_amulet.st = st_input
        emperors_amulet.ma = ma_input
        emperors_amulet.en = en_input
        emperors_amulet.ag = ag_input
        emperors_amulet.lu = lu_input
        emperors_amulet.skill1 = skill1_input
        emperors_amulet.skill2 = skill2_input
        emperors_amulet.skill3 = skill3_input
        emperors_amulet.skill4 = skill4_input
        emperors_amulet.skill5 = skill5_input
        emperors_amulet.skill6 = skill6_input
        emperors_amulet.skill7 = skill7_input
        emperors_amulet.skill8 = skill8_input

# Registration option for Hecatoncheires
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = hecatoncheires.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        hecatoncheires.level = level_input
        hecatoncheires.st = st_input
        hecatoncheires.ma = ma_input
        hecatoncheires.en = en_input
        hecatoncheires.ag = ag_input
        hecatoncheires.lu = lu_input
        hecatoncheires.skill1 = skill1_input
        hecatoncheires.skill2 = skill2_input
        hecatoncheires.skill3 = skill3_input
        hecatoncheires.skill4 = skill4_input
        hecatoncheires.skill5 = skill5_input
        hecatoncheires.skill6 = skill6_input
        hecatoncheires.skill7 = skill7_input
        hecatoncheires.skill8 = skill8_input

# Registration option for Jatayu
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = jatayu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        jatayu.level = level_input
        jatayu.st = st_input
        jatayu.ma = ma_input
        jatayu.en = en_input
        jatayu.ag = ag_input
        jatayu.lu = lu_input
        jatayu.skill1 = skill1_input
        jatayu.skill2 = skill2_input
        jatayu.skill3 = skill3_input
        jatayu.skill4 = skill4_input
        jatayu.skill5 = skill5_input
        jatayu.skill6 = skill6_input
        jatayu.skill7 = skill7_input
        jatayu.skill8 = skill8_input

# Registration option for Moloch
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = moloch.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        moloch.level = level_input
        moloch.st = st_input
        moloch.ma = ma_input
        moloch.en = en_input
        moloch.ag = ag_input
        moloch.lu = lu_input
        moloch.skill1 = skill1_input
        moloch.skill2 = skill2_input
        moloch.skill3 = skill3_input
        moloch.skill4 = skill4_input
        moloch.skill5 = skill5_input
        moloch.skill6 = skill6_input
        moloch.skill7 = skill7_input
        moloch.skill8 = skill8_input

# Registration option for Macabre
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = macabre.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        macabre.level = level_input
        macabre.st = st_input
        macabre.ma = ma_input
        macabre.en = en_input
        macabre.ag = ag_input
        macabre.lu = lu_input
        macabre.skill1 = skill1_input
        macabre.skill2 = skill2_input
        macabre.skill3 = skill3_input
        macabre.skill4 = skill4_input
        macabre.skill5 = skill5_input
        macabre.skill6 = skill6_input
        macabre.skill7 = skill7_input
        macabre.skill8 = skill8_input

# Registration option for Attis
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = attis.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        attis.level = level_input
        attis.st = st_input
        attis.ma = ma_input
        attis.en = en_input
        attis.ag = ag_input
        attis.lu = lu_input
        attis.skill1 = skill1_input
        attis.skill2 = skill2_input
        attis.skill3 = skill3_input
        attis.skill4 = skill4_input
        attis.skill5 = skill5_input
        attis.skill6 = skill6_input
        attis.skill7 = skill7_input
        attis.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 14:
    # Sets the selected Arcana to the Death Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[13]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_death_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Death
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = mandrake.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            mandrake.level = level_input
            mandrake.st = st_input
            mandrake.ma = ma_input
            mandrake.en = en_input
            mandrake.ag = ag_input
            mandrake.lu = lu_input
            mandrake.skill1 = skill1_input
            mandrake.skill2 = skill2_input
            mandrake.skill3 = skill3_input
            mandrake.skill4 = skill4_input
            mandrake.skill5 = skill5_input
            mandrake.skill6 = skill6_input
            mandrake.skill7 = skill7_input
            mandrake.skill8 = skill8_input

# Registration option for Mokoi
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mokoi.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mokoi.level = level_input
        mokoi.st = st_input
        mokoi.ma = ma_input
        mokoi.en = en_input
        mokoi.ag = ag_input
        mokoi.lu = lu_input
        mokoi.skill1 = skill1_input
        mokoi.skill2 = skill2_input
        mokoi.skill3 = skill3_input
        mokoi.skill4 = skill4_input
        mokoi.skill5 = skill5_input
        mokoi.skill6 = skill6_input
        mokoi.skill7 = skill7_input
        mokoi.skill8 = skill8_input

# Registration option for Matador
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = matador.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        matador.level = level_input
        matador.st = st_input
        matador.ma = ma_input
        matador.en = en_input
        matador.ag = ag_input
        matador.lu = lu_input
        matador.skill1 = skill1_input
        matador.skill2 = skill2_input
        matador.skill3 = skill3_input
        matador.skill4 = skill4_input
        matador.skill5 = skill5_input
        matador.skill6 = skill6_input
        matador.skill7 = skill7_input
        matador.skill8 = skill8_input

# Registration option for Nue
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = nue.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        nue.level = level_input
        nue.st = st_input
        nue.ma = ma_input
        nue.en = en_input
        nue.ag = ag_input
        nue.lu = lu_input
        nue.skill1 = skill1_input
        nue.skill2 = skill2_input
        nue.skill3 = skill3_input
        nue.skill4 = skill4_input
        nue.skill5 = skill5_input
        nue.skill6 = skill6_input
        nue.skill7 = skill7_input
        nue.skill8 = skill8_input

# Registration option for Pisaca
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = pisaca.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        pisaca.level = level_input
        pisaca.st = st_input
        pisaca.ma = ma_input
        pisaca.en = en_input
        pisaca.ag = ag_input
        pisaca.lu = lu_input
        pisaca.skill1 = skill1_input
        pisaca.skill2 = skill2_input
        pisaca.skill3 = skill3_input
        pisaca.skill4 = skill4_input
        pisaca.skill5 = skill5_input
        pisaca.skill6 = skill6_input
        pisaca.skill7 = skill7_input
        pisaca.skill8 = skill8_input

# Registration option for Hell Biker
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = hell_biker.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        hell_biker.level = level_input
        hell_biker.st = st_input
        hell_biker.ma = ma_input
        hell_biker.en = en_input
        hell_biker.ag = ag_input
        hell_biker.lu = lu_input
        hell_biker.skill1 = skill1_input
        hell_biker.skill2 = skill2_input
        hell_biker.skill3 = skill3_input
        hell_biker.skill4 = skill4_input
        hell_biker.skill5 = skill5_input
        hell_biker.skill6 = skill6_input
        hell_biker.skill7 = skill7_input
        hell_biker.skill8 = skill8_input

# Registration option for Hope Diamond 
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = hope_diamond .get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        hope_diamond .level = level_input
        hope_diamond .st = st_input
        hope_diamond .ma = ma_input
        hope_diamond .en = en_input
        hope_diamond .ag = ag_input
        hope_diamond .lu = lu_input
        hope_diamond .skill1 = skill1_input
        hope_diamond .skill2 = skill2_input
        hope_diamond .skill3 = skill3_input
        hope_diamond .skill4 = skill4_input
        hope_diamond .skill5 = skill5_input
        hope_diamond .skill6 = skill6_input
        hope_diamond .skill7 = skill7_input
        hope_diamond .skill8 = skill8_input

# Registration option for Pale Rider
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = pale_rider.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        pale_rider.level = level_input
        pale_rider.st = st_input
        pale_rider.ma = ma_input
        pale_rider.en = en_input
        pale_rider.ag = ag_input
        pale_rider.lu = lu_input
        pale_rider.skill1 = skill1_input
        pale_rider.skill2 = skill2_input
        pale_rider.skill3 = skill3_input
        pale_rider.skill4 = skill4_input
        pale_rider.skill5 = skill5_input
        pale_rider.skill6 = skill6_input
        pale_rider.skill7 = skill7_input
        pale_rider.skill8 = skill8_input

# Registration option for Chernobog
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = chernobog.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        chernobog.level = level_input
        chernobog.st = st_input
        chernobog.ma = ma_input
        chernobog.en = en_input
        chernobog.ag = ag_input
        chernobog.lu = lu_input
        chernobog.skill1 = skill1_input
        chernobog.skill2 = skill2_input
        chernobog.skill3 = skill3_input
        chernobog.skill4 = skill4_input
        chernobog.skill5 = skill5_input
        chernobog.skill6 = skill6_input
        chernobog.skill7 = skill7_input
        chernobog.skill8 = skill8_input

# Registration option for Thanatos 
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = thanatos.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        thanatos.level = level_input
        thanatos.st = st_input
        thanatos.ma = ma_input
        thanatos.en = en_input
        thanatos.ag = ag_input
        thanatos.lu = lu_input
        thanatos.skill1 = skill1_input
        thanatos.skill2 = skill2_input
        thanatos.skill3 = skill3_input
        thanatos.skill4 = skill4_input
        thanatos.skill5 = skill5_input
        thanatos.skill6 = skill6_input
        thanatos.skill7 = skill7_input
        thanatos.skill8 = skill8_input

# Registration option for Thanatos Picaro
elif persona_choice == 11:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = thanatos_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        thanatos_picaro.level = level_input
        thanatos_picaro.st = st_input
        thanatos_picaro.ma = ma_input
        thanatos_picaro.en = en_input
        thanatos_picaro.ag = ag_input
        thanatos_picaro.lu = lu_input
        thanatos_picaro.skill1 = skill1_input
        thanatos_picaro.skill2 = skill2_input
        thanatos_picaro.skill3 = skill3_input
        thanatos_picaro.skill4 = skill4_input
        thanatos_picaro.skill5 = skill5_input
        thanatos_picaro.skill6 = skill6_input
        thanatos_picaro.skill7 = skill7_input
        thanatos_picaro.skill8 = skill8_input

# Registration option for Mot 
elif persona_choice == 12:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mot.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mot.level = level_input
        mot.st = st_input
        mot.ma = ma_input
        mot.en = en_input
        mot.ag = ag_input
        mot.lu = lu_input
        mot.skill1 = skill1_input
        mot.skill2 = skill2_input
        mot.skill3 = skill3_input
        mot.skill4 = skill4_input
        mot.skill5 = skill5_input
        mot.skill6 = skill6_input
        mot.skill7 = skill7_input
        mot.skill8 = skill8_input

# Registration option for Alice
elif persona_choice == 13:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = alice.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        alice.level = level_input
        alice.st = st_input
        alice.ma = ma_input
        alice.en = en_input
        alice.ag = ag_input
        alice.lu = lu_input
        alice.skill1 = skill1_input
        alice.skill2 = skill2_input
        alice.skill3 = skill3_input
        alice.skill4 = skill4_input
        alice.skill5 = skill5_input
        alice.skill6 = skill6_input
        alice.skill7 = skill7_input
        alice.skill8 = skill8_input
    

# Personas Options    
elif arcana_choice == 15:
    # Sets the selected Arcana to the Temperance Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[14]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_temperance_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = genbu.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            genbu.level = level_input
            genbu.st = st_input
            genbu.ma = ma_input
            genbu.en = en_input
            genbu.ag = ag_input
            genbu.lu = lu_input
            genbu.skill1 = skill1_input
            genbu.skill2 = skill2_input
            genbu.skill3 = skill3_input
            genbu.skill4 = skill4_input
            genbu.skill5 = skill5_input
            genbu.skill6 = skill6_input
            genbu.skill7 = skill7_input
            genbu.skill8 = skill8_input

# Registration option for Koppa Tengu
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = koppa_tengu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        koppa_tengu.level = level_input
        koppa_tengu.st = st_input
        koppa_tengu.ma = ma_input
        koppa_tengu.en = en_input
        koppa_tengu.ag = ag_input
        koppa_tengu.lu = lu_input
        koppa_tengu.skill1 = skill1_input
        koppa_tengu.skill2 = skill2_input
        koppa_tengu.skill3 = skill3_input
        koppa_tengu.skill4 = skill4_input
        koppa_tengu.skill5 = skill5_input
        koppa_tengu.skill6 = skill6_input
        koppa_tengu.skill7 = skill7_input
        koppa_tengu.skill8 = skill8_input

# Registration option for Makami
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = makami.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        makami.level = level_input
        makami.st = st_input
        makami.ma = ma_input
        makami.en = en_input
        makami.ag = ag_input
        makami.lu = lu_input
        makami.skill1 = skill1_input
        makami.skill2 = skill2_input
        makami.skill3 = skill3_input
        makami.skill4 = skill4_input
        makami.skill5 = skill5_input
        makami.skill6 = skill6_input
        makami.skill7 = skill7_input
        makami.skill8 = skill8_input

# Registration option for Jikokuten
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = jikokuten.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        jikokuten.level = level_input
        jikokuten.st = st_input
        jikokuten.ma = ma_input
        jikokuten.en = en_input
        jikokuten.ag = ag_input
        jikokuten.lu = lu_input
        jikokuten.skill1 = skill1_input
        jikokuten.skill2 = skill2_input
        jikokuten.skill3 = skill3_input
        jikokuten.skill4 = skill4_input
        jikokuten.skill5 = skill5_input
        jikokuten.skill6 = skill6_input
        jikokuten.skill7 = skill7_input
        jikokuten.skill8 = skill8_input

# Registration option for Mithra
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mithra.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mithra.level = level_input
        mithra.st = st_input
        mithra.ma = ma_input
        mithra.en = en_input
        mithra.ag = ag_input
        mithra.lu = lu_input
        mithra.skill1 = skill1_input
        mithra.skill2 = skill2_input
        mithra.skill3 = skill3_input
        mithra.skill4 = skill4_input
        mithra.skill5 = skill5_input
        mithra.skill6 = skill6_input
        mithra.skill7 = skill7_input
        mithra.skill8 = skill8_input

# Registration option for Byakko
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = byakko.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        byakko.level = level_input
        byakko.st = st_input
        byakko.ma = ma_input
        byakko.en = en_input
        byakko.ag = ag_input
        byakko.lu = lu_input
        byakko.skill1 = skill1_input
        byakko.skill2 = skill2_input
        byakko.skill3 = skill3_input
        byakko.skill4 = skill4_input
        byakko.skill5 = skill5_input
        byakko.skill6 = skill6_input
        byakko.skill7 = skill7_input
        byakko.skill8 = skill8_input

# Registration option for Raja Naga
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = raja_naga.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        raja_naga.level = level_input
        raja_naga.st = st_input
        raja_naga.ma = ma_input
        raja_naga.en = en_input
        raja_naga.ag = ag_input
        raja_naga.lu = lu_input
        raja_naga.skill1 = skill1_input
        raja_naga.skill2 = skill2_input
        raja_naga.skill3 = skill3_input
        raja_naga.skill4 = skill4_input
        raja_naga.skill5 = skill5_input
        raja_naga.skill6 = skill6_input
        raja_naga.skill7 = skill7_input
        raja_naga.skill8 = skill8_input

# Registration option for Gabriel
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = gabriel.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        gabriel.level = level_input
        gabriel.st = st_input
        gabriel.ma = ma_input
        gabriel.en = en_input
        gabriel.ag = ag_input
        gabriel.lu = lu_input
        gabriel.skill1 = skill1_input
        gabriel.skill2 = skill2_input
        gabriel.skill3 = skill3_input
        gabriel.skill4 = skill4_input
        gabriel.skill5 = skill5_input
        gabriel.skill6 = skill6_input
        gabriel.skill7 = skill7_input
        gabriel.skill8 = skill8_input

# Registration option for Ardha
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ardha.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ardha.level = level_input
        ardha.st = st_input
        ardha.ma = ma_input
        ardha.en = en_input
        ardha.ag = ag_input
        ardha.lu = lu_input
        ardha.skill1 = skill1_input
        ardha.skill2 = skill2_input
        ardha.skill3 = skill3_input
        ardha.skill4 = skill4_input
        ardha.skill5 = skill5_input
        ardha.skill6 = skill6_input
        ardha.skill7 = skill7_input
        ardha.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 16:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[15]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_devil_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Incubus
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = incubus.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            incubus.level = level_input
            incubus.st = st_input
            incubus.ma = ma_input
            incubus.en = en_input
            incubus.ag = ag_input
            incubus.lu = lu_input
            incubus.skill1 = skill1_input
            incubus.skill2 = skill2_input
            incubus.skill3 = skill3_input
            incubus.skill4 = skill4_input
            incubus.skill5 = skill5_input
            incubus.skill6 = skill6_input
            incubus.skill7 = skill7_input
            incubus.skill8 = skill8_input

# Registration option for Flauros
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = flauros.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        flauros.level = level_input
        flauros.st = st_input
        flauros.ma = ma_input
        flauros.en = en_input
        flauros.ag = ag_input
        flauros.lu = lu_input
        flauros.skill1 = skill1_input
        flauros.skill2 = skill2_input
        flauros.skill3 = skill3_input
        flauros.skill4 = skill4_input
        flauros.skill5 = skill5_input
        flauros.skill6 = skill6_input
        flauros.skill7 = skill7_input
        flauros.skill8 = skill8_input

# Registration option for Andras
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = andras.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        andras.level = level_input
        andras.st = st_input
        andras.ma = ma_input
        andras.en = en_input
        andras.ag = ag_input
        andras.lu = lu_input
        andras.skill1 = skill1_input
        andras.skill2 = skill2_input
        andras.skill3 = skill3_input
        andras.skill4 = skill4_input
        andras.skill5 = skill5_input
        andras.skill6 = skill6_input
        andras.skill7 = skill7_input
        andras.skill8 = skill8_input

# Registration option for Lilim
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = lilim.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        lilim.level = level_input
        lilim.st = st_input
        lilim.ma = ma_input
        lilim.en = en_input
        lilim.ag = ag_input
        lilim.lu = lu_input
        lilim.skill1 = skill1_input
        lilim.skill2 = skill2_input
        lilim.skill3 = skill3_input
        lilim.skill4 = skill4_input
        lilim.skill5 = skill5_input
        lilim.skill6 = skill6_input
        lilim.skill7 = skill7_input
        lilim.skill8 = skill8_input

# Registration option for Pazuzu
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = pazuzu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        pazuzu.level = level_input
        pazuzu.st = st_input
        pazuzu.ma = ma_input
        pazuzu.en = en_input
        pazuzu.ag = ag_input
        pazuzu .lu = lu_input
        pazuzu.skill1 = skill1_input
        pazuzu.skill2 = skill2_input
        pazuzu.skill3 = skill3_input
        pazuzu.skill4 = skill4_input
        pazuzu.skill5 = skill5_input
        pazuzu.skill6 = skill6_input
        pazuzu.skill7 = skill7_input
        pazuzu.skill8 = skill8_input

# Registration option for Baphomet
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = baphomet.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        baphomet.level = level_input
        baphomet.st = st_input
        baphomet.ma = ma_input
        baphomet.en = en_input
        baphomet.ag = ag_input
        baphomet.lu = lu_input
        baphomet.skill1 = skill1_input
        baphomet.skill2 = skill2_input
        baphomet.skill3 = skill3_input
        baphomet.skill4 = skill4_input
        baphomet.skill5 = skill5_input
        baphomet.skill6 = skill6_input
        baphomet.skill7 = skill7_input
        baphomet.skill8 = skill8_input

# Registration option for Nebiros
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = nebiros.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        nebiros.level = level_input
        nebiros.st = st_input
        nebiros.ma = ma_input
        nebiros.en = en_input
        nebiros.ag = ag_input
        nebiros.lu = lu_input
        nebiros.skill1 = skill1_input
        nebiros.skill2 = skill2_input
        nebiros.skill3 = skill3_input
        nebiros.skill4 = skill4_input
        nebiros.skill5 = skill5_input
        nebiros.skill6 = skill6_input
        nebiros.skill7 = skill7_input
        nebiros.skill8 = skill8_input

# Registration option for Belial
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = belial.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        belial.level = level_input
        belial.st = st_input
        belial.ma = ma_input
        belial.en = en_input
        belial.ag = ag_input
        belial.lu = lu_input
        belial.skill1 = skill1_input
        belial.skill2 = skill2_input
        belial.skill3 = skill3_input
        belial.skill4 = skill4_input
        belial.skill5 = skill5_input
        belial.skill6 = skill6_input
        belial.skill7 = skill7_input
        belial.skill8 = skill8_input

# Registration option for Beelzebub
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = beelzebub.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        beelzebub.level = level_input
        beelzebub.st = st_input
        beelzebub.ma = ma_input
        beelzebub.en = en_input
        beelzebub.ag = ag_input
        beelzebub.lu = lu_input
        beelzebub.skill1 = skill1_input
        beelzebub.skill2 = skill2_input
        beelzebub.skill3 = skill3_input
        beelzebub.skill4 = skill4_input
        beelzebub.skill5 = skill5_input
        beelzebub.skill6 = skill6_input
        beelzebub.skill7 = skill7_input
        beelzebub.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 17:
    # Sets the selected Arcana to the Tower Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[16]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_tower_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = belphegor.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            belphegor.level = level_input
            belphegor.st = st_input
            belphegor.ma = ma_input
            belphegor.en = en_input
            belphegor.ag = ag_input
            belphegor.lu = lu_input
            belphegor.skill1 = skill1_input
            belphegor.skill2 = skill2_input
            belphegor.skill3 = skill3_input
            belphegor.skill4 = skill4_input
            belphegor.skill5 = skill5_input
            belphegor.skill6 = skill6_input
            belphegor.skill7 = skill7_input
            belphegor.skill8 = skill8_input

# Registration option for Red Rider 
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = red_rider.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        red_rider.level = level_input
        red_rider.st = st_input
        red_rider.ma = ma_input
        red_rider.en = en_input
        red_rider.ag = ag_input
        red_rider.lu = lu_input
        red_rider.skill1 = skill1_input
        red_rider.skill2 = skill2_input
        red_rider.skill3 = skill3_input
        red_rider.skill4 = skill4_input
        red_rider.skill5 = skill5_input
        red_rider.skill6 = skill6_input
        red_rider.skill7 = skill7_input
        red_rider.skill8 = skill8_input

# Registration option for Magatsu-Izanagi
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = magatsu_izanagi.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        magatsu_izanagi.level = level_input
        magatsu_izanagi.st = st_input
        magatsu_izanagi.ma = ma_input
        magatsu_izanagi.en = en_input
        magatsu_izanagi.ag = ag_input
        magatsu_izanagi.lu = lu_input
        magatsu_izanagi.skill1 = skill1_input
        magatsu_izanagi.skill2 = skill2_input
        magatsu_izanagi.skill3 = skill3_input
        magatsu_izanagi.skill4 = skill4_input
        magatsu_izanagi.skill5 = skill5_input
        magatsu_izanagi.skill6 = skill6_input
        magatsu_izanagi.skill7 = skill7_input
        magatsu_izanagi.skill8 = skill8_input

# Registration option for Seth
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = seth.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        seth.level = level_input
        seth.st = st_input
        seth.ma = ma_input
        seth.en = en_input
        seth.ag = ag_input
        seth.lu = lu_input
        seth.skill1 = skill1_input
        seth.skill2 = skill2_input
        seth.skill3 = skill3_input
        seth.skill4 = skill4_input
        seth.skill5 = skill5_input
        seth.skill6 = skill6_input
        seth.skill7 = skill7_input
        seth.skill8 = skill8_input

# Registration option for Black Rider
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = black_rider.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        black_rider.level = level_input
        black_rider.st = st_input
        black_rider.ma = ma_input
        black_rider.en = en_input
        black_rider.ag = ag_input
        black_rider.lu = lu_input
        black_rider.skill1 = skill1_input
        black_rider.skill2 = skill2_input
        black_rider.skill3 = skill3_input
        black_rider.skill4 = skill4_input
        black_rider.skill5 = skill5_input
        black_rider.skill6 = skill6_input
        black_rider.skill7 = skill7_input
        black_rider.skill8 = skill8_input

# Registration option for Mara
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mara.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mara.level = level_input
        mara.st = st_input
        mara.ma = ma_input
        mara.en = en_input
        mara.ag = ag_input
        mara.lu = lu_input
        mara.skill1 = skill1_input
        mara.skill2 = skill2_input
        mara.skill3 = skill3_input
        mara.skill4 = skill4_input
        mara.skill5 = skill5_input
        mara.skill6 = skill6_input
        mara.skill7 = skill7_input
        mara.skill8 = skill8_input

# Registration option for Yoshitsune
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = yoshitsune.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        yoshitsune.level = level_input
        yoshitsune.st = st_input
        yoshitsune.ma = ma_input
        yoshitsune.en = en_input
        yoshitsune.ag = ag_input
        yoshitsune.lu = lu_input
        yoshitsune.skill1 = skill1_input
        yoshitsune.skill2 = skill2_input
        yoshitsune.skill3 = skill3_input
        yoshitsune.skill4 = skill4_input
        yoshitsune.skill5 = skill5_input
        yoshitsune.skill6 = skill6_input
        yoshitsune.skill7 = skill7_input
        yoshitsune.skill8 = skill8_input

# Registration option for Mada
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mada.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mada.level = level_input
        mada.st = st_input
        mada.ma = ma_input
        mada.en = en_input
        mada.ag = ag_input
        mada.lu = lu_input
        mada.skill1 = skill1_input
        mada.skill2 = skill2_input
        mada.skill3 = skill3_input
        mada.skill4 = skill4_input
        mada.skill5 = skill5_input
        mada.skill6 = skill6_input
        mada.skill7 = skill7_input
        mada.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 18:
    # Sets the selected Arcana to the Star Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[17]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_star_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Kodama
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = kodama.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            kodama.level = level_input
            kodama.st = st_input
            kodama.ma = ma_input
            kodama.en = en_input
            kodama.ag = ag_input
            kodama.lu = lu_input
            kodama.skill1 = skill1_input
            kodama.skill2 = skill2_input
            kodama.skill3 = skill3_input
            kodama.skill4 = skill4_input
            kodama.skill5 = skill5_input
            kodama.skill6 = skill6_input
            kodama.skill7 = skill7_input
            kodama.skill8 = skill8_input

# Registration option for Fuu-Ki
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = fuuki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        fuuki.level = level_input
        fuuki.st = st_input
        fuuki.ma = ma_input
        fuuki.en = en_input
        fuuki.ag = ag_input
        fuuki.lu = lu_input
        fuuki.skill1 = skill1_input
        fuuki.skill2 = skill2_input
        fuuki.skill3 = skill3_input
        fuuki.skill4 = skill4_input
        fuuki.skill5 = skill5_input
        fuuki.skill6 = skill6_input
        fuuki.skill7 = skill7_input
        fuuki.skill8 = skill8_input

# Registration option for Neko Shogun
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = neko_shogun.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        neko_shogun.level = level_input
        neko_shogun.st = st_input
        neko_shogun.ma = ma_input
        neko_shogun.en = en_input
        neko_shogun.ag = ag_input
        neko_shogun.lu = lu_input
        neko_shogun.skill1 = skill1_input
        neko_shogun.skill2 = skill2_input
        neko_shogun.skill3 = skill3_input
        neko_shogun.skill4 = skill4_input
        neko_shogun.skill5 = skill5_input
        neko_shogun.skill6 = skill6_input
        neko_shogun.skill7 = skill7_input
        neko_shogun.skill8 = skill8_input

# Registration option for Kaiwan
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kaiwan.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kaiwan.level = level_input
        kaiwan.st = st_input
        kaiwan.ma = ma_input
        kaiwan.en = en_input
        kaiwan.ag = ag_input
        kaiwan.lu = lu_input
        kaiwan.skill1 = skill1_input
        kaiwan.skill2 = skill2_input
        kaiwan.skill3 = skill3_input
        kaiwan.skill4 = skill4_input
        kaiwan.skill5 = skill5_input
        kaiwan.skill6 = skill6_input
        kaiwan.skill7 = skill7_input
        kaiwan.skill8 = skill8_input

# Registration option for Gardua
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = gardua.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        gardua.level = level_input
        gardua.st = st_input
        gardua.ma = ma_input
        gardua.en = en_input
        gardua.ag = ag_input
        gardua.lu = lu_input
        gardua.skill1 = skill1_input
        gardua.skill2 = skill2_input
        gardua.skill3 = skill3_input
        gardua.skill4 = skill4_input
        gardua.skill5 = skill5_input
        gardua.skill6 = skill6_input
        gardua.skill7 = skill7_input
        gardua.skill8 = skill8_input

# Registration option for Vasuki
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = vasuki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        vasuki.level = level_input
        vasuki.st = st_input
        vasuki.ma = ma_input
        vasuki.en = en_input
        vasuki.ag = ag_input
        vasuki.lu = lu_input
        vasuki.skill1 = skill1_input
        vasuki.skill2 = skill2_input
        vasuki.skill3 = skill3_input
        vasuki.skill4 = skill4_input
        vasuki.skill5 = skill5_input
        vasuki.skill6 = skill6_input
        vasuki.skill7 = skill7_input
        vasuki.skill8 = skill8_input

# Registration option for Sraosha
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = sraosha.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        sraosha.level = level_input
        sraosha.st = st_input
        sraosha.ma = ma_input
        sraosha.en = en_input
        sraosha.ag = ag_input
        sraosha.lu = lu_input
        sraosha.skill1 = skill1_input
        sraosha.skill2 = skill2_input
        sraosha.skill3 = skill3_input
        sraosha.skill4 = skill4_input
        sraosha.skill5 = skill5_input
        sraosha.skill6 = skill6_input
        sraosha.skill7 = skill7_input
        sraosha.skill8 = skill8_input

# Registration option for Hastur
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = hastur.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        hastur.level = level_input
        hastur.st = st_input
        hastur.ma = ma_input
        hastur.en = en_input
        hastur.ag = ag_input
        hastur.lu = lu_input
        hastur.skill1 = skill1_input
        hastur.skill2 = skill2_input
        hastur.skill3 = skill3_input
        hastur.skill4 = skill4_input
        hastur.skill5 = skill5_input
        hastur.skill6 = skill6_input
        hastur.skill7 = skill7_input
        hastur.skill8 = skill8_input

# Registration option for Lucifer
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = lucifer.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        lucifer.level = level_input
        lucifer.st = st_input
        lucifer.ma = ma_input
        lucifer.en = en_input
        lucifer.ag = ag_input
        lucifer.lu = lu_input
        lucifer.skill1 = skill1_input
        lucifer.skill2 = skill2_input
        lucifer.skill3 = skill3_input
        lucifer.skill4 = skill4_input
        lucifer.skill5 = skill5_input
        lucifer.skill6 = skill6_input
        lucifer.skill7 = skill7_input
        lucifer.skill8 = skill8_input

# Personas Options    
elif arcana_choice == 19:
    # Sets the selected Arcana to the Moon Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[18]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_moon_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Succubus
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = succbus.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            succbus.level = level_input
            succbus.st = st_input
            succbus.ma = ma_input
            succbus.en = en_input
            succbus.ag = ag_input
            succbus.lu = lu_input
            succbus.skill1 = skill1_input
            succbus.skill2 = skill2_input
            succbus.skill3 = skill3_input
            succbus.skill4 = skill4_input
            succbus.skill5 = skill5_input
            succbus.skill6 = skill6_input
            succbus.skill7 = skill7_input
            succbus.skill8 = skill8_input

# Registration option for Onmoraki
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = onmoraki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        onmoraki.level = level_input
        onmoraki.st = st_input
        onmoraki.ma = ma_input
        onmoraki.en = en_input
        onmoraki.ag = ag_input
        onmoraki.lu = lu_input
        onmoraki.skill1 = skill1_input
        onmoraki.skill2 = skill2_input
        onmoraki.skill3 = skill3_input
        onmoraki.skill4 = skill4_input
        onmoraki.skill5 = skill5_input
        onmoraki.skill6 = skill6_input
        onmoraki.skill7 = skill7_input
        onmoraki.skill8 = skill8_input

# Registration option for Kaguya
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kaguya.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kaguya.level = level_input
        kaguya.st = st_input
        kaguya.ma = ma_input
        kaguya.en = en_input
        kaguya.ag = ag_input
        kaguya.lu = lu_input
        kaguya.skill1 = skill1_input
        kaguya.skill2 = skill2_input
        kaguya.skill3 = skill3_input
        kaguya.skill4 = skill4_input
        kaguya.skill5 = skill5_input
        kaguya.skill6 = skill6_input
        kaguya.skill7 = skill7_input
        kaguya.skill8 = skill8_input

# Registration option for Black Ooze
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = black_ooze.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        black_ooze.level = level_input
        black_ooze.st = st_input
        black_ooze.ma = ma_input
        black_ooze.en = en_input
        black_ooze.ag = ag_input
        black_ooze.lu = lu_input
        black_ooze.skill1 = skill1_input
        black_ooze.skill2 = skill2_input
        black_ooze.skill3 = skill3_input
        black_ooze.skill4 = skill4_input
        black_ooze.skill5 = skill5_input
        black_ooze.skill6 = skill6_input
        black_ooze.skill7 = skill7_input
        black_ooze.skill8 = skill8_input

# Registration option for Sui-Ki
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = sui_ki.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        sui_ki.level = level_input
        sui_ki.st = st_input
        sui_ki.ma = ma_input
        sui_ki.en = en_input
        sui_ki.ag = ag_input
        sui_ki.lu = lu_input
        sui_ki.skill1 = skill1_input
        sui_ki.skill2 = skill2_input
        sui_ki.skill3 = skill3_input
        sui_ki.skill4 = skill4_input
        sui_ki.skill5 = skill5_input
        sui_ki.skill6 = skill6_input
        sui_ki.skill7 = skill7_input
        sui_ki.skill8 = skill8_input

# Registration option for Kaguya Picaro
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = kaguya_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        kaguya_picaro.level = level_input
        kaguya_picaro.st = st_input
        kaguya_picaro.ma = ma_input
        kaguya_picaro.en = en_input
        kaguya_picaro.ag = ag_input
        kaguya_picaro.lu = lu_input
        kaguya_picaro.skill1 = skill1_input
        kaguya_picaro.skill2 = skill2_input
        kaguya_picaro.skill3 = skill3_input
        kaguya_picaro.skill4 = skill4_input
        kaguya_picaro.skill5 = skill5_input
        kaguya_picaro.skill6 = skill6_input
        kaguya_picaro.skill7 = skill7_input
        kaguya_picaro.skill8 = skill8_input

# Registration option for Mothman
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mothman.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mothman.level = level_input
        mothman.st = st_input
        mothman.ma = ma_input
        mothman.en = en_input
        mothman.ag = ag_input
        mothman.lu = lu_input
        mothman.skill1 = skill1_input
        mothman.skill2 = skill2_input
        mothman.skill3 = skill3_input
        mothman.skill4 = skill4_input
        mothman.skill5 = skill5_input
        mothman.skill6 = skill6_input
        mothman.skill7 = skill7_input
        mothman.skill8 = skill8_input

# Registration option for Girimehkala 
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = girimehkala.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        girimehkala.level = level_input
        girimehkala.st = st_input
        girimehkala.ma = ma_input
        girimehkala.en = en_input
        girimehkala.ag = ag_input
        girimehkala.lu = lu_input
        girimehkala.skill1 = skill1_input
        girimehkala.skill2 = skill2_input
        girimehkala.skill3 = skill3_input
        girimehkala.skill4 = skill4_input
        girimehkala.skill5 = skill5_input
        girimehkala.skill6 = skill6_input
        girimehkala.skill7 = skill7_input
        girimehkala.skill8 = skill8_input

# Registration option for Tsukiyomi 
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = tsukiyomi.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        tsukiyomi.level = level_input
        tsukiyomi.st = st_input
        tsukiyomi.ma = ma_input
        tsukiyomi.en = en_input
        tsukiyomi.ag = ag_input
        tsukiyomi.lu = lu_input
        tsukiyomi.skill1 = skill1_input
        tsukiyomi.skill2 = skill2_input
        tsukiyomi.skill3 = skill3_input
        tsukiyomi.skill4 = skill4_input
        tsukiyomi.skill5 = skill5_input
        tsukiyomi.skill6 = skill6_input
        tsukiyomi.skill7 = skill7_input
        tsukiyomi.skill8 = skill8_input

# Registration option for Tsukiyomi Picaro
elif persona_choice == 10:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = tsukiyomi_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        tsukiyomi_picaro.level = level_input
        tsukiyomi_picaro.st = st_input
        tsukiyomi_picaro.ma = ma_input
        tsukiyomi_picaro.en = en_input
        tsukiyomi_picaro.ag = ag_input
        tsukiyomi_picaro.lu = lu_input
        tsukiyomi_picaro.skill1 = skill1_input
        tsukiyomi_picaro.skill2 = skill2_input
        tsukiyomi_picaro.skill3 = skill3_input
        tsukiyomi_picaro.skill4 = skill4_input
        tsukiyomi_picaro.skill5 = skill5_input
        tsukiyomi_picaro.skill6 = skill6_input
        tsukiyomi_picaro.skill7 = skill7_input
        tsukiyomi_picaro.skill8 = skill8_input

# Registration option for Lilith
elif persona_choice == 11:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = lilith.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        lilith.level = level_input
        lilith.st = st_input
        lilith.ma = ma_input
        lilith.en = en_input
        lilith.ag = ag_input
        lilith.lu = lu_input
        lilith.skill1 = skill1_input
        lilith.skill2 = skill2_input
        lilith.skill3 = skill3_input
        lilith.skill4 = skill4_input
        lilith.skill5 = skill5_input
        lilith.skill6 = skill6_input
        lilith.skill7 = skill7_input
        lilith.skill8 = skill8_input

# Registration option for Byakhee
elif persona_choice == 12:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = byakhee.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        byakhee.level = level_input
        byakhee.st = st_input
        byakhee.ma = ma_input
        byakhee.en = en_input
        byakhee.ag = ag_input
        byakhee.lu = lu_input
        byakhee.skill1 = skill1_input
        byakhee.skill2 = skill2_input
        byakhee.skill3 = skill3_input
        byakhee.skill4 = skill4_input
        byakhee.skill5 = skill5_input
        byakheeskill6 = skill6_input
        byakhee.skill7 = skill7_input
        byakhee.skill8 = skill8_input

# Registration option for Sandalphon
elif persona_choice == 13:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = sandalphon.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        sandalphon.level = level_input
        sandalphon.st = st_input
        sandalphon.ma = ma_input
        sandalphon.en = en_input
        sandalphon.ag = ag_input
        sandalphon.lu = lu_input
        sandalphon.skill1 = skill1_input
        sandalphon.skill2 = skill2_input
        sandalphon.skill3 = skill3_input
        sandalphon.skill4 = skill4_input
        sandalphon.skill5 = skill5_input
        sandalphon.skill6 = skill6_input
        sandalphon.skill7 = skill7_input
        sandalphon.skill8 = skill8_input

# Personas Options    
elif arcana_choice == 20:
    # Sets the selected Arcana to the Sun Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[19]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_sun_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Suzaku
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = suzaku.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            suzaku.level = level_input
            suzaku.st = st_input
            suzaku.ma = ma_input
            suzaku.en = en_input
            suzaku.ag = ag_input
            suzaku.lu = lu_input
            suzaku.skill1 = skill1_input
            suzaku.skill2 = skill2_input
            suzaku.skill3 = skill3_input
            suzaku.skill4 = skill4_input
            suzaku.skill5 = skill5_input
            suzaku.skill6 = skill6_input
            suzaku.skill7 = skill7_input
            suzaku.skill8 = skill8_input

# Registration option for Thunderbird
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = thunderbird.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        thunderbird.level = level_input
        thunderbird.st = st_input
        thunderbird.ma = ma_input
        thunderbird.en = en_input
        thunderbird.ag = ag_input
        thunderbird.lu = lu_input
        thunderbird.skill1 = skill1_input
        thunderbird.skill2 = skill2_input
        thunderbird.skill3 = skill3_input
        thunderbird.skill4 = skill4_input
        thunderbird.skill5 = skill5_input
        thunderbird.skill6 = skill6_input
        thunderbird.skill7 = skill7_input
        thunderbird.skill8 = skill8_input

# Registration option for Mithras
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = mithras.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        mithras.level = level_input
        mithras.st = st_input
        mithras.ma = ma_input
        mithras.en = en_input
        mithras.ag = ag_input
        mithras.lu = lu_input
        mithras.skill1 = skill1_input
        mithras.skill2 = skill2_input
        mithras.skill3 = skill3_input
        mithras.skill4 = skill4_input
        mithras.skill5 = skill5_input
        mithras.skill6 = skill6_input
        mithras.skill7 = skill7_input
        mithras.skill8 = skill8_input

# Registration option for Yurlungur
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = yurlungur.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        yurlungur.level = level_input
        yurlungur.st = st_input
        yurlungur.ma = ma_input
        yurlungur.en = en_input
        yurlungur.ag = ag_input
        yurlungur.lu = lu_input
        yurlungur.skill1 = skill1_input
        yurlungur.skill2 = skill2_input
        yurlungur.skill3 = skill3_input
        yurlungur.skill4 = skill4_input
        yurlungur.skill5 = skill5_input
        yurlungur.skill6 = skill6_input
        yurlungur.skill7 = skill7_input
        yurlungur.skill8 = skill8_input

# Registration option for Horus
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = horus.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        horus.level = level_input
        horus.st = st_input
        horus.ma = ma_input
        horus.en = en_input
        horus.ag = ag_input
        horus.lu = lu_input
        horus.skill1 = skill1_input
        horus.skill2 = skill2_input
        horus.skill3 = skill3_input
        horus.skill4 = skill4_input
        horus.skill5 = skill5_input
        horus.skill6 = skill6_input
        horus.skill7 = skill7_input
        horus.skill8 = skill8_input

# Registration option for Ganesha
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ganesha.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ganesha.level = level_input
        ganesha.st = st_input
        ganesha.ma = ma_input
        ganesha.en = en_input
        ganesha.ag = ag_input
        ganesha.lu = lu_input
        ganesha.skill1 = skill1_input
        ganesha.skill2 = skill2_input
        ganesha.skill3 = skill3_input
        ganesha.skill4 = skill4_input
        ganesha.skill5 = skill5_input
        ganesha.skill6 = skill6_input
        ganesha.skill7 = skill7_input
        ganesha.skill8 = skill8_input

# Registration option for Quetzalcoatl
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = quetzalcoatl.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        quetzalcoatl.level = level_input
        quetzalcoatl.st = st_input
        quetzalcoatl.ma = ma_input
        quetzalcoatl.en = en_input
        quetzalcoatl.ag = ag_input
        quetzalcoatl.lu = lu_input
        quetzalcoatl.skill1 = skill1_input
        quetzalcoatl.skill2 = skill2_input
        quetzalcoatl.skill3 = skill3_input
        quetzalcoatl.skill4 = skill4_input
        quetzalcoatl.skill5 = skill5_input
        quetzalcoatl.skill6 = skill6_input
        quetzalcoatl.skill7 = skill7_input
        quetzalcoatl.skill8 = skill8_input

# Registration option for Asura
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = asura.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        asura.level = level_input
        asura.st = st_input
        asura.ma = ma_input
        asura.en = en_input
        asura.ag = ag_input
        asura.lu = lu_input
        asura.skill1 = skill1_input
        asura.skill2 = skill2_input
        asura.skill3 = skill3_input
        asura.skill4 = skill4_input
        asura.skill5 = skill5_input
        asura.skill6 = skill6_input
        asura.skill7 = skill7_input
        asura.skill8 = skill8_input


# Personas Options    
elif arcana_choice == 21:
    # Sets the selected Arcana to the Judgement Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[20]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_judgement_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
# Registration option for Anubis
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = anubis.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            anubis.level = level_input
            anubis.st = st_input
            anubis.ma = ma_input
            anubis.en = en_input
            anubis.ag = ag_input
            anubis.lu = lu_input
            anubis.skill1 = skill1_input
            anubis.skill2 = skill2_input
            anubis.skill3 = skill3_input
            anubis.skill4 = skill4_input
            anubis.skill5 = skill5_input
            anubis.skill6 = skill6_input
            anubis.skill7 = skill7_input
            anubis.skill8 = skill8_input

# Registration option for Trumpeter
elif persona_choice == :
        print()
        # Call the function to get the stats from the user 
        stats_to_register = trumpeter.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        trumpeter.level = level_input
        trumpeter.st = st_input
        trumpeter.ma = ma_input
        trumpeter.en = en_input
        trumpeter.ag = ag_input
        trumpeter.lu = lu_input
        trumpeter.skill1 = skill1_input
        trumpeter.skill2 = skill2_input
        trumpeter.skill3 = skill3_input
        trumpeter.skill4 = skill4_input
        trumpeter.skill5 = skill5_input
        trumpeter.skill6 = skill6_input
        trumpeter.skill7 = skill7_input
        trumpeter.skill8 = skill8_input

# Registration option for Yamata-no-Orochi
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = yamata_no_orochi.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        yamata_no_orochi.level = level_input
        yamata_no_orochi.st = st_input
        yamata_no_orochi.ma = ma_input
        yamata_no_orochi.en = en_input
        yamata_no_orochi.ag = ag_input
        yamata_no_orochi.lu = lu_input
        yamata_no_orochi.skill1 = skill1_input
        yamata_no_orochi.skill2 = skill2_input
        yamata_no_orochi.skill3 = skill3_input
        yamata_no_orochi.skill4 = skill4_input
        yamata_no_orochi.skill5 = skill5_input
        yamata_no_orochi.skill6 = skill6_input
        yamata_no_orochi.skill7 = skill7_input
        yamata_no_orochi.skill8 = skill8_input

# Registration option for Abaddon
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = abaddon.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        abaddon.level = level_input
        abaddon.st = st_input
        abaddon.ma = ma_input
        abaddon.en = en_input
        abaddon.ag = ag_input
        abaddon.lu = lu_input
        abaddon.skill1 = skill1_input
        abaddon.skill2 = skill2_input
        abaddon.skill3 = skill3_input
        abaddon.skill5 = skill5_input
        abaddon.skill6 = skill6_input
        abaddon.skill7 = skill7_input
        abaddon.skill8 = skill8_input

# Registration option for Messiah
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = messiah.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        messiah.level = level_input
        messiah.st = st_input
        messiah.ma = ma_input
        messiah.en = en_input
        messiah.ag = ag_input
        messiah.lu = lu_input
        messiah.skill1 = skill1_input
        messiah.skill2 = skill2_input
        messiah.skill3 = skill3_input
        messiah.skill4 = skill4_input
        messiah.skill5 = skill5_input
        messiah.skill6 = skill6_input
        messiah.skill7 = skill7_input
        messiah.skill8 = skill8_input

# Registration option for Shiva
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = shiva.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        shiva.level = level_input
        shiva.st = st_input
        shiva.ma = ma_input
        shiva.en = en_input
        shiva.ag = ag_input
        shiva.lu = lu_input
        shiva.skill1 = skill1_input
        shiva.skill2 = skill2_input
        shiva.skill3 = skill3_input
        shiva.skill4 = skill4_input
        shiva.skill5 = skill5_input
        shiva.skill6 = skill6_input
        shiva.skill7 = skill7_input
        shiva.skill8 = skill8_input

# Registration option for Michael
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = michael.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        michael.level = level_input
        michael.st = st_input
        michael.ma = ma_input
        michael.en = en_input
        michael.ag = ag_input
        michael.lu = lu_input
        michael.skill1 = skill1_input
        michael.skill2 = skill2_input
        michael.skill3 = skill3_input
        michael.skill4 = skill4_input
        michael.skill5 = skill5_input
        michael.skill6 = skill6_input
        michael.skill7 = skill7_input
        michael.skill8 = skill8_input

# Registration option for Messiah Picaro
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = messiah_picaro.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        messiah_picaro.level = level_input
        messiah_picaro.st = st_input
        messiah_picaro.ma = ma_input
        messiah_picaro.en = en_input
        messiah_picaro.ag = ag_input
        messiah_picaro.lu = lu_input
        messiah_picaro.skill1 = skill1_input
        messiah_picaro.skill2 = skill2_input
        messiah_picaro.skill3 = skill3_input
        messiah_picaro.skill4 = skill4_input
        messiah_picaro.skill5 = skill5_input
        messiah_picaro.skill6 = skill6_input
        messiah_picaro.skill7 = skill7_input
        messiah_picaro.skill8 = skill8_input

# Registration option for Satan
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = satan.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        satan.level = level_input
        satan.st = st_input
        satan.ma = ma_input
        satan.en = en_input
        satan.ag = ag_input
        satan.lu = lu_input
        satan.skill1 = skill1_input
        satan.skill2 = skill2_input
        satan.skill3 = skill3_input
        satan.skill4 = skill4_input
        satan.skill5 = skill5_input
        satan.skill6 = skill6_input
        satan.skill7 = skill7_input
        satan.skill8 = skill8_input

# Personas Options    
elif arcana_choice == 22:
    # Sets the selected Arcana to the Faith Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[21]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_faith_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Phoenix
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = phoenix.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            phoenix.level = level_input
            phoenix.st = st_input
            phoenix.ma = ma_input
            phoenix.en = en_input
            phoenix.ag = ag_input
            phoenix.lu = lu_input
            phoenix.skill1 = skill1_input
            phoenix.skill2 = skill2_input
            phoenix.skill3 = skill3_input
            phoenix.skill4 = skill4_input
            phoenix.skill5 = skill5_input
            phoenix.skill6 = skill6_input
            phoenix.skill7 = skill7_input
            phoenix.skill8 = skill8_input

# Registration option for Tam Lin
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = tam_lin.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        tam_lin.level = level_input
        tam_lin.st = st_input
        tam_lin.ma = ma_input
        tam_lin.en = en_input
        tam_lin.ag = ag_input
        tam_lin.lu = lu_input
        tam_lin.skill1 = skill1_input
        tam_lin.skill2 = skill2_input
        tam_lin.skill3 = skill3_input
        tam_lin.skill4 = skill4_input
        tam_lin.skill5 = skill5_input
        tam_lin.skill6 = skill6_input
        tam_lin.skill7 = skill7_input
        tam_lin.skill8 = skill8_input

# Registration option for Unicorn
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = unicorn.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        unicorn.level = level_input
        unicorn.st = st_input
        unicorn.ma = ma_input
        unicorn.en = en_input
        unicorn.ag = ag_input
        unicorn.lu = lu_input
        unicorn.skill1 = skill1_input
        unicorn.skill2 = skill2_input
        unicorn.skill3 = skill3_input
        unicorn.skill4 = skill4_input
        unicorn.skill5 = skill5_input
        unicorn.skill6 = skill6_input
        unicorn.skill7 = skill7_input
        unicorn.skill8 = skill8_input

# Registration option for Okuninushi
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = okuninushi.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        okuninushi.level = level_input
        okuninushi.st = st_input
        okuninushi.ma = ma_input
        okuninushi.en = en_input
        okuninushi.ag = ag_input
        okuninushi.lu = lu_input
        okuninushi .skill1 = skill1_input
        okuninushi.skill2 = skill2_input
        okuninushi.skill3 = skill3_input
        okuninushi.skill4 = skill4_input
        okuninushi.skill5 = skill5_input
        okuninushi.skill6 = skill6_input
        okuninushi.skill7 = skill7_input
        okuninushi.skill8 = skill8_input

# Registration option for Orichalcum
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = orichalcum.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        orichalcum.level = level_input
        orichalcum.st = st_input
        orichalcum.ma = ma_input
        orichalcum.en = en_input
        orichalcum.ag = ag_input
        orichalcum.lu = lu_input
        orichalcum.skill1 = skill1_input
        orichalcum.skill2 = skill2_input
        orichalcum.skill3 = skill3_input
        orichalcum.skill4 = skill4_input
        orichalcum.skill5 = skill5_input
        orichalcum.skill6 = skill6_input
        orichalcum.skill7 = skill7_input
        orichalcum.skill8 = skill8_input

# Registration option for Atavaka
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = atavaka.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        atavaka.level = level_input
        atavaka.st = st_input
        atavaka.ma = ma_input
        atavaka.en = en_input
        atavaka.ag = ag_input
        atavaka.lu = lu_input
        atavaka.skill1 = skill1_input
        atavaka.skill2 = skill2_input
        atavaka.skill3 = skill3_input
        atavaka.skill4 = skill4_input
        atavaka.skill5 = skill5_input
        atavaka.skill6 = skill6_input
        atavaka.skill7 = skill7_input
        atavaka.skill8 = skill8_input

# Registration option for Cu Chulainn
elif persona_choice == 7:
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
        cu_chulainn.level = level_input
        cu_chulainn.st = st_input
        cu_chulainn.ma = ma_input
        cu_chulainn.en = en_input
        cu_chulainn.ag = ag_input
        cu_chulainn.lu = lu_input
        cu_chulainn.skill1 = skill1_input
        cu_chulainn.skill2 = skill2_input
        cu_chulainn.skill3 = skill3_input
        cu_chulainn.skill4 = skill4_input
        cu_chulainn.skill5 = skill5_input
        cu_chulainn.skill6 = skill6_input
        cu_chulainn.skill7 = skill7_input
        cu_chulainn.skill8 = skill8_input

# Registration option for Siegfried
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = siegfried.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        siegfried.level = level_input
        siegfried.st = st_input
        siegfried.ma = ma_input
        siegfried.en = en_input
        siegfried.ag = ag_input
        siegfried.lu = lu_input
        siegfried.skill1 = skill1_input
        siegfried.skill2 = skill2_input
        siegfried.skill3 = skill3_input
        siegfried.skill4 = skill4_input
        siegfried.skill5 = skill5_input
        siegfried.skill6 = skill6_input
        siegfried.skill7 = skill7_input
        siegfried.skill8 = skill8_input

# Registration option for Maria
elif persona_choice == 9:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = maria.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        maria.level = level_input
        maria.st = st_input
        maria.ma = ma_input
        maria.en = en_input
        maria.ag = ag_input
        maria.lu = lu_input
        maria.skill1 = skill1_input
        maria.skill2 = skill2_input
        maria.skill3 = skill3_input
        maria.skill4 = skill4_input
        maria.skill5 = skill5_input
        maria.skill6 = skill6_input
        maria.skill7 = skill7_input
        maria.skill8 = skill8_input

# Personas Options    
elif arcana_choice == 23:
    # Sets the selected Arcana to the Councillor Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[22]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_councillor_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    
    # Registration option for Kushi Mitama
    if persona_choice == 1:
            print()
            # Call the function to get the stats from the user 
            stats_to_register = kushi_mitama.get_persona_info()
            # Unpack them into values
            level_input = stats_to_register[0]
            st_input = stats_to_register[1]
            ma_input = stats_to_register[2]
            en_input = stats_to_register[3]
            ag_input = stats_to_register[4]
            lu_input = stats_to_register[5]
            skill1_input = stats_to_register[6]
            skill2_input = stats_to_register[7]
            skill3_input = stats_to_register[8]
            skill4_input = stats_to_register[9]
            skill5_input = stats_to_register[10]
            skill6_input = stats_to_register[11]
            skill7_input = stats_to_register[12]
            skill8_input = stats_to_register[13]
            
            # Now set the default values to the values of the user input
            kushi_mitama.level = level_input
            kushi_mitama.st = st_input
            kushi_mitama.ma = ma_input
            kushi_mitama.en = en_input
            kushi_mitama.ag = ag_input
            kushi_mitama.lu = lu_input
            kushi_mitama.skill1 = skill1_input
            kushi_mitama.skill2 = skill2_input
            kushi_mitama.skill3 = skill3_input
            kushi_mitama.skill4 = skill4_input
            kushi_mitama.skill5 = skill5_input
            kushi_mitama.skill6 = skill6_input
            kushi_mitama.skill7 = skill7_input
            kushi_mitama.skill8 = skill8_input

# Registration option for Nigi Mitama
elif persona_choice == 2:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = nigi_mitama.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        nigi_mitama.level = level_input
        nigi_mitama.st = st_input
        nigi_mitama.ma = ma_input
        nigi_mitama.en = en_input
        nigi_mitama.ag = ag_input
        nigi_mitama.lu = lu_input
        nigi_mitama.skill1 = skill1_input
        nigi_mitama.skill2 = skill2_input
        nigi_mitama.skill3 = skill3_input
        nigi_mitama.skill4 = skill4_input
        nigi_mitama.skill5 = skill5_input
        nigi_mitama.skill6 = skill6_input
        nigi_mitama.skill7 = skill7_input
        nigi_mitama.skill8 = skill8_input

# Registration option for Decarabia
elif persona_choice == 3:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = decarabia.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        decarabia.level = level_input
        decarabia.st = st_input
        decarabia.ma = ma_input
        decarabia.en = en_input
        decarabia.ag = ag_input
        decarabia.lu = lu_input
        decarabia.skill1 = skill1_input
        decarabia.skill2 = skill2_input
        decarabia.skill3 = skill3_input
        decarabia.skill4 = skill4_input
        decarabia.skill5 = skill5_input
        decarabia.skill6 = skill6_input
        decarabia.skill7 = skill7_input
        decarabia.skill8 = skill8_input

# Registration option for Ananta
elif persona_choice == 4:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = ananta.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        ananta.level = level_input
        ananta.st = st_input
        ananta.ma = ma_input
        ananta.en = en_input
        ananta.ag = ag_input
        ananta.lu = lu_input
        ananta.skill1 = skill1_input
        ananta.skill2 = skill2_input
        ananta.skill3 = skill3_input
        ananta.skill4 = skill4_input
        ananta.skill5 = skill5_input
        ananta.skill6 = skill6_input
        ananta.skill7 = skill7_input
        ananta.skill8 = skill8_input

# Registration option for Yatagarasu
elif persona_choice == 5:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = yatagarasu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        yatagarasu.level = level_input
        yatagarasu.st = st_input
        yatagarasu.ma = ma_input
        yatagarasu.en = en_input
        yatagarasu.ag = ag_input
        yatagarasu.lu = lu_input
        yatagarasu.skill1 = skill1_input
        yatagarasu.skill2 = skill2_input
        yatagarasu.skill3 = skill3_input
        yatagarasu.skill4 = skill4_input
        yatagarasu.skill5 = skill5_input
        yatagarasu.skill6 = skill6_input
        yatagarasu.skill7 = skill7_input
        yatagarasu.skill8 = skill8_input

# Registration option for Seiryu
elif persona_choice == 6:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = seiryu.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        seiryu.level = level_input
        seiryu.st = st_input
        seiryu.ma = ma_input
        seiryu.en = en_input
        seiryu.ag = ag_input
        seiryu.lu = lu_input
        seiryu.skill1 = skill1_input
        seiryu.skill2 = skill2_input
        seiryu.skill3 = skill3_input
        seiryu.skill4 = skill4_input
        seiryu.skill5 = skill5_input
        seiryu.skill6 = skill6_input
        seiryu.skill7 = skill7_input
        seiryu.skill8 = skill8_input

# Registration option for Dionysus
elif persona_choice == 7:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = dionysus.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        dionysus.level = level_input
        dionysus.st = st_input
        dionysus.ma = ma_input
        dionysus .en = en_input
        dionysus.ag = ag_input
        dionysus.lu = lu_input
        dionysus.skill1 = skill1_input
        dionysus.skill2 = skill2_input
        dionysus.skill3 = skill3_input
        dionysus.skill4 = skill4_input
        dionysus.skill5 = skill5_input
        dionysus.skill6 = skill6_input
        dionysus.skill7 = skill7_input
        dionysus.skill8 = skill8_input

# Registration option for Vohu Manah
elif persona_choice == 8:
        print()
        # Call the function to get the stats from the user 
        stats_to_register = vohu_manah.get_persona_info()
        # Unpack them into values
        level_input = stats_to_register[0]
        st_input = stats_to_register[1]
        ma_input = stats_to_register[2]
        en_input = stats_to_register[3]
        ag_input = stats_to_register[4]
        lu_input = stats_to_register[5]
        skill1_input = stats_to_register[6]
        skill2_input = stats_to_register[7]
        skill3_input = stats_to_register[8]
        skill4_input = stats_to_register[9]
        skill5_input = stats_to_register[10]
        skill6_input = stats_to_register[11]
        skill7_input = stats_to_register[12]
        skill8_input = stats_to_register[13]
        
        # Now set the default values to the values of the user input
        vohu_manah.level = level_input
        vohu_manah.st = st_input
        vohu_manah.ma = ma_input
        vohu_manah .en = en_input
        vohu_manah.ag = ag_input
        vohu_manah.lu = lu_input
        vohu_manah.skill1 = skill1_input
        vohu_manah.skill2 = skill2_input
        vohu_manah.skill3 = skill3_input
        vohu_manah.skill4 = skill4_input
        vohu_manah.skill5 = skill5_input
        vohu_manah.skill6 = skill6_input
        vohu_manah.skill7 = skill7_input
        vohu_manah.skill8 = skill8_input



    

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
