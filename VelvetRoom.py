# Filename: VelvetRoom.py
# Date: 6/26/26
# Author: Aoi | shadowsnowwolf 
# Description:
# A program that utlizes modules to perform all major Persona building operations within one program for easy access


# Register to compendium
# Skill randomizer
# EXP Program
# Optimal build Program



# List of option choices in the menu
main_menu_choices = ("View List of Personas", "View Persona Optimal Builds", "Persona EXP Menu", "Persona Skill List", "Persona Skill Randomizer", "Register Persona to Compendium", "View Persona Compendium")


print("Igor: \"Welcome to the Velvet Room!\"\n")

print("Velvet Room Menu:")
print("------------------------------------------------------------------------")
for index, choice in enumerate(main_menu_choices,start=1):
    print(f"{index}. {choice}")

menu_choice = int(input("\nEnter a choice (1-4): "))

# View List of Personas
if menu_choice == 1:
    import ListOfPersonasV3
# View Persona Optimal Builds
elif menu_choice == 2:
    import PersonaOptimalBuildProgram
# Persona EXP Menu
elif menu_choice == 3:
    import PersonaEXPProgram
# Persona Skill List 
elif menu_choice == 4:
    import PersonaSkillListProgramV1
# Persona Skill Randomizer
elif menu_choice == 5:
    import PersonaSkillRandomizer
# Register Persona to Compendium
elif menu_choice == 6:
    pass
# View Persona Compendium
elif menu_choice == 7:
    with open("Persona_compendium_logbookV1.txt","r") as compendium:
        print(compendium.read())
