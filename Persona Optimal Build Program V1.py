# Filename: Persona Optimal Build Program V1.py
# Date: 1/30/25
# Author: Aoi | shadowsnowwolf

# Processing:

# Notes:
# A program meant to display the optimal build template of each Arcana 
# Program idea: 
# Persona build randomizer 
# uses random.choice from an array
# New realization: You can use F strings in function parameters
# 16 elements in the number of skill (15 indexes)
# 23 elements in the number of arcanas (22 indexes)

class OptimalBuildSystem:
    list_of_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant",
                    "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                        "Hanged Man","Death","Temperance","Devil","Tower","Star",
                        "Moon","Sun","Judgement","Faith","Councillor") # A tuple that will hold the list of all valid Arcanas

    skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives") # A tuple that will hold the list of all skill types 


    # Function that displays the optimal build template for Fool Personas | Clear
    def display_fool_optimal_build(arcana=f"{list_of_arcanas[0]}",skill_quantity=8):
        print(f"{arcana} Persona Optimal Build Template:")
        print(f"Any {skill_quantity} skills of your choice ")

    # Function that displays the optimal build template for Magician Personas | Clear
    def display_magician_optimal_build(arcana=f"{list_of_arcanas[1]}", **kwargs,): # using kwargs for the element + number
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")

    # Function that displays the optimal build template for Priestess Personas | Clear
    def display_priestess_optimal_build(arcana=f"{list_of_arcanas[2]}", **kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")
        
    # Function that displays the optimal build template for Empress Personas | Clear     
    def display_empress_optimal_build(arcana=f"{list_of_arcanas[3]}", **kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")

    # Function that displays the optimal build template for Emperor Personas | Clear
    def display_emperor_optimal_build(arcana=f"{list_of_arcanas[4]}", **kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")

    # Function that displays the optimal build template for Hierophant Personas | Clear
    def display_hierophant_optimal_build(arcana=f"{list_of_arcanas[5]}",**kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")

    # Function that displays the optimal build template for Lovers Personas | Clear
    def display_lovers_optimal_build(arcana=f"{list_of_arcanas[6]}", **kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")

    # Function that displays the optimal build template for Chariot Personas | Clear
    def display_chariot_optimal_build(arcana=f"{list_of_arcanas[7]}", **kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for skill_type, skill_quantity in kwargs.items():
            print(f"{skill_type} - {skill_quantity} skill(s)")

    # Function that displays the optimal build template for Justice Personas | WIP
    def display_justice_optimal_build(arcana=f"{list_of_arcanas[8]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Hermit Personas | WIP
    def display_hermit_optimal_build(arcana=f"{list_of_arcanas[9]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Fortune Personas | WIP
    def display_fortune_optimal_build(arcana=f"{list_of_arcanas[10]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Strength Personas | WIP
    def display_strength_optimal_build(arcana=f"{list_of_arcanas[11]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Hanged Man Personas | WIP
    def display_hanged_man_optimal_build(arcana=f"{list_of_arcanas[12]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Death Personas | WIP
    def display_death_optimal_build(arcana=f"{list_of_arcanas[13]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Temperance Personas | WIP
    def display_temperance_optimal_build(arcana=f"{list_of_arcanas[14]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Devil Personas | WIP
    def display_devil_optimal_build(arcana=f"{list_of_arcanas[15]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Tower Personas | WIP
    def display_tower_optimal_build(arcana=f"{list_of_arcanas[16]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Star Personas | WIP
    def display_star_optimal_build(arcana=f"{list_of_arcanas[17]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Moon Personas | WIP
    def display_moon_optimal_build(arcana=f"{list_of_arcanas[18]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Sun Personas | WIP
    def display_sun_optimal_build(arcana=f"{list_of_arcanas[19]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Judgement Personas | WIP    
    def display_judgement_optimal_build(arcana=f"{list_of_arcanas[20]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Faith Personas | WIP
    def display_faith_optimal_build(arcana=f"{list_of_arcanas[21]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    # Function that displays the optimal build template for Councillor Personas | WIP
    def display_councillor_optimal_build(arcana=f"{list_of_arcanas[22]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

    
    

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
    OptimalBuildSystem.skill_types[8] : 4,
    OptimalBuildSystem.skill_types[3] : 2,
    OptimalBuildSystem.skill_types[0] : 1,
    OptimalBuildSystem.skill_types[10] : 1,
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

# Function calls / debugging
#OptimalBuildSystem.display_fool_optimal_build()  
#OptimalBuildSystem.display_magician_optimal_build(**magician_skills)  
#OptimalBuildSystem.display_priestess_optimal_build(**priestess_skills) 
#OptimalBuildSystem.display_empress_optimal_build(**empress_skills)
#OptimalBuildSystem.display_emperor_optimal_build(**emperor_skills)
#OptimalBuildSystem.display_hierophant_optimal_build(**hierophant_skills)
#OptimalBuildSystem.display_lovers_optimal_build(**lovers_skills)
#OptimalBuildSystem.display_chariot_optimal_build(**chariot_skills)


is_valid_arcana_choice = False
try:
    arcana_choice = input("Please enter an Arcana: ") # Get the user input
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
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[9]: # Hermit
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[10]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[11]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[12]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[13]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[14]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[15]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[16]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[17]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[18]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[19]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[20]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[21]:
                pass
        elif arcana_choice == OptimalBuildSystem.list_of_arcanas[22]:
                pass
except:
    raise ValueError("Incorrect Arcana entered")
