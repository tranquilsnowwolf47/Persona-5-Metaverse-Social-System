# Filename: Metaverse EXP Calculator.py 
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
# HEAVY_PERSONA_SKILL = 8
# MEDIUM_PERSONA_SKILL = 7
# LIGHT_PERSONA_SKILL =  6


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
    def calculate_severe_persona_skill(,BASE_EXP=3):
        pass
    def calculate_heavy_persona_skill(,BASE_EXP=3):
        pass
    def calculate_medium_persona_skill(,BASE_EXP=3):
        pass
    def calculate_light_persona_skill(,BASE_EXP=3):
        pass
    
shadow_types = ("Red Shadow", "Yellow Shadow", "Blue Shadow")
battle_types = ("All-Out Attack")





#RSA1 =
#RSA2 =

