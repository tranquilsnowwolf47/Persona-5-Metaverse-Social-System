# Filename: Elec Skill List.py
# Date: 2/7/26
# Author: Aoi | shadowsnowwolf
# List of Elec skills (Wit/Humor)

class ElecSkills:
    def __init__(self, name, element, damage_grade, SP_cost, description):
        self.name = name
        self.element = element
        self.damage_grade = damage_grade
        self.SP_cost = SP_cost 
        self.description = description 

    # Shows the full info of the skill
    def display_skill(self):
        print(f"- {self.name} ({self.element})")
        print(f"SP Cost: {self.SP_cost}")
        print(f"Description:\n{self.description}")

class SevereSkills(ElecSkills):
    pass

class HeavySkills(ElecSkills):
    pass

class MediumSkills(ElecSkills):
    pass

class LightSkills(ElecSkills):
    pass

example = HeavySkills("X", "Elec", "Heavy", 0,
"""   - X""")

lightning_retort = HeavySkills("X", "Elec", "Heavy", 0,
"""   - X""")

