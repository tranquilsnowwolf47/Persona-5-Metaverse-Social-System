# Filename: SkillListProgramV1.py 
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf

# Processing:
# A program that has a full list of all Persona skills
# Imports the Skill lists as modules 

# Imports the modules of all the skill categories 
import PhysSkillList
import GunSkillList
import FireSkillList
import IceSkillList
import ElecSkillList
import WindSkillList
import PsySkillList
import NukeSkillList
import BlessSkillList
import CurseSkillList
import BuffSkillList
import DebuffSkillList
import PassiveBuffList
import HPRecoverySkillList
import AilmentRecoverySkillList
import PassiveSkillList


skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives", "Status Ailment") # A tuple that will hold the list of all skill types 

# Elemental skills that reference indexes from valid skill types 
elemental_skills = (skill_types[0],skill_types[1],skill_types[2],skill_types[3],
skill_types[4],skill_types[5], skill_types[6], skill_types[7], skill_types[8],
skill_types[9])

valid_skill_types_indexes = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

damage_grades = ("Light", "Medium", "Heavy", "Severe")

def display_skill_types():
    print("Skill types:")
    print("-----------------------------")
    for index, skill_type in enumerate(skill_types,start=1):
        print(f"{index}. {skill_type}")
        
def get_skill_type():
    # Get the skill type from the user
    skill_type_choice = int(input("\nPlease enter a skill type (1-17): "))
    # 
    if skill_type_choice not in skill_types:
        print("You did not enter a valid skill type.")
    else:
        # if the user chooses other than an elemental skill
        # Buffs
        # --------------------------------------------------------------
        if skill_type_choice == 11: 
            valid_buff_format_choices = ("Singular", "AOE", "Both")
            buff_format_choice_indexes = (1,2,3)
            print("Buff choices:")
            for index, buff_choice in enumerate(valid_buff_format_choices,start=1):
                print(f"{index}. {buff_choice}")
            print("Would you like to see AOE buff skills, singular buff skills or both?")
            buff_format_choice = int(input("Enter a choice (1-3): "))
            # Display the list of all singular buff skills
            if buff_format_choice == 1:
                for skill in BuffSkillList.singular_skills:
                    skill.display_simplified_info()
            # Display the list of AOE buff skills 
            elif buff_format_choice == 2:
                for skill in BuffSkillList.AOE_skills:
                    skill.display_simplified_info()
            # Display the list of all buffs skills
            elif buff_format_choice == 3:
                for group in BuffSkillList.full_buff_skill_list:
                    for buff in group:
                        buff.display_simplified_info()
                    
        # Debuffs
        # --------------------------------------------------------------
        elif skill_type_choice == 12:
            valid_debuff_format_choices = ("Singular", "AOE", "Both")
            debuff_format_choice_indexes = (1,2,3)
            print("Debuff choices:")
            for index, debuff_choice in enumerate(valid_debuff_format_choices,start=1):
                print(f"{index}. {debuff_choice}")
            print("Would you like to see AOE buff skills, singular buff skills or both?")
            debuff_format_choice = int(input("Enter a choice (1-3): "))
            # Display the list of all singular debuff skills
            if buff_format_choice == 1:
                for skill in DebuffSkillList.singular_skills:
                    skill.display_simplified_info()

            # Display the list of all AOE debuff skills
            elif buff_format_choice == 2:
                for skill in DebuffSkillList.aoe_skills:
                    skill.display_simplified_info()

            # Display the list of all debuff skills
            elif buff_format_choice == 3:
                for group in DebuffSkillList.full_debuff_skills:
                    for skill in group:
                        skill.display_simplified_info()
            
        # Passive Buffs   
        # --------------------------------------------------------------
        elif skill_type_choice == 13:
            for skill in PassiveBuffList.passive_buffs:
                skill.display_simplified_info()

        # HP Recovery
        # --------------------------------------------------------------
        elif skill_type_choice == 14:
            pass

        # Ailment Recovery
        elif skill_type_choice == 15:
            print("Ailment Recovery skills are not yet available, sorry :(")
            print("(Comning soon)")

        # Passives
        # --------------------------------------------------------------
        elif skill_type_choice == 16:
            valid_passive_choices = ("Normal", "Affinity", "Both")
            passive_format_choice_indexes = (1,2,3)
            print("Passive choices:")
            for index, passive_choice in enumerate(valid_passive_choices,start=1):
                print(f"{index}. {passive_choice}")
            print("Would you like to see Normal passive skills, affinity passive skills or both?")
            passive_format_choice = int(input("Enter a chioce (1-3): "))
            # Display the list of normal passives
            if passive_format_choice == 1:
                for skill in PassiveSkillList.normal_passive_skills:
                    skill.display_simplified_info()
            # Display the list of affinity passives
            elif passive_format_choice == 2:
                for skill in PassiveSkillList.affinity_passive_skills:
                    skill.display_simplified_info()
            # Display all passive skills
            elif passive_format_choice == 3:
                for group in PassiveSkillList.full_passive_skill_list:
                    for skill in group:
                        skill.display_simplified_info()


        # Status Ailment
        # --------------------------------------------------------------
        if skill_type_choice == 17:
            print("Status Ailment skills are not yet available, sorry :(")
            print("(Comning soon)")

            



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

    
display_skill_types()
get_skill_type()
