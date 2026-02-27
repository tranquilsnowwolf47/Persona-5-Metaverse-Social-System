# Filename: SkillListDebug.py
# Date: 2/27/26
# Author: Aoi | shadowsnowwolf


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

#PhysSkillList.severe_skills
#PhysSkillList.heavy_skills
#PhysSkillList.medium_skills
#PhysSkillList.light_skills

#PhysSkillList.PhysSkills.display_skill(PhysSkillList.severe_skills[0])

print("List of Heavy Phys Skills: ")
for skill in PhysSkillList.heavy_skills:
    skill.display_simplified_info()
    
# Prints an individual skill
#PsySkillList.shadow_talk.display_simplified_info()

