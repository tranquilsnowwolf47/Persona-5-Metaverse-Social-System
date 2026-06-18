# Filename: ShadowLogsV1.py
# Date: 6/17/26
# Author: Aoi | shadowsnowwolf
# Description:
# A program that logs data about a specific type of Shadow that can be use for 
# tactical battle strategy within the Metaverse

class ShadowLog:
    def __init__(self, shadow_name, arcana, type, personality_type, third_eye_color, elemental_affinities,
                 resistances, neutral, weaknesses, location_type, specific_location, encounter_context, environmental_buffs, 
                 reccomended_tactics, threat_level, security_sensitivity, loot, reccommended_builds, synopsis):
        # The name of the Shadow whether it's literal or classification of the Shadow
        self.shadow_name = shadow_name
        # The Shadow's Arcana
        self.arcana = arcana
        # The type of Shadow
        self.type = type
        # The Shadow's negotiation type during 
        self.personality_type = personality_type
        # THe Shadow's color when scanning them with Third Eye
        self.third_eye_color = third_eye_color
        # The elemental affiniies of the Shadow (what elements and skill types they commonly use)
        self.elemental_affinities = elemental_affinities
        # What elements the Shadow resists
        self.resistances = resistances 
        # What elements the Shadow is neutral to
        self.neutral = neutral
        # What elements the Shadow is weak to
        self.weaknesses = weaknesses
        # What the Metaverse Location type of the Shadow is
        self.location_type = location_type
        # The specific location within the Metaverse location that the Shadow is located at
        self.specific_location = specific_location
        # The context of when you'll encounter this Shadow
        self.encounter_context = encounter_context
        # The potential buffs and effects that the Shadow will receive in response to that specific environment 
        self.environmental_buffs = environmental_buffs
        # The reccomended tactics to use against the Shadow to ensure a favorable outcome 
        self.recommended_tactics = reccomended_tactics
        # How much of a threat to your well-being/operations the Shadow is 
        self.threat_level = threat_level
        # How sensitive the Shadow is/will react to actions you make within the Metaverse location
        self.security_sensitivity = security_sensitivity
        # The loot you obtain from beating the Shadow or fighting it
        self.loot = loot
        # The reccomended Personas/skills to use against the Shadow
        self.recommended_builds = reccommended_builds
        # The overall read on the Shadow
        self.synopsis = synopsis
       
    # Tuples with defined info types 
    shadow_types = ("Normal", "Disaster Shadow", "Treasure Demon", "Mini-Boss", "Boss")
    third_eye_colors = ("Red", "Yellow", "Blue")
    negotiation_types = ("Upbeat", "Timid", "Gloomy", "Irritable")
    location_types = ("Jail", "Palace","Mementos")
    threat_levels = ("Very High", "High", "Medium", "Low")

    # Elemental affinites
    # Wk = Weak, Res = Resist, Nul = Nullify, Dr = Drain, Rpl = Repel
    elemental_affinities = ("Wk", "Res", "Nul", "Dr", "Rpl")
    elements = ("Phys", "Gun", "Fire", "Ice", "Elec", "Wind", "Psy", "Nuke", "Bless", "Curse")

    # Function that displays the full info of the Shadow Log
    def display_full_shadow_log(self):
        print(f"Shadow Name: {self.shadow_name}")
        print(f"Arcana: {self.arcana}")
        print(f"Type: {self.type}")
        print(f"Negotiation Personality Type: {self.personality_type}")
        print(f"Third Eye Color: {self.third_eye_color}")
        print(f"Elemental Affinities: {self.elemental_affinities}")
        print(f"Resistances: {self.resistances}")
        print(f"Neutral: {self.neutral}")
        print(f"Weaknesses: {self.weaknesses}")
        print(f"Location Type: {self.location_type}")
        print(f"Specific Location: {self.specific_location}")
        print(f"Encounter Context: {self.encounter_context}")
        print(f"Environmental Buffs (if applicable): {self.environmental_buffs}")
        print(f"Reccomended Tactics: {self.recommended_tactics}")
        print(f"Threat Level: {self.threat_level}")
        print(f"Security Sensitivity: {self.security_sensitivity}")
        print(f"Loot: {self.loot}")
        print(f"Reccommended Builds: {self.recommended_builds}")
        print(f"Synopsis: {self.synopsis}")

    # Function that displays just the essential info of the Shadow Log that would be encountered mid-battle
    def display_battle_shadow_log(self):
        print(f"Shadow Name: {self.shadow_name}")
        print(f"Arcana: {self.arcana}")
        print(f"Type: {self.type}")
        print(f"Negotiation Type: {self.personality_type}")
        print(f"Elemental Affinities: {self.elemental_affinities}")
        print(f"Resistances: {self.resistances}")
        print(f"Neutral: {self.neutral}")
        print(f"Weaknesses: {self.weaknesses}")

# A tuple that holds the logs for all Normal Shadows logged
normal_shadows = ()

# A tuple that holds the logs for all Disaster Shadows
disaster_shadows = ()

# A tuple that holds the logs for all Treasure Demons logged
treasure_demon = ()

# A tuple that holds the logs for all Mini-boss Shadows logged
mini_boss_shadows = ()

# A tuple that holds the loggs for all Boss Shadows logged
boss_shadows = ()

        


