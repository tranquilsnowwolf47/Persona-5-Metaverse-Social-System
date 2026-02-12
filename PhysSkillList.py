# Filename: PhysSkillList.py
# Date: 2/4/26
# Author: Aoi | shadowsnowwolf
# Processing: utilizes OOP
# Inheritance, classes 
# List of Phys (Bluntness/Assertivness) skills from the Metaverse Social System sorted by damage grade 


# Self note: It might actually be easier to use a method with attributes rather than a dictionary for stuff like this because
# With dictionaries, I need to individually type out the attributes and keys every single time which becomes a pain in the ass
# When having to do that over and over. With OOP, I don't have to worry about retyping the same thing over and over again since
# the format is already established within the method 

# Program idea:
# Element skills that has individual programs per element, and then in the big main program I import the smaller programs as modules 

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
        print(f"HP Cost: {self.HP_cost}")
        print(f"Description:\n{self.description}")

class SevereSkills(PhysSkills):
    pass

class HeavySkills(PhysSkills):
    pass

class MediumSkills(PhysSkills):
    pass 

class LightSkills(PhysSkills):
    pass

# Heavy Skills
advance_slash = HeavySkills("Advance Slash", "Phys", "Heavy", "18%", 
"""   - After establishing brief rapport, assertively propose spending time together to escalate the interaction and force clarity. 
This skill is delivered calmly and directly, without selling, chasing, or over-investment. It collapses ambiguity early and tests willingness to progress beyond surface interaction. 
If accepted, the bond escalates and forward momentum is established. If declined or met with hesitation, you immediately disengage and disqualify, preventing friendzone dynamics, wasted investment, or false compatibility. 
This move values clarity over comfort and decisiveness over delay.
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

hard_check = HeavySkills("Hard Check", "Phys", "Heavy", "15%", 
"""   - Directly call out a behavior, intention, or social dynamic with firm, controlled bluntness that confronts the Shadow on their behavior. 
It isn't yelling or emotional escalation, but it's calm, confident assertiveness that puts pressure on the other person to clarify, adjust, or back down. 
Hard Check is used to check someone in a way that protects your frame and demands accountability without apology. 
Establishes dominance and clarity, especially within an established power dynamic and earns respect when well-executed, but may risk escalation if poorly timed or overly aggressive. 
(Ex 1: "You’ve been passive-aggressive all night. Tell me what’s up with that.", 
 Ex 2: "If that was a joke, it missed. Let’s be real for a second.", 
 Ex 3: "You’re coming off pretty disrespectful. Is that intentional?", 
 Ex 4: "You trying to start something, or is that just how you talk to people?"
 Ex 5: “Why would you not have done that earlier?”). 
 Deals heavy Phys damage.""")

iron_gaze = HeavySkills("Iron Gaze", "Phys", "Heavy", "14%", 
"""   - Lock eyes with unwavering intensity to project dominance, resolve, and absolute presence during moments of conflict or challenge. 
This gaze is a powerful stand and a silent declaration that you will not flinch, look away, or yield ground. 
Used in tense negotiations, confrontations, standoffs, or when you want to assert dominance. It applies psychological pressure and can rattle low-confidence opponents. 
(Ex: Meeting an aggressive glare without blinking, holding a stare through a heated silence, or fixing your eyes on someone mid-challenge until they speak first).
Deals heavy Phys damage.""")


# Medium Skills
alpha_directive = MediumSkills("Alpha Directive", "Phys", "Medium", "10%", 
"""   - Take command of the social dynamic by establishing direction, clarity, and accountability. 
Whether you're calling the next move, assigning roles, or making a decisive call in a group, Alpha Directive grounds everyone in your presence. 
It’s not about being bossy, but carrying the weight others hesitate to. Using this skill effectively earns respect, sets structure, and exercises leadership. 
(Ex: "Alright, we’ll split up” (assign each person roles), 
Ex 2: "Here’s the plan: we’re doing [X]. Everyone good with that?", 
Ex: 3: "We’re not standing around anymore. Let’s move– back me up when I give the signal"). 
Deals medium Phys damage.""")

bind_blade = MediumSkills("Bind Blade", "Phys", "Medium", "12%",
"""     - Deliver a blunt, unambiguous rejection to shut down offers, advances, requests, or pitches without justification or emotional engagement. 
This skill prioritizes efficiency and self-respect by clearly signaling disinterest and ending the interaction immediately. 
No debating, no softening, no follow-up—just a clean “no” that preserves your frame and time.
(Ex: “I’m good.”
 Ex 2: “Not interested.”
 Ex 3: “I’ll pass.”
 Ex 4: “Not for me.”
 Ex 5: “No, thanks.”
 Ex 6: “Not happening.”).
Deals medium Phys damage.
""")

social_dominance = MediumSkills("Social Dominance", "Phys", "Medium", "9%",
"""   - After establishing brief rapport, assertively give your social handle to the target rather than requesting theirs. 
This skill forces commitment and eliminates ambiguity, pressuring Ice-type or Reverse Bless-type defenses that would allow silent avoidance or fake compliance. 
Delivered confidently and directly, it asserts dominance without chasing or over-investing. If accepted, the target is committed to the connection, raising your social momentum and forward pressure. 
If met with hesitation or refusal, you disengage while maintaining authority, preventing wasted energy or lowered status.
(Ex: “Let me put my Instagram in your phone real quick.”
Ex 2: “Here, take my instagram. It’s easier this way.”
Ex 3: “I’ll drop my handle in your phone so you’ve got it.”
Ex 4: “Let me give you my contact real quick.”
Ex 5: “Let me give you my tag real quick”
Ex 6: “Let me give you my instagram before you go.”)
Deals medium Phys damage.""")

assertive_slice = MediumSkills("Assertive Slice", "Phys", "Medium", "10%",
"""   - Confidently and assertively state your needs, preferences, boundaries, or acts without apology, aggression, or hesitation. 
This move grounds you in your self-respect and forces the other party to adapt to your standard. 
You can use this skill defensively when someone tries to press you for something, or offensively to assert dominance and show that you’re the one in charge. 
Rather than a direct attack on someone, Assertive Slice commands space and cooperation. 
(Defensive use: 
Ex: "That doesn't work for me.",
Ex 2: "I'm not okay with that-- I need something different", 
Ex 3: "I'm going to do what feels right for me", 
Ex 4: "I'm not comfortable with that, and I'm gonna be upfront about it.”,
Ex 5: “Take me off the list now.”) 

(Offensive use:
Ex 1: “No, we’re doing it this way.”, 
Ex 2: “I’m not going to repeat myself.”, 
Ex 3: “If you have a problem, say it directly”
Ex 4: “You need to make a payment.”
Ex 5: “You have a payment.”
Ex 5: “You have a $X copay. Cash or card?”).
Deals medium Phys damage.""")

opening_gambit = MediumSkills("Opening Gambit", "Phys", "Medium", "10%",
"""   - Open with a bold, attention-grabbing statement or question that immediately breaks the ice and asserts your presence. 
It’s not subtle or polite, it's confident and built to spark intrigue or shift the energy instantly. 
(Ex: “You seemed interesting and I wanted to introduce myself”
Ex 2: "You seemed interestering and I wanted to come introduce myself"
Ex 3: "Is it cool if I sit with you?"
Ex 4: “You seemed cool and I wanted to come say hi
Ex 5: “You seemed cool and I wanted to say hi”
Ex 6: “You seemed interesting and I wanted to say hi”).
Deals medium Phys damage.""")

stone_wall = MediumSkills("Stonewall", "Phys", "Medium", "12%",
"""   - Clearly and firmly communicate a non-negotiable boundary without sugarcoating or softening. It draws a line with no room for debate, setting the tone that you respect yourself and expect others to do the same. When someone tests your patience, pushes too far, or tries to emotionally manipulate you, Stonewall slams the door with power and authority. 
(Ex: "Don’t talk to me like that again", 
Ex 2: "That’s not something I tolerate. 
Ex 3: If it happens again, I’ll walk", 
Ex 4: "I’m not interested in that dynamic. 
Ex 5: I won’t be part of it", 
Ex 6: "I don’t do passive aggression"
Ex 7: “Don’t call me again”). 
Deals medium Phys damage.""")

decision_strike = MediumSkills("Opening Gambit", "Phys", "Medium", "10%",
"""   - When a person hesitates, avoids making a decision, or is uncertain about clearly deciding on a plan, you cut through the mental fog with a decisive, authoritative call. This blunt, take-charge move asserts dominance and can earn respect, relief, appreciation, or even admiration by taking control of the moment and decide when no one is deciding. 
Best to use when the other person is stalling, passive, unsure, or overwhelmed by choice and when you're aiming to display leadership, decisiveness, or grounded masculinity. 
(Ex: Person: “I don't know what I want to eat…” 
You: "We're going to Chilli's")
Ex 2: Patient hesitating to make an appointment: 
You: “I can do (insert date).”  
Deals medium Phys damage.""")              

# Light Skills 
cold_cut = LightSkills("Cold Cut", "Phys", "Light", "5%",
"""   - Confidently introduce yourself without waiting to be asked. Cold Cut is a proactive power move that is short, direct, and deliberate. 
It’s blunt and doesn’t beg for validation or approval. This skill shows you're comfortable in your own presence and assertive enough to steer the flow from the start. 
May not be super effective on more timid types.
(Ex: "I’m [Name], by the way", 
Ex 2: “I’m [Name], nice to meet you”
Ex 2: “I’m [Name], good to meet you", 
Ex 3: “I’m [Name]. We’re in the same class aren’t we?"). 
Deals light Phys damage.""")

calling_fang = LightSkills("Calling Fang", "Phys", "Light", "4%",
"""   - Directly request someone’s name or introduce yourself in a way that puts subtle social pressure on the other person to respond.  
It’s about taking initiative and steering the energy, not waiting to be invited in. 
It shows presence, confidence, and control over the interaction from the jump. It isn’t “Hi, I’m Jake”, it's, “What’s your name?” with eye contact and intent. 
(Ex: "What’s your name?", 
Ex 2: “Didn’t catch your name earlier",
Ex 3: “Tell me about yourself”). 
Deals light Phys damage.""")

severe_skills = () # A tuple that holds every severe Phys skill 
heavy_skills = (advance_slash, consequence_hammer, verdict_slice, hard_check, iron_gaze) # A tuple that holds every heavy Phys skill
medium_skills = (alpha_directive, bind_blade, social_dominance, assertive_slice, opening_gambit, stone_wall, decision_strike) # A tuple that holds every medium Phys skill
light_skills = (cold_cut, calling_fang) # A tuple that holds every light Phys skill


# Maybe make a tuple of strings for user input choice later on

#for skill in heavy_skills:
    #skill.display_skill()
    #print()


#PhysSkills.display_skill(advance_slash)
