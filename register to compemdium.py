
def register_persona(f, name,arcana,level,st,ma,en,ag,lu,skill_one,skill_two,skill_three,skill_four,skill_five,skill_six,skill_seven,skill_eight):
    print("Persona Registered:", file=f)
    print(f"Name: {name}", file=f)
    print(f"Arcana: {arcana}", file=f)
    print(f"Level: {level}\n", file=f)
    print("Stats: \n------------------------", file=f)
    print(f"St: {st}", file=f)
    print(f"Ma: {ma}", file=f)
    print(f"En: {en}", file=f)
    print(f"Ag: {ag}", file=f)
    print(f"Lu: {lu}\n", file=f)

    print("Skills:", file=f)
    print(f"1. {skill_one}", file=f)
    print(f"2. {skill_two}", file=f)
    print(f"3. {skill_three}", file=f)
    print(f"4. {skill_four}", file=f)
    print(f"5. {skill_five}", file=f)
    print(f"6. {skill_six}", file=f)
    print(f"7. {skill_seven}", file=f)
    print(f"8. {skill_eight}", file=f)
    print("\n", file=f)


def register_arsene_build(f):
    return register_persona(
        f, 
        "Arsene","Fool",17,
        2,4,7,2,5,
        "","","","","","","",""
    )

def register_jack_o_lantern_build(f):
    # Register update: 9/14/25
    return register_persona(
        f, 
        "Jack-o'-Lantern", "Magician",20,
        4,10,5,3,2,
        "Winds of Knowledge (Medium Wind)","Career Current (Medium Wind)","Deep Dive (Medium Wind)","Mind Glide (Medium Wind)","Subject Shift (Light Gun)",
        "Mini-Talk (Light Gun)","Echo Shot (Light Gun)","Velvet Note (Medium Fire)")

def register_silky_build(f):
    return register_persona(
        f, 
        "Silky","Priestess",17,
        2,10,6,6,1,
        "Shadow Read (Hvy Psy)","Temperament Read (Light Psy)","Environment Scan (Med Psy)",
        "Observation (Light Psy)","Extraction Shot (Light Gun)","Small-talk (Light Gun)","Reassuring Chill (Light Ice)",
        "Slowed Speech (Ag Buff)"
    )

def register_eligor_build(f):
    return register_persona(
        f, 
        "Eligor", "Emperor",24,
        10,5,7,3,5,
        "Assertive Slice (Phys)","Request Denial (Curse)","Name Repeat (Psy)","Extraction Shot (Gun)","","","",""
    )

def register_bicorn_build(f):
    return register_persona(
        f,
        "Bicorn", "Hermit",16, 
        1,6,6,1,7,
        "Cooldown (Ice)", "Prioritized Presence (Med Psy)","Soulshare (Ice)","Empathic Echo (Ice)","Reassuring Chill (Ice)","","",""
    )

def register_mandrake_build(f):
    return register_persona(
        f,
        "Mandrake", "Death", 20,
        2,4,7,5,7,
        "Slowed Speech (Ag buff)","Self-Control (Auto-Def buff)","Self-Security (Def buff)",
        "Confidence (Atk buff)", "3 Second Rule (Charge)", "", "", ""
    )

def register_kelpie_build(f):
    return register_persona(
        f,
        "Kelpie", "Strength", 16,
        6,3,7,1,2,
        "","","","","","","",""
    )

def register_pixie_build(f):
    return register_persona(
        f,
        "Pixie", "Lovers", 19,
        1,7,4,5,5,
        "Self Respect Affirmation","Prioritized Presence (Med Psy)","Nonchalance (Med Psy)","Interest Level Read (Light Psy)","","","",""
    )

def register_agathion_build(f):
    return register_persona(
        f, 
        "Agathion","Chariot", 20,
        5,4,5,3,2,
        "Self-Control","Gentleman's Flattery","Direct Curiosity","","","","",""
    )

def register_angel_build(f):
    return register_persona(
        f,
        "Angel","Justice", 12,
        3,4,4,4,1,
        "Self-Control","Quick Quip","Shadow Read","Emotoinal Stimulation","Observation","","",""

    )

def register_hua_po_build(f):
    return register_persona(
        f,
        "Hua Po","Hanged Man", 10,
        4,4,1,4,1,
        "Prioritized Presence,","Slowed Speech","Echo Shot","Casual Greeting Shot","Small-talk","Subject Change","Interest Probe",""
    )

def register_stone_of_scone_build(f):
    return register_persona(
        f,
        "Stone of Scone", "Fortune", 13,
        1,1,3 ,3,6,
        "Social Competence","Interest Level Read","","","","","",""
    )

def register_regent_build(f):
    # Register update: 8/31/25
    return register_persona(
        # Register update: 9/15/25
        f,
        "Regent", "Emperor", 20,
        9,6,6,2,1,
        "Assertive Slice (Med Phys)","Stonewall (Med Phys)","Decision Strike (Med Phys)","Cold Cut (Med Phys)",
        "Magnetic Aura (Med Fire)","Verbal Parry (Med Elec)","3 Second Rule (Charge)","Rhythm Break (Ag Debuff)"
    )

def register_queens_necklace_build(f):
    return register_persona(
        f,
        "Queen's Necklace","Empress", 16,
        5,4,3,6,3,
        "Temperament Read","","","","","","",""
    )

def register_slime_build(f):
    # Register update: 9/15/25
    return register_persona(
        f,
        # Register update: 9/15/25
        "Slime","Chariot", 20,
        7,5,5,4,1,
        "Sync surge (Med Nuke)","Hyper Link (Med Nuke)","Flare Blast (Med Nuke)","3 Second Rule (Charge)",
        "Confidence (Atk Buff)","Opening Gambit (Hvy Phys)","Calling Fang (Med Phys)","Brain Flicker (Med Elec)"
    )

def register_mokoi_build(f):
    # Register udpate: 9/15/25
    return register_persona(
        f,
        "Mokoi","Death", 22,
        1,5,9,7,4,
        "Slowed Speech (Ag buff)","Self-Control (Auto Def buff)","Self-Security (Def buff)",
        "Confidence (Atk buff)","Act Sense (Med Psy)","Tranquil Edge (Med Psy)","Hollow Stance (Light Curse)","Minimum Echo (Med Curse)",
    )

def register_obariyon_build(f):
    return register_persona(
        # Register update: 9/15/25
        f,
        "Obariyon","Fool",19,
        6,3,5,3,6
        "Mind Glide (Med Wind)","Deep Dive (Med Wind)","Interest Probe (Med Gun)",
        "Shocking Humor (Light Elec)","Crowd Echo (Med Nuke)","Sync Surge (Med Nuke)",
        "Human Nature Savant (Auto Ag Buff)","Looksmax (Auto Heat-Riser)",
    )

with open("Persona_compendium_list.txt", "w") as out:
    register_arsene_build(out)
    register_jack_o_lantern_build(out)
    register_silky_build(out)
    register_eligor_build(out)
    register_bicorn_build(out)
    register_mandrake_build(out)
    register_kelpie_build(out)
    register_pixie_build(out)
    register_agathion_build(out)
    register_angel_build(out)
    register_hua_po_build(out)
    register_stone_of_scone_build(out)
    register_regent_build(out)
    register_queens_necklace_build(out)
    register_slime_build(out)



def display_persona():
    result = register_persona()
    return result



#name = str(input("Please enter the name of the Persona to register: "))
#arcana = str(input("Please enter the Arcana of the Persona to register: "))
#level = int(input("Please enter the level of the Persona to register: "))
#st = int(input("Please enter the St stat of the Persona to register: "))
#ma = int(input("Please enter the Ma stat of the Persona to register: "))
#en = int(input("Please enter the En stat of the Persona to register: "))
#ag = int(input("Please enter the Ag stat of the Persona to register: "))

#lu = int(input("Please enter the Lu stat of the Persona to register: "))
