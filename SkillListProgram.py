# Filename: SkillListProgram.py 
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf

# Processing:
# A program that has a full list of all Persona skills
# Imports the Skill lists as modules 

# Imports the modules of all the skill categories 
import PhysSkillList
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
valid_skill_types[4],valid_skill_types[5], valid_skill_types[6], valid_skill_types[7], valid_skill_types[8],
valid_skill_types[9])

damage_grades = ("Light", "Medium", "Heavy", "Severe")

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
        # If the user chooses an elemental skill, give them the choice the filter by damage grade
        if skill_type_choice in elemental_skills:
            damage_grade_validation = input("Would you like to choose a specific damage grade? (Y-N): ").upper().strip()
            if damage_grade_validation == "Y":
                damage_grade_choice = input("Please enter a damage grade (or enter Instant Kill for Instant Kill skills (Curse only)): ").capitalize()
                # If the user chooses Light damage grade, display light skills
                if damage_grade_choice == damage_grades[0]:
                    pass
            # If the user doesn't choose a specific damage grade, just display the list of all elemental skills to them
            else:
                print("List of elemental skills: ")
                print("------------------------------------")
                for elemental_skill in elemental_skills: # I would put the data here from the imported modules, replace later
                    print(elemental_skill)

#print(elemental_skills[9])

    
#display_skill_types()
#get_skill_type()
