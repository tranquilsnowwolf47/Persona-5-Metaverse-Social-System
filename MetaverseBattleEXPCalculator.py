# Filename: MetaverseBattleEXPCalculator.py 
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


# Self-note: there's a logic error in the arithmetic calculations 
# Self-note: Shouldn't there be a mini boss and boss all out attack exp amount...?

class EXPCalculator:
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

        # Phantom Thief Info
        self._name = name
        
        
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

    # Returns the numbers in the list 
    def get_EXP_total(self):
        return self._EXP_multipliers

class RedShadow(EXPCalculator):
    # Ambushed
    def calculate_red_shadow_ambushed(EXP_GAINED, self): 
        EXP_GAINED = self._RED_SHADOW_AMBUSHED *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._RED_SHADOW_AMBUSHED) 

    def get_red_shadow_ambushed_EXP(self):
        return self._RED_SHADOW_AMBUSHED

    # Normal
    def calculate_red_shadow_normal(self): 
        self._RED_SHADOW_NORMAL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._RED_SHADOW_NORMAL) 

    # Ambushing
    def calculate_red_shadow_ambushing(self): 
        self._RED_SHADOW_AMBUSHING *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._RED_SHADOW_AMBUSHING) 


class YellowShadow(EXPCalculator):
    # Ambushed
    def calculate_yellow_shadow_ambushed(self): 
        self._YELLOW_SHADOW_AMBUSHED *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._YELLOW_SHADOW_AMBUSHED) 

    # Normal
    def calculate_yellow_shadow_normal(self): 
        self._YELLOW_SHADOW_NORMAL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._YELLOW_SHADOW_NORMAL) 

    # Ambushing
    def calculate_yellow_shadow_ambushing(self): 
        self._YELLOW_SHADOW_AMBUSHING *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._YELLOW_SHADOW_AMBUSHING) 


class BlueShadow(EXPCalculator):
    # Ambushed
    def calculate_blue_shadow_ambushed(self): 
        self._BLUE_SHADOW_AMBUSHED *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._BLUE_SHADOW_AMBUSHED) 
    # Normal
    def calculate_blue_shadow_normal(self): 
        self._BLUE_SHADOW_NORMAL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._BLUE_SHADOW_NORMAL) 
    # Ambushing
    def calculate_blue_shadow_ambushing(self): 
        self._BLUE_SHADOW_AMBUSHING *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._BLUE_SHADOW_AMBUSHING) 


class AllOutAttackOptions(EXPCalculator):
    # Red Shadow All-Out Attack
    def calculate_red_shadow_all_out_attack(self):
        self._RED_SHADOW_ALL_OUT_ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._RED_SHADOW_ALL_OUT_ATTACK) 
    # Yellow Shadow All-Out Attack
    def calculate_yellow_shadow_all_out_attack(self): 
        self._YELLOW_SHADOW_ALL_OUT_ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._YELLOW_SHADOW_ALL_OUT_ATTACK) 
    def calculate_blue_shadow_all_out_attack(self): 
        # Blue Shadow All-Out Attack
        self._BLUE_SHADOW_ALL_OUT_ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._BLUE_SHADOW_ALL_OUT_ATTACK) 

    
class PersonaSkill(EXPCalculator):
    # Severe
    def calculate_severe_persona_skill(self): 
        self._SEVERE_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._SEVERE_PERSONA_SKILL) 
    # Heavy
    def calculate_heavy_persona_skill(self): 
        self._HEAVY_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._HEAVY_PERSONA_SKILL) 
    # Medium
    def calculate_medium_persona_skill(self): 
        self._MEDIUM_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._MEDIUM_PERSONA_SKILL) 
    # Light 
    def calculate_light_persona_skill(self): 
        self._LIGHT_PERSONA_SKILL *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._LIGHT_PERSONA_SKILL) 


class MiniBoss(EXPCalculator):
    # Mini Boss
    def calculate_mini_boss(self):
        self._MINI_BOSS *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._MINI_BOSS) 

    
class Boss(EXPCalculator):
    # Boss
    def calculate_boss(self):
        self._BOSS *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._BOSS) 

    
class BattleOptions(EXPCalculator):
    # Attack
    def calculate_attack(self):
        self._ATTACK *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._ATTACK) 
    # Gun
    def calculate_gun(self):
        self._GUN *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._GUN) 
    # Item
    def calculate_item(self):
        self._ITEM *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._ITEM) 
    # Guard
    def calculate_guard(self):
        self._GUARD *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._GUARD) 
    # Tactics
    def calculate_tactics(self):
        self._TACTICS *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._TACTICS) 


class ArcanaBoost(EXPCalculator):
    def calculate_arcana_boost_activity(self):
        self._ARCANA_BOOST_ACTIVITY *= self._EXP_MULTIPLIER
        self._EXP_multipliers.append(self._ARCANA_BOOST_ACTIVITY) 


class EXPMenu(RedShadow, YellowShadow, BlueShadow, AllOutAttackOptions, PersonaSkill, MiniBoss, Boss, BattleOptions, ArcanaBoost):
    pass




battle_types = ("All-Out Attack")

# Input:
# Please enter an option choice
# if option choice is equal to ambushed, normal, or ambushing  or all out attack options --> Please enter a shadow color:
# 

# Show the user a list of the battle experience choices 
def display_menu_options():
    print("\t\tPersona Battle Experience Accumulator Menu: ")
    print("----------------------------------------------------------")
    print(""" 
    Ambushed:
    1. Red Shadow Ambushed
    2. Yellow Shadow Ambushed
    3. Blue Shadow Ambushed
    -------------------------------------
    Normal:
    4. Red Shadow Normal
    5. Yellow Shadow Normal
    6. Blue Shadow Normal
    -------------------------------------      
    Ambushing:
    7. Red Shadow Ambushing
    8. Yellow Shadow Ambushing
    9. Blue Shadow Ambushing
    -------------------------------------      
    All-Out Attacking:
    10. Red Shadow All-Out Attacked
    11. Yellow Shadow All-Out Attacked
    12. Blue Shadow All-Out Attacked
    -------------------------------------      
    Persona Skills:
    13. Severe Persona skill used
    14. Heavy Perona skill used
    15. Medium Persona skill used
    16. Light Persona skill used
    -------------------------------------
    Operational:
    17. View current EXP
    18. Quit 
    -------------------------------------\n""")

display_menu_options()
valid_options = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)


example_phantom_thief = EXPMenu("Aoi", 50, 0, 0, 0)

battle_choice = int(input("Please enter an option choice to accumualate EXP (1-18) (Enter 18 to quit): ")) # get the user inputa
while battle_choice in valid_options:
#gained_EXP_total = 0 # Accumulator variable 
#exp = input("Enter the base EXP: ")
    # Input validation
    
    #   1. Red Shadow Ambushed
    if battle_choice == valid_options[0]: 
        # Call fuction here
        example_phantom_thief.calculate_red_shadow_ambushed()
        print(f"\n{example_phantom_thief._name} ambushed a Red Shadow.\n")

    # 2. Yellow Shadow Ambushed
    elif battle_choice == valid_options[1]: 
        # Call fuction here
        example_phantom_thief.calculate_yellow_shadow_ambushed()
        print(f"\n{example_phantom_thief._name} ambushed a Yellow Shadow.\n")

    #   3. Blue Shadow Ambushed
    elif battle_choice == valid_options[2]: 
        # Call fuction here
        example_phantom_thief.calculate_blue_shadow_ambushed
        print(f"\n{example_phantom_thief._name} ambushed a Blue Shadow.\n")


    #   4. Red Shadow Normal
    elif battle_choice == valid_options[3]: 
        # Call fuction here
        example_phantom_thief.calculate_red_shadow_normal()
        print(f"\n{example_phantom_thief._name} started a normal encounter with a Red Shadow.\n")


    # 5. Yellow Shadow Normal
    elif battle_choice == valid_options[4]: 
        # Call fuction here
        example_phantom_thief.calculate_yellow_shadow_normal()
        print(f"\n{example_phantom_thief._name} started a normal encounter with a Yellow Shadow.\n")


    # 6. Blue Shadow Normal
    elif battle_choice == valid_options[5]: 
        # Call fuction here
        example_phantom_thief.calculate_blue_shadow_normal()
        print(f"\n{example_phantom_thief._name} started a normal encounter with a Blue Shadow.\n")


    # 7. Red Shadow Ambushing
    elif battle_choice == valid_options[6]: 
        # Call function here 
        example_phantom_thief.calculate_red_shadow_ambushing()
        print(f"\n{example_phantom_thief._name} was ambushed by a Red Shadow.\n")


    # 8. Yellow Shadow Ambushing
    elif battle_choice == valid_options[7]: 
        # Call function here 
        example_phantom_thief.calculate_yellow_shadow_ambushing()
        print(f"\n{example_phantom_thief._name} was ambushed by a Yellow Shadow.\n")
        
    # 9. Blue Shadow Ambushing
    elif battle_choice == valid_options[8]: 
        # Call function here 
        example_phantom_thief.calculate_blue_shadow_ambushing()
        print(f"\n{example_phantom_thief._name} was ambushed by a Blue Shadow.\n")


    # 10. Red Shadow All-Out Attack
    elif battle_choice == valid_options[9]: 
        # Call function here 
        example_phantom_thief._RED_SHADOW_ALL_OUT_ATTACK
        print(f"\n{example_phantom_thief._name} All-Out Attacked a Red Shadow.\n")


    # 11. Yellow Shadow All-Out Attack
    elif battle_choice == valid_options[10]: 
        # Call function here 
        example_phantom_thief.calculate_yellow_shadow_all_out_attack()
        print(f"\n{example_phantom_thief._name} All-Out Attacked a Yellow Shadow.\n")


    # 12. Blue Shadow All-Out Attack
    elif battle_choice == valid_options[11]: 
        # Call function here 
        example_phantom_thief.calculate_blue_shadow_all_out_attack()
        print(f"\n{example_phantom_thief._name} All-Out Attacked a Blue Shadow.\n")


    # 13. Severe Persona Skill
    elif battle_choice == valid_options[12]: 
        # Call function here 
        example_phantom_thief.calculate_severe_persona_skill()
        print(f"\n{example_phantom_thief._name} used a Severe Persona skill.\n")


    # 14. Heavy Persona Skill
    elif battle_choice == valid_options[13]: 
        # Call function here 
        example_phantom_thief.calculate_heavy_persona_skill()
        print(f"\n{example_phantom_thief._name} used a Heavy Persona skill.\n")


    # 15. Medium Persona Skill
    elif battle_choice == valid_options[14]: 
        # Call function here 
        example_phantom_thief.calculate_medium_persona_skill()
        print(f"\n{example_phantom_thief._name} used a Medium Persona skill.\n")


    # 16. Light Persona Skill Used
    elif battle_choice == valid_options[15]: 
        # Call function here 
        example_phantom_thief.calculate_light_persona_skill()
        print(f"\n{example_phantom_thief._name} used a Light Persona skill.\n")


    # 17. View Current EXP
    # Returns and displays the total EXP gained
    elif battle_choice == valid_options[16]:
        total_EXP = sum(example_phantom_thief.get_EXP_total())
        print()
        print(f"\nEXP gained: {total_EXP}")

    # 18. Quit
    # Break the loop and exit the program if chosen
    elif battle_choice == valid_options[17]:
        print()
        print("Exited.")
        break

    #display_menu_options()    
    battle_choice = int(input("\nPlease enter an option choice to accumualate EXP (1-18) (Enter 18 to quit): ")) # get the user inputa


#RSA1 =
#RSA2 =
