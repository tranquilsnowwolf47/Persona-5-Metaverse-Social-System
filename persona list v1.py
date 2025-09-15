#
# Use arrays to list personas of each confidant
#


# Clear
def foolArcanaPersonasList():
    fool_persona_list = ["Arsene","Obariyon","Orpheus F","Orpheus F Picaro","High Pixie",
    "Izanagi","Izanagi Picaro","Orpheus","Orpheus Picaro","Legion","Ose",
    "Bugs","Crystal Skull", "Black Frost","Raoul","Vishnu","Satanael"]
    return fool_persona_list

# Clear
def magicianArcanaPersonasList():
    magician_persona_List = ["Jack-o'-Lantern","Cait Sith","Jack Frost","Nekomata","Sandman",
    "Choronzon","Queen Mab","Rangda","Forneus","Surt","Futsunushi"]
    return magician_persona_List

# Clear
def priestessArcanaPersonasList():
    priestess_persona_list = ["Silky","Apsaras","Koh-i-Noor","Isis","Kikuri-Hime",
    "Sarasvati","Skadi","Scathach","Cybele"]
    return priestess_persona_list

# Clear
def empressArcanaPersonasList():
    empress_persona_list = ["Queen's Necklace","Yaksini","Lamia","Hariti","Dakini",
    "Titania","Kali","Alilat","Mother Harlot"]
    return empress_persona_list

# Clear
def emperorArcanaPersonasList():
    emperor_persona_list = ["Regent","Eligor","Setanta","Thoth",
    "Barong","King Frost","Oberon","Baal","Odin"]
    return emperor_persona_list

# Clear
def hierophantArcanaPersonasList():
    hierophant_persona_list = ["Berith","Orobas","Anzu","Daisoujou","Mishaguji","Bishamonten","Kohryu"]
    return hierophant_persona_list

# Clear
def loversArcanaPersonasList():
    lovers_persona_list = ["Pixie","Saki Mitama","Ame-no-Uzume","Leanan Sidhe","Kushinada","Narcissus",
    "Parvati","Raphael","Ishtar"]
    return lovers_persona_list

# Clear
def chariotArcanaPersonasList():
    chariot_persona_list = ["Agathion","Slime","Shiki-Ouji","Kin-Ki","Ara Mitama","White Rider","Athena",
    "Athena Picaro","Cerberus","Thor","Chi You"]
    return chariot_persona_list

# Clear
def justiceArcanaPersonasList():
    justice_persona_list = ["Angel","Archangel","Principality","Power","Melchizedek","Throne",
    "Uriel","Metatron"]
    return justice_persona_list

# Clear
def hermitArcanaPersonasList():
    hermit_persona_list = ["Bicorn","Koropokkuru","Ippon-Datara","Sudama","Naga","Kurama Tengu","Arahabaki",
    "Kumbhanda","Koumokuten","Loa","Fafnir","Ongyo-Ki"]
    return hermit_persona_list

# Clear
def fortuneArcanaPersonaList():
    fortune_persona_list = ["Stone of Scone","Clotho","Ariadne","Lachesis","Atropos","Ariadne Picaro","Fortuna","Norn",
    "Asterius","Asterius Picaro","Lakshmi"]
    return fortune_persona_list

# Clear
def strengthArcanaPersonaList():
    strength_persona_list = ["Kelpie","Shiisaa","Oni","Rakshasa","Orlov","Zouchouten","Valkyrie","Hanuman","Chimera","Zaou-Gongen"]
    return strength_persona_list

# Clear
def hangedManArcanaPersonaList():
    hanged_man_persona_list = ["Hua Po","Inugami","Orthrus","Take-Minakata","Emperor's Amulet","Hecatoncheires","Jatayu",
    "Moloch","Macabre","Attis"]
    return hanged_man_persona_list

# Clear
def deathArcanaPersonaList():
    death_persona_list = ["Mandrake","Mokoi","Matador","Nue","Pisaca","Hell Biker","Hope Diamond","Pale Rider","Chernobog",
    "Thanatos","Thanatos Picaro","Mot","Alice"]
    return death_persona_list

# Clear
def temperanceArcanaPersonasList():
    temperance_persona_list = ["Genbu","Koppa Tengu","Makami","Jikokuten","Mithra","Byakko","Raja Naga","Gabriel",
    "Ardha"]
    return temperance_persona_list

# Clear
def devilArcanaPersonasList():
    devil_persona_list = ["Incubus","Flauros","Andras","Lilim","Pazuzu","Baphomet","Nebiros","Belial","Beelzebub"]
    return devil_persona_list

# Clear
def towerArcanaPersonasList():
    tower_persona_list = ["Belphegor","Red Rider","Magatsu-Izanagi","Magatsu-Izanagi Picaro","Seth","Black Rider",
    "Mara","Yoshitsune","Mada"]
    return tower_persona_list

# Clear
def starArcanaPersonasList():
    star_persona_list = ["Kodama","Fuu-Ki","Neko Shogun","Kaiwan","Garuda","Vasuki","Sraosha","Hastur","Lucifer"]
    return star_persona_list

# Clear
def moonArcanaPersonasList():
    moon_persona_list = ["Succubus","Onmoraki","Kaguya","Black Ooze","Sui-Ki","Kaguya Picaro","Mothman",
    "Girimehkala","Tsukiyomi","Tsukiyomi Picaro","Lilith","Byakhee","Sandalphon"]
    return moon_persona_list

# Clear
def sunArcanaPersonasList():
   sun_persona_list = ["Suzaku","Thunderbird","Mithras","Yurlungur","Horus","Ganesha","Quetzalcoatl","Asura"]
   return sun_persona_list

# Clear
def judgementArcanaPersonasList():
    judgement_persona_list = ["Anubis","Trumpeter","Yamata-no-Orochi","Abaddon","Messiah",
    "Shiva","Michael","Messiah Picaro","Satan"]
    return judgement_persona_list

# Clear
def faithArcanaPersonasList():
    faith_persona_list = ["Phoenix","Tam Lin","Unicorn","Okuninushi","Orichalcum","Atavaka","Cu Chulainn",
    "Siegfried","Maria"]
    return faith_persona_list

# Clear
def councillorArcanaPersonasList():
    councillor_persona_list = ["Kushi Mitama","Nigi Mitama","Decarabia","Ananta","Yatagarasu","Seiryu",
    "Dionysus","Vohu Manah"]
    return councillor_persona_list


def revealPersonaArcana(prompt):
    personaChoice = str(input(prompt))
    return personaChoice

fool = foolArcanaPersonasList()
magician = magicianArcanaPersonasList()
priestess = priestessArcanaPersonasList()
empress = empressArcanaPersonasList()
emperor = emperorArcanaPersonasList()
hierophant = hierophantArcanaPersonasList()
lovers = loversArcanaPersonasList()
chariot = chariotArcanaPersonasList()
justice = justiceArcanaPersonasList()
hermit = hermitArcanaPersonasList()
fortune = fortuneArcanaPersonaList()
strength = strengthArcanaPersonaList()
hanged_man = hangedManArcanaPersonaList()
death = deathArcanaPersonaList()
temperance = temperanceArcanaPersonasList()
devil = devilArcanaPersonasList()
tower = towerArcanaPersonasList()
star = starArcanaPersonasList()
moon = moonArcanaPersonasList()
sun = sunArcanaPersonasList()
judgement = judgementArcanaPersonasList()
faith = faithArcanaPersonasList()
councillor = councillorArcanaPersonasList()



persona = revealPersonaArcana("Please enter a Persona: ").title()


#def validatePersonas():

# Input validation:
# Validates whether the persona entered is a X Persona
if persona in fool:
    # Validates whether the persona entered is a Fool Persona
    isFoolPersona = True
    if isFoolPersona:
        arcanaType = "Fool"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a X Persona    
elif persona in magician:
    # Validates whether the persona entered is a X Persona
    isMagicianPersona = True
    if isMagicianPersona:
        arcanaType = "Magician"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Priestess Persona
elif persona in priestess:
    isPriestessPersona = True
    if isPriestessPersona:
        arcanaType = "Priestess"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Empress Persona
elif persona in empress:
    isEmpressPersona = True
    if isEmpressPersona:
        arcanaType = "Empress"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Emperor Persona
elif persona in emperor:
    isEmperorPersona = True
    if isEmperorPersona:
        arcanaType = "Emperor"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Hierophant Persona
elif persona in hierophant:
    isHierophantPersona = True
    if isHierophantPersona:
        arcanaType = "Hierophant"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Lovers Persona
elif persona in lovers:
    isLoversPersona = True
    if isLoversPersona:
        arcanaType = "Lovers"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Chariot Persona
elif persona in chariot:
    isChariotPersona = True
    if isChariotPersona:
        arcanaType = "Chariot"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Justice Persona
elif persona in justice:
    isJusticePersona = True
    if isJusticePersona:
        arcanaType = "Justice"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Hermit Persona
elif persona in hermit:
    isHermitPersona = True
    if isHermitPersona:
        arcanaType = "Hermit"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Temperance Persona
elif persona in temperance:
    isTemperancePersona = True
    if isTemperancePersona:
        arcanaType = "Temperance"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Devil Persona
elif persona in devil:
    isDevilPersona = True
    if isDevilPersona:
        arcanaType = "Devil"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging
    
# Validates whether the persona entered is a Tower Persona
elif persona in tower:
    isTowerPersona = True
    if isTowerPersona:
        arcanaType = "Tower"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Star Persona
elif persona in star:
    isStarPersona = True
    if isStarPersona:
        arcanaType = "Star"
    isValidPersona = True 
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Moon Persona
elif persona in moon:
    isMoonPersona = True
    if isMoonPersona:
        arcanaType = "Moon"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Sun Persona
elif persona in sun:
    isSunPersona = True
    if isSunPersona:
        arcanaType = "Sun"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Judgement Persona
elif persona in judgement:
    isJudgementPersona = True
    if isJudgementPersona:
        arcanaType = "Judgement"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Faith Persona
elif persona in faith:
    isFaithPersona = True
    if isFaithPersona:
        arcanaType = "Faith"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# Validates whether the persona entered is a Councillor Persona
elif persona in councillor:
    isCouncillorPersona = True
    if isCouncillorPersona:
        arcanaType = "Councillor"
    isValidPersona = True
    print("\nPersona Summary:")
    print(f"-------------------------------------------")
    print(f"Arcana: {arcanaType}")
    print(f"Persona Name: {persona}")
    #print(f"\nValid Persona = {isValidPersona}") # For debugging

# For if an invalid input is entered
else: 
    isValidPersona = False
    #print(f"\nValid Persona = {isValidPersona}") # For debugging
    print("\nYou did not enter a valid Persona.")


def dualFusion():
    pass
    # Enter one persona
    # Enter another persona
    # The new persona is: 