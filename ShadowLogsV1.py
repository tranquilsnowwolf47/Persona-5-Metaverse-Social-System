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
    

class BossShadowLog:
    def __init__(self):
        pass
