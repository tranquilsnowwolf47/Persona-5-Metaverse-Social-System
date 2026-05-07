# Filename: MetaverseLocationProgram.py
# Date: 5/7/26
# Author: Aoi | shadowsnowwolf 


# I WILL be using file handling in this program

# Description:
# Program that builds Palaces based on attributes. Contains functions that will assist 
# with Metaverse infiltration, field strategy, and navigation


class MetaverseLocation:
    # Contructor that defines the attributes of a Metaverse Location
    def __init__(self, name, metaverse_location_type, location, priority, social_receptiveness,
                 repeatability, risk, reward, treasure_demon_potential, resource_cost, growth_alignment, 
                 loot_potential, awakening_potential, date_duration, party_compatability, rarity, exp_yield):
        # Name of the Palace
        self.name = name
        # Attribute for the Metaverse Location type (Palace, Jail, Mementos)
        self.name = metaverse_location_type
        # 
        self.location = location
        # The Metaverse location's priority
        self.priority = priority

        # The amount of anticipated HP, SP, item usage, or strategy that will be required for successful infiltration
        self.resource_cost = resource_cost

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
