# Program that handles EXP with individual Personas


class Persona:
    def __init__(self, name, arcana, level, st, ma, en, ag, lu, allotment_points):
        self.name = name
        self.arcana = arcana
        self.level = level
        self.st = st
        self.ma = ma
        self.en = en
        self.ag = ag
        self.lu = lu
        self.allotment_points = allotment_points
        
    def display_persona_info(self):
        print(f"Name: {self.name}")
        print(f"Arcana: {self.arcana}")
        print(f"Lvl: {self.level}")
        print(f"St: {self.st}")
        print(f"Ma: {self.ma}")
        print(f"En: {self.en}")
        print(f"Ag: {self.ag}")
        print(f"Lu: {self.lu}")
        print(f"Allotment points: {self.allotment_points}")

    def level_up(self):
        levels = int(input("How many levels would you like to add?: "))
        if levels > 0:
            self.level += levels
            self.allotment_points += levels
        else:
            print("Please enter a positive number or a number greater than 0.")
        # use a for loop to increment the allotment points 

    def get_allotment_points(self):
        return self.allotment_points
    
    # Function that helps the user keep track of their allotment points. Value is influenced by incremenets
    # and decrements 
    def display_current_allotment_points(self):
        current_allotment_points = self.get_allotment_points()
        print(f"Current Allotment Points: {current_allotment_points}")

    def allot_st(self):
        # Allot from points to st
        self.display_current_allotment_points()
        st_allotment = int(input("Please enter the number of St pts to allot to this Persona: "))
        if st_allotment > 0:
            self.allotment_points -= st_allotment # Decrements the current allotment points from the input
            self.st += st_allotment # Increments the Lu stat with the input variable

    def allot_ma(self):
       self.display_current_allotment_points()
       ma_allotment = int(input("Please enter the number of Ma pts to allot to this Persona: "))
       if ma_allotment > 0:
           self.allotment_points -= ma_allotment # Decrements the current allotment points from the input
           self.ma += ma_allotment # Increments the Lu stat with the input variable

    def allot_en(self):
       self.display_current_allotment_points()
       en_allotment = int(input("Please enter the number of En pts to allot to this Persona: "))
       if en_allotment > 0:
           self.allotment_points -= en_allotment # Decrements the current allotment points from the input
           self.en += en_allotment # Increments the Lu stat with the input variable

    def allot_ag(self):
       self.display_current_allotment_points()
       ag_allotment = int(input("Please enter the number of Ag pts to allot to this Persona: "))
       if ag_allotment > 0:
           self.allotment_points -= ag_allotment # Decrements the current allotment points from the input
           self.ag += ag_allotment # Increments the Lu stat with the input variable

    def allot_lu(self):
       self.display_current_allotment_points()
       lu_allotment = int(input("Please enter the number of Lu pts to allot to this Persona: "))
       if lu_allotment > 0:
           self.allotment_points -= lu_allotment # Decrements the current allotment points from the input
           self.lu += lu_allotment # Increments the Lu stat with the input variable

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

    
