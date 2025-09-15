#
# List the personas of the Arcana type depending on the user's input
#


# "Emperor's Amulet" - hanged man


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

# Clear
def getPersonaArcana(prompt):
    arcana_choice = str(input(prompt))
    return arcana_choice


# 23 arcanas in total
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



#arcana_input = getPersonaArcana("Please enter an Arcana: ").title()
#if arcana_input in fool or arcana_input in magician or arcana_input in priestess or arcana_input in empress or arcana_input in emperor or arcana_input in hierophant or arcana_input in lovers or arcana_input in chariot or arcana_input in justice or arcana_input in hermit  


for i in death:
    print(i)