# Filename: SkillListProgram.py 
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


skill_types = ("Phys","Gun","Fire","Ice","Elec","Wind","Psy","Nuke","Bless","Curse",
                "Buff","Debuff","Passive Buff","HP Recovery","Ailment Recovery","Passives", "Status Ailment") # A tuple that will hold the list of all skill types 


print("Skill types:")
for skill_type in skill_types:
    print(skill_types)

skill_type = input("Pleae enter a skill type: ") 
# if 
damage_grade_choice = input("Would you look to choose a specific damage grade? (Y-N): ")
