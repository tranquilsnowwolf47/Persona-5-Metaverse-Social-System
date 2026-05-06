# Filename: RegisterToComepndiumV1.py
# Date: 5/5/26
# Author: Aoi | shadowsnowwolf

# This specifically registers Personas to the compendium
# For the final, large program, import this as a module feature with a menu for the choices 
# File will be named VelvetRoom.py

# Program idea:
# Uses OOP to add to increment persona stats based on decrementing allotment points 
# Will help with buildiing Personas 
# A Persona building program, you choose if you want to build manually or with an optimal build 
# select an element and then choose skills based on damage grade 

# Make a fusion program
# Level is calcualted by Arcana burst multiplier (confidant rank), Persona level, etc

# Right now, the values are hard-coded. In the update, import the finished skill list program and set the arguments as indexes of the skills from the 
# imported data

# Descrption:
# Program allows the creation of Persona objects by Arcana and writes them to a file known as the Persona compendium
# Any new Persona data written will be overwritten when the program is run
# This logs and tracks Persona build data so that I can automate registering my Personas 

#import SkillListProgramV1.py
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


# Note:
# Im gonna hardcode the attributes for now, but later once I complete the Skill List Program,
# I'll need to import it and use variables as arguments rather than hard coding it

# Construct some fool Persona objects
# then put them in a tuple so i can loop through them to write them

# Persona Objects:

# Fool Personas:
# ------------------------------------------------------------------------------------
# 1. Arsene
# Register update: (Forgot lol)
arsene = FoolPersonas(
                "Arsene","Fool",28,
                7,8,7,7,4,
                "Slowed Speech (Ag Buff)","3 Second Rule (Charge)","Ether Break (Atk debuff)",
                "Minimum Echo (Med Curse)","Data Hex (Med Curse)","Decision Strike (Med Phys)",
                "Assertive Slice (Med Phys)","Shadow Read (Hvy Psy)")
# 2. Obariyon
# Register update: (Forgot lol)
obariyon = FoolPersonas(
                "Obariyon","Fool",31,
                9,7,7,5,7,
                "Mind Glide (Med Wind)","Deep Dive (Med Wind)","Interest Probe (Med Gun)",
                "Shocking Humor (Light Elec)","Crowd Echo (Med Nuke)","Sync Surge (Med Nuke)",
                "Human Nature Savant (Auto Ag Buff)","Looksmax (Auto Heat-Riser)")
# 3. Orpheus F
# Register update: 11/17/25
# Register update 12/17/25
orpheus_f = FoolPersonas(
                "Orpheus F", "Fool", 29,
                8,6,7,7,4,
                "Act Sense (Med Psy)","Tranquil Edge (Med Psy)","Ether Break (Atk debuff)","Volt Nudge (Light Elec)",
                "Clock Hold (Med Curse)","Hidden Blueprint (Med Curse)","Data Hex (Med Curse)","Minimum Echo (Med Curse)")
# 4. Orpheus F Picaro
# Register update: 12/19/25
# Register update: 1/5/26
# Register update: 1/6/26
orpheus_f_picaro = FoolPersonas(
                    "Orpheus F Picaro", "Fool", 22,
                    6,5,5,6,4,
                    "Tailwind Cascade (Hvy Wind)","Black List (Curse Instant Kill)","Starter Shot (Light Gun)",
                    "Mini-Gun (Light Gun)","Surface Graze (Light Gun)","Acknowledgement Shot (Light Gun)",
                    "Everflow (Hvy Wind)","Career Current (Med Wind)")
# 5. High Pixie
# Register update: 2/7/26
high_pixie = FoolPersonas(
                    "High Pixie", "Fool", 30,
                    7,4,6,7,9,
                    "Affinity Beacon (Debilitate)","Acknowledgement Shot (Light Gun)","Opening Gambit (Med Phys)","Starter Shot (Light Gun)",
                    "Cold Cut (Light Phys)","Inferno Grip (Med Fire)","Calling Fang (Phys)","Slowed Speech (Ag buff)")
# 6. Izanagi
# Register update: 3/10/26
# Register update: 3/26/26
izanagi = FoolPersonas(
                    "Izanagi", "Fool", 35,
                    8,8,6,8,9,
                    "Mind Glide (Med Wind)", "Career Current (Med Wind)", "Commentary Jab (Med Gun)", "Black List (Curse Instant Kill)",
                    "Shocking Humor (Light Elec)", "Quick Invite (Med Gun)", "Purpose Focus (Concentrate)", "Everflow (Hvy Wind)")
# 7. Izanagi Picaro
# Register update: 4/3/26
# Register update: 4/30/26
izanagi_picaro = FoolPersonas(
                    "Izanagi Picaro", "Fool", 36,
                    9,7,6,9,9,
                    "Mind Glide (Med Wind)", "Career Current (Med Wind)", "Commentary Jab (Med Gun)", "Black List (Curse Instant Kill)",
                    "Data Hex (Hvy Curse)", "Quick Invite (Med Gun)", "Purpose Focus (Concentrate)", "Everflow (Hvy Wind)")
# 8. Orpheus
# Register update: 5/5/26
orpheus = FoolPersonas(
                    "Orhpeus", "Fool", "25",
                    5,6,4,7,7,
                    "Mind Glide (Med Wind)", "Career Current (Med Wind)", "Commentary Jab (Med Gun)", "Black List (Curse Instant Kill)",
                    "Data Hex (Hvy Curse)", "Quick Invite (Med Gun)", "Purpose Focus (Concentrate)", "Everflow (Hvy Wind)")

# All Fool Personas registered 
fool_personas = (arsene, obariyon, orpheus_f, orpheus_f_picaro, high_pixie, izanagi, 
                 izanagi_picaro, orpheus)


# Magician Personas:
# ------------------------------------------------------------------------------------
# 1. Jack-o'-lantern 
# Register update: 9/14/25
jack_o_lantern = MagicianPersonas(
                "Jack-o'-Lantern", "Magician",20,
                4,10,5,3,2,
                "Winds of Knowledge (Med Wind)","Career Current (Med Wind)","Deep Dive (Med Wind)","Mind Glide (Med Wind)","Subject Shift (Light Gun)",
                "Mini-Talk (Light Gun)","Echo Shot (Light Gun)","Velvet Note (Med Fire)")
# 2. Cait Sith 
# Register update: (Idk lol)
cait_sith = MagicianPersonas( 
                "Cait Sith", "Magician", 21,
                3,9,5,6,1,
                "","","","","","","","")
# 3. Jack Frost
# Register Update: 12/17/25
jack_frost = MagicianPersonas(
                    "Jack Frost", "Magician", 22,
                    5,10,5,5,1,
                    "","","","","","","","")
# 4. Nekomata
# Register Update: 2/7/26
nekomata = MagicianPersonas(
                "Nekomata", "Magician", 20,
                5,9,4,5,1,
                "","","","","","","","")
# 5. Sandman
# Register update: 3/27/26
sandman = MagicianPersonas( 
                    "Sandman", "Magician", 25,
                    5,12,6,5,1,
                    "","","","","","","","")

# All Magician Personas registered 
magician_personas = (jack_o_lantern, cait_sith, jack_frost, nekomata, sandman)


# Priestess Personas:
# ------------------------------------------------------------------------------------
# 1. Silky
# Register update: (Idk lol)
silky = PriestessPersonas(  
                "Silky","Priestess",17,
                2,10,6,6,1,
                "Shadow Read (Hvy Psy)","Temperament Read (Light Psy)","Environment Scan (Med Psy)",
                "Observation (Light Psy)","Extraction Shot (Light Gun)","Small-talk (Light Gun)","Reassuring Chill (Light Ice)",
                "Slowed Speech (Ag Buff)")
# 2. Apsaras
# Register update: 9/29/25
apsaras = PriestessPersonas(
                "Apsaras","Priestess",29,
                2,10,8,10,4,
                "Shadow Read (Hvy Psy)","Temperament Read (Light Psy)","Environment Scan (Psy)","Observation (Light Psy)",
                "","","Reassuring Chill (Ice)","Slowed Speech (Ag Buff)")
# 3. Koh-i-Noor
# Register update: 12/7/25
kohi_i_noor = PriestessPersonas(
                    "Koh-i-Noor","Priestess",23,
                    2,11,6,6,1,
                    "","","","","",
                    "","","")
# 4. Isis
# Register update: 2/3/26
# Register update: 2/8/26
isis = PriestessPersonas(
                    "Isis", "Priestess", 17,
                    1,7,6,6,1,
                    "","","","","",
                    "","","")
# 5. Kikuri-Hime
# Register update: 3/11/26
# Register update: 3/27/26
kikuri_hime = PriestessPersonas(
                    "Kikuri-Hime", "Priestess", 30,
                    1,10,12,10,1,
                    "Sixth Observation (Light Psy)", "Intent Rift (Hvy Psy)", "Interest Gauge (Light Psy)", "Cold Admission (Med Ice)",
                    "Anchor Presence (Med Ice)", "Social Probe (Med Gun)", "Self-Control (Auto def buff)", "Coordination Vector (AOE Ag debuff)")

priestess_personas = (silky, apsaras, kohi_i_noor, isis, kikuri_hime)

# Empress Personas:
# ------------------------------------------------------------------------------------
# 1. Queen's Necklace
# Register update: (Idk lol)
queens_necklace = EmpressPersonas(
                "Queen's Necklace","Empress", 16,
                5,4,3,6,3,
                "Temperament Read","","","","","","","")
# 2. Yaksini
# Register update: 12/17/25
# Register update: 3/11/26
yaksini = EmpressPersonas(
                    "Yaksini", "Empress", 17,
                    6,8,3,4,1,
                    "Warm Smile (Light Bless)","Gracious Thanks (Light Bless)","Hope Pulse (Med Bless)","Light of Insight (Med Bless)",
                    "Reassuring Chill (Light Ice)","Acknowledgement Frost (Light Ice)","Assertive Slice (Med Phys)","Slowed Speech (Ag Buff)")
# 3. Lamia 
# Register update: 5/1/26
lamia = EmpressPersonas(
                    "Lamia","Empress", 21,
                    11,10,3,6,1,
                    "Warm Smile (Light Bless)","Gracious Thanks (Light Bless)","Hope Pulse (Med Bless)","Light of Insight (Med Bless)",
                    "Reassuring Chill (Light Ice)","Acknowledgement Frost (Light Ice)","Assertive Slice (Med Phys)","Slowed Speech (Ag Buff)")

empress_personas = (queens_necklace, yaksini, lamia)

# Emperor Personas:
# ------------------------------------------------------------------------------------
# 1. Eligor
# Register update: (Idk lol)
eligor = EmperorPersonas(
                "Eligor", "Emperor",24,
                10,5,7,3,5,
                "Assertive Slice (Phys)","Request Denial (Curse)","Name Repeat (Psy)","Extraction Shot (Gun)","","","","")
# 2. Regent
# Register update: 8/31/25
# Register update: 9/15/25
# Register update: 10/4/25
regent = EmperorPersonas(
                "Regent", "Emperor", 28,
                13,6,10,2,1,
                "Assertive Slice (Med Phys)","Stonewall (Med Phys)","Decision Strike (Med Phys)","Cold Cut (Med Phys)",
                "Magnetic Aura (Med Fire)","Verbal Parry (Med Elec)","3 Second Rule (Charge)","Rhythm Break (Ag Debuff)")
# 3. Setanta
# Register update: 11/17/25
# Register update: 12/17/25 
setanta = EmperorPersonas(
                        "Setanta", "Emperor", 30,
                        14,8,10,2,1,
                        "Assertive Slice (Med Phys)", "Stonewall (Med Phys)", "Decision Strike (Med Phys)", "Calling Fang (Med Phys)", 
                        "Magnetic Aura (Med Fire)","Verbal Parry (Med Elec)", "3 Second Rule (Charge)","")
# 4. Thoth
# Register update: 1/12/26
# Register udpate: 2/7/26
thoth = EmperorPersonas(
                    "Thoth", "Emperor", 37,
                    16,9,8,6,1,
                    "Assertive Slice (Med Phys)","Decision Strike (Med Phys)","Social Dominance (Med Phys)","Iron Gaze (Med Phys)",
                    "Inferno Grip (Med Fire)","Gentleman's Flattery (Light Fire)","Deadpan Discharge (Light Elec)","3-Second Rule (Charge)")
# 5. Barong
# Register update: 3/3/26
# Register update: 3/10/26
# Register update: 3/26/26
barong = EmperorPersonas(
                    "Barong", "Emperor", 35,
                    15,11,7,5,1,
                    "Assertive Slice (Med Phys)", "Social Dominance (Med Phys)", "Decision Strike (Med Phys)", "Advance Slash (Hvy Phys)",
                    "Value Touch (Hvy Fire)", "Ember Gaze (Med Fire)", "Shocking Humor (Light Elec)", "3 Second Rule (Charge)"
           )

emperor_personas = (eligor, regent, setanta, thoth, barong)

# Hierophant Personas:
# ------------------------------------------------------------------------------------
# 1. Berith 
# Register update: 1/8/26
# Register update: 2/7/26
berith = HierophantPersonas(
                    "Berith", "Hierophant", 7,
                    6,1,2,1,1,
                    "Alpha Directive (Med Phys)","Career Current (Med Wind)","Confidence Drive (Atk buff)","Slowed Speech (Ag buff)",
                    "Social Competence (Auto Atk buff)","Wind Boost","Dodge Reverse Curse","Purpose Anchor (Despair Recovery)")

hierophant_personas = (berith,)

# Lovers Personas:
# ------------------------------------------------------------------------------------
# 1. Pixie
# Register update: (Idk lol)
pixie = LoversPersonas(
                "Pixie", "Lovers", 19,
                1,7,4,5,5,
                "Self Respect Affirmation","Prioritized Presence (Med Psy)","Nonchalance (Med Psy)","Interest Level Read (Light Psy)",
                "","","","")
# 2. Saki Mitama
# Register update: 10/4/25
saki_mitama = LoversPersonas(
                "Saki Mitama","Lovers",25,
                7,8,3,6,6,
                "Focused Breathing (Lvl 1 Healing)", "Cat Nap (Lvl 2 Healing)","","",
                "","","","")
# 3. Ame-no-Uzume
# Register update: 11/17/25
# Register update: 12/17/25
ame_no_uzume = LoversPersonas(
                    "Ame-no-Uzume", "Lovers",25,
                    5,11,3,5,5,
                    "Focused Breathing (Lvl 1 Healing)","Cat Nap (Lvl 2 Healing)","","",
                    "","","","")
# 4. Leanan Sidhe 
# Register update: 2/8/26
leanan_sidhe = LoversPersonas(
                    "Leanan Sidhe", "Lovers", 19,
                    5,8,1,5,4,
                    "", "", "","",
                    "", "", "","")
# 5. Kushinada
# Register update: 3/11/26
# Register update: 3/27/26
kushinada = LoversPersonas(
                    "Kushinada", "Lovers", 25,
                    6,11,1,6,4,
                    "Sync Surge (Med Nuke)", "Tailwind Cascade (Hvy Wind)", "Purpose Focus (Concentrate)","Confidence Drive (Atk buff)",
                    "Twin Breath (Lvl 1 Healing)", "Focused Breathing (Lvl 1 Healing)", "Hazard Audit (Fear Recovery)","Temper Drop (Rage Recovery)")
# 6. Narcissus
# Register update: 4/3/26
# Register update: 5/1/26
narcissus = LoversPersonas(
                    "Narcissus", "Lovers", 25,
                    6,10,1,8,4,
                    "Sync Surge (Med Nuke)", "Tailwind Cascade (Hvy Wind)", "Purpose Focus (Concentrate)","Confidence Drive (Atk buff)",
                    "Twin Breath (Lvl 1 Healing)", "Focused Breathing (Lvl 1 Healing)", "Hazard Audit (Fear Recovery)","Temper Drop (Rage Recovery)"
           )

lovers_personas = (pixie, saki_mitama, ame_no_uzume, leanan_sidhe, kushinada, narcissus)

# Chariot Personas:
# ------------------------------------------------------------------------------------
# 1. Agathion
# Register update: (Idk lol)
agathion = ChariotPersonas(
                "Agathion","Chariot", 20,
                5,4,5,3,2,
                "Self-Control (Auto def buff)","Gentleman's Flattery","Direct Curiosity","",
                "","","","")
# 2. Slime
# Register update: 9/15/25
# Register update: 9/15/25
slime = ChariotPersonas( 
                "Slime","Chariot", 20,
                7,5,5,4,1,
                "Sync surge (Med Nuke)","Hyper Link (Med Nuke)","Flare Blast (Med Nuke)","3 Second Rule (Charge)",
                "Confidence (Atk Buff)","Opening Gambit (Hvy Phys)","Calling Fang (Med Phys)","Brain Flicker (Med Elec)")
# 3. Shiki-Ouji
# Register update: 1/5/25
shiki_ouji = ChariotPersonas(
                    "Shiki-Ouji","Chariot",26,
                    10,7,7,5,1,
                    "Sync Surge (Med Nuke)","Hyper Link (Med Nuke)","Flare Blast (Med Nuke)","Confidence Surge (Atk buff)",
                    "3-Second Rule (Charge)","Opening Gambit (Med Phys)","Advance Slash (Hvy Phys)","Volt Revive (Light Elec)")
# 4. Kin-Ki
# Register update: 2/7/26
kin_ki = ChariotPersonas(
                    "Kin-Ki", "Chariot", 21,
                    7,6,8,3,1,
                    "", "", "","",
                    "", "", "","")
# 5. Ara Mitama 
# Register update: 3/11/26
ara_mitama = ChariotPersonas(
                    "Ara Mitama", "Chariot", 30,
                    11,9,9,4,1,
                    "Crowd Echo (Med Nuke)", "Spotlight Surge (Hvy Nuke)", "Flash Bounce (Med Nuke)","Cold Cut (Light Phys)",
                    "Calling Fang (Light Phys)", "Shocking Humor (Light Elec)", "3-Second Rule (Charge)","Confidence Drive (Atk buff)")

chariot_personas = (agathion, slime, shiki_ouji, kin_ki, ara_mitama)

# Justice Personas:
# ------------------------------------------------------------------------------------
# 1. Angel
# Register update: 10/4/25
angel = JusticePersonas(
                "Angel","Justice", 27,
                4,6,6,6,5,
                "","","","","","","","")
# 2. Archangel
# Register update: 12/19/25
# Register update: 1/5/26
# Register update: 2/7/26
archangel = JusticePersonas(
                    "Archangel","Justice", 22,
                    7,5,2,10,4,
                    "Intent Rift (Hvy Psy)","Atmosphere Read (Med Psy)","Sniper Question (Med Gun)","Soft Deflect (Med Gun)",
                    "Psy Boost","Dodge Reverse Fire","Contagion Wave (AOE Def Debuff)","Human Nature Savant (Auto Ag Buff)")
# 3. Principality
# Register update: 2/18/26
# Register update: 3/10/26
# Register update: 3/27/26
principality = JusticePersonas(
                    "Principality", "Justice", 33,
                    11,7,1,13,5,
                    "Interest Probe (Med Gun)", "Social Probe (Med Gun)", "Temperament Read (Light Psy)","Atmosphere Read (Med Psy)",
                    "Psy Boost", "Gun Boost", "Contagion Wave (AOE Def Debuff)","Human Nature Savant (Auto Ag Buff)")

justice_personas = (angel, archangel, principality)

# Hermit Personas:
# ------------------------------------------------------------------------------------
# 1. Bicorn
# Register update: (Idk lol)
bicorn = HermitPersonas(
                "Bicorn", "Hermit",16, 
                1,6,6,1,7,
                "Cooldown (Ice)", "Prioritized Presence (Med Psy)","Soulshare (Ice)","Empathic Echo (Ice)","Reassuring Chill (Ice)","","","")
# 2. Koropokkuru 
# Register Update: 12/17/25
# Register Update: 1/8/25
koropokkuru = HermitPersonas(
                    "Koropokkuru", "Hermit", 15,
                    1,7,6,4,1,
                    "Prioritized Presence (Hvy Psy)","Tranquil Edge (Med Psy)","Regenerate I (HP Regen)","Invigorate I (SP Regen)",
                    "Temper Drop (Rage recovery)","","","")
# 3. Ippon-Datara
# Register update: 2/18/26
# Register update: 3/11/26
ippon_datara = HermitPersonas(
                    "Ippon-Datara", "Hermit", 20,
                    1,8,6,6,3,
                    "Prioritized Presence (Hvy Psy)", "Tranquil Edge (Med Psy)", "Regenerate I (HP Regen)","Invigorate I (SP Regen)",
                    "Temper Drop (Rage recovery)", "Self-Control (Auto Def buff)", "Frequency Barrier (AOE atk buff)","Twin Breath (Lvl 1 Healing)"
           )
# 4. Sudama
# Register update: 4/3/26
# Register update: 5/1/26
sudama = HermitPersonas(
                    "Sudama", "Hermit", 20,
                    1,11,5,6,1,
                    "Prioritized Presence (Hvy Psy)", "Tranquil Edge (Med Psy)", "Regenerate I (HP Regen)","Invigorate I (SP Regen)",
                    "Temper Drop (Rage recovery)", "Self-Control (Auto Def buff)", "Frequency Barrier (AOE atk buff)","Twin Breath (Lvl 1 Healing)")

hermit_personas = (bicorn, koropokkuru, ippon_datara, sudama)

# Fortune Personas:
# ------------------------------------------------------------------------------------
# 1. Stone of Scone
# Register update: (Idk lol)
stone_of_scone = FortunePersonas(
                "Stone of Scone", "Fortune", 13,
                1,1,3,3,6,
                "Social Competence","Interest Level Read","","",
                "","","","")
# 2. Clotho
# Register udpate: 12/17/25
clotho = FortunePersonas(
                    "Clotho","Fortune", 20,
                    3,2,4,6,9,
                    "","","","","","","","")
# 3. Ariadne
# Register update: 2/7/26
ariadne  = FortunePersonas(
                    "Ariadne", "Fortune", 21,
                    3,2,4,6,10,
                    "", "", "","",
                    "", "", "","")
# 4. Lachesis
# Register update: 3/3/26
# Register update: 3/10/26
# Register update: 3/27/26
lachesis = FortunePersonas("Lachesis", "Fortune", 35,
           6,6,3,9,15,
           "Affinity Beacon (Debilitate)", "Self-Security (Def buff)", "Temperament Read (Light Psy)", "Veiled Initiative (Hvy Curse)",
           "Looksmax (Auto Heat Riser)", "Human Nature Savant (Auto Ag Buff)", "Psy Boost", "Hazard Audit (Fear Recovery)")

fortune_personas = (stone_of_scone, clotho, ariadne, lachesis)

# Strength Personas:
# ------------------------------------------------------------------------------------
# 1. Kelpie
# Register update: (Idk lol)
kelpie = StrengthPersonas(
                "Kelpie", "Strength", 16,
                6,3,7,1,2,
                "","","","",
                "","","","")
# 2. Shiisaa
# Register update: 10/4/25
shiisa = StrengthPersonas(
                "Shiisaa", "Strength", 21,
                5,4,11,3,2,
                "","","","",
                "","","","")
# 3. Oni
# Register update: 11/17/25
oni = StrengthPersonas(
                    "Oni","Strength", 15,
                    5,2,9,1,2,
                    "","","","",
                    "","","", "Self-Control (Auto Def buff)")
# 4. Rakshasa 
# Register update: 2/7/26
# Register update: 3/27/26
rakshasa = StrengthPersonas(
                    "Rakshasa", "Strength", 25,
                    4,6,13,3,3,
                    "", "", "","",
                    "", "", "","")
# 5. Orlov
# Register update: 4/3/26
orlov = StrengthPersonas(
                    "Orlov", "Strength", 12,
                    3,2,7,3,1,
                    "", "", "","",
                    "", "", "","")

strength_personas = (kelpie, shiisa, oni, rakshasa, orlov)

# Hanged Man Personas:
# ------------------------------------------------------------------------------------
# 1. Hua Po
# Register update: 12/17/25
hua_po = HangedManPersonas(
                    "Hua Po","Hanged Man", 18,
                    5,4,8,3,1,
                    "Prioritized Presence","Slowed Speech","Echo Shot","Casual Greeting Shot",
                    "Small-talk","Subject Change","Interest Probe","")
# 2. Inugami
# Register update: 12/17/25
# Register update: 12/19/25
# Register update: 1/5/26
inugami = HangedManPersonas(
                    "Inugami", "Hanged Man", 19,
                    5,5,7,4,1,
                    "Dodge Phys","Dodge Reverse Phys","Dodge Reverse Ice","Ether Break (Atk debuff)",
                    "Tactic Diffuser (Ag debuff)","Self-Security (Def buff)","Intent Rift (Hvy Psy)", "Focused Breathing (LVl 1 Healing)")
# 3. Orthrus
# Register update: 1/12/26
# Register update: 2/8/26
orthrus = HangedManPersonas(
                    "Orthrus", "Hanged Man", 15,
                    1,5,6,6,1,
                    "Dodge Phys","Dodge Reverse Phys","Dodge Reverse Ice","Ether Break (Atk debuff)",
                    "Tactic Diffuser (Ag debuff)","Self-Security (Def buff)","Intent Rift (Hvy Psy)", "Focused Breathing (LVl 1 Healing)")
# 4. Take-Minakata
# Register update: 3/11/26
# Register update: 3/27/26
take_minakata = HangedManPersonas(
                    "Take-Minakata", "Hanged Man", 30,
                    5,10,10,8,1,
                    "Dodge Phys","Dodge Reverse Phys","Dodge Reverse Ice","Ether Break (Atk debuff)",
                    "Tactic Diffuser (Ag debuff)","Self-Security (Def buff)","Intent Rift (Hvy Psy)", "Focused Breathing (LVl 1 Healing)")

hanged_man_personas = (hua_po, inugami, orthrus, take_minakata)

# Death Personas:
# ------------------------------------------------------------------------------------
# 1. Mandrake
# Register update: (Idk lol)
mandrake = DeathPersonas(
                "Mandrake", "Death", 20,
                2,4,7,5,7,
                "Slowed Speech (Ag buff)","Self-Control (Auto-Def buff)","Self-Security (Def buff)",
                "Confidence (Atk buff)", "3 Second Rule (Charge)", "", "", "")
# 2. Mokoi
# Register udpate: 9/15/25
# Register update: 10/4/25
mokoi = DeathPersonas(
                "Mokoi","Death", 27,
                1,9,9,8,4,
                "Slowed Speech (Ag buff)","Self-Control (Auto Def buff)","Self-Security (Def buff)",
                "Confidence (Atk buff)","Act Sense (Med Psy)","Tranquil Edge (Med Psy)","Hollow Stance (Light Curse)","Minimum Echo (Med Curse)")
# 3. Matador
           # Register update 12/17/25 (had him like a month+ ago but lost the data)

matador = DeathPersonas(
                    "Matador", "Death", 26,
                    5,11,9,5,1,
                    "Slowed Speech (Ag buff)", "Self-Control (Auto Def buff)", 
                    "Human Nature Savant (Auto Ag Buff)", "Confidence (Atk buff)", "Interest Guage (Med Psy)",
                    "Tranquil Edge (Med Psy)", "Hollow Stance (Light Curse)", "Minimum Echo (Med Curse)")
# 4. Nue
# Register update: 2/7/26
nue = DeathPersonas(
                    "Nue", "Death", 22,
                    2,11,5,6,3,
                    "Slowed Speech (Ag buff)", "Self-Security (Def buff)", "","",
                    "", "", "","")
# 5. Pisaca
# Register update: 2/18/26
# Register update: 3/3/26
# Register update: 3/27/26
pisaca = DeathPersonas(
                    "Pisaca", "Death", 31,
                    2,13,8,9,3,
                    "Slowed Speech (Ag buff)", "Self-Security (Def buff)", "Intent Rift (Hvy Psy)","Effort Reaper (Curse Instant Kill)",
                    "Timeout Clause (Curse Instant Kill)", "Self-Control (Auto Def buff)", "Drain Ice","Dodge Reverse Ice")
# 6. Hell Biker
# Register update: 4/3/26
# Register update: 5/1/26
hell_biker = DeathPersonas(
                    "Hell Biker", "Death", 29,
                    2,12,7,9,3,
                    "Slowed Speech (Ag buff)", "Self-Security (Def buff)", "Intent Rift (Hvy Psy)","Effort Reaper (Curse Instant Kill)",
                    "Timeout Clause (Curse Instant Kill)", "Self-Control (Auto Def buff)", "Drain Ice","Dodge Reverse Ice")

death_personas = (mandrake, mokoi, matador, nue, pisaca, hell_biker)

# Temperance Personas:
# ------------------------------------------------------------------------------------
# 1. Genbu 
# Register update: 12/19/25
# Register update: 1/8/26
# Register update: 2/7/26
genbu = TemperancePersonas( 
                    "Genbu", "Temperance", 13,
                    1,5,6,4,1,
                    "Slowed Speech (Ag buff)","Self-Control (Auto def buff)","Regen I (HP Regen)","Invigorate I (SP Regen)",
                    "","","","",)

temperance_personas = (genbu,)

# Devil Personas:
# ------------------------------------------------------------------------------------
# 1. Incubus
# Register update 12/19/25
incubus = TemperancePersonas(
                    "Incubus","Devil",1,
                    1,1,1,1,1,
                    "","","","","",
                    "","","")

devil_personas = (incubus,)

# Tower Personas:
# ------------------------------------------------------------------------------------
# 1. Belphegor
# Register update: 12/19/25
# Register update: 1/8/25
# Register update: 2/8/26
# Reguster update: 5/1/26
belphegor = TowerPersonas(
                    "Belphegor", "Tower", 27,
                    2,10,6,10,3,
                    "Black List (Curse Instant Kill)","Effort Reaper (Curse Instant Kill)","Advance Slash (Hvy Phys)","Dodge Ice","Curse Boost",
                    "Human Nature Savant (Auto Ag buff)","Hazard Audit (Confuse Recovery)","Tactic Diffuser (Ag debuff)")

tower_personas = (belphegor,)

# Star Personas:
# ------------------------------------------------------------------------------------

star_personas = ()

# Moon Personas:
# ------------------------------------------------------------------------------------
# 1. Succubus 
# Register update 12/19/25
# Register update: 1/5/26
succubus = MoonPersonas(
                    "Succubus", "Moon", 19,
                    1,7,6,8,1,
                    "Intent Rift (Hvy Psy)","Sixth Observation (Light Psy)","Kinesis Gap (Med Psy)","Effort Reaper (Curse High instant kill)",
                    "Hollow Stance (Med Curse)","Drain Reverse Psy","Dodge Reverse Bless","Drain Reverse Fire")
# 2. Onmoraki
# Register update: 2/7/26
onmoraki = MoonPersonas( 
                    "Onmoraki", "Moon", 20,
                    1,8,6,8,1,
                    "Intent Rift (Hvy Psy)","Sixth Observation (Light Psy)","Kinesis Gap (Med Psy)","Effort Reaper (Curse High instant kill)",
                    "Hollow Stance (Med Curse)","Drain Reverse Psy","Dodge Reverse Bless","Drain Reverse Fire")
# 3. Kaguya
# Register update: 3/10/26
# Register update: 3/24/26
kaguya = MoonPersonas(
                    "Kaguya", "Moon", 35,
                    1,12,8,13,5,
                    "Atmosphere Read (Med Psy)", "Temperament Read (Light Psy)", "Hollow Stance (Med Curse)", "Effort Reaper (Curse High instant kill)",
                    "Drain Ice","Dodge Reverse Bless","Dodge Reverse Wind", "Frame Reset (Confusion Recovery)")

moon_personas = (succubus, onmoraki, kaguya)

# Sun Personas:
# ------------------------------------------------------------------------------------
# 1. Suzaku
# Register update: 10/4/25
# Register update: 11/17/25
suzaku = SunPersonas("Suzaku", "Sun", 23,
                7,8,5,3,4,
                "Ember Gaze (Med Fire)","","","","Looksmax (Auto Heat-Riser)","Confidence (Atk buff)","Social Competence (Auto Atk Buff)",
                "Ascendancy Wave (AOE Ag Debuff)")
# 2. Thunderbird
# Register update: 2/7/26
thunderbird = SunPersonas("Thunderbird", "Sun", 19,
                  8,8,3,3,1,
                  "Charming Smile (Light Fire)", "Inferno Grip (Med Fire)", "Flame Tease (Med Fire)","Sonic Quip (Light Elec)",
                  "Looksmax (Auto Heat-Riser)", "Confidence Drive (Atk buff)", "Self-Control (Auto def buff)","Ether Break (Atk debuff)")
# 3. Mithras
# Register update: 3/10/26
# Register update: 3/26/26
mithras = SunPersonas("Mithras", "Sun", 33,
                  12,12,3,3,7,
                  "Charming Smile (Light Fire)", "Inferno Grip (Med Fire)", "Gentleman's Flattery (Med Fire)", "Sonic Quip (Light Elec)",
                  "Looksmax (Auto Heat-Riser)", "Confidence Drive (Atk buff)", "Self-Control (Auto def buff)","Ascendancy Link (Def debuff)")
# 4. Yurlungur
# Register update: 4/3/26
yurlungur = SunPersonas("Yurlungur", "Sun", 28,
              9,10,3,3,7,
              "Charming Smile (Light Fire)", "Inferno Grip (Med Fire)", "Gentleman's Flattery (Med Fire)", "Sonic Quip (Light Elec)",
              "Looksmax (Auto Heat-Riser)", "Confidence Drive (Atk buff)", "Self-Control (Auto def buff)","Ascendancy Link (Def debuff)")

sun_personas = (suzaku, thunderbird, mithras, yurlungur)


# Judgement Personas:
# ------------------------------------------------------------------------------------

judgement_personas = ()

# Faith Personas:
# ------------------------------------------------------------------------------------
# 1. Phoenix
# Register update: 11/17/25
phoenix = FaithPersonas(
            "Phoenix","Faith",11,
            3,1,3,1,2,
            "","","","","","","","")
# 2. Tam Lin
# Register update: 12/17/25
# Register update: 2/8/26
tam_lin = FaithPersonas(
                    "Tam Lin", "Faith", 22,
                    3,1,8,6,7,
                    "","","","","","","","")
# 3. Unicorn
# Register update: 3/11/26
# Register update: 3/26/26
unicorn = FaithPersonas(
                    "Unicorn", "Faith", 31,
                    5,4,9,8,9,
                    "Heartfelt Thanks (Med Bless)","Gracious Thanks (Light Bless)","Warm Smile (Light Bless)","Confidence Drive (Atk buff)",
                    "Self-Security (Def buff)","Drain Bless","Looksmax (Auto Heat Riser)","Hazard Audit (Fear Recovery)")
# 4. Okuninushi
# Register update: 4/3/26
# Register update: 5/1/26
okuninushi = FaithPersonas(
                    "Okuninushi", "Faith", 25,
                    5,4,9,5,6,
                    "Heartfelt Thanks (Med Bless)","Gracious Thanks (Light Bless)","Warm Smile (Light Bless)","Confidence Drive (Atk buff)",
                    "Self-Security (Def buff)","Drain Bless","Looksmax (Auto Heat Riser)","Hazard Audit (Fear Recovery)")

faith_personas = (phoenix, tam_lin, unicorn, okuninushi)

# Councillor Personas:
# ------------------------------------------------------------------------------------

councillor_personas = ()



# Containers for formatted log data for all Persona arcanas 
fool_personas_log_data = []
magician_personas_log_data = []
priestess_personas_log_data = []
empress_personas_log_data = []
emperor_personas_log_data = []
hieroophant_personas_log_data = []
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
    hieroophant_personas_log_data.append(formatted_data)

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
with open("Persona_compendium_logbookV2.txt","w") as compendium_log:
    # Write Fool Personas to the compendium
    for fool_persona_log in fool_personas_log_data:
        compendium_log.write(fool_persona_log)

    # Magician Personas
    for magician_persona_log in magician_personas_log_data:
        compendium_log.write(magician_persona_log)
        
    # Priestess Personas
    for priestess_persona_log in priestess_personas_log_data:
            compendium_log.write(priestess_persona_log)

    # Empress Personas
    for empress_persona_log in empress_personas_log_data:
        compendium_log.write(empress_persona_log)

    # Emperor Personas
    for emperor_persona_log in emperor_personas_log_data:
        compendium_log.write(emperor_persona_log)

    # Hierophant Personas
    for hierophant_persona_log in hieroophant_personas_log_data:
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
    
    print("Current Personas registered to compendium.")
    print("Previous Personas have been overwritten.")

