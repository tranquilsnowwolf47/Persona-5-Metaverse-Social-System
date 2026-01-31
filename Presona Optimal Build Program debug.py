# Test program for debugging and testing for the Optimal Build main program

class OptimalBuildSystem:
    list_of_arcanas = ("Fool","Magician","Priestes","Empress","Emperor","Hierophant",
                    "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                        "Hanged Man","Death","Temperance","Devil","Tower","Star",
                        "Moon","Sun","Judgement","Faith","Councillor") # A tuple that will hold the list of all valid Arcanas

    skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives") # A tuple that will hold the list of all skill types 

    # Function that displays the optimal build template for Magician Personas | WIP
    def display_magician_optimal_build(arcana=f"{list_of_arcanas[1]}", **kwargs,): # using kwargs for the element + number
        print(f"{arcana} Persona Optimal Build Template:")
        for element, skill_quantity in kwargs.items():
            print(f"{element} - {skill_quantity} skills")


OptimalBuildSystem.display_magician_optimal_build()  # Debugging 
