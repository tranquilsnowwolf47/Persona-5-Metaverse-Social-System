# Filename: MetaverseLocationProgram.py
# Date: 5/7/26
# Author: Aoi | shadowsnowwolf 


# I WILL be using file handling in this program

# Description:
# Program that builds Palaces based on attributes. Contains functions that will assist 
# with Metaverse infiltration, field strategy, and navigation


class MetaverseLocation:
    # Contructor that defines the attributes of a Metaverse Location
    def __init__(self, name, metaverse_location_type, location, priority, date, distance, rarity,
                 social_receptiveness, security_level_sensitivity, repeatability, exp_yield, loot_potential, risk, reward, 
                 resource_cost, treasure_demon_potential, growth_alignment, awakening_potential, date_duration, party_compatability):
        # Name of the Metaverse Location
        self.name = name
        # Attribute for the Metaverse Location type (Palace, Jail, Mementos)
        self.name = metaverse_location_type
        # Real world location of the Metaverse location
        self.location = location
        # The Metaverse location's priority (in terms of how relevant it is to puruse that area)
        self.priority = priority
        # The date in which the event takes place (if applicable)
        self.date = date
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
    priority_types = ("Urgent", "High", "Medium", "Low", "Void")
    distance_types = ("Out-of-state", "Very Far", "Far", "Medium", "Close", "Very Close")
    rarity_types = ("Ultra-Rare", "Rare", "Uncommon", "Common")
    social_receptiveness_types = ("Very High", priority_types[1], priority_types[2], priority_types[3])
    security_level_sensitivity_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    repeatability_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    exp_yield_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    loot_potential_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    risk_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    reward_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    resource_cost_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    treasure_demon_potential_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    growth_alignment_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    awakening_potential_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])
    party_compatability_types = (social_receptiveness_types[0], social_receptiveness_types[1], social_receptiveness_types[2], social_receptiveness_types[3])


    date_duration_types = (priority_types[0], "Moderate", "Not Urgent")
    growth_alignment = ("Ultra-High",priority_types[1], priority_types[2], priority_types[3], "Very Low")

    # Displays all necessary details about the Metaverse Location
    def display_location_summary(self):
        print("Location Summary:")
        print("-------------------------------------")
        print(f"Name: {self.name}")
        print(f"Type: {self.metaverse_location_types}")
        print(f"Location: {self.location}")
        print(f"Priority: {self.priority}")
        print(f"Social Receptiveness: {self.social_receptiveness}")
        print(f"Repeatability: {self.repeatability}")
        print(f"EXP Yield: {self.exp_yield}")
        print(f"Loot Potential: {self.loot_potential}")
        print(f"Risk: {self.risk}")
        print(f"Reward: {self.reward}")
        print(f"Resource Cost: {self.resource_cost}")
        print(f"Treasure Demon Potential {self.treasure_demon_potential}")
        print(f"Growth Alignment: {self.growth_alignment}")
        print(f"Awakening Potential: {self.growth_alignment}")
        print(f"Date Duration: {self.date_duration}")
        print(f"Party Compatability: {self.party_compataiblity}")


class Palace(MetaverseLocation):
    pass

class Jail(MetaverseLocation):
    pass

class MementosFloor(MetaverseLocation):
    pass

# Palaces
#-------------------------------------------------------------------------
# Palace location objects
fau = Palace("Florida Atlantic University (FAU)", Palace.metaverse_location_types[0], "Boca Raton, FL", Palace.priority_types[3], "N/A", Palace.distance_types[3], 
             Palace.rarity_types[], Palace.social_receptiveness_types[])
supercon = Palace()
otakufest = Palace()
megacon = Palace()

# Tuple that holds all the list of Palace objects
palaces = (fau, supercon, otakufest, megacon)
accepted_palaces = []
voided_palaces = []

# Jails
#-------------------------------------------------------------------------
# Jail location objects
wpb_jail = Jail()
boca_jail = Jail()
miami_jail = Jail()

# Tuple that holds all the list of Jail objects
jails = (wpb_jail, boca_jail, miami_jail)
accepted_jails = []
voided_jails = []

# Mementos
#-------------------------------------------------------------------------
# Mementos Location objects
hero_hype_con = MementosFloor()
fau_career_fair = MementosFloor()

# Tuple that holds all teh list of Mementos floor objects
mementos_floors = (hero_hype_con, fau_career_fair)
accepted_mementos_floors = []
