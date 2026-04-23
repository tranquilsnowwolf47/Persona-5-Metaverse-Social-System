# Filename: SkillListProgram.py 
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf

# Processing:
# A program that has a full list of all Persona skills
# Imports the Skill lists as modules 

# Imports the modules of all the skill categories 
#import PhysSkillList
#import GunSkillList
#import FireSkillList
#import IceSkillList
#import ElecSkillList
#import WindSkillList
#import PsySkillList
#import NukeSkillList
#import BlessSkillList
#import CurseSkillList
#import BuffSkillList
#import DebuffSkillList
#import PassiveBuffList


valid_skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives", "Status Ailment") # A tuple that will hold the list of all skill types 

# Elemental skills that reference indexes from valid skill types 
elemental_skills = (valid_skill_types[0],valid_skill_types[1],valid_skill_types[2],valid_skill_types[3],
valid_skill_types[4],valid_skill_types[5])

def display_skill_types():
    print("Skill types:")
    print("-----------------------------")
    for skill_type in valid_skill_types:
        print(skill_type)
        
def get_skill_type():
    skill_type_choice = input("\nPlease enter a skill type: ") 
    if skill_type_choice not in valid_skill_types:
        print("You did not enter a valid skill type.")
    else:
        if skill_type_choice 
    
    
    
    # If they choose an attack skill
    #damage_grade_choice = input("Would you like to choose a specific damage grade? (Y-N): ")
