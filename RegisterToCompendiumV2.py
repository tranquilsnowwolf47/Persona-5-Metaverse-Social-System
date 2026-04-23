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
    skill_one, skill_two,skill_three, skill_four, skill_five, skill_six,
    skill_seven, skill_eight):
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
        self.skill_one = skill_one 
        self.skill_two = skill_two
        self.skill_three = skill_three 
        self.skill_four = skill_four
        self.skill_five = skill_five
        self.skill_six = skill_six
        self.skill_seven = skill_seven 
        self.skill_eight = skill_eight
        

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

        return name, arcana, level, st, ma, ag, en, lu


    # Format's the data from the user input and returns it's info
    def set_persona_info(self,):
        persona_info_input = self.get_persona_info()
        self.name = persona_info_input[0]


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
    def register_persona():
        pass
        

    

class Persona(Compendium):
    pass
