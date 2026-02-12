# Filename: PassiveBuffSkillList.py
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf
# List of Passive Buff Skills 

class PassiveBuffSkills:
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

social_competence = PassiveBuffSkills("Social Competence", "Passive Atk Buff | Auto-Tarukaja effect", 0,
""""   - Enter every social encounter with a foundation of practiced social skill. 
This skill comes from social enhancements from going through many successful social interactions to the point where socializing and using elaborate Persona skills becomes second-nature to you. 
Your tone, delivery, timing, body language, and speech skill has been trained and internalized, allowing your words and presence to strike with more impact. Confidence is no longer a guess, it's built in. 
Raises your Atk automatically temporarily upon entering a battle.""")

self_control = PassiveBuffSkills("Self-Control", "Passive Def Buff | Auto-Rakukaja effect", 0,
""""   - Utilize strong internal regulation and emotional discipline, which, at the start of any interaction, automatically reinforces your social defenses. 
The skill causes you to resist overreactions, validation-chasing, frame breaks, or attention/approval seeking. 
Self- Control creates a wall against internal emotional reactions and undesired behaviors and subtly deflects emotional pressure. 
Raises your Def automatically temporarily upon entering a battle.""")

human_nature_savant = PassiveBuffSkills("Human Nature Savant", "Passive Ag Buff | Auto-Sukukaja effect", 0,
""""   - Leverage a deep, intuitive understanding of human behavior and psychology. 
By understanding the expected reactions, behaviors, and patterns behind Shadows, you enter every interaction with heightened precision and adaptability. 
Your techniques rarely miss the mark and you know when to dodge tension before it forms.
Raises your Accuracy/Evasion automatically temporarily upon entering a battle.""")

looksmax = PassiveBuffSkills("Looksmax", "Passive Buff | effect", 0,
""""   -  Enter an encounter with an amplified presence via good looks, enhancing your social power capability. 
The passive aura grants increased presence, resilience, and calibration, framing yourself as high-value before you even speak and granting a good first impression, making people more likely to take you seriously at the start of an interaction. 
The way that you feel in general is also enhanced which grants your overall abilities more traction. 
This may reduce the resistance in conversations through the potential to attract someone passively on top of making you more confident. 
A combination of clear skin, fragrance, a good haircut, a nice outfit, good physique, etc. May trigger the Halo Effect which assumes positive traits about you even if it’s not necessarily true. 
Raises your Atk, Def, and Accuracy/Evasion automatically temporarily upon entering a battle. """)

passive_buffs = (social_competence, self_control, human_nature_savant, looksmax)

