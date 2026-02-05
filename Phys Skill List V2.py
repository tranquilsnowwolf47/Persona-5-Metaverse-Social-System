# Filename: Phys Skill List V2.py
# Date: 2/4/26
# Author: Aoi | shadowsnowwolf
# Processing: utilizes OOP
# Inheritance, classes 

# Self note: It might actually be easier to use a method with attributes rather than a dictionary for stuff like this because
# With dictionaries, I need to individually type out the attributes and keys every single time which becomes a pain in the ass
# When having to do that over and over. With OOP, I don't have to worry about retyping the same thing over and over again since
# the format is already established within the method 

class PhysSkills:
    def __init__(self,name, element, damage_grade, HP_cost, description):
        self.name = name
        self.element = element
        self.damage_grade = damage_grade
        self.HP_cost = HP_cost
        self.description = description

    # Shows the full info of the skill
    def display_skill(self):
        print(f"- {self.name} ({self.element})")
        print(f"HP Cost {self.HP_cost}")
        print(f"Description:\n{self.description}")

class SevereSkills(PhysSkills):
    pass

class HeavySkills(PhysSkills):
    pass

class MediumSkills(PhysSkills):
    pass 

class LightSkills(PhysSkills):
    pass

advance_slash = HeavySkills("Advance Slash", "Phys", "Heavy", "18%", 
"""   - After establishing brief rapport, assertively propose spending time together to escalate the interaction and force clarity. This skill is delivered calmly and directly, without selling, chasing, or over-investment. It collapses ambiguity early and tests willingness to progress beyond surface interaction. If accepted, the bond escalates and forward momentum is established. If declined or met with hesitation, you immediately disengage and disqualify, preventing friendzone dynamics, wasted investment, or false compatibility. This move values clarity over comfort and decisiveness over delay.
(Ex: “We should hang out sometime.”
Ex 2: “Let’s grab coffee sometime.”
Ex 3: “We should meet up again sometime”
Ex 4: “We should do something together soon”).
Deals heavy Phys damage. """)

consequence_hammer = HeavySkills("Consequence Hammer", "Phys", "Heavy", "18%",
"""   - Enforce consequences for continued negative behavior by clearly stating what will happen if the behavior does not change. 
This skill is delivered once, calmly, and without emotion, establishing a hard boundary backed by action. 
It does not threaten, negotiate, or repeat. If the behavior continues, disengagement is automatic. 
Ends dynamics and puts people in check if they fear losing you, or allows you to All-Out Attack if they don’t. 
High chance of critical hit. Deals heavy Phys damage. 
(Ex: “If you call me that again I’m blocking you.”\"
Ex 2: “If you cancel again, we’re done. You won’t be hearing from me again”
Ex 3: “Do that shit again and you’re permanently banned from being on my property”
Ex 4: “Leave right now or I’ll make you”
Ex 5: “Disrespect me like that one more time and I’m never playing this game with you again”
Ex 6: “This isn’t gonna happen twice. Next time I walk”).
Deals heavy Phys damage. """)

verdict_slice = HeavySkills("Verdict Slice", "Phys", "Heavy", "18%", 
"""   - Combine a clear ultimatum with a direct demand for a concrete answer or decision, collapsing all ambiguity into a single decision point. 
This skill shuts down “maybe,” deflection, and stalling by making continuation conditional on a definitive response. 
Delivered calmly and without emotion, it asserts dominance over the frame and treats refusal to answer as an answer in itself.
(Ex: “I didn’t ask ‘maybe.’ I asked yes or no. Which is it?”
 Ex 2: “I need a clear answer—yes or no.”
 Ex 3: “We either do this or we don’t. Decide.”
 Ex 4: “I’m not moving forward without a straight answer.”
 Ex 5: “Answer the question. Yes or no?”
 Ex 6: “What are we doing? I don’t have all day to wait around for you to decide”).
Deals heavy Phys damage.""")

heavy_skills = (advance_slash, consequence_hammer)


# Debugging  
#HeavySkills.display_skill(advance_slash)
#HeavySkills.display_skill(consequence_hammer)
HeavySkills.display_skill(verdict_slice)


