# Update 2026:
# Note:
# Need to write to files, don't append. 
# For example, if you want to register a Lvl 18 Arsene when your previous Arsene was Lvl 10, you would have to 
# overwrite the Lvl 10 Arsene to register it. This would require the write paramater for the mode instead of append
# requirements:
# Get user input and store it


# Store Personas as Objects


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
        

    # Gets input from the user on the Persona they want to register
    def get_persona_info(self):
        name = input("Please enter the Persona's name to register: ")
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
        
        return name, arcana, level, st, ma, ag, en, lu, skill1, skill2, skill3, skill4, skill5, skill6, skill7,skill8

    # Format's the data from the user input and returns it's info
    def set_persona_info(self):
        persona_info_input = self.get_persona_info()
        
        # Sets the empty arguments to the users inputs
        self.name = persona_info_input[0] # name input
        self.arcana = persona_info_output[1] # arcana input
        self.level = persona_info_output[2] # level input
        self.st = persona_info_output[3] # st input
        self.ma = persona_info_output[4] # ma
        self.en = persona_info_output[5] # en
        self.lu = persona_info_output[6] # lu
        self.skill1 = persona_info_output[7] # skill 1
        self.skill2 = persona_info_output[8] # skill 2
        self.skill3 = persona_info_output[9] # skill 3
        self.skill4 = persona_info_output[10] # skill 4
        self.skill5 = persona_info_output[11] # skill 5
        self.skill6 = persona_info_output[12] # skill 6
        self.skill7 = persona_info_output[13] # skill 7
        self.skill8 = persona_info_output[14] # skill 8
        
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
    1. {self.skill_one}
    2. {self.skill_two}
    3. {self.skill_three}
    4. {self.skill_four}
    5. {self.skill_five}
    6. {self.skill_six}
    7. {self.skill_seven}
    8. {self.skill_eight}
    \n"""
        return persona_info

    # Writes the data to the file 
    def register_persona(self, filename="PersonaCompendiumLogbook.txt", mode="w"):
        arsene_build = set_persona_info()
        with open(filename, mode) as compendium:
            compendium.write(arsene)
        

class Persona(Compendium):
    pass

persona_input = Persona.get_persona_info()
arsene_build = Persona(*persona_input)
