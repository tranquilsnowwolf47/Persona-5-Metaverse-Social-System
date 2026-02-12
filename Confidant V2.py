# Filename: Confidant V2.py
# Date: 2/12/26
# Author: Aoi | shadowsnowwolf
# Update since I got better at OOP and programming in general since the last one

class ConfidantSystem:
    def __init__(self, confidant_name, arcana_name,
                 ability_one, ability_one_description,
                 ability_two, ability_two_description,
                 ability_three, ability_three_description,
                 ability_four, ability_four_description,
                 ability_five, ability_five_description,
                 ability_six, ability_six_description,
                 ability_seven, ability_seven_description,
                 ability_eight, ability_eight_description,
                 ability_nine, ability_nine_description,
                 ability_ten, ability_ten_description):
        
        self.confidant_name = confidant_name # The name of the Confidant 
        self.arcana_name = arcana_name # The Confidant's Arcana
        
        # Confidant abilities 
        # -----------------------------------------------------------
        # Rank 1 Confidant ability 
        self.ability_one = ability_one 
        self.ability_one_description = ability_one_description

        # Rank 2 Confidant ability
        self.ability_two = ability_two 
        self.ability_two_description = ability_two_description

        # Rank 3 Confidant ability
        self.ability_three = ability_three
        self.ability_three_description = ability_three_description

        # Rank 4 Confidant ability
        self.ability_four = ability_four 
        self.ability_four_description = ability_four_description

        # Rank 5 Confidant ability
        self.ability_five = ability_five 
        self.ability_five_description = ability_five_description

        # Rank 6 Confidant ability
        self.ability_six = ability_six 
        self.ability_six_description = ability_six_description

        # Rank 7 Confidant ability
        self.ability_seven = ability_seven 
        self.ability_seven_description = ability_seven_description

        # Rank 8 Confidant ability
        self.ability_eight = ability_eight 
        self.ability_eight_description = ability_eight_description

        # Rank 9 Confidant ability
        self.ability_nine = ability_nine 
        self.ability_nine_description = ability_nine_description

        # Rank 10 Confidant ability
        self.ability_ten = ability_ten 
        self.ability_ten_description = ability_ten_description

    # Displays the Rank 1 confidant ability along with it's description
    def display_rank_one(self):
        print(self.ability_one)
        print(self.ability_one_description)

    # Displays the Rank 2 confidant ability along with it's description
    def display_rank_two(self):
        print(self.ability_two)
        print(self.ability_two_description)

    # Displays the Rank 3 confidant ability along with it's description
    def display_rank_three(self):
        print(self.ability_three)
        print(self.ability_three_description)

    # Displays the Rank 4 confidant ability along with it's description
    def display_rank_four(self):
        print(self.ability_four)
        print(self.ability_four_description)

    # Displays the Rank 5 confidant ability along with it's description
    def display_rank_five(self):
        print(self.ability_five)
        print(self.ability_five_description)

    # Displays the Rank 6 confidant ability along with it's description
    def display_rank_six(self):
        print(self.ability_six)
        print(self.ability_six_description)

    # Displays the Rank 7 confidant ability along with it's description
    def display_rank_seven(self):
        print(self.ability_seven)
        print(self.ability_seven_description)

    # Displays the Rank 8 confidant ability along with it's description
    def display_rank_eight(self):
        print(self.ability_eight)
        print(self.ability_eight_description)

    # Displays the Rank 9 confidant ability along with it's description
    def display_rank_nine(self):
        print(self.ability_nine)
        print(self.ability_nine_description)

    # Displays the Rank 10 confidant ability along with it's description
    def display_rank_ten(self):
        print(self.ability_ten)
        print(self.ability_ten_description)


class FoolConfidant(ConfidantSystem):
    pass
class MagicianConfidant(ConfidantSystem):
    pass
class PriestessConfidant(ConfidantSystem):
    pass
class EmpressConfidant(ConfidantSystem):
    pass
class EmperorConfidant(ConfidantSystem):
        pass
class HierophantConfidant(ConfidantSystem):
    pass
class LoversConfidant(ConfidantSystem):
    pass
class ChariotConfidant(ConfidantSystem):
    pass
class JusticeConfidant(ConfidantSystem):
    pass
class HermitConfidant(ConfidantSystem):
    pass
class FortuneConfidant(ConfidantSystem):
    pass
class StrengthConfidant(ConfidantSystem):
    pass
class HangedManConfidant(ConfidantSystem):
    pass
class DeathConfidant(ConfidantSystem):
    pass
class TemperanceConfidant(ConfidantSystem):
    pass
class DevilConfidant(ConfidantSystem):
    pass
class TowerConfidant(ConfidantSystem):
    pass
class StarConfidant(ConfidantSystem):
    pass
class MoonConfidant(ConfidantSystem):
    pass
class SunConfidant(ConfidantSystem):
    pass
class JudgementConfidant(ConfidantSystem):
    pass
class FaithConfidant(ConfidantSystem):
    pass
class CouncillorConfidant(ConfidantSystem):
    pass
