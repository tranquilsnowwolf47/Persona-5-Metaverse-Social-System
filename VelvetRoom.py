# Filename: VelvetRoom.py
# Date: 6/26/26
# Author: Aoi | shadowsnowwolf 
# Description:
# A program that utlizes modules to perform all major Persona operations within one program for easy access


# Register to compendium
# Skill randomizer
# EXP Program
# Optimal build Program



# List of option choices in the menu
main_menu_choices = ("View a List of Personas", "View Persona Optimal Builds", "Randomize Persona Arcanas", "Open Persona EXP Menu", "View Persona Skill List", "Randomize Persona Skills", "Register Persona to Compendium", "View Persona Compendium")

while True:
    print("Igor: *chuckle* \"Welcome to the Velvet Room.\"\n")

    print("Velvet Room Menu:")
    print("------------------------------------------------------------------------")
    for index, choice in enumerate(main_menu_choices,start=1):
        print(f"{index}. {choice}")

    menu_choice = int(input("\nIgor: \"Please enter a choice (1-8)\": "))

    # View List of Personas
    #-------------------------------------------------------------------------------
    #
    if menu_choice == 1:
        import ListOfPersonas
        
        
    # View Persona Optimal Builds
    #-------------------------------------------------------------------------------
    # Assists with Persona building by giving a recommended skill type template
    elif menu_choice == 2:
        import PersonaOptimalBuildProgram
        
        
    # Persona Arcana Randomizer 
    #-------------------------------------------------------------------------------
    # Assists with choosing Personas to rotate for Wild Card fusion
    elif menu_choice == 3:
        import PersonaArcanaRandomizer
        
        
    # Persona EXP Menu
    #-------------------------------------------------------------------------------
    #
    elif menu_choice == 4:
        import PersonaEXPProgram
        
        
    # Persona Skill List 
    #-------------------------------------------------------------------------------
    #
    elif menu_choice == 5:
        import PersonaSkillListProgramV1
        
    # Persona Skill Randomizer
    #-------------------------------------------------------------------------------
    #
    elif menu_choice == 6:
        import PersonaSkillRandomizer
        
    # Register Persona to Compendium
    #-------------------------------------------------------------------------------
    #
    elif menu_choice == 7:
        print("This function is not available yet! Coming soon")

    # View Persona Compendium
    #-------------------------------------------------------------------------------
    #
    elif menu_choice == 8:
        with open("Persona_compendium_logbookV1.txt","r") as compendium:
                print(compendium.read())

    reprompt = input("Igor: \"Would you like to try again? (Enter y for yes or anything else to quit):\"").lower()
    if reprompt != "y":
        print("Take care Trickster...")
        break
