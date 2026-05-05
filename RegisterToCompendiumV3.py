import SkillListProgramV1.py

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
        return f"""Persona Registered: 
        Name: {self.name}
        Arcana: {self.arcana}
        f"Level: {self.level}\n
        Stats: \n------------------------
        St: {self.st}
        Ma: {self.ma}
        En: {self.en}
        Ag: {self.ag}
        Lu: {self.lu}\n

        Skills: 
        1. {self.skill_one}
        2. {self.skill_two}
        3. {self.skill_three}
        4. {self.skill_four}
        5. {self.skill_five}
        6. {self.skill_six}
        7. {self.skill_seven}
        8. {self.skill_eight}\n"""

# Class Template for Personas (For creating Persona objects)
class Persona(Compendium):
    pass

# Class Template for Fool Personas (Creating Persona objects)
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


# Note:
# Im gonna hardcode the attributes for now, but later once I complete the Skill List Program,
# I'll need to import it and use variables as arguments rather than hard coding it

# Construct some fool Persona objects
# Fool Personas:
# ------------------------------------------------------------------------------------
# 1. Arsene
arsene = FoolPersonas()
# 2. Obariyon
obariyon = FoolPersonas()
# 3. Orpheus F
orpheus_f = FoolPersonas()
# 4. Orpheus F Picaro
orpheus_f_picaro = FoolPersonas()
# 5. High Pixie
high_pixie = FoolPersonas()
# 6. Izanagi
izanagi = FoolPersonas()
# 7. Izanagi Picaro
izanagi_picaro = FoolPersonas()
# 8. Orpheus
opehus = FoolPersonas()


with open("Persona_compendium_logbookV2.py","w") as file:
    pass

    # Fool Personas
    # Magician Personas
    # Priestess Personas
    # Empress Personas
    # Emperor Personas
    # Hierophant Personas
    # Lovers Personas
    # Chariot Personas
    # Justice Personas
    # Hermit Personas
    # Fortune Personas
    # Strength Personas
    # Hanged Man Personas
    # Death Personas
    # Temperance Personas
    # Devil Personas
    # Tower Personas
    # Star Personas
    # Moon Personas 
    # Sun Personas
    # Judgement
    # Faith Personas

