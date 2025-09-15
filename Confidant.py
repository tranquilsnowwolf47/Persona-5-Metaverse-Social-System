class TemplateConfidant:
    # Number, name, description
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class FoolConfidant:
    fool_confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    fool_confidant_ability_names = ["Wild Talk",
                                    "Arcana Burst",
                                    "Third Eye",
                                    "X",
                                    "X",
                                    "X",
                                    "X",
                                    "X",
                                    "X",
                                    "X"]
    fool_confidant_ability_descriptions = ["Allows you to negotiate with Shadows after performing a Hold Up.",
                                           "Earn bonus EXP when fusing Personas based on their arcana's Confidant rank.",
                                           "X","X","X","X","X","X","X","X"]


class MagicianConfidant:
    magician_confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    magician_confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    magician_confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class PriestessConfidant:
    priestess_confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    priestess_confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    priestess_confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class EmpressConfidant:
    empress_confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    empress_confidant_ability_names = ["Carpool","Smart Shopper","Antibody","Skincare Specialist","X","X","X","X","X","X"]
    empress_confidant_ability_descriptions = ["Allows you to carpool to work with Jessica, letting you keep more money from working",
                                              "Allows you to use the Instacart shopping app and adds support and HP recovery items to the online shopping inventory.",
                                              "Grants you knowledge on how to most optimally fend off colds and viruses. \nAdds bulk Vitamin C packets to the online shopping inventory. "
                                              "\nAdditionally, allows you to keep more money from working by reducing the amount of sicks days off of work.",
                                              "Grants you knowledge on the effects of the sun's rays on the skin, such as SPF, UVB, and melanin. "
                                              "\nAdds mineral sunscreen sticks to the online shopping inventory."
                                              "\nApplying sunscreen and skincare products may contribute to receiving buffs and unlocking the Looksmax buff skill.",
                                              "X","X","X","X","X","X"]


class EmperorConfidant:
    emperor_confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    emperor_confidant_ability_names = ["Martial Prowess",
                                       "Sage Learning",
                                       "Negotiation Whisperer",
                                       "Commanding Presence",
                                       "X",
                                       "X",
                                       "X",
                                       "X",
                                       "X",
                                       "X"]
    emperor_confidant_ability_descriptions = ["Improves Martial Arts Skills.",
                                              "Improves your ability to deeply understand concepts, strengthening your learning ability.",
                                              "Increases the chances of triggering a Hold Up, as well as increases the chances of obtaining money or items during Shadow negotations.",
                                        "IAq    aAZSXAZ azXmproves your body language and eye contact skills, granting better first impressions and influence over individual Shadows and Shadows in groups. "
                                              "\nAt the start of battle, you or all allies receive a 1-turn Speed or Attack buff.",
                                              "X",
                                              "X",
                                              "X",
                                              "X",
                                              "X",
                                              "X"]
    
    def display_rank_one_info():
        print(f"Rank {EmperorConfidant.emperor_confidant_rank_numbers[0]}: {EmperorConfidant.emperor_confidant_ability_names[0]}")
        print(f"Description:\n{EmperorConfidant.emperor_confidant_ability_descriptions[0]}")

    def display_rank_two_info():
        print(f"Rank {EmperorConfidant.emperor_confidant_rank_numbers[1]}: {EmperorConfidant.emperor_confidant_ability_names[1]}")
        print(f"Description: \n{EmperorConfidant.emperor_confidant_ability_descriptions[1]}")

    def display_rank_three_info():
        print(f"Rank {EmperorConfidant.emperor_confidant_rank_numbers[2]}: {EmperorConfidant.emperor_confidant_ability_names[2]}")
        print(f"Description: {EmperorConfidant.emperor_confidant_ability_descriptions[2]}")

    def display_rank_four_info():
        print(f"Rank {EmperorConfidant.emperor_confidant_rank_numbers[3]}: {EmperorConfidant.emperor_confidant_ability_names[3]}")
        print(f"Description: {EmperorConfidant.emperor_confidant_ability_descriptions[3]}")
    
EmperorConfidant.display_rank_one_info()
print()
EmperorConfidant.display_rank_two_info()
print()
EmperorConfidant.display_rank_three_info()
print()
EmperorConfidant.display_rank_four_info()


class HierophantConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["Bookworm","Atomic Habits","Shaq's Support","Finance Guru","Orlando Refuge","X","X","X","X","X"]
    _confidant_ability_descriptions = ["Increases the selection of book topics you can read and allows access to the public library.",
                                       "Allows you to hone the power of microhabits to increase productivity quicker and learn Persona skills faster.",
                                       "Slightly increases EXP earned from battle.",
                                       "Improves your financial literacy skills, allowing you to keep more money when working due to enhanced financial management.",
                                       "Allows access to Shaq's apartment in Orlando, heavily reducing costs of attending cons in Ornaldo, increasing the number of cons available to attend.",
                                       "X","X","X","X","X"]


class LoversConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["Meta-Manifestation","Girl Talk","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["Allows you to manifest desired outcomes and improve growth performance through positive affirmations, journaling, and mindset changes.",
                                       "Grants you knowledge on the behavior of quality women, increasing the chances of triggering a Hold Up with female Shadows.",
                                       "X","X","X","X","X","X","X","X"]


class ChariotConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["Story Talk","Macho Education","Time Guru","Artist Collab","Follow Up","Harisen Recovery","Endure","Story Master","Second Awakening","Second Awakening R"]
    _confidant_ability_descriptions = ["Allows you to brainstorm and discuss story ideas with Lee. Enhances your storywriting capability.",
                                       "Allows you to discuss nutrition and gym related topics with Lee. Enhances your physical fitness capability and may unlock new food recipes that restore HP.",
                                       "Rewires your perception of time, granting you more free time in day-to-day life and increasing your overall productivity.",
                                       "Allows you to discuss and practice art with Lee. Enhances your art skills.",
                                       "Chance to perform a follow-up attack if Joker's attack does not down the enemy.",
                                       "Chance to cure status ailments inflicted upon party members.",
                                       "Chance to withstand an otherwise fatal attack with 1 HP remaining.",
                                       "Greatly enhances your storywriting, time management, and physical fitness abilities.",
                                       "Transforms Persona into a mythological trickster.",
                                       "Fuse with the mythological Trickster, awakening it's true power."]


class JusticeConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class HermitConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class FortuneConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class StrengthConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class HangedManConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class DeathConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class TemperanceConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class DevilConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["High-Value Man","Culinary Talk","Bad-Body Look","EM Grandmaster","Cow-tipper","Valedictorian","X","X","X","X"]
    _confidant_ability_descriptions = ["Increases the chances of triggering a Hold Up with attractive female Shadows.",
                                       "Allows you to learn about meal prep nutrition, and healthy eating habits, allowing you to improve your physical health and fitness.",
                                       "Allows you to get fashion ideas from Dulce to improve your look. \nWearing these clothes may grant passive buffs before battle.",
                                       "Improves your overall emotional maturity, increasing the chances of triggering a Hold Up with gloomy Shadows.",
                                       "Grants you access to steak and beef recipes which can be used to restore HP in the Metaverse.",
                                       "Improves your school performance, allowing you more free time in day-to-day life.",
                                       "X","X","X","X"]


class TowerConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]


class StarConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["Affirmation Talk","Gentle Energy","Brain Picker","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["Improves the strengthening effect of positive self-talk affirmations.",
                                       "Increases the chances of triggering a Hold Up with timid Shadows.",
                                       "Grants a deeper understanding of human psychology, allowing you to learn Psy skills quicker.",
                                       "X","X","X","X","X","X","X"]


class MoonConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]

class SunConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]

class JudgementConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]

class FaithConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]

class CouncillorConfidant:
    _confidant_rank_numbers = [1,2,3,4,5,6,7,8,9,10]
    _confidant_ability_names = ["X","X","X","X","X","X","X","X","X","X"]
    _confidant_ability_descriptions = ["X","X","X","X","X","X","X","X","X","X"]