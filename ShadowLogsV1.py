# Filename: ShadowLogsV1.py
# Date: 6/17/26
# Author: Aoi | shadowsnowwolf
# Description:
# A program that logs data about a specific type of Shadow that can be use for 
# tactical battle strategy within the Metaverse

class ShadowLog:
    def __init__(self, shadow_name, arcana, type, negotiation_personality_type, third_eye_color, elemental_affinities,
                 resistances, neutral, weaknesses, location_type, specific_location, encounter_context, environmental_buffs, 
                 reccomended_tactics, threat_level, security_sensitivity, loot, reccommended_builds, synopsis):
        # The name of the Shadow whether it's literal or classification of the Shadow
        self._shadow_name = shadow_name
        # The Shadow's Arcana
        self._arcana = arcana
        # The type of Shadow
        self._type = type
        # The Shadow's negotiation type during 
        self._negotiation_personality_type = negotiation_personality_type
        # THe Shadow's color when scanning them with Third Eye
        self._third_eye_color = third_eye_color
        # The elemental affiniies of the Shadow (what elements and skill types they commonly use)
        self._elemental_affinities = elemental_affinities
        # What elements the Shadow resists
        self._resistances = resistances 
        # What elements the Shadow is neutral to
        self._neutral = neutral
        # What elements the Shadow is weak to
        self._weaknesses = weaknesses
        # What the Metaverse Location type of the Shadow is
        self._location_type = location_type
        # The specific location within the Metaverse location that the Shadow is located at
        self._specific_location = specific_location
        # The context of when you'll encounter this Shadow
        self._encounter_context = encounter_context
        # The potential buffs and effects that the Shadow will receive in response to that specific environment 
        self._environmental_buffs = environmental_buffs
        # The reccomended tactics to use against the Shadow to ensure a favorable outcome 
        self._recommended_tactics = reccomended_tactics
        # How much of a threat to your well-being/operations the Shadow is 
        self._threat_level = threat_level
        # How sensitive the Shadow is/will react to actions you make within the Metaverse location
        self._security_sensitivity = security_sensitivity
        # The loot you obtain from beating the Shadow or fighting it
        self._loot = loot
        # The reccomended Personas/skills to use against the Shadow
        self._recommended_builds = reccommended_builds
        # The overall read on the Shadow
        self._synopsis = synopsis
       
    # Tuples with defined info types 
    shadow_types = ("Normal", "Disaster Shadow","Distorted Shadow", "Female Shadow"
                    "Treasure Demon", "Mini-Boss", "Boss")
    third_eye_colors = ("Red", "Yellow", "Blue")
    negotiation_personality_types = ("Upbeat", "Timid", "Gloomy", "Irritable")
    location_types = ("Jail", "Palace","Mementos")
    threat_level_types = ("Very High", "High", "Medium", "Low")
    security_level_sensitivity_types = ("Very High", "High", "Medium", "Low")

    # Elemental affinites
    # Wk = Weak, Res = Resist, Nul = Nullify, Dr = Drain, Rpl = Repel
    elemental_affinity_types = ("Wk", "Res", "Nul", "Dr", "Rpl")
    elements = ("Phys", "Gun", "Fire", "Ice", "Elec", "Wind", "Psy", "Nuke", "Bless", "Curse", 
    "Reverse Phys", "Reverse Gun", "Reverse Fire", "Reverse Ice", "Reverse Elec","Reverse Wind","Reverse Psy","Reverse Nuke","Reverse Bless","Reverse Curse")

    # Function that displays the full info of the Shadow Log
    def display_full_shadow_log(self):
        print(f"Shadow Name: {self._shadow_name}")
        print(f"Arcana: {self._arcana}")
        print(f"Type: {self._type}")
        print(f"Negotiation Personality Type: {self._negotiation_personality_type}")
        print(f"Third Eye Color: {self._third_eye_color}")
        print(f"Elemental Affinities: {self._elemental_affinities}")
        print(f"Resistances: {self._resistances}")
        print(f"Neutral: {self._neutral}")
        print(f"Weaknesses: {self._weaknesses}")
        print(f"Location Type: {self._location_type}")
        print(f"Specific Location: {self._specific_location}")
        print(f"Encounter Context: {self._encounter_context}")
        print(f"Environmental Buffs (if applicable): {self._environmental_buffs}")
        print(f"Reccomended Tactics: {self._recommended_tactics}")
        print(f"Threat Level: {self._threat_level}")
        print(f"Security Sensitivity: {self._security_sensitivity}")
        print(f"Loot: {self._loot}")
        print(f"Reccommended Builds: {self._recommended_builds}")
        print(f"Synopsis: {self._synopsis}")

    # Function that displays just the essential info of the Shadow Log that would be encountered mid-battle
    def display_battle_shadow_log(self):
        print(f"Shadow Name: {self._shadow_name}")
        print(f"Arcana: {self._arcana}")
        print(f"Type: {self._type}")
        print(f"Negotiation Type: {self._negotiation_personality_type}")
        print(f"Elemental Affinities: {self._elemental_affinities}")
        print(f"Resistances: {self._resistances}")
        print(f"Neutral: {self._neutral}")
        print(f"Weaknesses: {self._weaknesses}")


class NormalShadows(ShadowLog):
    pass

class DisasterShadow(ShadowLog):
    pass

class DistoredShadows(ShadowLog):
    pass

class FemaleShadow(ShadowLog):
    pass

class TreasureDemon(ShadowLog):
    pass

class MiniBoss(ShadowLog):
    pass

class BossShadows(ShadowLog):
    pass


# Example
example_shadow = NormalShadows("Dirty Two Horned Beast","Strength", ShadowLog.shadow_types[0], ShadowLog.negotiation_personality_types[0], ShadowLog.third_eye_colors[0],
                               ["Elemental Affinities goes here (use tuple indexes)"], ["Resistances goes here (use tuple indexes)"], ["Neutral goes here (use tuple indexes)"], ["Weaknesses goes here (use tuple indexes)"], "","","","","",
                               ShadowLog.threat_level_types[0],ShadowLog.security_level_sensitivity_types[0], "Loot goes here","Recommended Builds goes here","Synopsis goes here")

# Disaster Shadows
#drama_lover_shadow = DisasterShadow("Drama Lover Shadow", "Moon", ShadowLog.shadow_types[1], ShadowLog.negotiation_personality_types[2],f"{ShadowLog.third_eye_colors[1]}-{ShadowLog.third_eye_colors[0]}",[])
#feminazi_shadow = DisasterShadow("Feminazi Shadow", "", ShadowLog.shadow_types[1],)

# Distorted Shadows
#narcissist_shadow = DistoredShadows("Narcissist Shadow", "", ShadowLog.shadow_types[2], ShadowLog.negotiation_personality_types[3],)

# Female Shadows 
#promiscuous_woman_shadow = FemaleShadow("Promiscuous Woman Shadow","Devil", ShadowLog.shadow_types[5], ShadowLog.negotiation_personality_types[],)
#high_smv_woman_shadow = FemaleShadow("High SMV Woman Shadow","", ShadowLog.shadow_types[3], ShadowLog.negotiation_personality_types[],)
#masculine_woman_shadow = FemaleShadow("Masucline Woman Shadow","", ShadowLog.shadow_types[3], ShadowLog.negotiation_personality_types[],)
#seller_shadow = FemaleShadow("Seller/Onlyfans Girl Shadow","", ShadowLog.shadow_types[3], ShadowLog.negotiation_personality_types[],)
#uninterested_woman_shadow = FemaleShadow()

# Treasure Demons

# Mini Boss Shadows
#high_status_shadow = MiniBoss("High Status Shadow","", ShadowLog.shadow_types[5],)

# Regular Shadows
#victim_mindset_shadow = NormalShadows("Victim Mindset Shadow","", ShadowLog.shadow_types[6],)







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

        


