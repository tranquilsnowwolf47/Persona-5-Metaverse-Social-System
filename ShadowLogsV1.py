# Filename: ShadowLogsV1.py
# Date:
# Author: Aoi | shadowsnowwolf


class ShadowLog:
    def __init__(self, shadow_name, shadow_arcana, type, third_eye_color, temperament, affinity,
                 resistances, neutral, weaknesses, encounter_context, reccomended_tactics,
                 loot, synopsis):
        self.shadow_name = shadow_name
        self.shadow_arcana = shadow_arcana
        self.type = type
        self.third_eye_color = third_eye_color
        self.temperament = temperament
        self.affinity = affinity
        self.resistances = resistances
        self.neutral = neutral
        self.weaknesses = weaknesses
        self.encounter_context = encounter_context
        self.reccomended_tactics = reccomended_tactics
        self.loot = loot
        self.synopsis = synopsis
     
     shadow_types = ("Normal", "Mini Boss", "Boss")
     
     def display_shadow_log_info(self):
         print(f"Shadow Name: {self.shadow_name}")
         print(f"Arcana: {self.shadow_arcana}")
         print(f"Type: {self.type}")
         print(f"Third Eye Color: {self.third_eye_color}")
         print(f"Temperament/Behavior: {self.temperament}")
         print(f"Affinity: {}")
         print(f"Resistances: {}")
         print(f"Neutral: {}")
         print(f"Weaknesses: {}")
         print(f"Encounter Context/Location: {}")
         print(f"Reccomended Tactics: {}")
         print(f"Loot/Outcome: {}")
         print(f"Synopsis: {}")
         

class BossShadowLog:
    def __init__(self):
        pass
