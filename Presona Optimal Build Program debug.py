# Test program for debugging and testing for the Optimal Build main program
# 23 elements in the number of arcanas (22 indexes)
# 16 elements in the number of skill (15 indexes)

class OptimalBuildSystem:
    list_of_arcanas = ("Fool","Magician","Priestes","Empress","Emperor","Hierophant",
                    "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                        "Hanged Man","Death","Temperance","Devil","Tower","Star",
                        "Moon","Sun","Judgement","Faith","Councillor") # A tuple that will hold the list of all valid Arcanas

    skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives") # A tuple that will hold the list of all skill types 

    # Function that displays the optimal build template for Priestess Personas | WIP
    def display_priestess_optimal_build(arcana=f"{list_of_arcanas[2]}", **kwargs):
        print(f"{arcana} Persona Optimal Build Template:")
        for element, skill_quantity in kwargs:
            print(f"{element} - {skill_quantity} skill(s)")


# Debugging 

priestess_skills = {
    OptimalBuildSystem.skill_types[6] : 3, # Psy
    OptimalBuildSystem.skill_types[3] : 2, # Ice
    OptimalBuildSystem.skill_types[1] : 1, # Gun
    OptimalBuildSystem.skill_types[12] : 1, # Passive buff
    OptimalBuildSystem.skill_types[11] : 1 # Debuff
}

# 

