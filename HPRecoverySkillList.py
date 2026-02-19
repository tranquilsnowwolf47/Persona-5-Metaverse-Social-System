# Filename: HPRecoverySkillList.py
# Date: 2/19/26
# Author: Aoi | shadowsnowwolf
# List of HP (Social Stamina) recovery skills

class HPRecoverySkills:
    def __init__(self, name, type, SP_cost, description):
        self.name = name
        self.type = type
        self.SP_cost = SP_cost
        self.description = description

    # Shows the full info of the skill 
    def display_skill(self):
        print(f"- {self.name} ({self.type})")
        print(f"SP Cost: {self.SP_cost}")
        print(f"Description:\n{self.description}")


#example = LightRecoverySkills("X", "Light HP Recovery", 0,
#"""   - X""")

class LightRecoverySkills(HPRecoverySkills):
        pass

class ModerateRecoverySkills(HPRecoverySkills):
        pass

class FullRecoverySkills(HPRecoverySkills):
        pass


# Light HP Recovery Skills
twin_breath = LightRecoverySkills("Twin Breath", "Light HP Recovery", 3,
"""   - Rapidly reset your nervous system through a controlled double inhale and extended exhale, immediately lowering stress and stabilizing your composure. 
Inhale deeply through your nose, take a second short inhale to fully expand the lungs, then release a long, slow exhale through your mouth until empty. 
Repeat 3 times for one cast. 
The technique is based on physiological sighing, and executed outside of combat, or subtly during combat through attentive listening, brief pauses, relaxed posture, and measured speech to avoid suspicion from the Shadow.
Restores a small amount of HP (15%). """)

centered_breathing = LightRecoverySkills("Centered Breathing", "Light HP Recovery", 3,
"""   - Maintain composure and reduce ongoing stress by controlling your diaphragm. Inhale deeply into your abdomen, exhale slowly, and keep your posture relaxed. 
his subtle, continuous breathing restores a small amount of HP over time, helping prevent minor attrition from repeated social pressure. 
Repeat 3 times for one cast. 
Can be used during interactions without drawing attention. Based on belly breathing. 
Restores a small amount of HP (15%).""")

charged_breathing = LightRecoverySkills("Charged Breathing", "Light HP Recovery", 3,
"""   - Calm your nervous system instantly by focusing solely on long, controlled exhales. 
Let the air leave your lungs fully while allowing inhalation to occur naturally and unconsciously. 
This subtle technique lowers heart rate, stabilizes stress, and maintains composure during tense Palace encounters. Repeat 3 times for one cast. 
Can be used mid-interaction without drawing attention from Shadows. 
Restores a small amount of HP (18%).""")

focused_breathing = LightRecoverySkills("Focused Breathing", "Light HP Recovery", 3,
"""   - Calm yourself down and lower your heart rate through deliberate breathing, reducing minor stress and regaining a small amount of HP. 
In this skill, you slowly inhale through your nose, and let out a long exhale through your mouth. 
Inhale for 4 seconds through your nose, hold for 1 second, and then exhale 3 seconds out through your mouth. Repeat 3 times for one cast. 
The skill is performed in a subtle and natural way through listening, pausing, smiling, and speaking to reduce suspicion from the Shadow. 
Restores a moderate amount of HP (35%).""")


# Moderate HP Recovery Skills
cat_nap = ModerateRecoverySkills("Cat Nap", "Moderate HP Recovery", 6,
"""   - A brief power nap that channels mental focus into rapid rest. 
In just minutes, you awaken refreshed, your body’s stamina restored as though you’d slept for hours. 
Can only be used outside an encounter (you can’t nap in the middle of a conversation). 
Restores a moderate amount of HP (35%).""")


# Full HP Recovery Skills


light_recovery_skills = (twin_breath, centered_breathing, charged_breathing, focused_breathing)
moderate_recovery_skills = (cat_nap)
full_recovery_skills = ()
