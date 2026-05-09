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

def create_jail():
    name = input("Enter the name of the Jail: ")


def create_mementos_floor():
    name = input("Enter the name of the Mementos Floor: ")
    location = input("Enter the location: ")
    print("Infiltration Priority Types:")
    for index, priority in enumerate(MementosFloor.infiltration_priority_types,start=1):
        print(f"{index}. {priority}")
    priority = input("Enter the priority (1-5): ")
    date = input("Enter the date: ")
    cost = input("Enter the cost to attend the Mementos Floor: ")

    print("Distance Types:")
    for index, distance in enumerate(MementosFloor.distance_types,start=1):
        print(f"{index}. {distance}")
    distance = input("Enter the distance (1-6): ")

    for index, rarity in enumerate(MementosFloor.rarity_types,start=1):
        print(f"{index}. {rarity}")
    rarity = input("Enter the rarity: ")

    for index, receptiveness in enumerate(MementosFloor.social_receptiveness_types,start=1):
        print(f"{index}. {receptiveness}")
    receptiveness = input("Enter the social receptiveness level: ")

    for index, security in enumerate(MementosFloor.security_level_sensitivity_types,start=1):
        print(f"{index}. {security}")
    security = input("Enter the security level sensitivity: ")

    for index, repeatability in enumerate(MementosFloor.repeatability_types):
        print(f"{index}. {repeatability}")
    repeatability = input("Enter the repeatability: ")

    for index, exp_yield in enumerate(MementosFloor.exp_yield_types,start=1):
        print(f"{index}. {exp_yield}")
    exp_yield = input("Enter the exp yield level: ")

    for index, loot_potential in enumerate(MementosFloor.loot_potential_types,start=1):
        print(f"{index}. {loot_potential}")
    loot_potential = input("Enter the loot potential level: ")

    for index, risk in enumerate(MementosFloor.risk_types,start=1):
        print(f"{index}. {risk}")
    risk = input("Enter the risk level: ")

    for index, reward in enumerate(MementosFloor.reward_types,start=1):
        print(f"{index}. {reward}")
    reward = input("Enter the reward level: ")

    for index, resource_cost in enumerate(MementosFloor.resource_cost_types,start=1):
        print(f"{index}. {resource_cost}")
    resource_cost = input("Enter the resource cost: ")

    for index, treasure_demon_potential in enumerate(MementosFloor.treasure_demon_potential_types,start=1):
        print(f"{index}. {treasure_demon_potential}")
    treasure_demon_potential = input("Enter the Treasure Demon potential level: ")

    for index, growth_alignment in enumerate(MementosFloor.growth_alignment,start=1):
        print(f"{index}. {growth_alignment}")
    growth_alignment = input("Enter the growth potential: ")

    for index, awakening_potential in enumerate(MementosFloor,start=1):
        print(f"{index}. {awakening_potential}")
    awakening_potential = input("Enter the awakening potential: ")

    date_duration = input("Enter the date duration: ")

    for index, party_compatability in enumerate(MementosFloor.party_compatability_types):
        print(f"{index}. {party_compatability}")
    party_compatability = input("Enter the party compatability: ")


def create_palace():
    name = input("Enter the name of the Palace: ")
    

create_mementos_floor()
