# Program that handles EXP with individual Personas


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
        if st_allotment > 0:
            self.base_allotment_points -= st_allotment # Decrements the current allotment points from the input
            self.base_st += st_allotment # Increments the Lu stat with the input variable

    # Function that increases Ma points based on the number of allotment point available
    def allot_ma(self):
       # Allot points to ma
       self.display_current_allotment_points()
       ma_allotment = int(input("Please enter the number of Ma pts to allot to this Persona: "))
       if ma_allotment > 0:
           self.base_allotment_points -= ma_allotment # Decrements the current allotment points from the input
           self.base_ma += ma_allotment # Increments the Lu stat with the input variable

    # Function that increases En points based on the number of allotment point available
    def allot_en(self):
       # Allot points to  en
       self.display_current_allotment_points()
       en_allotment = int(input("Please enter the number of En pts to allot to this Persona: "))
       if en_allotment > 0:
           self.base_allotment_points -= en_allotment # Decrements the current allotment points from the input
           self.base_en += en_allotment # Increments the Lu stat with the input variable

    # Function that increases Ag points based on the number of allotment point available
    def allot_ag(self):
       # Allot points to ag
       self.display_current_allotment_points()
       ag_allotment = int(input("Please enter the number of Ag pts to allot to this Persona: "))
       if ag_allotment > 0:
           self.base_allotment_points -= ag_allotment # Decrements the current allotment points from the input
           self.base_ag += ag_allotment # Increments the Lu stat with the input variable

    # Function that increases Lu points based on the number of allotment point available
    def allot_lu(self):
       # Allot points to lu
       self.display_current_allotment_points()
       lu_allotment = int(input("Please enter the number of Lu pts to allot to this Persona: "))
       if lu_allotment > 0:
           self.base_allotment_points -= lu_allotment # Decrements the current allotment points from the input
           self.base_lu += lu_allotment # Increments the Lu stat with the input variable


    def display_menu(self):
            # Option choices:
            # Level up
            # Display current allotment points
            # Display persona info
            # Allocate st
            # Allocate ma
            # Allocate en
            # Allocate ag
            # Allocate lu
            menu_options = ("Level Up a Persona","Display current Persona allotment points","Display Persona info",
                            "Allocate St Points","Allocate Ma Points","Allocate En Points","Allocate Ag Points",
                            "Allocate Lu Points")
            menu_option_indexes = (1,2,3,4,5,6,7,8)
            print("Persona Menu Option Choices:")
            print("---------------------------------------------------------------")
            for option_index, menu_option in enumerate(menu_options, start=1):
                print(f"{option_index}. {menu_option}")

            print()
            menu_option_choice = int(input("Please choose an option choice (1-8): "))
            if menu_option_choice not in menu_option_indexes:
                valid_menu_choice = False
                print("You did not enter the correct option choice.")
            elif menu_option_choice == menu_option_indexes[0]:
                Persona.level_up() # Call the function
            elif menu_option_choice == menu_option_indexes[1]:
                Persona.display_current_allotment_points() # Call the function
            elif menu_option_choice == menu_option_indexes[2]:
                Persona.display_persona_info() # Call the function
            elif menu_option_choice == menu_option_indexes[3]:
                Persona.allot_st() # Call the function
            elif menu_option_choice == menu_option_indexes[4]:
                Persona.allot_ma() # Call the function
            elif menu_option_choice == menu_option_indexes[5]:
                Persona.allot_en() # Call the function
            elif menu_option_choice == menu_option_indexes[6]:
                Persona.allot_ag() # Call the function
            elif menu_option_choice == menu_option_indexes[7]:
                Persona.allot_lu() # Call the function


    menu_options = ("Level Up a Persona","Display current Persona allotment points","Display Persona info",
                            "Allocate St Points","Allocate Ma Points","Allocate En Points","Allocate Ag Points",
                            "Allocate Lu Points")

    
