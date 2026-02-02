# Test program for debugging and testing for the Optimal Build main program
# 23 elements in the number of arcanas (22 indexes)
# 16 elements in the number of skill (15 indexes)

class OptimalBuildSystem:
    list_of_arcanas = ("Fool","Magician","Priestes","Empress","Emperor","Hierophant",
                    "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                        "Hanged Man","Death","Temperance","Devil","Tower","Star",
                        "Moon","Sun","Judgement","Faith","Councillor") # A tuple that will hold the list of all valid Arcanas

    skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passive") # A tuple that will hold the list of all skill types 

    # Function that displays the optimal build template for Justice Personas | WIP
    def display_justice_optimal_build(arcana=f"{list_of_arcanas[8]}"):
        print(f"{arcana} Persona Optimal Build Template:")
        print("")

# Debugging 


# Call the function
