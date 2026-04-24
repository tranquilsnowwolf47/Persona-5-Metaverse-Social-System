# Filename: RegisterToCompendiumV2.py
# Date: 4/23/26
# Author: Aoi | shadowsnowwolf 

# Update 2026:
# Note:
# Need to write to files, don't append. 
# For example, if you want to register a Lvl 18 Arsene when your previous Arsene was Lvl 10, you would have to 
# overwrite the Lvl 10 Arsene to register it. This would require the write paramater for the mode instead of append
# requirements:
# Get user input and store it


# Store Personas as Objects

# For now, this Program will focus on just registering Personas to the compendium.
# Later, we'll have it do everything, like retrieve Persona info, etc. I would have to read 
# the data from the variable of the Persona object in that case to see 

# Give the user the option choice to register multiple Personas at once
# (Use a list or tuple for this)

# Maybe make inherited classes from the Persona class for each Arcana
# Logic:
# Compendium --> Persona --> Arcana (i.e, Fool)


class Compendium:
    # Constructor that sets the attributes for a Persona's info
    def __init__(self, name, arcana, level, 
    st, ma, en, ag, lu,
    skill1, skill2,skill3, skill4, skill5, skill6,
    skill7, skill8):
        # Info attributes
        self.name = name
        self.arcana = arcana
        self.level = level
       
        # Stat attributes
        self.st = st 
        self.ma = ma 
        self.en = en 
        self.ag = ag 
        self.lu = lu
       
        # Skill attributes
        self.skill1 = skill1 
        self.skill2 = skill2
        self.skill3 = skill3
        self.skill4 = skill4
        self.skill5 = skill5
        self.skill6 = skill6
        self.skill7 = skill7
        self.skill8 = skill8

    def display_persona_arcanas():
        # List of Arcanas that the user will be able to choose from
        list_of_arcanas = ("Fool","Magician","Priestess","Empress","Emperor","Hierophant",
                "Lovers","Chariot","Justice","Hermit","Fortune","Strength",
                "Hanged Man","Death","Temperance","Devil","Tower","Star",
                "Moon","Sun","Judgement","Faith","Councillor") 

        # Uses a for loop to display all the Arcanas 
        print("List of Arcanas: ")
        print("---------------------------------------------")
        for valid_arcana in list_of_arcanas:
            print(valid_arcana)
    

    # Gets input from the user on the Persona they want to register
    def get_persona_info(self):
        # User inputs
        name = input("Enter the Persona's name to register: ")
        # Calls the function so the user can see the list of Arcanas
        self.display_persona_arcanas()

        arcana = input("Enter the Arcana: ")
        try:
            level = int(input("Enter the level: "))
        except ValueError:
            print("You did not enter a valid level.")
        try:
            st = int(input("Enter the St stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            ma = int(input("Enter the stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            en = int(input("Enter the stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            ag = int(input("Enter the stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        try:
            lu = int(input("Enter Lu stat: "))
        except ValueError:
            print("Integer values only are accepted.")
        
        print("Next, please enter the skills of the Persona in the following format: ")
        print("(Skill Name) (Damage Grade Element) | Ex: Data Hex (Heavy Curse)")
        
        try:
            skill1 = input("Enter skill 1: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill2 = input("Enter skill 2: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill3 = input("Enter skill 3: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill4 = input("Enter skill 4: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill5 = input("Enter skill 5: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill6 = input("Enter skill 6: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill7 = input("Enter skill 7: ")
        except ValueError:
            print("Please enter a valid string.")
        try:
            skill8 = input("Enter skill 8: ")
        except ValueError:
            print("Please enter a valid string.")
        
        return name, arcana, level, st, ma, en, ag, lu, skill1, skill2, skill3, skill4, skill5, skill6, skill7,skill8

    # Format's the data from the user input and returns it's info
    def set_persona_info(self):
        persona_info_input = self.get_persona_info()
        
        # Sets the empty arguments to the users inputs
        self.name = persona_info_input[0] # name input
        self.arcana = persona_info_output[1] # arcana input
        self.level = persona_info_output[2] # level input
        self.st = persona_info_output[3] # st input
        self.ma = persona_info_output[4] # ma input
        self.en = persona_info_output[5] # en input
        self.ag = persona_info_input[6] # ag input
        self.lu = persona_info_output[7] # lu input
        self.skill1 = persona_info_output[8] # skill 1 input
        self.skill2 = persona_info_output[9] # skill 2 input
        self.skill3 = persona_info_output[10] # skill 3 input
        self.skill4 = persona_info_output[11] # skill 4 input
        self.skill5 = persona_info_output[12] # skill 5 input
        self.skill6 = persona_info_output[13] # skill 6 input
        self.skill7 = persona_info_output[14] # skill 7 input
        self.skill8 = persona_info_output[15] # skill 8 input
        
        persona_info_output =  f"""
    Persona Registered:  
    Name: {self.name}
    Arcana: {self.arcana}
    Level: {self.level}
    Stats: \n------------------------         
    St: {self.st}
    Ma: {self.ma}
    En: {self.en}
    Ag: {self.ag}
    Lu: {self.lu}

    Skills:
    1. {self.skill1}
    2. {self.skill2}
    3. {self.skill3}
    4. {self.skill4}
    5. {self.skill5}
    6. {self.skill6}
    7. {self.skill7}
    8. {self.skill8}
    \n"""
        return persona_info_output

    # Writes the data to the file 
    def register_persona(self, filename="persona_compendium.txt", mode="w"):
        # Set the data as a variable to manipulate 
        arsene_build = self.set_persona_info()  # Test build for debugging

        # Type cast the data to a string so it can be validly written
        arsene_build = str(arsene_build)

        # Writes the data as a string into the compenidum
        with open(filename, mode) as compendium: # I would write all the persona objects in here, not just this one
            compendium.write(arsene_build)
        

class Persona(Compendium):
    pass


