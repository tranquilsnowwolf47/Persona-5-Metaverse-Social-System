# Filename: MetaverseEXPCalculator.py 
# Date: 2/11/26
# Author: Aoi | shadowsnowolf 

# EXP references
# Base EXP = 3
# Ambushed
# RED_SHADOW_AMBUSHED = 9
# YELLOW_SHADOW_AMBUSHED  = 8
# BLUE_SHADOW_AMBUSHED = 7
 
# Normal
# RED_SHADOW_NORMAL = 12
# YELLOW_SHADOW_NORMAL = 11
# BLUE_SHADOW_NORMAL = 10

# Ambushing
# RED_SHADOW_AMBUSHING = 15
# YELLOW_SHADOW_AMBUSHING = 14
# BLUE_SHADOW_AMBUSHING = 13

# All-Out-Attack
# BLUE_SHADOW_ALL_OUT_ATTACK = 8
# YELLOW_SHADOW_ALL_OUT_ATTACK = 9 
# RED_SHADOW_ALL_OUT_ATTACK = 10

# Skills
# Severe Persona skill used - 
# Heavy Persona skill used - 8
# Medium Persona skill used - 7
# Light Persona skill used - 6

class EXPSystem:
    pass

class RedShadow:
    def calculate_red_shadow_ambushed(RED_SHADOW_AMBUSHED=9, BASE_EXP=3): # Ambushed
        return RED_SHADOW_AMBUSHED * BASE_EXP
    def calculate_red_shadow_normal(RED_SHADOW_NORMAL=12, BASE_EXP=3): # Normal
        return RED_SHADOW_NORMAL * BASE_EXP
    def calculate_red_shadow_ambushing(RED_SHADOW_AMUSHING=15, BASE_EXP=3): # Ambushing
        return RED_SHADOW_AMUSHING * BASE_EXP
    def calculate_shadow_all_out_attack(RED_SHADOW_ALL_OUT_ATTACK=8, BASE_EXP=3): # All-Out Attack
        return RED_SHADOW_ALL_OUT_ATTACK * BASE_EXP

class YellowShadow:
    def calculate_yellow_shadow_ambushed(YELLOW_SHADOW_AMBUSHED=8, BASE_EXP=3): # Ambushed
        return YELLOW_SHADOW_AMBUSHED * BASE_EXP
    def calculate_yellow_shadow_normal(YELLOW_SHADOW_NORMAL=11, BASE_EXP=3): # Normal
        return YELLOW_SHADOW_NORMAL * BASE_EXP
    def calculate_yellow_shadow_ambushing(YELLOW_SHADOW_AMBUSHING=14, BASE_EXP=3): # Ambushing
        return YELLOW_SHADOW_AMBUSHING * BASE_EXP
    def calculate_shadow_all_out_attack(YELLOW_SHADOW_ALL_OUT_ATTACK=9, BASE_EXP=3): # All-Out Attack
        return YELLOW_SHADOW_ALL_OUT_ATTACK * BASE_EXP

class BlueShadow:
    def calculate_blue_shadow_ambushed(BLUE_SHADOW_AMBUSHED=7, BASE_EXP=3): # Ambushed
        return BLUE_SHADOW_AMBUSHED * BASE_EXP
    def calculate_blue_shadow_normal(BLUE_SHADOW_NORMAL=10, BASE_EXP=3): # Ambushing
        return BLUE_SHADOW_NORMAL * BASE_EXP
    def calculate_blue_shadow_ambushing(BLUE_SHADOW_AMBUSHING=13, BASE_EXP=3): # Normal
        return BLUE_SHADOW_AMBUSHING * BASE_EXP
    def calculate_shadow_all_out_attack(BLUE_SHADOW_ALL_OUT_ATTACK=10, BASE_EXP=3): # All-Out Attack
        return BLUE_SHADOW_ALL_OUT_ATTACK * BASE_EXP
    
class PersonaSkill:
    def calculate_severe_persona_skill(SEVERE_PERSONA_SKILL=10, BASE_EXP=3): # Severe
        return SEVERE_PERSONA_SKILL * BASE_EXP
    def calculate_heavy_persona_skill(HEAVY_PERSONA_SKILL=8, BASE_EXP=3): # Heavy
        return HEAVY_PERSONA_SKILL * BASE_EXP
    def calculate_medium_persona_skill(MEDIUM_PERSONA_SKILL=7, BASE_EXP=3): # Medium
        return MEDIUM_PERSONA_SKILL * BASE_EXP
    def calculate_light_persona_skill(LIGHT_PERSONA_SKILL=6, BASE_EXP=3): # Light
        return LIGHT_PERSONA_SKILL * BASE_EXP

battle_types = ("All-Out Attack")

# Input:
# Please enter an option choice
# if option choice is equal to ambushed, normal, or ambushing  or all out attack options --> Please enter a shadow color:
# 

experience_choices = ("Ambushing", "Normal", "Ambushed", "All-Out Attack", "Persona skill")

shadow_types = ("Red Shadow", "Yellow Shadow", "Blue Shadow")
skill_grades = ("Severe","Heavy","Medium","Light")



# Show the user a list of the battle experience choices 
print("Battle experience options: ")
print("----------------------------------------------------------")
for index, choice in enumerate(experience_choices, start=1):
    print(f"{index}. {choice}")
print()


battle_choice = int(input("Please enter an option choice (1-5): ")) # get the user inputa


# Input validation
if battle_choice == experience_choices[0]: # For ambushing
    for index, shadow_type in enumerate(shadow_types):
        print(f"{index}. {shadow_type}")
    shadow_color_choice = int(input("Please enter a number for the Shadow's color (-): "))

elif battle_choice == experience_choices[1]: # For normal
    for index, shadow_type in enumerate(shadow_types):
        print(f"{index}. {shadow_type}")
    shadow_color_choice = int(input("Please enter a number for the Shadow's color (-): "))
    
elif battle_choice == experience_choices[2]: # For ambushed 
    for index, shadow_type in enumerate(shadow_types):
        print(f"{index}. {shadow_type}")
    shadow_color_choice = int(input("Please enter a number for the Shadow's color (-): "))

elif battle_choice == experience_choices[3]: # For All-Out Attack
    for index, shadow_type in enumerate(shadow_types):
        print(f"{index}. {shadow_type}")
    shadow_color_choice = int(input("Please enter a number for the Shadow's color (-): "))

elif battle_choice == experience_choices[4]:
    for index, grade in enumerate(skill_grades):
        print(f"{index}. {grade}")
    skill_grade = input("Please enter the damage grade of the skill used (-): ")

#RSA1 =
#RSA2 =

