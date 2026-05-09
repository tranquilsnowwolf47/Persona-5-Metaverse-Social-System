# Filename: MetaverseLocationProgram.py
# Date: 5/7/26
# Author: Aoi | shadowsnowwolf 


# I WILL be using file handling in this program

# Description:
# Program that builds Palaces based on attributes. Contains functions that will assist 
# with Metaverse infiltration, field strategy, and navigation


class MetaverseLocation:
    # Contructor that defines the attributes of a Metaverse Location
    def __init__(self, name, metaverse_location_type, location, infiltration_priority, date,  cost, distance, rarity,
                 social_receptiveness, security_level_sensitivity, repeatability, exp_yield, loot_potential, risk, reward, 
                 resource_cost, treasure_demon_potential, growth_alignment, awakening_potential, date_duration, party_compatability):
        # Name of the Metaverse Location
        self.name = name
        # Attribute for the Metaverse Location type (Palace, Jail, Mementos)
        self.metaverse_location_type = metaverse_location_type
        # Real world location of the Metaverse location
        self.location = location
        # The Metaverse location's infiltration priority (in terms of how relevant it is to puruse that area)
        self.infiltration_priority = infiltration_priority
        # The date in which the event takes place (if applicable)
        self.date = date
        # The cost of attending the event (excluding gas)
        self.cost = cost
        # The distance that the location is in in relativity to you
        self.distance = distance
        # How difficult or infrequent it is to access the location
        self.rarity = rarity
        # How receptive the Shadows in the are are to engaing in combat 
        self.social_receptiveness = social_receptiveness
        # How strongly the environment reacts to your actions in terms of reputation change 
        self.security_level_sensitivity = security_level_sensitivity
        # How often you can realistically and consistently attend the location over time (includes transportation friction, scheduling feasability)
        self.repeatability = repeatability
        # The expected amount of experience points/Persona growth/character growth expected to be received from interacting with the location
        self.exp_yield = exp_yield
        # The potential to obtain tangible external gains from a location (i.e., money, items)
        self.loot_potential = loot_potential
        # The probablity and severity of negative outcomes from engaging with the location
        self.risk = risk
        # The overall value expected to be gained (XP, relationships, status, opportunity, etc)
        self.reward = reward
        # The amount of anticipated HP, SP, item usage, or strategy that will be required for successful infiltration
        self.resource_cost = resource_cost
        # The potential for high value connections (Treasure Demons) to be present and engagable 
        self.treasure_demon_potential = treasure_demon_potential
        # How strongly the location supports long-term evolution and growth trajectory, indepedent of immediate reward
        self.growth_alignment = growth_alignment
        # The potential for meeting high quality connections that could be capable of becoming candidate Persona users/Phantom Thieves
        self.awakening_potential = awakening_potential
        # How long the event will take place for/be available for in the infiltration run 
        self.date_duration = date_duration
        # How likely the party will be able to participate/be aligned with the event (This excludes just myself when it comes to solo runs)
        self.party_compatability = party_compatability


    # Categorize the Metaverse Location types into a tuple 
    metaverse_location_types = ("Palace", "Jail", "Mementos Location")
    
    infiltration_priority_types = ("Urgent", "High", "Medium", "Low", "Void")
    
    distance_types = ("Out-of-state", "Very Far", "Far", "Medium", "Close", "Very Close")
    
    rarity_types = ("Ultra-Rare", "Rare", "Uncommon", "Common")
    
    social_receptiveness_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    security_level_sensitivity_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    repeatability_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    exp_yield_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    loot_potential_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    risk_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    reward_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    resource_cost_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    treasure_demon_potential_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    growth_alignment_types = ("Very High", "High", "Medium", "Low", "Very Low")
    
    awakening_potential_types = ("Very High", "High", "Medium", "Low", "Very Low")

    party_compatability_types = ("Very High", "High", "Medium", "Low", "Very Low")


    date_duration_types = (infiltration_priority_types[0], "Moderate", "Not Urgent")
    growth_alignment = ("Ultra-High",infiltration_priority_types[1], infiltration_priority_types[2], infiltration_priority_types[3], "Very Low")

    # Displays all necessary details about the Metaverse Location
    def display_location_summary(self):
        print("Location Summary:")
        print("-------------------------------------")
        print(f"Name: {self.name}")
        print(f"Type: {self.metaverse_location_type}")
        print(f"Location: {self.location}")
        print(f"Infiltration Priority: {self.infiltration_priority}")
        print(f"Date: {self.date}")
        print(f"Cost: {self.cost}")
        print(f"Distance: {self.distance}")
        print(f"Rarity: {self.rarity}")
        print(f"Social Receptiveness: {self.social_receptiveness}")
        print(f"Security Level Sensitivity: {self.security_level_sensitivity}")
        print(f"Repeatability: {self.repeatability}")
        print(f"EXP Yield: {self.exp_yield}")
        print(f"Loot Potential: {self.loot_potential}")
        print(f"Risk: {self.risk}")
        print(f"Reward: {self.reward}")
        print(f"Resource Cost: {self.resource_cost}")
        print(f"Treasure Demon Potential: {self.treasure_demon_potential}")
        print(f"Growth Alignment: {self.growth_alignment}")
        print(f"Awakening Potential: {self.growth_alignment}")
        print(f"Date Duration: {self.date_duration}")
        print(f"Party Compatability: {self.party_compatability}")


class Palace(MetaverseLocation):
    pass

class Jail(MetaverseLocation):
    pass

class MementosFloor(MetaverseLocation):
    pass

# Palaces
#-------------------------------------------------------------------------
# Palace location objects

# Debugged
example = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                 Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[2], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                 Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                 Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

# Cleared
fau = Palace("Florida Atlantic University (FAU) | Castle of Wrath", Palace.metaverse_location_types[0], "Boca Raton, FL", Palace.infiltration_priority_types[3], "N/A", "A lot of money (college tuition)",
             Palace.distance_types[3],  Palace.rarity_types[2], Palace.social_receptiveness_types[2], Palace.security_level_sensitivity_types[1], Palace.repeatability_types[2], 
             Palace.exp_yield_types[2], Palace.loot_potential_types[2], Palace.risk_types[1], Palace.reward_types[2], Palace.resource_cost_types[1], 
             Palace.treasure_demon_potential_types[2], Palace.growth_alignment[2], Palace.awakening_potential_types[3], Palace.date_duration_types[2], Palace.party_compatability_types[3])

supercon = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                  Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                  Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[2], Palace.reward_types[2], Palace.resource_cost_types[1], 
                  Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

otakufest = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                   Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                   Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                   Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

megacon = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                 Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                 Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                 Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

anime_iwai = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                    Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                    Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                    Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

miraicon = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                  Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                  Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                  Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

mizucon = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                 Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                 Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                 Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

holiday_matsuri = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                         Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                         Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                         Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

ultracon = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                  Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                  Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                  Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

metrocon = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                  Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                  Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                  Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])

anime_festival_orlando = Palace("", Palace.metaverse_location_types[0], "", Palace.infiltration_priority_types[0], "", "",
                                Palace.distance_types[0], Palace.rarity_types[0], Palace.social_receptiveness_types[0], Palace.security_level_sensitivity_types[0], Palace.repeatability_types[0], 
                                Palace.exp_yield_types[0], Palace.loot_potential_types[0], Palace.risk_types[0], Palace.reward_types[0], Palace.resource_cost_types[0], 
                                Palace.treasure_demon_potential_types[0], Palace.growth_alignment[0], Palace.awakening_potential_types[0], Palace.date_duration_types[0], Palace.party_compatability_types[0])


# Tuple that holds all the list of Palace objects
palaces = (fau, supercon, otakufest, megacon, anime_iwai, miraicon, mizucon, holiday_matsuri, ultracon, metrocon, anime_festival_orlando)
accepted_palaces = []
voided_palaces = []

# Jails
#-------------------------------------------------------------------------
# Jail location objects
example = Jail("", Jail.metaverse_location_types[1],"", Jail.infiltration_priority_types[0], "", "",
               Jail.distance_types[0], Jail.rarity_types[0], Jail.social_receptiveness_types[0], Jail.security_level_sensitivity_types[0], Jail.repeatability_types[0],
               Jail.exp_yield_types[0], Jail.loot_potential_types[0], Jail.risk_types[0], Jail.reward_types[0], Jail.resource_cost_types[0], 
               Jail.treasure_demon_potential_types[0], Jail.growth_alignment_types[0], Jail.awakening_potential_types[0], Jail.date_duration_types[0], Jail.party_compatability_types[0])

wpb_jail = Jail("", Jail.metaverse_location_types[1],"", Jail.infiltration_priority_types[0], "", "",
                Jail.distance_types[0], Jail.rarity_types[0], Jail.social_receptiveness_types[0], Jail.security_level_sensitivity_types[0], Jail.repeatability_types[0],
               Jail.exp_yield_types[0], Jail.loot_potential_types[0], Jail.risk_types[0], Jail.reward_types[0], Jail.resource_cost_types[0], 
               Jail.treasure_demon_potential_types[0], Jail.growth_alignment_types[0], Jail.awakening_potential_types[0], Jail.date_duration_types[0], Jail.party_compatability_types[0])


boca_jail = Jail("", Jail.metaverse_location_types[1],"", Jail.infiltration_priority_types[0], "", "",
               Jail.distance_types[0], Jail.rarity_types[0], Jail.social_receptiveness_types[0], Jail.security_level_sensitivity_types[0], Jail.repeatability_types[0],
               Jail.exp_yield_types[0], Jail.loot_potential_types[0], Jail.risk_types[0], Jail.reward_types[0], Jail.resource_cost_types[0], 
               Jail.treasure_demon_potential_types[0], Jail.growth_alignment_types[0], Jail.awakening_potential_types[0], Jail.date_duration_types[0], Jail.party_compatability_types[0])

miami_jail = Jail("", Jail.metaverse_location_types[1],"", Jail.infiltration_priority_types[0], "", "",
                  Jail.distance_types[0], Jail.rarity_types[0], Jail.social_receptiveness_types[0], Jail.security_level_sensitivity_types[0], Jail.repeatability_types[0],
               Jail.exp_yield_types[0], Jail.loot_potential_types[0], Jail.risk_types[0], Jail.reward_types[0], Jail.resource_cost_types[0], 
               Jail.treasure_demon_potential_types[0], Jail.growth_alignment_types[0], Jail.awakening_potential_types[0], Jail.date_duration_types[0], Jail.party_compatability_types[0])

# Tuple that holds all the list of Jail objects
jails = (wpb_jail, boca_jail, miami_jail)
accepted_jails = []
voided_jails = []

# Mementos Floors
#-------------------------------------------------------------------------
# Mementos Location objects
example = MementosFloor("", MementosFloor.metaverse_location_types[2], "", MementosFloor.infiltration_priority_types[0], "", "",
                        MementosFloor.distance_types[0], MementosFloor.rarity_types[0], MementosFloor.social_receptiveness_types[0], MementosFloor.security_level_sensitivity_types[0], MementosFloor.repeatability_types[0],
                        MementosFloor.exp_yield_types[0], MementosFloor.loot_potential_types[0], MementosFloor.risk_types[0], MementosFloor.reward_types[0], MementosFloor.resource_cost_types[0], 
                        MementosFloor.treasure_demon_potential_types[0], MementosFloor.growth_alignment_types[0], MementosFloor.awakening_potential_types[0], MementosFloor.date_duration_types[0], MementosFloor.party_compatability_types[0])

hero_hype_con = MementosFloor("", MementosFloor.metaverse_location_types[2], "", MementosFloor.infiltration_priority_types[0], "", "",
                        MementosFloor.distance_types[0], MementosFloor.rarity_types[0], MementosFloor.social_receptiveness_types[0], MementosFloor.security_level_sensitivity_types[0], MementosFloor.repeatability_types[0],
                        MementosFloor.exp_yield_types[0], MementosFloor.loot_potential_types[0], MementosFloor.risk_types[0], MementosFloor.reward_types[0], MementosFloor.resource_cost_types[0], 
                        MementosFloor.treasure_demon_potential_types[0], MementosFloor.growth_alignment_types[0], MementosFloor.awakening_potential_types[0], MementosFloor.date_duration_types[0], MementosFloor.party_compatability_types[0])


sunrise_comic_con = MementosFloor("", MementosFloor.metaverse_location_types[2], "", MementosFloor.infiltration_priority_types[0], "", "",
                        MementosFloor.distance_types[0], MementosFloor.rarity_types[0], MementosFloor.social_receptiveness_types[0], MementosFloor.security_level_sensitivity_types[0], MementosFloor.repeatability_types[0],
                        MementosFloor.exp_yield_types[0], MementosFloor.loot_potential_types[0], MementosFloor.risk_types[0], MementosFloor.reward_types[0], MementosFloor.resource_cost_types[0], 
                        MementosFloor.treasure_demon_potential_types[0], MementosFloor.growth_alignment_types[0], MementosFloor.awakening_potential_types[0], MementosFloor.date_duration_types[0], MementosFloor.party_compatability_types[0])


fau_career_fair = MementosFloor("", MementosFloor.metaverse_location_types[2], "", MementosFloor.infiltration_priority_types[0], "", "",
                        MementosFloor.distance_types[0], MementosFloor.rarity_types[0], MementosFloor.social_receptiveness_types[0], MementosFloor.security_level_sensitivity_types[0], MementosFloor.repeatability_types[0],
                        MementosFloor.exp_yield_types[0], MementosFloor.loot_potential_types[0], MementosFloor.risk_types[0], MementosFloor.reward_types[0], MementosFloor.resource_cost_types[0], 
                        MementosFloor.treasure_demon_potential_types[0], MementosFloor.growth_alignment_types[0], MementosFloor.awakening_potential_types[0], MementosFloor.date_duration_types[0], MementosFloor.party_compatability_types[0])


plasticon = MementosFloor("", MementosFloor.metaverse_location_types[2], "", MementosFloor.infiltration_priority_types[0], "", "",
                        MementosFloor.distance_types[0], MementosFloor.rarity_types[0], MementosFloor.social_receptiveness_types[0], MementosFloor.security_level_sensitivity_types[0], MementosFloor.repeatability_types[0],
                        MementosFloor.exp_yield_types[0], MementosFloor.loot_potential_types[0], MementosFloor.risk_types[0], MementosFloor.reward_types[0], MementosFloor.resource_cost_types[0], 
                        MementosFloor.treasure_demon_potential_types[0], MementosFloor.growth_alignment_types[0], MementosFloor.awakening_potential_types[0], MementosFloor.date_duration_types[0], MementosFloor.party_compatability_types[0])


# Tuple that holds all teh list of Mementos floor objects
mementos_floors = (hero_hype_con, hero_hype_con, sunrise_comic_con, fau_career_fair, plasticon)
accepted_mementos_floors = []
