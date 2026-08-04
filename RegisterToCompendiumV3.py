# Filename: RegisterToCompendiumV3.py
# Date: 7/7/26
# Author: Aoi | shadowsnowwolf

# should take user input
# should use arrays


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
                     skill_one, skill_two, 
                     skill_three, skill_four,
                     skill_five, skill_six,
                     skill_seven, skill_eight):
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
            self.skill_one = skill_one
            self.skill_two = skill_two
            self.skill_three = skill_three
            self.skill_four = skill_four
            self.skill_five = skill_five
            self.skill_six = skill_six
            self.skill_seven = skill_seven
            self.skill_eight = skill_eight
    

            def format_persona_log_entry(self):
                return f"""\n\nPersona Registered: 
        Name: {self.name}
        Arcana: {self.arcana}
        Level: {self.level}\n
        Stats: \n------------------------
        St: {self.st}
        Ma: {self.ma}
        En: {self.en}
        Ag: {self.ag}
        Lu: {self.lu}

        Skills: 
        1. {self.skill_one}
        2. {self.skill_two}
        3. {self.skill_three}
        4. {self.skill_four}
        5. {self.skill_five}
        6. {self.skill_six}
        7. {self.skill_seven}
        8. {self.skill_eight}\n"""



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
arsene = FoolPersonas("Arsene", f"{Persona.persona_arcanas[0]},")
obariyon = 
orpheus_f = 
orpheus_f_picaro = 
high_pixie = 
izanagi = 
izanagi_picaro =
orpheus =
orpheus_picaro =


fool_personas = ()

# Magician Personas:
# ------------------------------------------------------------------------------------
jack_o_lantern = 
cait_sith = 
jack_frost = 
nekomata = 
sandman = 
choronzon = 
magician_personas = ()


# Priestess Personas:
# ------------------------------------------------------------------------------------
silky = 
apsaras = 
kohi_i_noor = 
isis = 
kikuri_hime =
sarasvati = 


priestess_personas = ()

# Empress Personas:
# ------------------------------------------------------------------------------------
queens_necklace = 
yaksini = 
lamia = 
hariti = 

empress_personas = ()

# Emperor Personas:
# ------------------------------------------------------------------------------------
eligor = 
regent = 
setanta = 
thoth = 
barong = 
king_frost = 

emperor_personas = ()

# Hierophant Personas:
# ------------------------------------------------------------------------------------
berith = 
orobas = 

hierophant_personas = ()

# Lovers Personas:
# ------------------------------------------------------------------------------------
pixie = 
saki_mitama = 
ame_no_uzume = 
leanan_sidhe =
kushinada = 
narcissus = 
parvati = 

lovers_personas = ()


# Chariot Personas:
# ------------------------------------------------------------------------------------
agation = 
slime = 
shiki_ouji = 
kin_ki = 
ara_mitama = 
white_rider = 
athena = 

chariot_personas = ()

# Justice Personas:
# ------------------------------------------------------------------------------------
angel = 
archangel = 
principality = 
power = 

justice_personas = ()

# Hermit Personas:
# ------------------------------------------------------------------------------------
hermit_personas = ()

# Fortune Personas:
# ------------------------------------------------------------------------------------
fortune_personas = ()

# Strength Personas:
# ------------------------------------------------------------------------------------
strength_personas = ()

# Hanged Man Personas:
# ------------------------------------------------------------------------------------
hanged_man_personas = ()
# Death Personas:
# ------------------------------------------------------------------------------------

death_personas = ()
# Temperance Personas:
# ------------------------------------------------------------------------------------

temeperance_personas = ()
# Devil Personas:
# ------------------------------------------------------------------------------------

devil_personas = ()
# Tower Personas:
# ------------------------------------------------------------------------------------


tower_personas = ()
# Star Personas:
# ------------------------------------------------------------------------------------

star_personas = ()
# Moon Personas: 
# ------------------------------------------------------------------------------------

moon_personas = ()
# Sun Personas:
# ------------------------------------------------------------------------------------

sun_personas = ()
# Judgement Personas:
# ------------------------------------------------------------------------------------


judgement_personas = ()
# Faith Personas:
# ---------------------------------------------------------------------------

faith_personas = ()
# Councillor Personas:
# ---------------------------------------------------------------------------

councillor_personas = ()

# Operations
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

# I need to get the final index after the loop has looped through all of them

# Fool Personas Options
if arcana_choice == 1:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[0]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_fool_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    pass

# Magician Personas Options
elif arcana_choice == 2:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[1]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_magician_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 3:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[2]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_priestess_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 4:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[3]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_empress_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 5:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[4]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_emperor_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 6:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[5]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hierophant_personas()
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 7:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[6]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_lovers_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 8:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[7]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_chariot_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 9:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[8]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_justice_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 10:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[9]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hermit_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 11:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[10]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_fortune_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 12:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[11]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_strength_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 13:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[12]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_hanged_man_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))


# Personas Options    
elif arcana_choice == 14:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[13]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_death_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    

# Personas Options    
elif arcana_choice == 15:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[14]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_temperance_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 16:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[15]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_devil_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 17:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[16]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_tower_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 18:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[17]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_star_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 19:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[18]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_moon_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 20:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[19]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_sun_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 21:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[20]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_judgement_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 22:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[21]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_faith_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))

# Personas Options    
elif arcana_choice == 23:
    # Sets the selected Arcana to the X Arcana
    selected_persona_arcana = f"{Persona.persona_arcanas[22]}"
    # Gets the ending index for the final Persona for output formatting
    ending_range = Persona.display_councillor_personas()
    # Gets the user's Persona choice for registration operations 
    persona_choice = int(input(f"Enter a Persona to register (1-{ending_range}): "))
    

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
