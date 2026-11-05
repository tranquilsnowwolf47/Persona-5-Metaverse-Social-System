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
# Severe Persona skill used - 15
# Heavy Persona skill used - 10
# Medium Persona skill used - 9
# Light Persona skill used - 8


# Self-note: Shouldn't there be a mini boss and boss all out attack exp amount...?

class EXPSystem:
    def __init__(self, 
    name, level, current_EXP, EXP_to_next, total_EXP, EXP_multipliers =[],
    RED_SHADOW_AMBUSHED=9, RED_SHADOW_NORMAL=12, RED_SHADOW_AMBUSHING=15, 
    YELLOW_SHADOW_AMBUSHED=8, YELLOW_SHADOW_NORMAL=11, YELLOW_SHADOW_AMBUSHING=14, 
    BLUE_SHADOW_AMBUSHED=7, BLUE_SHADOW_NORMAL=10, BLUE_SHADOW_AMBUSHING=13, 
    SEVERE_PERSONA_SKILL=15, HEAVY_PERSONA_SKILL=10, MEDIUM_PERSONA_SKILL=9, LIGHT_PERSONA_SKILL=8,
    RED_SHADOW_ALL_OUT_ATTACK=10, YELLOW_SHADOW_ALL_OUT_ATTACK=9, BLUE_SHADOW_ALL_OUT_ATTACK=8,
    MINI_BOSS=30, BOSS=50,
    ARCANA_BOOST_ACTIVITY=10,
    ATTACK=8,GUN=8,ITEM=5,GUARD=5,TACTICS=5,
    EXP_MULTIPLIER=3):
        self._EXP_multipliers = EXP_multipliers
        # Red Shadow EXP values
        self._RED_SHADOW_AMBUSHED = RED_SHADOW_AMBUSHED
        self._RED_SHADOW_NORMAL = RED_SHADOW_NORMAL
        self._RED_SHADOW_AMBUSHING = RED_SHADOW_AMBUSHING
        # Yellow Shadow EXP values 
        self._YELLOW_SHADOW_AMBUSHED = YELLOW_SHADOW_AMBUSHING
        self._YELLOW_SHADOW_NORMAL = YELLOW_SHADOW_NORMAL
        self._YELLOW_SHADOW_AMBUSHING = YELLOW_SHADOW_AMBUSHED
        # Blue Shadow EXP values
        self._BLUE_SHADOW_AMBUSHED = BLUE_SHADOW_AMBUSHED
        self._BLUE_SHADOW_NORMAL = BLUE_SHADOW_NORMAL
        self._BLUE_SHADOW_AMBUSHING = BLUE_SHADOW_AMBUSHING
        # Persona Skill EXP values
        self._LIGHT_PERSONA_SKILL = LIGHT_PERSONA_SKILL
        self._MEDIUM_PERSONA_SKILL = MEDIUM_PERSONA_SKILL
        self._HEAVY_PERSONA_SKILL = HEAVY_PERSONA_SKILL
        self._SEVERE_PERSONA_SKILL = SEVERE_PERSONA_SKILL
        # Mini Boss EXP values
        self._MINI_BOSS = MINI_BOSS
        # Boss EXP values
        self._BOSS = BOSS
        # Arcana Boost Activity
        self._ARCANA_BOOST_ACTIVITY = ARCANA_BOOST_ACTIVITY
        # Battle Options
        self._ATTACK = ATTACK
        self._GUN = GUN
        self._ITEM = ITEM
        self._GUARD = GUARD 
        self._TACTICS = TACTICS
        # All Out Attack Options
        self._RED_SHADOW_ALL_OUT_ATTACK = RED_SHADOW_ALL_OUT_ATTACK
        self._YELLOW_SHADOW_ALL_OUT_ATTACK = YELLOW_SHADOW_ALL_OUT_ATTACK
        self._BLUE_SHADOW_ALL_OUT_ATTACK = BLUE_SHADOW_ALL_OUT_ATTACK
        # EXP Multiplier 
        self._EXP_MULTIPLIER = EXP_MULTIPLIER

    

class RedShadow(EXPSystem):
    # Ambushed
    def calculate_red_shadow_ambushed(self): 
        self._RED_SHADOW_AMBUSHED *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    # Normal
    def calculate_red_shadow_normal(self): 
        self._RED_SHADOW_NORMAL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    # Ambushing
    def calculate_red_shadow_ambushing(self): 
        self._RED_SHADOW_AMBUSHING *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 


class YellowShadow(EXPSystem):
    # Ambushed
    def calculate_yellow_shadow_ambushed(self): 
        self._YELLOW_SHADOW_AMBUSHED *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    # Normal
    def calculate_yellow_shadow_normal(self): 
        self._YELLOW_SHADOW_NORMAL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    # Ambushing
    def calculate_yellow_shadow_ambushing(self): 
        self._YELLOW_SHADOW_AMBUSHING *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 


class BlueShadow(EXPSystem):
    # Ambushed
    def calculate_blue_shadow_ambushed(self): 
        self._BLUE_SHADOW_AMBUSHED *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 
    # Normal
    def calculate_blue_shadow_normal(self): 
        self._BLUE_SHADOW_NORMAL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 
    # Ambushing
    def calculate_blue_shadow_ambushing(self): 
        self._BLUE_SHADOW_AMBUSHING *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 


class AllOutAttackOptions(EXPSystem):
    # Red Shadow All-Out Attack
    def calculate_red_shadow_all_out_attack(self):
        self._RED_SHADOW_ALL_OUT_ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 
    # Yellow Shadow All-Out Attack
    def calculate_yellow_shadow_all_out_attack(self): 
        self._YELLOW_SHADOW_ALL_OUT_ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 
    def calculate_blue_shadow_all_out_attack(self): 
        # Blue Shadow All-Out Attack
        self._BLUE_SHADOW_ALL_OUT_ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    
class PersonaSkill(EXPSystem):
    # Severe
    def calculate_severe_persona_skill(self): 
        self._SEVERE_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    # Heavy
    def calculate_heavy_persona_skill(self): 
        self._HEAVY_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    # Medium
    def calculate_medium_persona_skill(self): 
    # Light
        self._MEDIUM_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    def calculate_light_persona_skill(self): 
        self._LIGHT_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 


class MiniBoss(EXPSystem):
    def calculate_mini_boss(self):
        self._MINI_BOSS *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    
class Boss(EXPSystem):
    def calculate_boss(self):
        self._BOSS *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    
class BattleOptions(EXPSystem):
    # 
    def calculate_attack(self):
        self._ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    #
    def calculate_gun(self):
        self._GUN *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    #
    def calculate_item(self):
        self._ITEM *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    #
    def calculate_guard(self):
        self._GUARD *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 

    #
    def calculate_tactics(self):
        self._TACTICS *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 


    
class ArcanaBoost(EXPSystem):
    def calculate_arcana_boost_activity(self):
        self._ARCANA_BOOST_ACTIVITY *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._EXP_MULTIPLIER) 



    def get_EXP_total(self):
        return self._EXP_multipliers

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

