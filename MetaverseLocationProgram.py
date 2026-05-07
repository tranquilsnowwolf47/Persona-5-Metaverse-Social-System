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
                 social_receptiveness, repeatability, exp_yield, loot_potential, risk, reward, resource_cost, 
                 treasure_demon_potential, growth_alignment, awakening_potential, date_duration, party_compatability):
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
        # How accessible the location is and how often you can go to and back from it (includes transportation friction, scheduling feasability)
        self.repeatability = repeatability
        #
        self.exp_yield = exp_yield
        #
        self.loot_potential = loot_potential
        #
        self.risk = risk
        #
        self.reward = reward
        # The amount of anticipated HP, SP, item usage, or strategy that will be required for successful infiltration
        self.resource_cost = resource_cost
        #
        self.treasure_demon_potential = treasure_demon_potential
        #
        self.growth_alignment = growth_alignment
        #
        self.awakening_potential = awakening_potential
        #
        self.date_duration = date_duration
        #
        self.party_compataiblity = party_compatability



    # Categorieze the Metaverse Location types into a tuple 
    metaverse_location_types = ("Palace", "Jail", "Mementos")
    priorities = ("Urgent", "High", "Medium", "Low", "Void")
    date_duration = ("Urgent", "Moderate", "Not Urgent")

    def display_info():
        print("")


class Palace(MetaverseLocation):
    pass

class Jail(MetaverseLocation):
    pass

class MementosFloor(MetaverseLocation):
    pass


# Palace location objects
fau = Palace()
supercon = Palace()
otakufest = Palace()
megacon = Palace()

palaces = ()
accepted_palaces = []
voided_palaces = []

# Jail location objects
wpb_jail = Jail()
boca_jail = Jail()
miami_jail = Jail()

jails = ()
accepted_jails = []
voided_jails = []

# Mementos Location objects
hero_hype_con = MementosFloor()
fau_career_fair = MementosFloor()


mementos_floors = ()
accepted_mementos_floors = []
