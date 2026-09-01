# Filename: PersonaEXPProgram.py
# Date: 8/31/26
# Author: Aoi | shadowsnowwolf 

# Program that handles EXP with individual Personas
# Make an option to create a Persona from scratch

# Processing: 
# Displays a menu that lets the user choose various options
# The user can see Persona info, level up their Personas, see their
# allotment points, or put their current allotment points into the 5 battle 
# stats to strengthen their Personas 

# Add an option to save the Persona data that the user made through writing to a file 

class Persona:
    # Constructor that defines the attributes of the Persona
    def __init__(self, name, arcana, base_level, base_st, base_ma, base_en, base_ag, base_lu, base_allotment_points):
        self.name = name
        self.arcana = arcana
        self.base_level = base_level
        self.base_st = base_st
        self.base_ma = base_ma
        self.base_en = base_en
        self.base_ag = base_ag
        self.base_lu = base_lu
        self.base_allotment_points = base_allotment_points
        
    # Function that displays the current Personas's info including their combat stats
    def display_persona_info(self):
        print()
        print(f"Name: {self.name}")
        print(f"Arcana: {self.arcana}")
        print(f"Lvl: {self.base_level}")
        print(f"St: {self.base_st}")
        print(f"Ma: {self.base_ma}")
        print(f"En: {self.base_en}")
        print(f"Ag: {self.base_ag}")
        print(f"Lu: {self.base_lu}")
        print(f"Allotment points: {self.base_allotment_points}")

    # Function that levels up the Persona based on the number of levels the user desires 
    def level_up(self):
        levels = int(input("How many levels would you like to add?: ")) # Gets the number of levels from the user
        if levels > 0: # As long as the number is not a negative number, increments the level along with the allotment points
            self.base_level += levels
            self.base_allotment_points += levels
        else:
            print("Please enter a positive number or a number greater than 0.")
        
    # Returns the number of allotment points 
    def get_allotment_points(self):
        return self.base_allotment_points
    
    # Function that helps the user keep track of their allotment points. Value is influenced by incremenets
    # and decrements 
    def display_current_allotment_points(self):
        current_allotment_points = self.get_allotment_points()
        print(f"Current Allotment Points: {current_allotment_points}")

    # Function that increases St points based on the number of allotment point available
    def allot_st(self):
        # Allot from points to st
        self.display_current_allotment_points()
        st_allotment = int(input("Please enter the number of St pts to allot to this Persona: "))
        if self.base_allotment_points >= st_allotment:
            self.base_allotment_points -= st_allotment # Decrements the current allotment points from the input
            self.base_st += st_allotment # Increments the Lu stat with the input variable
        else:
            print()
            print("You don't have enough points to do that operation!")

    # Function that increases Ma points based on the number of allotment point available
    def allot_ma(self):
       # Allot points to ma
       self.display_current_allotment_points()
       ma_allotment = int(input("Please enter the number of Ma pts to allot to this Persona: "))
       if self.base_allotment_points >= ma_allotment:
           self.base_allotment_points -= ma_allotment # Decrements the current allotment points from the input
           self.base_ma += ma_allotment # Increments the Lu stat with the input variable
       else:
            print()
            print("You don't have enough points to do that operation!")

    # Function that increases En points based on the number of allotment point available
    def allot_en(self):
       # Allot points to en
       self.display_current_allotment_points()
       en_allotment = int(input("Please enter the number of En pts to allot to this Persona: "))
       if self.base_allotment_points >= en_allotment:
           self.base_allotment_points -= en_allotment # Decrements the current allotment points from the input
           self.base_en += en_allotment # Increments the Lu stat with the input variable
       else:
            print()
            print("You don't have enough points to do that operation!")

    # Function that increases Ag points based on the number of allotment point available
    def allot_ag(self):
       # Allot points to ag
       self.display_current_allotment_points()
       ag_allotment = int(input("Please enter the number of Ag pts to allot to this Persona: "))
       if self.base_allotment_points >= ag_allotment:
           self.base_allotment_points -= ag_allotment # Decrements the current allotment points from the input
           self.base_ag += ag_allotment # Increments the Lu stat with the input variable
       else:
            print()
            print("You don't have enough points to do that operation!")

    # Function that increases Lu points based on the number of allotment point available
    def allot_lu(self):
       # Allot points to lu
       self.display_current_allotment_points()
       lu_allotment = int(input("Please enter the number of Lu pts to allot to this Persona: "))
       if self.base_allotment_points >= lu_allotment:
           self.base_allotment_points -= lu_allotment # Decrements the current allotment points from the input
           self.base_lu += lu_allotment # Increments the Lu stat with the input variable
       else:
            print()
            print("You don't have enough points to do that operation!")

    # Get input from the user and then return the data
    def get_persona_info(self):
        name_input = input("Enter the Persona's name: ")
        arcana_input = input(f"Enter {name_input}'s Arcana: ")
        level_input = int(input(f"Enter {name_input}'s current level: "))
        st_input = int(input(f"Enter {name_input}'s current St: "))
        ma_input = int(input(f"Enter {name_input}'s current Ma: "))
        en_input = int(input(f"Enter {name_input}'s current En: "))
        ag_input = int(input(f"Enter {name_input}'s current Ag: "))
        lu_input = int(input(f"Enter {name_input}'s current Lu: "))
        allotment_points_input = int(input(f"Enter {name_input}'s current allotment points: "))
        print("--------------------------------------------------------------------")
        print()
        print()

        return name_input, arcana_input, level_input, st_input, ma_input, en_input, ag_input, lu_input, allotment_points_input

    # Set the user data to the arugment values 
    def set_persona_info(self):
        user_persona_info = self.get_persona_info()
        name_input = user_persona_info[0]
        arcana_input = user_persona_info[1]
        level_input = user_persona_info[2]
        st_input = user_persona_info[3]
        ma_input = user_persona_info[4]
        en_input = user_persona_info[5]
        ag_input = user_persona_info[6]
        lu_input = user_persona_info[7]
        allotment_points_input = user_persona_info[8]

        # Set the default Persona arguments to the user input
        self.name = name_input
        self.arcana = arcana_input
        self.base_level = level_input
        self.base_st = st_input
        self.base_ma = ma_input
        self.base_en = en_input
        self.base_ag = ag_input
        self.base_lu = lu_input
        self.base_allotment_points = allotment_points_input
        

    # This needs to be a class method
    @classmethod
    def display_menu(cls, persona):
        loop = True
        while loop:
            # Option choices:
            # Level up
            # Display current allotment points
            # Display persona info
            # Allocwate st
            # Allocate ma
            # Allocate en
            # Allocate ag
            # Allocate lu
            menu_options = ("Display Persona Info",
                            "Display Current Persona Allotment points",
                            "Level Up Persona",
                            "Allocate St Points",
                            "Allocate Ma Points",
                            "Allocate En Points",
                            "Allocate Ag Points",
                            "Allocate Lu Points")
            menu_option_elements = (1,2,3,4,5,6,7,8)

            print("Persona Menu Option Choices:")
            print("---------------------------------------------------------------")
            for option_index, menu_option in enumerate(menu_options, start=1):
                print(f"{option_index}. {menu_option}")

            print()
            menu_option_choice = int(input("Please choose an option choice (1-9): "))
            if menu_option_choice not in menu_option_elements:
                valid_menu_choice = False
                print("You did not enter the correct option choice.")
            elif menu_option_choice == menu_option_elements[0]:
                persona.display_persona_info() # Call the function
                print()
            elif menu_option_choice == menu_option_elements[1]:
                persona.display_current_allotment_points() # Call the function
            elif menu_option_choice == menu_option_elements[2]:
                persona.level_up() # Call the function
            elif menu_option_choice == menu_option_elements[3]:
                persona.allot_st() # Call the function
            elif menu_option_choice == menu_option_elements[4]:
                persona.allot_ma() # Call the function
            elif menu_option_choice == menu_option_elements[5]:
                persona.allot_en() # Call the function
            elif menu_option_choice == menu_option_elements[6]:
                persona.allot_ag() # Call the function
            elif menu_option_choice == menu_option_elements[7]:
                persona.allot_lu() # Call the function

            print()
            loop_choice = input("Would you like to choose another option? (y for yes, anything else to exit): ").lower()
            if loop_choice != "y":
                print("Exiting the program.")
                break
                
# Main operation
while True:
    # Blank template for a Persona which will be modified by user input
    user_persona = Persona("", "", 1, 1,1,1,1,1,1)

    # Main operations 
    user_persona.set_persona_info()
    
    print(f"Current Persona: {user_persona.name} ({user_persona.arcana})")
    Persona.display_menu(user_persona)

    try_again = input("Would you like to modify another Persona? (Enter y for yes, anything else for no): ").lower()
    if try_again != "y":
        break
