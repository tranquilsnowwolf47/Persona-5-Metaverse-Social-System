# Filename: Persona Optimal Build Program.py
# Date: 1/30/25
# Author: Aoi | shadowsnowwolf

# Processing:
# Allow the user to see the optimal bulid template for the corresponding Persona Arcana based on their user input
# Should have a while loop that lets the user keep going if they choose 

# Notes:
# A program meant to display the optimal build template of each Arcana 
# Program idea: 
# Persona build randomizer 
# uses random.choice from an array
# New realization: You can use F strings in function parameters
# 17 elements in the number of skill (16 indexes)
# 23 elements in the number of arcanas (22 indexes)

class OptimalBuildSystem:
    list_of_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant",
                    "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                        "Hanged Man","Death","Temperance","Devil","Tower","Star",
                        "Moon","Sun","Judgement","Faith","Councillor") # A tuple that will hold the list of all valid Arcanas

    skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives", "Status Ailment") # A tuple that will hold the list of all skill types 

    # Function that displays the optimal build template for Fool Personas | Clear
    def display_fool_optimal_build(arcana=f"{list_of_arcanas[0]}",skill_quantity=8):
        print(f"\n{arcana} Persona Optimal Build Template:")
        print(f"Any {skill_quantity} skills of your choice ")
        print("-----------------------------------------------------")

    # Function that displays the optimal build template for Magician Personas | Clear
    def display_magician_optimal_build(arcana=f"{list_of_arcanas[1]}", **kwargs,): # using kwargs for the element + number
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")


    # Function that displays the optimal build template for Priestess Personas | Clear
    def display_priestess_optimal_build(arcana=f"{list_of_arcanas[2]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")
        
    # Function that displays the optimal build template for Empress Personas | Clear     
    def display_empress_optimal_build(arcana=f"{list_of_arcanas[3]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Emperor Personas | Clear
    def display_emperor_optimal_build(arcana=f"{list_of_arcanas[4]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Hierophant Personas | Clear
    def display_hierophant_optimal_build(arcana=f"{list_of_arcanas[5]}",**kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Lovers Personas | Clear
    def display_lovers_optimal_build(arcana=f"{list_of_arcanas[6]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Chariot Personas | Clear
    def display_chariot_optimal_build(arcana=f"{list_of_arcanas[7]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Justice Personas | Clear
    def display_justice_optimal_build(arcana=f"{list_of_arcanas[8]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Hermit Personas | Clear
    def display_hermit_optimal_build(arcana=f"{list_of_arcanas[9]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Fortune Personas | Clear
    def display_fortune_optimal_build(arcana=f"{list_of_arcanas[10]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Strength Personas | Clear
    def display_strength_optimal_build(arcana=f"{list_of_arcanas[11]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Hanged Man Personas | Clear
    def display_hanged_man_optimal_build(arcana=f"{list_of_arcanas[12]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Death Personas | Clear
    def display_death_optimal_build(arcana=f"{list_of_arcanas[13]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Temperance Personas | Clear
    def display_temperance_optimal_build(arcana=f"{list_of_arcanas[14]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Devil Personas | Clear
    def display_devil_optimal_build(arcana=f"{list_of_arcanas[15]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Tower Personas | Clear
    def display_tower_optimal_build(arcana=f"{list_of_arcanas[16]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Star Personas | Clear
    def display_star_optimal_build(arcana=f"{list_of_arcanas[17]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Moon Personas | Clear
    def display_moon_optimal_build(arcana=f"{list_of_arcanas[18]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Sun Personas | Clear
    def display_sun_optimal_build(arcana=f"{list_of_arcanas[19]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Judgement Personas | Clear   
    def display_judgement_optimal_build(arcana=f"{list_of_arcanas[20]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Faith Personas | Clear
    def display_faith_optimal_build(arcana=f"{list_of_arcanas[21]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

    # Function that displays the optimal build template for Councillor Personas | Clear
    def display_councillor_optimal_build(arcana=f"{list_of_arcanas[22]}", **kwargs):
        print(f"\n{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
            print("-----------------------------------------------------")

#print(len(OptimalBuildSystem.skill_types))  # Debugging 
#print(len(OptimalBuildSystem.list_of_arcanas))  # Debugging 

magician_skills = {
    OptimalBuildSystem.skill_types[5]: 3, # Wind
    OptimalBuildSystem.skill_types[1]: 2, # Gun
    OptimalBuildSystem.skill_types[2]: 1, # Fire
    OptimalBuildSystem.skill_types[10]: 1, # Buff
    OptimalBuildSystem.skill_types[12]: 1 # Passive buff
    }

priestess_skills = {
    OptimalBuildSystem.skill_types[6] : 3, # Psy
    OptimalBuildSystem.skill_types[3] : 2, # Ice
    OptimalBuildSystem.skill_types[1] : 1, # Gun
    OptimalBuildSystem.skill_types[12] : 1, # Passive buff
    OptimalBuildSystem.skill_types[11] : 1 # Debuff
}

empress_skills = {
    OptimalBuildSystem.skill_types[8] : 4, # Bless
    OptimalBuildSystem.skill_types[3] : 2, # Ice
    OptimalBuildSystem.skill_types[0] : 1, # Phys
    OptimalBuildSystem.skill_types[10] : 1, # Buff
}

emperor_skills = {
    OptimalBuildSystem.skill_types[0] : 4, # Phys
    OptimalBuildSystem.skill_types[2] : 2, # Fire
    OptimalBuildSystem.skill_types[4] : 1, # Elec
    OptimalBuildSystem.skill_types[10] : 1 # Buff
}

hierophant_skills = {
    OptimalBuildSystem.skill_types[0] : 1, # Phys
    OptimalBuildSystem.skill_types[5] : 1, # Wind
    OptimalBuildSystem.skill_types[10] : 2, # Buffs
    OptimalBuildSystem.skill_types[12] : 1, # Passive buff
    OptimalBuildSystem.skill_types[15] : 2, # Passives
    OptimalBuildSystem.skill_types[14] : 1 # Ailment Recovery
} 

lovers_skills = {
    OptimalBuildSystem.skill_types[7] : 1, # Nuke
    OptimalBuildSystem.skill_types[5] : 1, # Wind
    OptimalBuildSystem.skill_types[10] : 2, # Buffs
    OptimalBuildSystem.skill_types[13] : 2, # HP recovery
    OptimalBuildSystem.skill_types[14] : 2 # Ailment Recovery
} 

chariot_skills = {
    OptimalBuildSystem.skill_types[7] : 3, # Nuke
    OptimalBuildSystem.skill_types[0] : 2, # Phys
    OptimalBuildSystem.skill_types[4] : 1, # Elec
    OptimalBuildSystem.skill_types[10] : 2, # Buff
}

justice_skills = {
    OptimalBuildSystem.skill_types[1] : 2, # Gun
    OptimalBuildSystem.skill_types[6] : 2, # Psy
    OptimalBuildSystem.skill_types[15] : 2, # Passive
    OptimalBuildSystem.skill_types[11] : 1, # Debuff
    OptimalBuildSystem.skill_types[12] : 1, # Passive buff 
}

hermit_skills = {
    OptimalBuildSystem.skill_types[6] : 2, # Psy
    OptimalBuildSystem.skill_types[15] : 2, # Passive
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
    OptimalBuildSystem.skill_types[12] : 1, # Passive buff
    OptimalBuildSystem.skill_types[11] : 1, # Debuff
    OptimalBuildSystem.skill_types[13] : 1, # HP Recovery
}

fortune_skills = {
    OptimalBuildSystem.skill_types[10] : 2, # Buff
    OptimalBuildSystem.skill_types[6] : 1, # Psy
    OptimalBuildSystem.skill_types[9] : 1, # Curse
    OptimalBuildSystem.skill_types[12] : 2, # Passive Buff
    OptimalBuildSystem.skill_types[15] : 1, # Passives
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery Skill
}

strength_skills = {
    OptimalBuildSystem.skill_types[10] : 4, # Buff
    OptimalBuildSystem.skill_types[0] : 2, # Phys
    OptimalBuildSystem.skill_types[12] : 2, # Passive Buffs
}

hanged_man_skills = {
    OptimalBuildSystem.skill_types[15] : 3, # Passive
    OptimalBuildSystem.skill_types[11] : 2, # Debuff
    OptimalBuildSystem.skill_types[10] : 1, # Buff
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
    OptimalBuildSystem.skill_types[13] : 1, # HP recovery
}

death_skills = {
    OptimalBuildSystem.skill_types[10] : 3, # Buff
    OptimalBuildSystem.skill_types[6] : 2, # Psy
    OptimalBuildSystem.skill_types[9] : 2, # Curse
    OptimalBuildSystem.skill_types[12] : 1, # Passive Buff
}

temperance_skills = {
    OptimalBuildSystem.skill_types[10] : 1, # Buff
    OptimalBuildSystem.skill_types[12] : 1, # Passive Buff
    OptimalBuildSystem.skill_types[15] : 2, # Passive
}

devil_skills = {
    OptimalBuildSystem.skill_types[9] : 3, # Curse
    OptimalBuildSystem.skill_types[16] : 2, # Status Ailment 
    OptimalBuildSystem.skill_types[15] : 2, # Passive
    OptimalBuildSystem.skill_types[11] : 1, # Debuff
}

tower_skills = {
    OptimalBuildSystem.skill_types[9] : 2, # Curse 
    OptimalBuildSystem.skill_types[0] : 1, # Phys
    OptimalBuildSystem.skill_types[15] : 2, # Passive
    OptimalBuildSystem.skill_types[12] : 1, # Passive Buff
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery 
    OptimalBuildSystem.skill_types[11] : 1, # Debuff
}

star_skills = {
    OptimalBuildSystem.skill_types[10] : 3, # Buff
    OptimalBuildSystem.skill_types[7] : 2, # Nuke
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
    OptimalBuildSystem.skill_types[12] : 1, # Passive Buff
    OptimalBuildSystem.skill_types[13] : 1, # HP recovery
}

moon_skills = {
    OptimalBuildSystem.skill_types[6] : 2, # Psy 
    OptimalBuildSystem.skill_types[9] : 2, # Curse
    OptimalBuildSystem.skill_types[15] : 3, # Passive
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
}

sun_skills = { 
    OptimalBuildSystem.skill_types[2] : 3, # Fire
    OptimalBuildSystem.skill_types[4] : 1, # Elec
    OptimalBuildSystem.skill_types[10] : 2, # Buff 
    OptimalBuildSystem.skill_types[12] : 1, # Passive Buff
    OptimalBuildSystem.skill_types[11] : 1, # Debuff 
}

judgement_skills = {
    OptimalBuildSystem.skill_types[11] : 2, # Debuff 
    OptimalBuildSystem.skill_types[10] : 2, # Buff 
    OptimalBuildSystem.skill_types[6] : 2, # Psy
    OptimalBuildSystem.skill_types[15] : 1, # Passive
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
}

faith_skills = {
    OptimalBuildSystem.skill_types[8] : 3, # Bless
    OptimalBuildSystem.skill_types[10] : 2, # Buff
    OptimalBuildSystem.skill_types[15] : 1, # Passive
    OptimalBuildSystem.skill_types[12] : 1, # Passive Buff
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
}

councillor_skills = {
    OptimalBuildSystem.skill_types[5] : 2, # Wind
    OptimalBuildSystem.skill_types[3] : 2, # Ice
    OptimalBuildSystem.skill_types[6] : 1, # Psy
    OptimalBuildSystem.skill_types[15] : 1, # Passive
    OptimalBuildSystem.skill_types[14] : 1, # Ailment Recovery
    OptimalBuildSystem.skill_types[13] : 1, # HP Recovery
}


# Now I Just need to implement a while loop
# While, valid arcana choice =

loop = True
while loop:
    arcana_choice = input("\nPlease enter an Arcana (Enter Q to quit): ").capitalize() # Get the user input
    if arcana_choice == "Q":
                print("\nYou have exited the program. Goodbye Trickster.") # Allow condition to exit the program if the user types Q 
                break
    if arcana_choice in OptimalBuildSystem.list_of_arcanas: # validate the input 
        is_valid_arcana_choice = True
        if arcana_choice == OptimalBuildSystem.list_of_arcanas[0]: # Fool
            OptimalBuildSystem.display_fool_optimal_build()
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[1]: # Magician
            OptimalBuildSystem.display_magician_optimal_build(**magician_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[2]: # Priestess
            OptimalBuildSystem.display_priestess_optimal_build(**priestess_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[3]: # Empress
            OptimalBuildSystem.display_empress_optimal_build(**empress_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[4]: # Emperor
            OptimalBuildSystem.display_emperor_optimal_build(**emperor_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[5]: # Hierophant
            OptimalBuildSystem.display_hierophant_optimal_build(**hierophant_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[6]: # Lovers
            OptimalBuildSystem.display_lovers_optimal_build(**lovers_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[7]: # Chariot
                OptimalBuildSystem.display_chariot_optimal_build(**chariot_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[8]: # Justice
            OptimalBuildSystem.display_justice_optimal_build(**justice_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[9]: # Hermit
            OptimalBuildSystem.display_hermit_optimal_build(**hermit_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[10]: # Fortune
            OptimalBuildSystem.display_fortune_optimal_build(**fortune_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[11]: # Strength
            OptimalBuildSystem.display_strength_optimal_build(**strength_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[12]: # Hanged Man
            OptimalBuildSystem.display_hanged_man_optimal_build(**hanged_man_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[13]: # Death
            OptimalBuildSystem.display_death_optimal_build(**death_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[14]: # Temperance
            OptimalBuildSystem.display_temperance_optimal_build(**temperance_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[15]: # Devil
            OptimalBuildSystem.display_devil_optimal_build(**devil_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[16]: # Tower
            OptimalBuildSystem.display_tower_optimal_build(**tower_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[17]: # Star
            OptimalBuildSystem.display_star_optimal_build(**star_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[18]: # Moon
            OptimalBuildSystem.display_moon_optimal_build(**moon_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[19]: # Sun
            OptimalBuildSystem.display_sun_optimal_build(**sun_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[20]: # Judgement
            OptimalBuildSystem.display_judgement_optimal_build(**judgement_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[21]: # Faith
            OptimalBuildSystem.display_faith_optimal_build(**faith_skills)
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[22]: # Councillor
            OptimalBuildSystem.display_councillor_optimal_build(**councillor_skills)
    else:
        print("Invalid input.")
        
