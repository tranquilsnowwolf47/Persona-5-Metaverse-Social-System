# Filename: PersonaPartyMenu.py
# Date: 11/21/26
# Author: Aoi | shadowsnowwolf
# Description: An interactable user interface that has a list of Personas in the user's party


# import the Persona skill list here to use
#import 

class PersonaMenu:
    def __init__(self, persona_name, arcana, level, current_EXP, EXP_to_next,
                 st, ma, ag, en, lu, 
                 skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8):
        # Persona Info
        self._persona_name = persona_name
        self._arcana = arcana
        self._level = level
        self._current_EXP = current_EXP
        self._EXP_to_next = EXP_to_next
        
        # Combat Stats
        self._st = st
        self._ma = ma
        self._ag = ag
        self._en = en
        self._lu = lu
        
        # Skills
        self._skill1 = skill1
        self._skill2 = skill2
        self._skill3 = skill3
        self._skill4 = skill4
        self._skill5 = skill5
        self._skill6 = skill6
        self._skill7 = skill7
        self._skill8 = skill8

    # Displays the Persona's info in a full format
    def display_full_persona_info(self):
        print(f"Persona Name: {self._persona_name}")
        print(f"Arcana: {self._arcana}")
        print(f"Level: {self._level}")
        print(f"EXP: {self._current_EXP}/{self._EXP_to_next}")
        print(f"St: {self._st}")
        print(f"Ma: {self._ma}")
        print(f"En: {self._en}")
        print(f"Ag: {self._ag}")
        print(f"Lu: {self._lu}")
        print(f"Skill 1: {self._skill1}")
        print(f"Skill 2: {self._skill2}")
        print(f"Skill 3: {self._skill3}")
        print(f"Skill 4: {self._skill4}")
        print(f"Skill 5: {self._skill5}")
        print(f"Skill 6: {self._skill6}")
        print(f"Skill 7: {self._skill7}")
        print(f"Skill 8: {self._skill8}")

    # Displays the Persona's info in a simplified format 
    def display_simplified_persona_info(self):
        print(f"{self._persona_name} ({self._arcana}) Lv {self._level}")
        



    current_persona_party = []
    reserve_personas = []


# use a for loop to get the number of Personas the user wants to operate with
# then ask for info based on the number of iterations the user asked for
# then place them in the appropriate lists
# have the user categorize them (select a party to add to: (current persona party, reserve personas, shafted personas))

    
